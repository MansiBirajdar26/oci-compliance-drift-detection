import pandas as pd
import numpy as np
import os

np.random.seed(42)

df = pd.read_csv("data/dataset.csv")

print(f"Before noise: {len(df)} rows")

# ── Add noise rows ────────────────────────────────────────────

noise_rows = []

# Edge case 1: Port 22 open BUT everything else perfect
# Some orgs allow port 22 with strict MFA — borderline case
for i in range(8):
    noise_rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 1,
        "all_ports_open": 0,
        "retention_days": 365,
        "users_without_mfa": 0,
        "label": "non-compliant"
    })

# Edge case 2: Compliant but retention is exactly at boundary
for i in range(8):
    noise_rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": np.random.randint(90, 100),
        "users_without_mfa": 0,
        "label": "compliant"
    })

# Edge case 3: Public bucket but short retention too
for i in range(8):
    noise_rows.append({
        "bucket_public": 1,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": np.random.randint(30, 89),
        "users_without_mfa": 0,
        "label": "non-compliant"
    })

# Edge case 4: MFA off but good retention and closed ports
for i in range(8):
    noise_rows.append({
        "bucket_public": 0,
        "mfa_active": 0,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": np.random.randint(180, 365),
        "users_without_mfa": 1,
        "label": "non-compliant"
    })

# Edge case 5: Fully compliant with varying retention
for i in range(8):
    noise_rows.append({
        "bucket_public": 0,
        "mfa_active": 1,
        "port_22_open": 0,
        "all_ports_open": 0,
        "retention_days": np.random.randint(200, 365),
        "users_without_mfa": 0,
        "label": "compliant"
    })

# Add noise rows to dataset
noise_df = pd.DataFrame(noise_rows)
df = pd.concat([df, noise_df], ignore_index=True)

# Shuffle
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save
df.to_csv("data/dataset.csv", index=False)

print(f"After noise:  {len(df)} rows")
print(f"Compliant:    {len(df[df['label']=='compliant'])}")
print(f"Non-compliant:{len(df[df['label']=='non-compliant'])}")