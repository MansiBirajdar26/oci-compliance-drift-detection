import pandas as pd
import numpy as np
import os

np.random.seed(42)
rows = []

# ── COMPLIANT scenarios (80 rows) ────────────────────────────

# Perfect compliance
for i in range(25):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(180, 400)),
        "users_without_mfa": 0,
        "label": "compliant"
    })

# Compliant with varying retention (just above threshold)
for i in range(20):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(90, 180)),
        "users_without_mfa": 0,
        "label": "compliant"
    })

# Compliant — port 22 restricted to internal only (not 0.0.0.0/0)
for i in range(20):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(100, 365)),
        "users_without_mfa": 0,
        "label": "compliant"
    })

# Compliant with 1 user without MFA but everything else perfect
# (borderline — still compliant if org policy allows)
for i in range(15):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(200, 365)),
        "users_without_mfa": 0,
        "label": "compliant"
    })

# ── NON-COMPLIANT scenarios (120 rows) ───────────────────────

# Your real snapshots — port 22 open to world
for i in range(9):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 1,
        "all_ports_open": 1,
        "retention_days": 365,
        "users_without_mfa": 0,
        "label": "non-compliant"
    })

# Port 22 open only (most common violation)
for i in range(25):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 1,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(90, 365)),
        "users_without_mfa": 0,
        "label": "non-compliant"
    })

# Public bucket only
for i in range(20):
    rows.append({
        "bucket_public": 1,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(90, 365)),
        "users_without_mfa": 0,
        "label": "non-compliant"
    })

# MFA disabled
for i in range(20):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 0,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(90, 365)),
        "users_without_mfa": int(np.random.randint(1, 4)),
        "label": "non-compliant"
    })

# Low retention
for i in range(20):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(1, 89)),
        "users_without_mfa": 0,
        "label": "non-compliant"
    })

# Multiple violations
for i in range(15):
    rows.append({
        "bucket_public": int(np.random.randint(0, 2)),
        "mfa_active": 0,
        "port_22_open": 1,
        "all_ports_open": int(np.random.randint(0, 2)),
        "retention_days": int(np.random.randint(1, 89)),
        "users_without_mfa": int(np.random.randint(1, 5)),
        "label": "non-compliant"
    })

# Port 22 open + low retention
for i in range(11):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 1,
        "all_ports_open": 0,
        "retention_days": int(np.random.randint(1, 89)),
        "users_without_mfa": 0,
        "label": "non-compliant"
    })

# ── Save ──────────────────────────────────────────────────────
df = pd.DataFrame(rows)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
os.makedirs("data", exist_ok=True)
df.to_csv("data/dataset.csv", index=False)

print(f"✅ Final dataset saved: {len(df)} rows")
print(f"   Compliant:     {len(df[df['label']=='compliant'])}")
print(f"   Non-compliant: {len(df[df['label']=='non-compliant'])}")