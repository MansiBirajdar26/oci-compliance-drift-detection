# OCI Compliance Drift Detection

A lightweight ML-based framework for detecting cloud compliance drift 
on Oracle Cloud Infrastructure (OCI).

## Research Paper
**Title:** Automated Cloud Compliance Drift Detection using Machine 
Learning — A Lightweight Framework on Oracle Cloud Infrastructure

**Authors:** [Your Name], [Partner Name]  
**Institution:** [Your College Name]  
**Target:** IEEE Access 2026

## System Overview
Monitors 5 OCI configuration parameters:
1. Storage bucket visibility (public/private)
2. MFA activation per user
3. Open inbound ports in security lists
4. Audit log retention period
5. Overall MFA compliance flag

## Tech Stack
- Oracle Cloud Infrastructure (OCI) — Always Free Tier
- Python 3.10+
- scikit-learn (Random Forest, Isolation Forest)
- OCI Python SDK

## Project Structure
oci-compliance-drift/
├── collector/
│   └── collect_config.py    # pulls live OCI config snapshots
├── data/
│   └── snapshots/           # raw JSON snapshots
├── models/                  # ML model files
└── README.md

## Setup
```bash
pip install oci pandas scikit-learn numpy matplotlib
oci setup config
python collector/collect_config.py
```