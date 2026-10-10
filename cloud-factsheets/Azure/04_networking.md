# Azure — Networking Factsheet

---

## Azure Load Balancer

| Tier | Cost | Features | Best For |
|---|---|---|---|
| Basic | Free | No SLA guarantees, limited features | Dev/test only |
| Standard | $0.005/hr per rule + $0.004/GB processed | Zone-redundant, 99.99% SLA, health probes | Production workloads |

### Standard Load Balancer Details
| Item | Cost |
|---|---|
| Load Balancer rules (per hr, first 5 rules) | $0.005 |
| Load Balancer rules (per hr, beyond 5) | $0.005 per additional rule |
| Data processed (per GB) | $0.004 |
| Outbound rules | Included |
| Global Load Balancer (cross-region, per hr) | $0.009 |
| Global LB data processed (per GB) | $0.006 |

### Key Features
- Layer 4 (TCP/UDP) load balancing
- Zone-redundant and zonal frontends
- HA ports rule (all ports/all protocols on one rule)
- Inbound and outbound NAT rules
- Internal (private) and External (public) configurations

---

## Azure Application Gateway — Layer 7 Load Balancer

| Tier | Fixed Cost/hr | Capacity Unit/hr | Best For |
|---|---|---|---|
| Standard v2 | $0.246 | $0.008/CU | Web apps without WAF |
| WAF v2 | $0.443 | $0.014/CU | Web apps with WAF protection |

### Capacity Units (CU) — 1 CU covers:
- 2,500 persistent connections
- 2.22 Mbps throughput
- 1 compute unit (1 connection/sec TLS or ~10 req/sec non-TLS)

### Application Gateway Features
- SSL/TLS termination and end-to-end SSL
- Cookie-based session affinity
- URL-based routing, multi-site hosting
- HTTP to HTTPS redirect
- WebSocket and HTTP/2 support
- Integration with Azure Key Vault (SSL certs)

---

## Azure CDN — Content Delivery Network

### Microsoft CDN
| Data Volume | Americas/Europe ($/GB) | Asia Pacific ($/GB) |
|---|---|---|
| First 10 TB/month | $0.087 | $0.138 |
| Next 40 TB | $0.083 | $0.130 |
| Next 100 TB | $0.072 | $0.118 |
| Next 350 TB | $0.060 | $0.100 |
| Over 500 TB | $0.044 | $0.080 |

### Verizon Standard CDN
| Data Volume | Americas/Europe ($/GB) |
|---|---|
| First 10 TB/month | $0.223 |
| Next 40 TB | $0.178 |
| Next 100 TB | $0.148 |

### Verizon Premium CDN
| Data Volume | Americas/Europe ($/GB) |
|---|---|
| First 10 TB/month | $0.466 |
| Next 40 TB | $0.374 |

### CDN HTTP Requests
| Provider | Per 10,000 requests |
|---|---|
| Microsoft CDN | $0.0075 |
| Verizon Standard | $0.011 |
| Verizon Premium | $0.011 |

---

## Azure Front Door — Global HTTP LB + CDN

### Classic
| Item | Cost |
|---|---|
| Routing rules (per month, first 5) | $0 |
| Routing rules (per month, beyond 5) | $5 each |
| Data transfer (per GB, Zone 1) | $0.087 |
| Inbound data | $0.025/GB |

### Standard (recommended)
| Item | Cost |
|---|---|
| Base fee (per month) | $35 |
| Outbound data Zone 1 (per GB, first 10 TB) | $0.087 |
| HTTP/HTTPS requests (per million) | $0.011 |
| Security policies | Included |

### Premium (with WAF + Bot protection)
| Item | Cost |
|---|---|
| Base fee (per month) | $330 |
| Outbound data Zone 1 (per GB, first 10 TB) | $0.087 |
| HTTP/HTTPS requests (per million) | $0.011 |
| WAF custom rules (per policy/month) | $5 |
| WAF managed rule sets (per policy/month) | $20 |
| Bot protection (per million requests) | $10 |

### Key Features
- Global load balancing with instant failover
- Built-in CDN caching (500+ PoPs)
- Web Application Firewall (WAF) at edge
- URL rewriting, session affinity, custom domains
- Health probes and priority/weighted routing

---

## Azure DNS

