# Literature Review Notes

## Papers Read

### Paper 1
- **Title:**
- **Authors:**
- **Year:**
- **Source:** (IEEE/Springer/ACM)
- **Cloud platform used:** (AWS/Azure/GCP/None)
- **ML model used:** (if any)
- **What they did:**
- **Their limitation/gap:**
- **Relevant to our work because:**

---
Paper 1
Title: LSTMDD: An Optimized LSTM-based Drift Detector for 
       Concept Drift in Dynamic Cloud Computing
Authors: Mehmood et al.
Year: 2024
Source: PeerJ Computer Science
Cloud platform: Google Cloud (usage traces)
ML model: LSTM + Attention Mechanism + Genetic Algorithm
What they did: Detected concept drift in cloud CPU/memory 
  resource usage using LSTM with attention mechanism
Their gap: Focuses on resource usage drift (CPU/memory), 
  NOT security configuration drift. No compliance mapping.
Relevant because: Proves ML works for cloud drift detection — 
  we extend this concept to security config drift on OCI

Paper 2
  Title: Adaptive Healthcare Monitoring Through Drift-Aware 
       Edge-Cloud Intelligence
Authors: Stojnev Ilic et al.
Year: 2026
Source: MDPI Future Internet
Cloud platform: Edge-Cloud (containerized, no specific provider)
ML model: Linear Regression + ADWIN + Page-Hinkley ensemble
What they did: Drift-aware architecture for healthcare IoT 
  data streams using edge-cloud hierarchy
Their gap: Healthcare domain only, no cloud security or 
  compliance focus, no OCI
Relevant because: Shows drift detection in distributed 
  cloud systems — our work applies similar concepts 
  to compliance monitoring

Paper 3
  Title: A Standardized Multi-Cloud Governance Model for 
       Policy Consistency and Drift Detection
Authors: Marella R.
Year: 2024
Source: SSRN (preprint)
Cloud platform: AWS + Azure + GCP
ML model: Rule-based (no ML)
What they did: Proposed centralized policy abstraction layer 
  for drift detection across AWS/Azure/GCP with CIS/compliance mapping
Their gap: No ML model, no OCI, rule-based only, 
  no experimental validation with real data
Relevant because: Closest to our work — we add ML-based 
  detection and validate on OCI free tier

Paper 4
  Title: AI-Driven Configuration Drift Detection in Cloud Environments
Authors: Thiyagarajan, Bist, Nayak
Year: 2024
Source: IJCNIS Vol.16
Cloud platform: AWS + Azure
ML model: Random Forest
What they did: ML framework using IaC templates + AWS Config 
  logs to detect drift using Random Forest classifier
Their gap: AWS/Azure only, no OCI, no GDPR/CIS compliance 
  mapping, small synthetic dataset
Relevant because: Most similar technical approach to ours — 
  we extend Random Forest to OCI with real compliance mapping

Paper 5
  Title: Systematic Enforcement of CIS-Aligned Security Controls 
       for Kubernetes Worker Nodes
Authors: Alti, Balaramakrishna
Year: 2023
Source: Eastasouth Journal of Information System and Computer Science
Cloud platform: Kubernetes (on-premise/hybrid, no specific cloud)
ML model: None — rule-based automation only
What they did: Automated CIS benchmark enforcement on 
  Kubernetes worker nodes using Linux hardening controls
Their gap: Kubernetes/on-premise only, no cloud provider, 
  no ML detection, no GDPR mapping, no OCI
Relevant because: Shows CIS benchmark mapping approach — 
  our work applies similar CIS mapping to OCI cloud configs 
  with ML-based detection on top