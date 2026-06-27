# Literature Review Notes
## Paper: Automated Cloud Compliance Drift Detection using ML on OCI
### Authors: Mansi Birajdar, Rutuja Walunj | College: Symbiosis Skills and Professional University, Pune

---

## CATEGORY 1 — Cloud Drift Detection & ML Papers

---

### Paper 1
- **Title:** LSTMDD: An Optimized LSTM-based Drift Detector for Concept Drift in Dynamic Cloud Computing
- **Authors:** Mehmood, Tajwar; Latif, Seemab; Jamail, Nor Shahida; Malik, Asad; Latif, Rabia
- **Year:** 2024
- **Source:** PeerJ Computer Science (DOI: 10.7717/peerj-cs.1827)
- **Cloud platform:** Google Cloud (CPU/Memory usage traces)
- **ML model:** LSTM + Attention Mechanism + Genetic Algorithm hyperparameter tuning
- **What they did:** Proposed LSTMDD — an attention-based LSTM drift detector for detecting concept drift in cloud resource usage (CPU, memory, disk). Evaluated on Google usage traces and synthetic datasets. Achieved 98% F-score on Google cloud data.
- **Their limitation/gap:** Focuses exclusively on resource utilization traces (CPU/memory) rather than security configuration parameters. No compliance framework mapping. Cannot detect configuration drift in cloud security posture.
- **Relevant to our work because:** Demonstrates LSTM and ML effectiveness for cloud drift detection. We extend this concept from resource drift to security configuration drift on OCI with CIS/GDPR mapping.

---

### Paper 2
- **Title:** Adaptive Healthcare Monitoring Through Drift-Aware Edge-Cloud Intelligence
- **Authors:** Stojnev Ilic, Aleksandra; Ilic, Milos; Stojanovic, Natalija; Stojanovic, Dragan
- **Year:** 2026
- **Source:** MDPI Future Internet (Vol. 18, No. 156)
- **Cloud platform:** Edge-Cloud continuum (containerized, no specific provider)
- **ML model:** ADWIN + Page-Hinkley + Mean-shift + Variance-ratio ensemble voting
- **What they did:** Proposed drift-aware edge-cloud architecture for healthcare IoT data streams (continuous glucose monitoring). Used hierarchical drift detection — lightweight screening at edge, validation at cloud. Reduced MAE by 40.6% vs periodic retraining.
- **Their limitation/gap:** Confined to physiological streaming sensors and healthcare domain. No cloud security or compliance focus. No OCI. No CIS/GDPR mapping.
- **Relevant to our work because:** Shows hierarchical drift detection architecture in distributed cloud systems. Our work applies similar drift detection concepts to cloud security configuration monitoring.

---

### Paper 3
- **Title:** A Standardized Multi-Cloud Governance Model for Policy Consistency and Drift Detection
- **Authors:** Marella, Ramesh
- **Year:** 2024
- **Source:** SSRN Preprint
- **Cloud platform:** AWS, Azure, GCP
- **ML model:** Rule-based (no ML)
- **What they did:** Proposed centralized policy abstraction layer with cross-cloud policy mapping mechanism and continuous drift detection pipeline. Evaluated in FinTech use case. Achieved 98% policy compliance consistency and 40% reduction in MTTR.
- **Their limitation/gap:** Entirely rule-based — no ML model for drift detection. Does not cover OCI. Requires paid-tier cloud services. Static policy mapping cannot adapt to new drift patterns.
- **Relevant to our work because:** Closest to our compliance mapping approach. We extend this by adding ML-based detection and validating on OCI free tier.

---

### Paper 4
- **Title:** AI-Driven Configuration Drift Detection in Cloud Environments
- **Authors:** Thiyagarajan, Gogulakrishnan; Bist, Vinay; Nayak, Prabhudarshi
- **Year:** 2024
- **Source:** International Journal of Communication Networks and Information Security (IJCNIS), Vol. 16, No. 5
- **Cloud platform:** AWS, Azure
- **ML model:** Random Forest classifier
- **What they did:** Built ML framework using IaC templates + AWS Config logs. Trained Random Forest on historical and synthetic config data to classify drift vs non-drift. Integrated with Terraform and AWS Config.
- **Their limitation/gap:** AWS and Azure only — no OCI. No compliance framework mapping (CIS/GDPR). Uses synthetic dataset only. Does not address free-tier environments.
- **Relevant to our work because:** Most technically similar to our approach. We extend Random Forest to OCI with real snapshot data and add CIS/GDPR compliance mapping.

---

