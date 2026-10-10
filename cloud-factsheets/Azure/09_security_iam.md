# Azure — Security & IAM Factsheet

---

## Microsoft Entra ID (formerly Azure Active Directory)

| Tier | Cost/user/month | Key Features |
|---|---|---|
| Free | Free (up to 500,000 objects) | SSO for SaaS apps, MFA, basic reporting |
| Microsoft 365 Apps | Free (with M365 license) | Core identity for M365 |
| P1 | $6.00 | Conditional Access, self-service password reset, hybrid identity, MFA (full) |
| P2 | $9.00 | All P1 + Identity Protection (risk-based CA), Privileged Identity Management (PIM), Access Reviews |

### Key Features
- SSO for 3,000+ SaaS applications
- SAML 2.0, OAuth 2.0, OpenID Connect, WS-Federation
- B2B guest access, B2C (external identities)
- Managed Identities for Azure resources (no credential management)
- Workload identities (service principals, managed identities)
- External ID (customer-facing apps with social login)

### Microsoft Entra External ID (B2C)
| Item | Free Tier | Paid Rate |
|---|---|---|
| Monthly Active Users (MAUs) | First 50,000 MAUs free | $0.01625/MAU after |
| MFA (per authentication) | First 50,000 free | $0.0025 |
| Phone OTP (per verification) | — | $0.03 |

---

## Azure Key Vault — Secrets, Keys, Certificates

### Standard Tier (Software-protected keys)
| Item | Free | Paid Rate |
|---|---|---|
| Secrets operations (per 10,000) | 10,000/month free | $0.03 |
| Key operations — RSA/EC software (per 10,000) | 10,000/month free | $0.03 |
| Certificate operations (per 10,000) | 10,000/month free | $3.00 |
| Certificates (per certificate/month) | — | $3.00 |
| Managed Storage Account keys (per renewal) | — | $1.00 |

### Premium Tier (HSM-protected keys)
| Item | Paid Rate |
|---|---|
| HSM-protected key (per key/month) | $1.00 |
| RSA-HSM / EC-HSM operations (per 10,000) | $0.15 |
| Advanced threat protection (per vault/month) | $0.02 |

### Managed HSM (Dedicated HSM Pool)
| Item | Cost |
|---|---|
| Managed HSM pool (per pool/hr) | $1.73 |
| Est. $/month | ~$1,246 |
| Best For | FIPS 140-2 Level 3 compliance, dedicated tenancy |

### Key Features
- Centralized secrets management
- Auto-rotation integration with Azure services
- Access policies + RBAC
- Soft delete + purge protection (accidental deletion prevention)
- Certificates: auto-renewal with DigiCert, GlobalSign integration
- Private endpoint support
- Integrates with AKS, App Service, VMs, Azure ML

---

## Azure DDoS Protection

| Tier | Cost | Coverage |
|---|---|---|
| Network (Basic) | Free | Always-on, automatic protection for all Azure public IPs |
| Network (Standard) | ~$2,944/month per virtual network | Enhanced mitigation, attack analytics, 24/7 DRT access, cost guarantee |
| IP Protection (per protected IP/month) | $199 | Per-IP protection without full VNet commitment |

### DDoS Standard Features
- Real-time attack metrics and alerts
- Attack reports and flow logs post-attack
- Azure DDoS Response Team (DRT) 24/7
- Cost guarantee (credit for scaled-out resources during attacks)
- Adaptive tuning based on traffic patterns
- WAF integration via Application Gateway/Front Door

---

## Azure WAF — Web Application Firewall

WAF is deployed with Application Gateway or Front Door.

### WAF on Application Gateway
| SKU | Cost/hr | Capacity Unit/hr |
|---|---|---|
| WAF v2 | $0.443 | $0.014/CU |

### WAF on Azure Front Door
| Item | Cost |
|---|---|
| WAF policy (per policy/month) | $5.00 |
| Custom WAF rules (per rule/month) | $1.00 |
| Managed rule sets (per policy/month) | $20.00 |
| WAF requests processed (per million) | $0.60 |
| Bot protection (per million requests) | $10.00 |

### OWASP Managed Rule Sets
- Default Rule Set (DRS) 2.1 — OWASP Core Rule Set 3.2 equivalent
- Microsoft Threat Intelligence rule set (Front Door Premium)
- Geographic filtering, rate limiting, IP allow/block lists

---

## Microsoft Defender for Cloud

### Free (Foundational CSPM)
| Feature | Cost |
|---|---|
| Azure Security Benchmark assessment | Free |
| Secure Score | Free |
| Azure Defender for Cloud Apps (discovery only) | Free |
| Security recommendations | Free |

### Defender Plans (Enhanced)
| Workload | Plan | Cost |
|---|---|---|
| Servers | Plan 1 | $5/server/month |
| Servers | Plan 2 | $15/server/month |
| Azure SQL Databases | — | $15/server/month |
| SQL Server on Machines | — | $15/server/month |
| Open-Source Relational DBs | — | $0.015/vCore/month |
| Cosmos DB | — | $0.007/100 RU-hr |
| Storage | — | $10/storage account/month |
| App Service | — | $15/App Service plan/month |
| Key Vault | — | $0.02/10K transactions |
| Azure Resource Manager | — | $4/subscription/month |
| DNS | — | $0.90/subscription/month |
| Containers (AKS, ACR, Docker hosts) | — | $7/vCore/month (AKS) + $0.29/image (ACR) |
| APIs | — | $0.90/million API calls |

### Defender CSPM (Premium)
| Feature | Cost |
|---|---|
| Per billable resource/month | $0.01 |
| Attack path analysis | Included |
| Agentless vulnerability scanning | Included |
| Data security posture | Included |

---

## Azure Policy

| Feature | Cost |
|---|---|
| Azure Policy definitions and assignments | Free |
| Policy compliance evaluations | Free |
| Guest Configuration (per node/month) | $0.50 (beyond free 6 VMs/subscription) |
| Regulatory compliance dashboards | Free |
| Custom policy definitions | Free |

---

## Microsoft Sentinel — SIEM & SOAR

### Log Analytics Ingestion (Sentinel adds on top)
| Item | Cost |
|---|---|
| Sentinel data ingestion (per GB/day, PAYG) | $2.46 |
| Commitment Tier 100 GB/day | ~$2.00/GB (effective) |
| Commitment Tier 200 GB/day | ~$1.95/GB (effective) |
| Commitment Tier 500 GB/day | ~$1.68/GB (effective) |
| Commitment Tier 1,000 GB/day | ~$1.52/GB (effective) |
| Commitment Tier 2,000 GB/day | ~$1.37/GB (effective) |
| Free data sources (M365 Defender, Azure AD, Activity) | Free (500 MB/workspace/day) |
| Automation (Logic Apps playbooks, per execution) | Logic Apps rates |
| SOAR playbooks (Logic App runs) | Logic Apps Consumption rates |

### Sentinel Features
- Built-in connectors (100+ data sources)
- KQL-based queries and analytics rules
- MITRE ATT&CK framework coverage mapping
- Workbooks (dashboards)
- Hunting queries
- Entity behavior analytics (UEBA)
- Threat Intelligence import
- Incident management workflow

---

## Azure Private DNS

| Feature | Cost |
|---|---|
| Private DNS zone (per zone/month) | $0.50 (first 25 zones) / $0.10 (beyond 25) |
| DNS queries (per million) | $0.40 |
| Virtual network links (per link/month) | $0.10 |

---

*Prices are East US pay-as-you-go rates as of 2024.*
