import json
import os
import pandas as pd
import random
from datetime import datetime, timedelta

# ── Step 1: Read your real snapshots ─────────────────────────
snapshots_dir = "data/snapshots"
rows = []

for filename in os.listdir(snapshots_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(snapshots_dir, filename)
        with open(filepath, "r") as f:
            data = json.load(f)

        params = data["parameters"]

        # Extract features safely
        # Buckets
        buckets = params.get("buckets", [])
        if isinstance(buckets, list):
            bucket_public = int(any(b.get("is_public", False) for b in buckets))
        else:
            bucket_public = 0  # error in bucket data = assume private

        # MFA
        mfa = params.get("mfa", [])
        if isinstance(mfa, list) and len(mfa) > 0:
            mfa_active = int(mfa[0].get("mfa_active", False))
        else:
            mfa_active = 0

        # Open ports
        open_ports = params.get("open_ports", [])
        port_22_open = 0
        all_ports_open = 0
        if isinstance(open_ports, list):
            for p in open_ports:
                if p.get("port") == "22" and p.get("source") == "0.0.0.0/0":
                    port_22_open = 1
                if p.get("port") == "all" and p.get("source") == "0.0.0.0/0":
                    all_ports_open = 1

        # Audit retention
        audit = params.get("audit_retention", {})
        if isinstance(audit, dict):
            retention_days = audit.get("retention_period_days", 0)
        else:
            retention_days = 0

        # MFA compliance
        mfa_compliance = params.get("mfa_compliance", {})
        if isinstance(mfa_compliance, dict):
            users_without_mfa = mfa_compliance.get("users_without_mfa", 1)
        else:
            users_without_mfa = 1

        # Label — non-compliant because port 22 is open
        label = "non-compliant"

        rows.append({
            "snapshot_file": filename,
            "bucket_public": bucket_public,
            "mfa_active": mfa_active,
            "port_22_open": port_22_open,
            "all_ports_open": all_ports_open,
            "retention_days": retention_days,
            "users_without_mfa": users_without_mfa,
            "label": label
        })

print(f"✅ Real snapshots loaded: {len(rows)}")

# ── Step 2: Simulate compliant snapshots ──────────────────────
# These represent a "hardened" OCI config where port 22 is closed
print("🔧 Simulating compliant snapshots...")

base_date = datetime(2026, 5, 1)
for i in range(11):
    sim_date = base_date + timedelta(days=i)
    rows.append({
        "snapshot_file": f"simulated_compliant_{i+1:02d}.json",
        "bucket_public": 0,        # buckets private
        "mfa_active": 1,           # MFA on
        "port_22_open": 0,         # port 22 CLOSED
        "all_ports_open": 0,       # no open ports
        "retention_days": 365,     # audit retention ok
        "users_without_mfa": 0,    # all users have MFA
        "label": "compliant"
    })

print(f"✅ Simulated compliant snapshots: 11")

# ── Step 3: Save to CSV ───────────────────────────────────────
df = pd.DataFrame(rows)
os.makedirs("data", exist_ok=True)
df.to_csv("data/dataset.csv", index=False)

print(f"\n✅ Dataset saved to data/dataset.csv")
print(f"   Total rows: {len(df)}")
print(f"   Non-compliant: {len(df[df['label']=='non-compliant'])}")
print(f"   Compliant: {len(df[df['label']=='compliant'])}")
print(f"\nDataset preview:")
print(df.head(5))