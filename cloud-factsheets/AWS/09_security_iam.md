# AWS — Security & IAM Factsheet

---

## AWS IAM — Identity and Access Management

| Feature | Cost | Notes |
|---|---|---|
| IAM Users, Groups, Roles, Policies | Free | No charge for identity management |
| IAM Identity Center (SSO) | Free | Centralized access management |
| IAM Access Analyzer | Free | Identify unintended resource access |
| IAM Credential Report | Free | Audit user credentials |
| Service Control Policies (via AWS Organizations) | Free | — |

### Key Features
- Fine-grained JSON policies (Allow/Deny per action/resource)
- MFA enforcement, password policies
- Cross-account roles
- SAML 2.0 / OIDC federation
- Attribute-based access control (ABAC)
- Permission Boundaries
- AWS Organizations integration (SCPs)

---

## AWS KMS — Key Management Service

| Item | Free Tier | Paid Rate |
|---|---|---|
| AWS managed keys (SSE-S3, SSE-RDS, etc.) | Free | Free |
| Customer managed keys (per key/month) | 1 free key | $1.00/key/month |
| API requests (per 10,000) | 20,000/month free | $0.03 |
| Automatic key rotation | Included | — |
| Multi-region keys (per replica key/month) | — | $1.00 |
| External key material (BYOK, per key/month) | — | $1.00 |
| Custom key store (CloudHSM-backed, per key/month) | — | $1.00 |

### Key Features
- FIPS 140-2 validated HSMs
- Envelope encryption pattern
- Key policies + IAM + grants for access control
- CloudTrail audit of all key usage
- Integrates with 100+ AWS services

---

## AWS Secrets Manager

| Item | Free Tier | Paid Rate |
|---|---|---|
| Secret storage (per secret/month) | 30-day free trial | $0.40 |
| API calls (per 10,000) | 10,000 free/month | $0.05 |

### Key Features
- Automatic rotation (RDS, Redshift, DocumentDB, custom Lambda)
- Version staging (AWSCURRENT, AWSPENDING, AWSPREVIOUS)
- Cross-account secret sharing
- Resource-based policies
- Secrets Manager vs Parameter Store: Secrets Manager for rotation, SSM Parameter Store for simpler/cheaper storage

### SSM Parameter Store (alternative)
| Tier | Cost |
|---|---|
| Standard parameters (up to 10,000) | Free |
| Advanced parameters | $0.05/parameter/month |
| API interactions (standard) | Free (up to 4,000/month) |
| API interactions (beyond) | $0.05/10,000 |

---

## AWS Certificate Manager (ACM)

| Certificate Type | Cost |
|---|---|
| Public SSL/TLS certificates | Free |
| Private CA (Private Certificate Authority, per CA/month) | $400 |
| Private certificates issued (per certificate/month) | $0.75 (first 1,000/month free) |

### Key Features
- Auto-renewal for public certificates
- Wildcard certificates supported
- Integrates with ALB, CloudFront, API Gateway, ELB
- Private CA for internal PKI

---

## AWS WAF — Web Application Firewall

| Item | Cost |
|---|---|
| Web ACL (per month) | $5.00 |
| Rule (per rule/month) | $1.00 |
| Rule group (per rule group/month) | $1.00 |
| Web requests processed (per million) | $0.60 |
| Bot Control (per million requests) | $10.00 |
| Account Takeover Prevention (per 1,000 login attempts) | $10.00 |
| Fraud Control — ATP (per 1,000 attempts) | $10.00 |
| Captcha (per 1,000 CAPTCHA attempts) | $0.40 |

### Key Features
- Protects: ALB, API Gateway, CloudFront, AppSync, Cognito
- OWASP Top 10 rule groups (managed, $1.00/month extra)
- Rate-based rules, IP reputation lists, geo-blocking
- AWS Managed Rules (Core Rule Set free)
- Logs to CloudWatch, S3, Kinesis Firehose

---

## AWS Shield — DDoS Protection

| Tier | Cost | Coverage |
|---|---|---|
| AWS Shield Standard | Free | Automatic L3/L4 protection for all AWS resources |
| AWS Shield Advanced | $3,000/month per organization | L3/L4/L7 DDoS, 24/7 DRT team, cost protection |

### Shield Advanced Features
- 24/7 access to AWS DDoS Response Team (DRT)
- Real-time attack metrics and visibility
- Proactive engagement during known events
- Cost protection (credits for scaling during DDoS)
- WAF integration included (no extra WAF cost)

---

## Amazon GuardDuty — Threat Detection

| Item | Free Tier | Paid Rate |
|---|---|---|
| CloudTrail events analyzed (per million) | 30-day free trial | $4.00 |
| VPC Flow Logs analyzed (per GB) | 30-day free trial | $1.00 |
| DNS logs analyzed (per GB) | 30-day free trial | $1.00 |
| EKS Audit Logs (per million events) | 30-day free trial | $2.00 |
| S3 data events (per million events) | — | $0.80 |
| Malware Protection (per GB scanned) | — | $0.68 |
| Lambda network activity (per million invocations) | — | $1.00 |

### Key Features
- ML-based anomaly detection
- Threat intelligence feeds (AWS + third-party)
- Findings severity: Low, Medium, High, Critical
- Integrates with Security Hub, EventBridge for automated response

---

## AWS Security Hub — Centralized Security Findings

| Item | Free Tier | Paid Rate |
|---|---|---|
| Security checks (per check/month) | 30-day free trial | $0.0010 |
| Finding ingestion events (per 10,000/month) | 10,000 free | $0.00003 |

### Key Features
- Aggregates findings from GuardDuty, Inspector, Macie, IAM Access Analyzer, Firewall Manager
- CIS AWS Foundations Benchmark, PCI-DSS, AWS Foundational Security Standard
- Automated remediation via EventBridge

---

## Amazon Macie — S3 Data Discovery

| Item | Free Tier | Paid Rate |
|---|---|---|
| S3 bucket inventory and monitoring (per bucket/month) | 30-day free trial | $0.10 |
| Data discovery — sensitive data (per GB) | 1 GB/month free | $1.00 |

---

## Amazon Inspector — Vulnerability Management

| Item | Free Tier | Paid Rate |
|---|---|---|
| EC2 instances (per instance/month) | 30-day free trial | $1.31 |
| ECR container images (per image/month) | 30-day free trial | $0.09 |
| Lambda functions (per function/month) | 30-day free trial | $0.30 |
| Lambda code analysis (per function/month) | — | $0.69 |

---

## AWS CloudHSM — Hardware Security Modules

| Item | Cost |
|---|---|
| HSM instance (per HSM/hr) | $1.45 |
| Estimated monthly (1 HSM) | ~$1,044 |
| Minimum recommended (2 HSMs for HA) | ~$2,088/month |
| Data transfer OUT | Standard EC2 rates |

### Key Features
- FIPS 140-2 Level 3 certified hardware
- Single-tenant dedicated HSM
- Customer-controlled keys (AWS has no access)
- Used for: PKI, SSL offloading, custom key stores in KMS
- Must deploy in a cluster (2+ HSMs for HA)

---

*Prices are US East (N. Virginia) rates as of 2024.*
