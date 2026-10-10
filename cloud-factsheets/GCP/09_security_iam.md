# GCP — Security & IAM Factsheet

---

## Cloud IAM — Identity & Access Management

| Feature | Cost |
|---|---|
| IAM roles and policies | Free |
| IAM conditions | Free |
| Organization policies | Free |
| IAM deny policies | Free |
| IAM Recommender (unused permissions, per recommendation used) | $0.25 |
| IAM audit logs (Admin Activity) | Free (required logs) |
| IAM audit logs (Data Access) | Logging rates per GB |
| Workload Identity Federation (OIDC/SAML) | Free |
| Service accounts | Free |
| Managed identities for GKE (Workload Identity) | Free |

### Key IAM Concepts
- **Principals**: Google accounts, service accounts, Google Groups, Cloud Identity, Workspace domains
- **Roles**: Primitive (Owner/Editor/Viewer), Predefined (100s), Custom (user-defined)
- **Conditions**: attribute-based access (time, resource name, IP)
- **Organization hierarchy**: Organization → Folder → Project → Resource
- **IAM Deny**: explicitly deny access regardless of Allow policies
- **VPC Service Controls**: restrict API access to protect resources from exfiltration

---

## Cloud KMS — Key Management Service

### Key Ring & Key Operations
| Item | Cost |
|---|---|
| Active key versions (per version/month) | $0.06 |
| Active key versions (HSM-protected, per version/month) | $1.00 |
| Active key versions (External KMS, per version/month) | $3.00 |
| Cryptographic operations (AES, RSA, EC, per 10,000) | $0.03 |
| HSM cryptographic operations (per 10,000) | $0.15 |
| Destroyed key versions | Free |
| Key import (per key) | $0.01 |

### Encryption Standards Supported
| Algorithm | Key Type |
|---|---|
| AES-128, AES-256 (GCM, CBC) | Symmetric |
| RSA 2048, 3072, 4096 | Asymmetric sign/decrypt |
| EC P256, P384, secp256k1 | Asymmetric sign |

### Key Features
- Customer-managed encryption keys (CMEK) for all GCP services
- Envelope encryption (Google-managed DEK encrypted by CMEK)
- Key rotation (automatic, configurable schedule)
- Key versioning (previous versions retained for decryption)
- HSM-backed keys (FIPS 140-2 Level 3)
- External Key Manager (EKMS) — keys stored outside GCP
- Cloud EKM (partner HSMs: Thales, Fortanix, etc.)

---

## Secret Manager — Secure Secret Storage

| Item | Free Tier | Paid Rate |
|---|---|---|
| Active secret versions (per 10,000/month) | First 6 free | $0.06/10,000 |
| Access operations (per 10,000/month) | First 10,000 free | $0.03/10,000 |
| Rotation notifications (Pub/Sub) | Pub/Sub rates | — |

### Key Features
- Versioned secrets (no secret destruction on rotation)
- Automatic secret rotation (Cloud Functions or custom endpoint)
- Regional vs global secrets
- CMEK encryption support
- VPC Service Controls for data exfiltration protection
- IAM-based access (per-secret or per-project)
- Audit logging (Admin Activity and Data Access)
- Integration: Cloud Run, GKE (Workload Identity), Cloud Functions, App Engine

---

## Certificate Manager — SSL/TLS Certificates

| Item | Cost |
|---|---|
| Google-managed certificates (Global LB) | Free |
| Google-managed certificates (regional) | Free |
| Certificate Map entries (per entry/month) | $0.10 |
| DNS Authorization (per auth/month) | $0.10 |
| Self-managed certificates | Free (cert itself not charged) |

---

## Cloud Armor — WAF & DDoS Protection

See GCP/04_networking.md for full Cloud Armor pricing.

| Quick Reference | Cost |
|---|---|
| Security policy | $5/month |
| Security rule | $1/rule/month |
| Requests evaluated | $0.75/million |
| Managed Protection Plus | $0.70/resource/month |
| Bot Management | $1.00/million requests |