| Feature | Cost |
|---|---|
| DNS hosted zones (per zone/month, first 25) | $0.50 |
| DNS hosted zones (per zone/month, beyond 25) | $0.10 |
| DNS queries (first billion/month) | $0.40/million |
| DNS queries (next 9 billion/month) | $0.20/million |
| DNSSEC | Free |
| Private DNS zones (per zone/month) | $0.50 |
| Private DNS — virtual network links | $0.10/link/month |

### Azure Traffic Manager
| Item | Cost |
|---|---|
| DNS queries (per million) | $0.54 |
| Health checks (per endpoint/month) | $0.36 |
| Traffic Manager profiles | $0.54/month each |
| Real User Measurements (per 100K measurements) | $2.00 |

---

## Azure ExpressRoute — Private Connectivity

### Circuit (Monthly Port Cost)
| Circuit SKU | Speed | Metered $/month | Unlimited $/month |
|---|---|---|---|
| Standard | 50 Mbps | $55 | $275 |
| Standard | 100 Mbps | $110 | $550 |
| Standard | 200 Mbps | $220 | $1,100 |
| Standard | 500 Mbps | $550 | $2,750 |
| Standard | 1 Gbps | $1,100 | $5,500 |
| Standard | 2 Gbps | $2,200 | $11,000 |
| Standard | 5 Gbps | $5,500 | — |
| Standard | 10 Gbps | $11,000 | — |
| Premium | 1 Gbps | $1,650 | $7,700 |
| Premium | 10 Gbps | $16,500 | — |

### Data Transfer (Metered plan)
| Zone | $/GB |
|---|---|
| Zone 1 (Americas, Europe) | $0.025 |
| Zone 2 (Asia Pacific) | $0.05 |
| Zone 3 (other) | $0.14 |

### ExpressRoute Direct (physical port)
| Port Speed | Monthly Cost |
|---|---|
| 10 Gbps port | $5,000 |
| 100 Gbps port | $31,000 |

### Key Features
- Private, dedicated connection (not over internet)
- BGP routing, redundant connections
- Global Reach (connect circuits across regions)
- Up to 10 Gbps per circuit (Standard), 100 Gbps (Direct)
- FastPath (bypass ExpressRoute Gateway for ultra-low latency)

---

## Azure VPN Gateway

| SKU | Throughput | Tunnels | Cost/hr | Est. $/month |
|---|---|---|---|---|
| Basic | 100 Mbps | 10 | $0.027 | ~$19 |
| VpnGw1 | 650 Mbps | 30 | $0.19 | ~$137 |
| VpnGw2 | 1 Gbps | 30 | $0.27 | ~$194 |
| VpnGw3 | 1.25 Gbps | 30 | $0.67 | ~$482 |
| VpnGw4 | 5 Gbps | 100 | $1.40 | ~$1,008 |
| VpnGw5 | 10 Gbps | 100 | $2.80 | ~$2,016 |
| VpnGw1AZ (zone-redundant) | 650 Mbps | 30 | $0.36 | ~$259 |
| VpnGw2AZ | 1 Gbps | 30 | $0.49 | ~$353 |
| VpnGw3AZ | 1.25 Gbps | 30 | $1.25 | ~$900 |

### VPN Data Transfer
| Item | Cost |
|---|---|
| Data OUT to internet (standard egress) | $0.087/GB |
| S2S VPN connections between VNets (same region) | $0.01/hr per gateway |

---

## Azure Virtual Network

| Feature | Cost |
|---|---|
| VNet creation | Free |
| Peering — ingress/egress (same region) | $0.01/GB each direction |
| Peering — global (cross-region) | $0.025–$0.10/GB by region pair |
| VNet NAT Gateway (per hr) | $0.045 |
| VNet NAT Gateway (per GB processed) | $0.045 |
| Private Link service (per hr) | $0.01 |
| Private Endpoint (per hr) | $0.01 |
| Private Endpoint (per GB processed) | $0.01 |
| VNet Flow Logs (per GB) | $0.50 |
| DDoS Network Protection (per protected VNet/month) | ~$2,944 |

### Data Transfer Summary
| Scenario | Cost |
|---|---|
| Inbound from internet | Free |
| Outbound to internet (first 5 GB/month) | Free |
| Outbound to internet (5 GB – 10 TB) | $0.087/GB |
| Between AZs (same region) | $0.01/GB each direction |
| Between Azure regions (US) | $0.02–$0.05/GB |

---

*Prices are East US pay-as-you-go rates as of 2024.*
