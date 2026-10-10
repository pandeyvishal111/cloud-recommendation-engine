# GCP — Networking Factsheet

---

## Cloud Load Balancing

| Type | Layer | Scope | Cost/hr | Per Unit/hr | Best For |
|---|---|---|---|---|---|
| Global External HTTP(S) LB | 7 | Global | $0.008 | $0.006/GB (0–100 TB) | Multi-region web apps, CDN integration |
| Regional External HTTP(S) LB | 7 | Regional | $0.008 | $0.006/GB | Single-region web apps |
| External TCP/SSL Proxy LB | 4 | Global | $0.025 | $0.008/GB | TCP/SSL, non-HTTP global apps |
| External Network LB (pass-through) | 4 | Regional | Forwarding rule: $0.008/hr | $0.008/GB | Regional pass-through, UDP support |
| Internal HTTP(S) LB | 7 | Regional | $0.008 | $0.006/GB | Internal microservices, GKE ingress |
| Internal TCP/UDP LB | 4 | Regional | Forwarding rule: $0.008/hr | $0.008/GB | Internal TCP/UDP apps |
| Internal Passthrough NLB | 4 | Regional | $0.008/hr | $0.008/GB | Internal low-level traffic |
| Cross-Region Internal LB | 7 | Multi-region | $0.012/hr | $0.008/GB | Internal cross-region failover |

### Forwarding Rules
| Item | Cost |
|---|---|
| First 5 forwarding rules/month | Free |
| Additional forwarding rules (per rule/month) | $0.010 |

### Key Features
- Auto-scales to millions of requests per second
- No pre-warming required
- Global Anycast (Global LB)
- Health checks (HTTP, HTTPS, HTTP/2, TCP, SSL, gRPC)
- Backend services (GCE, GKE, Cloud Run, Cloud Functions, NEGs)
- URL maps, host rules, path matchers (HTTP LB)
- SSL certificate management (Google-managed, self-managed)
- Session affinity (client IP, generated cookie, header)

---

## Cloud CDN — Content Delivery Network

### Cache Egress to Internet
| Destination | 0–10 TB/month | 10–100 TB | 100 TB–1 PB | 1 PB+ |
|---|---|---|---|---|
| Americas / Europe | $0.08/GB | $0.06/GB | $0.05/GB | $0.04/GB |
| Asia Pacific | $0.12/GB | $0.10/GB | $0.07/GB | $0.05/GB |
| Oceania | $0.15/GB | $0.12/GB | $0.10/GB | $0.08/GB |

### Cache Fill (Backend → CDN)
| Scenario | Cost |
|---|---|
| Cache fill from GCP region (same as CDN PoP) | Free |
| Cache fill from GCP region (cross-region) | Standard network egress rates |

### CDN HTTP/HTTPS Requests
| Item | Cost per 10,000 |
|---|---|
| HTTP requests | $0.0075 |
| HTTPS requests | $0.009 |

### Key Features
- 200+ edge locations globally
- Integrates with Global External HTTP(S) LB
- Signed URLs / Signed Cookies (access control)
- Cache keys customization
- CDN Interconnect (reduced egress to partner CDNs)
- Cloud Armor integration (WAF at edge)
- HTTP/2 and HTTP/3 support

---

## Cloud DNS

| Feature | Cost |
|---|---|
| Managed zones (per zone/month, first 25) | $0.20 |
| Managed zones (per zone/month, beyond 25) | $0.10 |
| Authoritative queries (first billion/month) | $0.40/million |
| Authoritative queries (next 9 billion/month) | $0.20/million |
| DNSSEC | Free |
| Private zones (peering-enabled) | Standard zone rate |
| Cross-project visibility | Free |
| DNS Routing Policies (per routing policy/month) | $0.70 |
| DNS Routing Policy queries (per million) | $0.40 |
| Cloud DNS Forwarding (per million queries) | $0.40 |

---

## Cloud Interconnect — Dedicated Private Connectivity

### Dedicated Interconnect
| Port Speed | Monthly Port Cost | Data Transfer OUT/GB |
|---|---|---|
| 10 Gbps | $1,700 | $0.02 |
| 100 Gbps | $17,000 | $0.02 |

