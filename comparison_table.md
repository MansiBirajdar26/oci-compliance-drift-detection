# Literature Review — Comparison Table
## OCI Compliance Drift Detection Research Paper
### Authors: Mansi Birajdar, Rutuja Walunj | College: Symbiosis Skills and Professional University, Pune

---

| # | Author & Year | Year | Platform | Method | Compliance Framework | Identified Research Gap |
|---|---|---|---|---|---|---|
| 1 | Mehmood et al. | 2024 | Google Cloud | Optimized Attention LSTM | Unspecified Cloud Usage Tracking | Limits profiling to multi-model resource utilization traces rather than structural posture metadata |
| 2 | Stojnev Ilic et al. | 2026 | Edge-Cloud | ADWIN Ensemble Voting | General Biomedical Anomaly | Confined to physiological streaming sensors; lacks system parameter evaluation |
| 3 | Marella | 2024 | AWS / Azure / GCP | Rule-based Mapping | Cross-Cloud Baseline | Bypasses actual machine learning drift modeling, using static mappings |
| 4 | Thiyagarajan et al. | 2024 | AWS / Azure | Random Forest | Generic Posture Controls | Bypasses lightweight free-tier optimization and does not map to OCI primitives |
| 5 | Alti | 2023 | Kubernetes | Rule-based Hardening | CIS Benchmarks (K8s/Linux) | Restricted to container node configurations; fails to look at host cloud metadata platforms |
| 6 | Owoade et al. | 2024 | Multi-Cloud | Rule-based CI/CD DevSecOps | GDPR, PCI-DSS, SOC 2 | Strictly deployment pipeline-oriented; lacks operational ML drift validation |
| 7 | Jansson | 2021 | AWS | Automated Reasoning (Zelkova) | CIS AWS Foundations, PCI-DSS | Relies on expensive paid cloud-native modules; lacks custom ML architectures |
| 8 | Yelkoti | 2025 | Multi-Cloud | Static Scanning & Policy Workflows | PCI-DSS, HIPAA, GDPR | Focuses on pre-deployment code commits; leaves runtime asset configurations unchecked |
| 9 | Okpomu & Ogoro | 2026 | Multi-Cloud | Supervised & Hybrid ML Ensembles | Unspecified Security Baseline | Network log and network intrusion traffic-oriented; ignores active host tenant drift states |
| 10 | Malaviya | 2026 | IoT Continuum | Isolation Forest Outlier Profiling | General Data Security | Geared entirely toward physical sensor streams instead of logical hypervisor data fields |
| 11 | Pookandy | 2021 | SaaS CRM Cloud | Federated IAM & RBAC Workflows | GDPR, CCPA, HIPAA | Restricted to SaaS Identity Provider structures; misses runtime cloud storage/port metrics |
| 12 | Naik | 2023 | Multi-Cloud | Dynamic Tokenization & Masking | GDPR, HIPAA, CCPA | Focuses on transactional processing privacy vaults rather than structural infrastructure decay |
| 13 | Vethachalam | 2024 | Multi-Cloud | Privacy-by-Design Blueprints | GDPR, CCPA | Highly abstract architectural principles; lacks executable ML engines or OCI validation |
| 14 | Guduru | 2020 | Multi-Cloud | Policy-as-Code Automation | CIS Benchmarks, NIST SP 800-53 | Bypasses lightweight setups; requires paid tier resources (AWS Config/Azure Policy) |
| 15 | Folorunso et al. | 2024 | Multi-Cloud | Conceptual AI Load Balancing | GDPR, HIPAA | Presents a high-level conceptual framework model without physical code deployment |
| 16 | Martseniuk et al. | 2024 | Multi-Cloud | Runbook Automation & Scripting | NIST 800-53, ISO 27001, PCI-DSS | Non-adaptive; requires premium third-party orchestration software suites (Prisma Cloud) |
| 17 | Singh | 2023 | OCI | Native Active Compartment Policies | ISO 27001, FedRAMP, GDPR | Tied entirely to commercial paid-tier tools (OCI Cloud Guard / paid security zones) |
| 18 | Marella | 2025 | AWS / Azure / GCP | Standardized Policy Abstraction | Multi-Cloud SLO-Driven Compliance | Fails to consider free-tier environments; focuses on multi-cloud orchestration overhead |
| 19 | Jimmy | 2023 | AWS | CSF Posture Management Controls | NIST CSF v1.1 | AWS API-specific; leaves alternative architectures like OCI completely unmapped |
| 20 | Pesaranghader et al. | 2018 | Evolving Streams | Fast Hoeffding Drift Stacking | Generic Drift Classification | Bypasses cloud security constraints entirely, focusing on raw data streams |

