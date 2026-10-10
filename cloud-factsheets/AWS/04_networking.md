# AWS — Networking Factsheet

---

## Elastic Load Balancing (ELB)

| Type | Layer | Cost/hr | Per LCU/hr | Best For |
|---|---|---|---|---|
| Application Load Balancer (ALB) | 7 (HTTP/HTTPS) | $0.008 | $0.008/LCU | Microservices, path/host routing, WebSockets |
| Network Load Balancer (NLB) | 4 (TCP/UDP/TLS) | $0.006 | $0.006/NLCU | Ultra-low latency, static IP, extreme throughput |
| Gateway Load Balancer (GWLB) | 3 (GENEVE) | $0.004 | $0.004/GLCU | Third-party virtual firewalls/appliances |
| Classic Load Balancer (CLB) | 4/7 | $0.025 | $0.008/GB | Legacy; not recommended for new workloads |

**1 LCU ≈** 25 new connections/sec, 3,000 active connections, 1 GB/hr, 1,000 rule evaluations/sec.

### Key Features
- ALB: content-based routing, Lambda targets, WAF integration, gRPC support
- NLB: static IPs per AZ, preserves client IP, TLS offloading, Zonal DNS
- Both: health checks, access logs, cross-zone load balancing

---

## Amazon CloudFront — CDN

### Data Transfer OUT (to Internet)
| Monthly Volume | Cost/GB |
|---|---|
| First 10 TB | $0.085 |
| Next 40 TB | $0.080 |
| Next 100 TB | $0.060 |
| Next 350 TB | $0.040 |
| Next 524 TB | $0.030 |
| Next 4 PB | $0.025 |
| Over 5 PB | $0.020 |

### HTTP Request Pricing
| Type | Cost per 10,000 |
|---|---|
| HTTP requests | $0.0075 |
| HTTPS requests | $0.0100 |

### CloudFront Key Facts
- 450+ Points of Presence (PoPs) globally
- Free data transfer from AWS origins (S3, ALB, EC2) to CloudFront
- AWS WAF integration (charged separately)
- Lambda@Edge: $0.60/million requests + $0.00000625128/GB-second
- CloudFront Functions: $0.10/million invocations
- Field-level encryption, TLS 1.3, Origin Shield (+$0.009/GB)
- Free SSL/TLS certificates via ACM

---

## Amazon Route 53 — DNS

| Feature | Cost |
|---|---|
| Hosted zone (per zone/month, first 25) | $0.50 |
| Hosted zone (per zone/month, over 25) | $0.10 |
| Standard DNS queries (per million) | $0.40 |
| Latency-based routing queries (per million) | $0.60 |
| Geo DNS / Geo-proximity queries (per million) | $0.70 |
| Health checks (standard, per check/month) | $0.50 |
| Health checks (with string matching) | $1.00 |
| Health checks (HTTPS) | $0.75 |
| Traffic flow (per policy record/month) | $50.00 |
| Domain registration (.com) | $13/year |

### Key Features
- 100% SLA uptime
- DNSSEC signing
- Private hosted zones (internal DNS within VPC)
- Alias records (point to AWS resources — free queries)
- Traffic policies: weighted, failover, multivalue, latency, geo

---

## AWS Direct Connect — Private Connectivity

### Dedicated Connections
| Port Speed | Port/month | Data Transfer OUT/GB |
|---|---|---|
| 1 Gbps | $216 | $0.02 |
| 10 Gbps | $1,620 | $0.02 |
| 100 Gbps | $16,200 | $0.02 |

### Hosted Connections (via partner)
| Speed | Data Transfer OUT/GB |
|---|---|
| 50 Mbps – 500 Mbps | $0.03 |
| 1 Gbps | $0.02 |
| 5 Gbps / 10 Gbps | $0.02 |

### Key Features
- Consistent latency (no public internet path)
- Supports Virtual Private Gateway or Transit Gateway attachment
- Redundant connections recommended for production (2x cost)
- Link Aggregation Group (LAG) supported

---

## AWS VPN

### Site-to-Site VPN
| Item | Cost |
|---|---|
| VPN connection/hr | $0.05 |
| Data transfer OUT (per GB) | Standard EC2 data transfer rates |
| Best For | Connecting on-premises networks to AWS VPC |

### AWS Client VPN
| Item | Cost |
|---|---|
| Endpoint association/hr (per subnet) | $0.10 |
| Client connection/hr | $0.05 |
| Best For | Remote workforce access to AWS resources |

---

## AWS Global Accelerator

| Item | Cost |
|---|---|
| Accelerator (per hr) | $0.025 |
| Data transfer premium — US/EU (per GB) | $0.015 |
| Data transfer premium — Asia Pacific | $0.035 |
| Data transfer premium — South America | $0.080 |

### Key Features
- Anycast IPs (2 static IPs per accelerator)
- Automatic traffic routing to optimal AWS edge
- Instant failover
- Integrates with ALB, NLB, EC2, Elastic IP

---

## Amazon VPC — Virtual Private Cloud

### VPC Components Pricing
| Component | Cost |
|---|---|
| VPC creation | Free |
| Subnets, route tables, IGW | Free |
| NAT Gateway (per hr) | $0.045 |
| NAT Gateway (per GB processed) | $0.045 |
| VPC Peering (intra-region data transfer) | $0.01/GB each direction |
| VPC Peering (cross-region) | Standard inter-region rates |
| VPC Interface Endpoint (per AZ/hr) | $0.01 |
| VPC Interface Endpoint (per GB) | $0.01 |
| VPC Gateway Endpoint (S3 / DynamoDB) | Free |
| AWS PrivateLink (per endpoint service/hr) | $0.01 |
| AWS PrivateLink (per GB) | $0.01 |
| VPC Flow Logs (per GB ingested to CloudWatch) | $0.50 |
| VPC Flow Logs (per GB ingested to S3) | $0.02 |

### Transit Gateway
| Item | Cost |
|---|---|
| Attachment (per hr) | $0.05 |
| Data processed (per GB) | $0.02 |
| Best For | Hub-and-spoke connectivity across many VPCs |

---

## Data Transfer Summary

| Scenario | Cost |
|---|---|
| Inbound from internet | Free |
| Outbound to internet (first 1 GB/month) | Free |
| Outbound to internet (up to 10 TB) | $0.09/GB |
| EC2 to EC2, same AZ, private IP | Free |
| EC2 to EC2, cross-AZ | $0.01/GB each direction |
| EC2 to EC2, cross-region | $0.02/GB (US) |
| To/from CloudFront | Free |
| To/from S3 (same region) | Free |

---

*Prices are US East (N. Virginia) rates as of 2024.*