### Partner Interconnect
| Speed | Availability Type | Monthly Cost |
|---|---|---|
| 50 Mbps | Shared (Availability 1) | ~$50 |
| 100 Mbps | Shared | ~$100 |
| 200 Mbps | Shared | ~$200 |
| 500 Mbps | Shared | ~$500 |
| 1 Gbps | Shared | ~$500 |
| 2 Gbps | Dedicated | ~$1,000 |
| 5 Gbps | Dedicated | ~$2,500 |
| 10 Gbps | Dedicated | ~$5,000 |

**Data Transfer (Partner Interconnect):** $0.02/GB (same zone) to $0.08/GB (cross-region).

### Key Features
- VLAN attachments (connect Interconnect to VPC)
- BGP routing
- Redundant configuration (MACsec encryption on Dedicated)
- Cross-Cloud Interconnect (connect to AWS/Azure over dedicated link)
- Up to 8 VLAN attachments per Interconnect circuit

---

## Cloud VPN

| Type | Cost/tunnel/hr | Data Transfer |
|---|---|---|
| HA VPN (recommended) | $0.05 | Standard egress rates |
| Classic VPN (legacy) | $0.05 | Standard egress rates |

### VPN Recommendations
| Config | Tunnels | SLA |
|---|---|---|
| HA VPN (2 tunnels to same peer) | 2 | 99.99% |
| Classic VPN (single tunnel) | 1 | 99.9% |

### Key Features
- IKEv2 (HA VPN) / IKEv1+IKEv2 (Classic VPN)
- 3 Gbps per tunnel maximum
- Dynamic routing (Cloud Router + BGP required for HA VPN)
- Works with on-premises VPN gateways and peer VPN gateways

---

## Virtual Private Cloud (VPC)

### VPC Costs
| Feature | Cost |
|---|---|
| VPC creation | Free |
| Subnets, firewall rules, routes | Free |
| Cloud NAT (per NAT gateway/hr) | $0.044 |
| Cloud NAT (per GB processed) | $0.044 |
| VPC Peering (intra-region data transfer) | Free (standard VM egress still charged) |
| VPC Peering (cross-region) | Standard inter-region egress |
| Private Service Connect endpoints (per hr) | $0.01 |
| Private Service Connect (per GB) | $0.01 |
| Shared VPC | Free |
| VPC Flow Logs (per GB generated) | $0.50 |
| VPC Flow Logs (per GB analyzed via Log Analytics) | Log Analytics rates |
| Network Intelligence Center (per GB analyzed) | $0.05 |
| VPC Network Peering (same zone intra-VPC) | Free |

### Cloud Router (BGP Dynamic Routing)
| Item | Cost |
|---|---|
| Cloud Router uptime (per hr) | Free |
| Data transfer | Standard egress rates |

---

## Cloud Armor — WAF & DDoS Protection

| Feature | Cost |
|---|---|
| Security policy (per policy/month) | $5.00 |
| Security policy rule (per rule/month) | $1.00 |
| Requests evaluated (per million) | $0.75 |
| Managed Protection Plus (per resource/month) | $0.70 |
| Adaptive Protection (included in Plus) | Included |
| Bot Management (per million requests) | $1.00 |
| Threat Intelligence (per policy/month) | $2.00 |
| Edge Security Policy (for Cloud CDN/LB) | Standard policy rates |

### Preconfigured WAF Rules
- OWASP Top 10 rule sets (CRS 3.3)
- SQL injection, XSS, LFI, RFI, RCE, Scanner Detection
- Protocol attack rules
- Available as preconfigured rule sets ($1/rule/month)

---

## Network Egress Summary

| Scenario | Cost |
|---|---|
| Inbound (ingress) | Free |
| Same zone (internal traffic) | Free |
| Cross-zone, same region (internal) | $0.01/GB each direction |
| Cross-region (within GCP) | $0.01–$0.08/GB depending on regions |
| Egress to internet (Americas/Europe, 0–1 TB) | $0.12/GB |
| Egress to internet (Americas/Europe, 1–10 TB) | $0.11/GB |
| Egress to internet (Americas/Europe, 10+ TB) | $0.08/GB |
| Egress to internet (Asia Pacific) | $0.15/GB |
| Egress via Cloud Interconnect | $0.02/GB |
| Egress via HA VPN | $0.12/GB (standard internet rate) |

---

*Prices are us-central1 / global rates as of 2024.*