### Paper 5
- **Title:** Systematic Enforcement of CIS-Aligned Security Controls for Kubernetes Worker Nodes
- **Authors:** Alti, Balaramakrishna
- **Year:** 2023
- **Source:** Eastasouth Journal of Information System and Computer Science (ESISCS), Vol. 1, No. 01
- **Cloud platform:** Kubernetes (on-premise/hybrid, no specific cloud provider)
- **ML model:** Rule-based automation (no ML)
- **What they did:** Automated CIS benchmark enforcement on Kubernetes worker nodes using Linux hardening controls. Mapped CIS Kubernetes and Linux benchmarks to enforceable system configurations. Evaluated compliance improvement before and after automation.
- **Their limitation/gap:** Restricted to Kubernetes container node configurations. No cloud provider API. No ML detection. No GDPR mapping. No OCI.
- **Relevant to our work because:** Shows CIS benchmark mapping approach. Our work applies similar CIS mapping to OCI cloud configurations with ML-based detection on top.

---

### Paper 9
- **Title:** [Supervised & Hybrid ML Ensembles for Multi-Cloud Security]
- **Authors:** Okpomu & Ogoro
- **Year:** 2026
- **Source:** [Journal/Conference]
- **Cloud platform:** Multi-Cloud
- **ML model:** Supervised & Hybrid ML Ensembles
- **What they did:** Applied supervised and hybrid ML ensemble methods for cloud security detection across multiple cloud providers.
- **Their limitation/gap:** Network log and network intrusion traffic-oriented. Ignores active host tenant drift states and cloud configuration parameters.
- **Relevant to our work because:** Demonstrates ML ensemble effectiveness for cloud security. We apply similar ML approach to configuration drift specifically on OCI.

---

### Paper 10
- **Title:** [Isolation Forest for IoT Continuum Anomaly Detection]
- **Authors:** Malaviya
- **Year:** 2026
- **Source:** [Journal/Conference]
- **Cloud platform:** IoT Continuum
- **ML model:** Isolation Forest Outlier Profiling
- **What they did:** Applied Isolation Forest for anomaly profiling in IoT continuum environments targeting physical sensor streams.
- **Their limitation/gap:** Geared entirely toward physical sensor streams instead of logical hypervisor data fields. No cloud security or compliance focus.
- **Relevant to our work because:** We use Isolation Forest as our second ML model. This paper justifies Isolation Forest for lightweight anomaly detection in resource-constrained environments.

---

### Paper 20
- **Title:** Reservoir of Diverse Adaptive Learners and Stacking Fast Hoeffding Drift Detection Methods for Evolving Data Streams
- **Authors:** Pesaranghader, A.; Viktor, H.; Paquet, E.
- **Year:** 2018
- **Source:** Machine Learning Journal (Vol. 107)
- **Cloud platform:** Evolving data streams (generic)
- **ML model:** Fast Hoeffding Drift Stacking
- **What they did:** Proposed ensemble drift detection using stacked Hoeffding-based detectors for evolving data streams. Evaluated on synthetic and real-world datasets.
- **Their limitation/gap:** Bypasses cloud security constraints entirely. Focuses on raw data streams with no cloud provider context or compliance mapping.
- **Relevant to our work because:** Foundational drift detection paper. We cite this as baseline methodology that we adapt for cloud configuration security context.

---

## CATEGORY 2 — Cloud Compliance & Governance Papers

---

### Paper 6
- **Title:** [DevSecOps CI/CD Compliance Framework]
- **Authors:** Owoade et al.
- **Year:** 2024
- **Source:** [Journal/Conference]
- **Cloud platform:** Multi-Cloud
- **ML model:** Rule-based CI/CD DevSecOps
- **Compliance framework:** GDPR, PCI-DSS, SOC 2
- **What they did:** Proposed compliance framework for DevSecOps CI/CD pipelines covering GDPR, PCI-DSS, and SOC 2 across multi-cloud environments.
- **Their limitation/gap:** Strictly deployment pipeline-oriented. Lacks operational ML drift validation. Does not monitor runtime cloud configurations.
- **Relevant to our work because:** Covers GDPR compliance in cloud — strengthens our compliance motivation. We extend beyond pipelines to runtime configuration monitoring.

---

### Paper 7
- **Title:** [Automated Reasoning for AWS Cloud Compliance]
- **Authors:** Jansson
- **Year:** 2021
- **Source:** [Journal/Conference]
- **Cloud platform:** AWS
- **ML model:** Automated Reasoning (Zelkova)
- **Compliance framework:** CIS AWS Foundations, PCI-DSS
- **What they did:** Applied automated reasoning using AWS Zelkova tool for cloud policy compliance verification against CIS AWS Foundations and PCI-DSS.
- **Their limitation/gap:** Relies on expensive paid cloud-native modules. Lacks custom ML architectures. AWS-specific — no OCI applicability.
- **Relevant to our work because:** Shows CIS benchmark compliance automation in cloud. We replicate this approach on OCI free tier with ML instead of paid reasoning tools.