---

## Cloud Identity — Identity Management

| Tier | Cost/user/month | Key Features |
|---|---|---|
| Cloud Identity Free | Free | Basic SSO, device management (limited) |
| Cloud Identity Premium | $6.00 | MDM, advanced device management, endpoint verification |
| Google Workspace (Business Starter) | $6.00 | Gmail + Workspace apps + identity |
| Google Workspace (Business Standard) | $12.00 | + advanced Meet, Drive features |
| Google Workspace (Business Plus) | $18.00 | + eDiscovery, audit, retention |
| Google Workspace (Enterprise) | Custom | + advanced security, DLP, SIEM |

### Key Features
- SSO for 1,000+ SAML/OIDC apps
- Multi-factor authentication (TOTP, Push, hardware key FIDO2)
- Context-Aware Access (BeyondCorp Enterprise)
- Endpoint management (MDM — Android, iOS, Windows, Mac, Linux)
- Directory sync with LDAP/AD
- Google Groups for access management

---

## VPC Service Controls — Data Perimeters

| Item | Cost |
|---|---|
| Access policy (per organization) | Free |
| Service perimeters (per perimeter/month) | $0.10 |
| Access levels (per level/month) | $0.10 |

### Key Features
- Define security perimeters around GCP resources
- Prevent data exfiltration via API calls
- Ingress/egress rules for perimeter crossing
- Bridge perimeters (cross-project access within org)
- Supported services: BigQuery, Cloud Storage, Cloud KMS, Pub/Sub, etc.
- Dry-run mode (audit without enforcement)

---

## Binary Authorization — Supply Chain Security

| Item | Cost |
|---|---|
| Policy evaluation (per 10,000 evaluations) | $0.30 |
| Attestation storage | Container Analysis rates |

### Key Features
- Require signed container images before deployment
- Works with GKE, Cloud Run, GKE Enterprise
- Attestation-based policies (Voucher, Kritis, Cloud Build)
- Integration with Artifact Registry vulnerability scanning
- Audit-only mode for policy evaluation

---

## Chronicle SIEM — Security Information & Event Management

| Tier | Cost |
|---|---|
| Chronicle Standard | Custom (per user/month, or per GB ingested) |
| Chronicle Enterprise | Custom pricing |
| SOAR (Chronicle SOAR) | Included with Chronicle or separate license |

### Key Features
- Petabyte-scale log storage (12 months default retention)
- UDM (Unified Data Model) schema normalization
- 700+ log parsers (pre-built)
- Detection rules (YARA-L language)
- MITRE ATT&CK mapping
- Threat intelligence integration (VirusTotal, Google Threat Intel)
- Retroactive detections (search historical logs with new rules)
- Federated search (across multiple environments)
- SOAR: playbook automation, case management

---

## Access Context Manager (BeyondCorp)

| Item | Cost |
|---|---|
| Access levels and policies | Free |
| BeyondCorp Enterprise (per user/month) | $6.00 |

### BeyondCorp Enterprise Features
- Zero-trust access for web apps (no VPN required)
- Context-aware access (device posture, identity, location)
- Endpoint verification (managed vs unmanaged devices)
- IAP (Identity-Aware Proxy) enforcement
- Real-time threat protection integration

---

## Security Command Center (SCC)

| Tier | Cost |
|---|---|
| Standard tier | Free |
| Premium tier (per resource/month) | $0.06 |

### Standard Tier Includes
- Security Health Analytics (misconfigurations)
- Web Security Scanner (limited)
- Cloud Armor findings
- Anomaly detection

### Premium Tier Adds
- Event Threat Detection (malware, data exfiltration, brute force)
- Container Threat Detection
- VM Threat Detection
- Compliance dashboards (PCI-DSS, CIS, NIST)
- Attack exposure score
- Simulation-based attack path analysis

---

*Prices are global rates as of 2024.*
