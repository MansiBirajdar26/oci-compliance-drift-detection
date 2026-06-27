# Related Work

## 2.1 Cloud Configuration Drift Detection
Configuration drift in cloud environments has been studied 
from multiple angles. Thiyagarajan et al. (2024) proposed 
an AI-driven framework using Random Forest classifiers on 
AWS Config logs to detect deviations from IaC-defined 
baselines, demonstrating that ML can automate drift 
detection effectively. However, their work targets AWS 
and Azure exclusively and does not map detected drift to 
regulatory compliance frameworks. Marella (2024) proposed 
a standardized multi-cloud governance model with a 
centralized policy abstraction layer for drift detection 
across AWS, Azure, and GCP, but relies on static rule-based 
mapping without ML-based detection. Guduru (2020) explored 
policy-as-code automation using CIS Benchmarks and NIST 
controls but requires paid-tier resources such as AWS 
Config and Azure Policy, limiting accessibility.

## 2.2 ML-Based Anomaly Detection in Cloud
Several studies apply machine learning to detect anomalies 
in cloud environments. Mehmood et al. (2024) proposed 
LSTMDD, an attention-based LSTM drift detector evaluated 
on Google Cloud usage traces, achieving 98% F-score for 
CPU and memory drift detection. Okpomu and Ogoro (2026) 
applied supervised and hybrid ML ensembles for cloud 
security, though their focus remains on network intrusion 
traffic rather than configuration parameters. Malaviya 
(2026) applied Isolation Forest for anomaly profiling in 
IoT continuum environments, demonstrating its suitability 
for lightweight outlier detection. While these works 
demonstrate the potential of ML for cloud anomaly 
detection, none apply ML to security configuration drift 
mapped against compliance standards.

## 2.3 Compliance Frameworks in Cloud Environments
Regulatory compliance in cloud environments has received 
growing attention. Vethachalam (2024) proposed 
privacy-by-design blueprints for GDPR and CCPA compliance 
in multi-cloud environments but presents abstract 
architectural principles without executable ML engines. 
Naik (2023) addressed GDPR, HIPAA, and CCPA through 
dynamic tokenization and data masking, focusing on 
transactional privacy rather than infrastructure 
configuration. Pookandy (2021) examined GDPR compliance 
through federated IAM and RBAC workflows in SaaS CRM 
environments but overlooks runtime cloud storage and 
network metrics. Alti (2023) presented CIS benchmark 
enforcement for Kubernetes worker nodes through automation, 
demonstrating the feasibility of benchmark-aligned 
security hardening, though restricted to container 
orchestration environments rather than cloud provider APIs.

## 2.4 OCI-Specific Security Research
Research targeting Oracle Cloud Infrastructure remains 
sparse. Singh (2023) examined OCI security through native 
compartment policies mapped to ISO 27001, FedRAMP, and 
GDPR, but relies entirely on paid-tier OCI Cloud Guard 
and security zones. No existing study proposes an 
ML-based drift detection framework validated on OCI 
Always Free Tier infrastructure.

## 2.5 Research Gap
The reviewed literature reveals that existing work either 
applies ML without compliance mapping, implements 
compliance frameworks without ML detection, or targets 
AWS and Azure while leaving OCI underrepresented. 
Furthermore, all existing frameworks depend on paid-tier 
cloud services, limiting reproducibility. No study 
combines ML-based drift detection with CIS Benchmark and 
GDPR compliance mapping on OCI free-tier infrastructure. 
This paper addresses these gaps by proposing a lightweight 
framework that monitors 5 runtime OCI configuration 
parameters, trains Random Forest and Isolation Forest 
classifiers on real snapshot data, and validates results 
against CIS OCI Benchmark controls and GDPR requirements.