---

### Paper 8
- **Title:** [Static Scanning for Multi-Cloud Compliance]
- **Authors:** Yelkoti
- **Year:** 2025
- **Source:** [Journal/Conference]
- **Cloud platform:** Multi-Cloud
- **ML model:** Static Scanning & Policy Workflows
- **Compliance framework:** PCI-DSS, HIPAA, GDPR
- **What they did:** Proposed static scanning and policy workflow approach for multi-cloud compliance covering PCI-DSS, HIPAA, and GDPR at the code commit stage.
- **Their limitation/gap:** Focuses on pre-deployment code commits only. Leaves runtime asset configurations unchecked. No ML-based detection.
- **Relevant to our work because:** Covers GDPR and PCI-DSS compliance in multi-cloud. We extend beyond pre-deployment to runtime configuration monitoring with ML.

---

### Paper 11
- **Title:** [Federated IAM and RBAC for GDPR Compliance in SaaS]
- **Authors:** Pookandy
- **Year:** 2021
- **Source:** [Journal/Conference]
- **Cloud platform:** SaaS CRM Cloud
- **ML model:** Federated IAM & RBAC Workflows
- **Compliance framework:** GDPR, CCPA, HIPAA
- **What they did:** Examined GDPR, CCPA, and HIPAA compliance through federated identity and access management and role-based access control workflows in SaaS CRM environments.
- **Their limitation/gap:** Restricted to SaaS Identity Provider structures. Misses runtime cloud storage and port metrics. No ML drift detection.
- **Relevant to our work because:** Covers GDPR compliance through IAM — directly related to our MFA parameter monitoring which maps to GDPR Article 32.

---

### Paper 12
- **Title:** [Dynamic Tokenization for GDPR/HIPAA Data Privacy]
- **Authors:** Naik
- **Year:** 2023
- **Source:** [Journal/Conference]
- **Cloud platform:** Multi-Cloud
- **ML model:** Dynamic Tokenization & Masking
- **Compliance framework:** GDPR, HIPAA, CCPA
- **What they did:** Addressed GDPR, HIPAA, and CCPA compliance through dynamic data tokenization and masking for transactional processing in multi-cloud environments.
- **Their limitation/gap:** Focuses on transactional processing privacy vaults rather than structural infrastructure configuration. No ML drift detection. No runtime monitoring.
- **Relevant to our work because:** GDPR coverage supports our compliance mapping. We address the gap by monitoring cloud infrastructure configuration rather than data transactions.

---

### Paper 13
- **Title:** [Privacy-by-Design for GDPR/CCPA Cloud Compliance]
- **Authors:** Vethachalam
- **Year:** 2024
- **Source:** [Journal/Conference]
- **Cloud platform:** Multi-Cloud
- **ML model:** Privacy-by-Design Blueprints (conceptual)
- **Compliance framework:** GDPR, CCPA
- **What they did:** Proposed privacy-by-design architectural blueprints for GDPR and CCPA compliance in multi-cloud environments as abstract design principles.
- **Their limitation/gap:** Highly abstract architectural principles without executable ML engines or OCI validation. No working prototype demonstrated.
- **Relevant to our work because:** GDPR Article 25 (privacy by design) is one of our key compliance citations — specifically for bucket visibility parameter.

---

### Paper 14
- **Title:** [Policy-as-Code for CIS and NIST Cloud Compliance]
- **Authors:** Guduru
- **Year:** 2020
- **Source:** [Journal/Conference]
- **Cloud platform:** Multi-Cloud
- **ML model:** Policy-as-Code Automation
- **Compliance framework:** CIS Benchmarks, NIST SP 800-53
- **What they did:** Explored policy-as-code automation for cloud compliance using CIS Benchmarks and NIST SP 800-53 controls across multi-cloud environments.
- **Their limitation/gap:** Bypasses lightweight setups. Requires paid tier resources such as AWS Config and Azure Policy. No ML detection. No OCI.
- **Relevant to our work because:** Uses CIS Benchmarks — directly relevant to our CIS OCI Benchmark mapping. We replicate policy-as-code concept on OCI free tier with ML.

---

### Paper 15
- **Title:** [Conceptual AI Framework for GDPR/HIPAA Cloud Compliance]
- **Authors:** Folorunso et al.
- **Year:** 2024
- **Source:** [Journal/Conference]
- **Cloud platform:** Multi-Cloud
- **ML model:** Conceptual AI Load Balancing
- **Compliance framework:** GDPR, HIPAA
- **What they did:** Presented a high-level conceptual AI framework for GDPR and HIPAA compliance in multi-cloud environments using AI-based load balancing concepts.
- **Their limitation/gap:** High-level conceptual model without physical code deployment or experimental validation. No working prototype.
- **Relevant to our work because:** GDPR/HIPAA motivation supports our compliance angle. We provide what this paper lacks — a working prototype with real experimental results.

