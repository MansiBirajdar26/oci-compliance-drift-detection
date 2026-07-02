import pandas as pd
import numpy as np
import os

random_state = 42
np.random.seed(random_state)

rows = []

# ── Scenario 1: Your real snapshots (9 rows) ─────────────────
# Port 22 open, everything else ok
for i in range(9):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 1,
        "all_ports_open": 1,
        "retention_days": 365,
        "users_without_mfa": 0,
        "label": "non-compliant"  # port 22 open = non-compliant
    })

# ── Scenario 2: Fully compliant (30 rows) ────────────────────
# Everything clean
for i in range(30):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": np.random.choice([90, 180, 365]),
        "users_without_mfa": 0,
        "label": "compliant"
    })

# ── Scenario 3: Public bucket (20 rows) ──────────────────────
# Bucket is public = non-compliant
for i in range(20):
    rows.append({
        "bucket_public": 1,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": 365,
        "users_without_mfa": 0,
        "label": "non-compliant"  # public bucket = non-compliant
    })

# ── Scenario 4: MFA disabled (20 rows) ───────────────────────
# MFA off = non-compliant
for i in range(20):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 0,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": 365,
        "users_without_mfa": np.random.randint(1, 3),
        "label": "non-compliant"  # MFA off = non-compliant
    })

# ── Scenario 5: Low audit retention (20 rows) ────────────────
# Retention < 90 days = non-compliant
for i in range(20):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": np.random.randint(1, 89),
        "users_without_mfa": 0,
        "label": "non-compliant"  # low retention = non-compliant
    })

# ── Scenario 6: Multiple violations (15 rows) ────────────────
# Multiple issues at once
for i in range(15):
    rows.append({
        "bucket_public": 1,
        "mfa_active": 0,
        "port_22_open": 1,
        "all_ports_open": 1,
        "retention_days": np.random.randint(1, 60),
        "users_without_mfa": np.random.randint(1, 5),
        "label": "non-compliant"
    })

# ── Scenario 7: Partial compliance (15 rows) ─────────────────
# Almost compliant — only retention slightly low
for i in range(15):
    rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": np.random.randint(90, 180),
        "users_without_mfa": 0,
        "label": "compliant"  # meets minimum threshold
    })

# ── Save ──────────────────────────────────────────────────────
df = pd.DataFrame(rows)

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

os.makedirs("data", exist_ok=True)
df.to_csv("data/dataset.csv", index=False)

print(f"✅ Expanded dataset saved to data/dataset.csv")
print(f"   Total rows:       {len(df)}")
print(f"   Compliant:        {len(df[df['label']=='compliant'])}")
print(f"   Non-compliant:    {len(df[df['label']=='non-compliant'])}")
print(f"\nClass distribution:")
print(df['label'].value_counts())
print(f"\nSample rows:")
print(df.head(10).to_string())