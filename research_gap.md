# Research Gap

A systematic review of 20 existing studies reveals four 
critical gaps in cloud compliance drift detection:

**Gap 1 — Platform Bias Toward AWS/Azure**
Of 20 reviewed papers, 17 exclusively target AWS, Azure, 
or GCP. Only Singh (2023) addresses OCI, but relies on 
paid-tier Cloud Guard and security zones unavailable in 
free-tier environments. No study proposes an ML-based 
framework validated on OCI Always Free infrastructure.

**Gap 2 — Separation of ML and Compliance Mapping**
Papers employing ML models (Mehmood 2024, Thiyagarajan 
2024, Okpomu 2026, Malaviya 2026) focus on resource usage 
or network traffic — none map detected drift to regulatory 
frameworks such as CIS Benchmarks or GDPR. Conversely, 
papers addressing compliance mapping (Guduru 2020, 
Martseniuk 2024, Vethachalam 2024) rely on rule-based 
or static policy approaches without ML-based detection.

**Gap 3 — Absence of Free-Tier Validation**
All existing frameworks require paid-tier cloud services — 
AWS Config, Azure Policy, OCI Cloud Guard, or Prisma Cloud. 
No study demonstrates a working compliance drift detection 
prototype on always-free cloud infrastructure, limiting 
reproducibility for resource-constrained organizations 
and student researchers.

**Gap 4 — Runtime Configuration Ignored**
Papers such as Yelkoti (2025) and Owoade (2024) focus on 
pre-deployment pipeline scanning. Papers like Naik (2023) 
and Pookandy (2021) target transactional or IAM structures. 
None monitor live runtime cloud configuration parameters 
— bucket visibility, open ports, MFA status, and audit 
retention — as a unified multi-parameter snapshot.

This paper addresses all four gaps by proposing a 
lightweight ML-based compliance drift detection framework 
that operates on OCI Always Free Tier, monitors 5 runtime 
configuration parameters, and validates detected drift 
against CIS OCI Benchmark controls and GDPR requirements.