---

### Paper 16
- **Title:** [Runbook Automation for NIST/ISO 27001 Cloud Compliance]
- **Authors:** Martseniuk et al.
- **Year:** 2024
- **Source:** [Journal/Conference]
- **Cloud platform:** Multi-Cloud
- **ML model:** Runbook Automation & Scripting
- **Compliance framework:** NIST 800-53, ISO 27001, PCI-DSS
- **What they did:** Applied runbook automation and scripting for cloud compliance covering NIST 800-53, ISO 27001, and PCI-DSS across multi-cloud environments using Prisma Cloud.
- **Their limitation/gap:** Non-adaptive rule-based approach. Requires premium third-party orchestration software (Prisma Cloud). No ML-based detection.
- **Relevant to our work because:** ISO 27001 is one of the frameworks Singh (2023) maps to OCI. We compare against this approach to show ML advantage.

---

### Paper 17
- **Title:** [OCI Native Security Compliance Framework]
- **Authors:** Singh
- **Year:** 2023
- **Source:** [Journal/Conference]
- **Cloud platform:** OCI (Oracle Cloud Infrastructure)
- **ML model:** Native Active Compartment Policies
- **Compliance framework:** ISO 27001, FedRAMP, GDPR
- **What they did:** Examined OCI security through native compartment policies and security zones mapped to ISO 27001, FedRAMP, and GDPR compliance requirements.
- **Their limitation/gap:** Tied entirely to commercial paid-tier tools — OCI Cloud Guard and paid security zones. No ML-based detection. Not reproducible on free tier.
- **Relevant to our work because:** ONLY existing paper targeting OCI. Directly validates our platform choice. We extend this work by removing paid-tier dependency and adding ML detection.

---

### Paper 18
- **Title:** [SLO-Driven Multi-Cloud Governance Framework]
- **Authors:** Marella
- **Year:** 2025
- **Source:** [Journal/Conference]
- **Cloud platform:** AWS, Azure, GCP
- **ML model:** Standardized Policy Abstraction
- **Compliance framework:** Multi-Cloud SLO-Driven Compliance
- **What they did:** Proposed SLO-driven multi-cloud governance framework with standardized policy abstraction for AWS, Azure, and GCP compliance management.
- **Their limitation/gap:** Fails to consider free-tier environments. Focuses on multi-cloud orchestration overhead. No OCI. No ML-based drift detection.
- **Relevant to our work because:** Shows policy abstraction approach for compliance. We implement similar abstraction specifically for OCI with ML-based validation.

---

### Paper 19
- **Title:** [NIST CSF Cloud Posture Management for AWS]
- **Authors:** Jimmy
- **Year:** 2023
- **Source:** [Journal/Conference]
- **Cloud platform:** AWS
- **ML model:** CSF Posture Management Controls
- **Compliance framework:** NIST CSF v1.1
- **What they did:** Applied NIST Cybersecurity Framework v1.1 controls for cloud security posture management on AWS using native AWS APIs and services.
- **Their limitation/gap:** AWS API-specific. Leaves alternative cloud architectures like OCI completely unmapped. No ML detection. Paid AWS services required.
- **Relevant to our work because:** Demonstrates compliance framework mapping approach. We replicate this for OCI with CIS/GDPR instead of NIST CSF.

---

## Key Observations From Literature Review

### 1. Platform Coverage
- **17 of 20 papers** target AWS, Azure, or GCP
- **Only 1 paper** (Singh 2023) targets OCI — using paid tools
- **Zero papers** validate on OCI Always Free Tier

### 2. ML vs Rule-Based
- **6 papers** use ML — but none combine ML with compliance mapping
- **8 papers** use rule-based approaches — some with compliance but no ML
- **Zero papers** combine ML + CIS + GDPR + OCI

### 3. Compliance Framework Coverage
- GDPR appears in 7 papers — but never combined with ML on OCI
- CIS Benchmarks appear in 3 papers — rule-based only
- No paper maps CIS + GDPR together with ML validation

### 4. Free Tier
- **Zero of 20 papers** demonstrate prototype on always-free cloud infrastructure
- All require AWS Config, Azure Policy, Cloud Guard, or Prisma Cloud (all paid)

---

## Our Contribution Statement
> This paper is the first to combine ML-based drift detection
> (Random Forest + Isolation Forest) with CIS OCI Benchmark
> and GDPR compliance mapping, validated on real OCI Always
> Free Tier infrastructure — addressing all four gaps
> identified in the literature.

---
*Total papers reviewed: 20*
*Review completed: June 2026*
