# Paper Outline

## Title
Automated Cloud Compliance Drift Detection using Machine 
Learning: A Lightweight Framework on Oracle Cloud 
Infrastructure

## Authors
[Your Name], [Partner Name]
[College Name], Pune, Maharashtra, India

## Abstract (Draft — update after results)
Cloud compliance drift occurs when cloud configurations 
deviate from security and regulatory baselines, posing 
risks to organizations. Existing approaches rely on 
rule-based tools or ML models targeting AWS and Azure, 
with no lightweight framework for Oracle Cloud 
Infrastructure (OCI). This paper proposes an automated 
ML-based compliance drift detection framework on OCI 
Always Free Tier, monitoring five runtime configuration 
parameters mapped to CIS Benchmark and GDPR requirements. 
Using Random Forest and Isolation Forest classifiers 
trained on real OCI configuration snapshots, the system 
detects non-compliant configurations with [X]% accuracy. 
Results demonstrate that lightweight ML models can 
effectively automate compliance monitoring on 
resource-constrained cloud environments without requiring 
paid-tier services.

## 1. Introduction (Partner writes)
- 1.1 Background and motivation
- 1.2 Problem statement
- 1.3 Research contributions (3 bullet points)
- 1.4 Paper organization

## 2. Related Work (Both write — already drafted above)
- 2.1 Cloud configuration drift detection
- 2.2 ML-based anomaly detection in cloud
- 2.3 Compliance frameworks in cloud
- 2.4 OCI-specific security research
- 2.5 Research gap

## 3. Methodology (You write)
- 3.1 System architecture overview
- 3.2 OCI configuration collection
- 3.3 Feature engineering
- 3.4 ML model selection (RF + IF)
- 3.5 Evaluation metrics

## 4. Implementation (You write)
- 4.1 OCI Always Free Tier setup
- 4.2 Python + OCI SDK integration
- 4.3 Dataset generation and labeling
- 4.4 Model training and validation

## 5. Compliance Mapping (Partner writes)
- 5.1 CIS OCI Benchmark mapping
- 5.2 GDPR article mapping
- 5.3 Labeling framework

## 6. Results and Evaluation (You write)
- 6.1 Dataset description
- 6.2 Model performance (accuracy, precision, recall, F1)
- 6.3 Comparison: RF vs Isolation Forest
- 6.4 Confusion matrix analysis

## 7. Discussion (Both write)
- 7.1 Key findings
- 7.2 Limitations
- 7.3 Future work

## 8. Conclusion (Both write)

## References (20 papers + OCI docs)