---

## Summary Analysis

### Platform Distribution
| Platform | Count | Papers |
|---|---|---|
| AWS only | 2 | Jansson 2021, Jimmy 2023 |
| AWS + Azure | 1 | Thiyagarajan 2024 |
| AWS / Azure / GCP | 2 | Marella 2024, Marella 2025 |
| Multi-Cloud | 6 | Owoade 2024, Yelkoti 2025, Okpomu 2026, Naik 2023, Vethachalam 2024, Guduru 2020, Folorunso 2024, Martseniuk 2024 |
| Google Cloud | 1 | Mehmood 2024 |
| Edge-Cloud | 1 | Stojnev Ilic 2026 |
| Kubernetes | 1 | Alti 2023 |
| IoT Continuum | 1 | Malaviya 2026 |
| SaaS CRM | 1 | Pookandy 2021 |
| Evolving Streams | 1 | Pesaranghader 2018 |
| OCI | 1 | Singh 2023 (paid tier only) |
| **OCI Free Tier** | **0** | **← YOUR PAPER** |

---

### ML Usage
| Category | Count | Papers |
|---|---|---|
| ML-based | 6 | Mehmood 2024, Stojnev Ilic 2026, Thiyagarajan 2024, Okpomu 2026, Malaviya 2026, Pesaranghader 2018 |
| Rule-based | 8 | Marella 2024, Alti 2023, Owoade 2024, Jansson 2021, Yelkoti 2025, Guduru 2020, Martseniuk 2024, Jimmy 2023 |
| Conceptual/Abstract | 3 | Vethachalam 2024, Folorunso 2024, Marella 2025 |
| IAM/Policy workflows | 2 | Pookandy 2021, Naik 2023 |
| Singh 2023 | 1 | Native OCI policies |
| **ML + CIS + GDPR + OCI** | **0** | **← YOUR PAPER** |

---

### Compliance Framework Coverage
| Framework | Papers Covering It |
|---|---|
| GDPR | Owoade 2024, Yelkoti 2025, Pookandy 2021, Naik 2023, Vethachalam 2024, Folorunso 2024, Singh 2023 |
| CIS Benchmarks | Alti 2023, Jansson 2021, Guduru 2020 |
| NIST | Guduru 2020, Martseniuk 2024, Jimmy 2023 |
| ISO 27001 | Martseniuk 2024, Singh 2023 |
| PCI-DSS | Owoade 2024, Jansson 2021, Yelkoti 2025, Martseniuk 2024 |
| HIPAA | Owoade 2024, Pookandy 2021, Naik 2023, Folorunso 2024 |
| **CIS + GDPR + ML + OCI** | **0 ← YOUR PAPER** |

---

## Confirmed Research Gaps

### Gap 1 — OCI Platform Bias
> Only 1 of 20 papers (Singh 2023) targets OCI, and it relies
> entirely on paid-tier Cloud Guard. No paper applies ML-based
> drift detection on OCI Always Free infrastructure.

### Gap 2 — ML and Compliance Never Combined
> Papers using ML (Mehmood, Thiyagarajan, Okpomu, Malaviya)
> do not map to compliance frameworks. Papers with compliance
> mapping (Guduru, Martseniuk, Vethachalam) use rule-based
> approaches without ML. No paper combines both.

### Gap 3 — No Free-Tier Validation
> All 20 papers require paid cloud services — AWS Config,
> Azure Policy, OCI Cloud Guard, or Prisma Cloud. No paper
> demonstrates a working prototype on always-free
> cloud infrastructure.

### Gap 4 — Runtime Configuration Ignored
> Papers like Yelkoti (2025) and Owoade (2024) focus on
> pre-deployment pipelines. None monitor live runtime
> parameters — bucket visibility, open ports, MFA status,
> audit retention — as a unified multi-parameter snapshot
> on a cloud provider API.

---

## Our Paper's Position
**"Automated Cloud Compliance Drift Detection using Machine Learning:
A Lightweight Framework on Oracle Cloud Infrastructure"**

| Criteria | Our Paper |
|---|---|
| Platform | OCI Always Free Tier ✅ |
| ML Model | Random Forest + Isolation Forest ✅ |
| Compliance Framework | CIS OCI Benchmark + GDPR ✅ |
| Free Tier | Yes ✅ |
| Runtime Parameters | 5 live OCI config parameters ✅ |
| Gaps Addressed | All 4 gaps above ✅ |

---
*Last updated: June 2026*
*Total papers reviewed: 20*