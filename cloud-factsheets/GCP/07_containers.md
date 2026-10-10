# GCP — Containers Factsheet

---

## Google Kubernetes Engine (GKE) — Managed Kubernetes

### Cluster Tiers
| Tier | Cluster Management Fee | SLA | Best For |
|---|---|---|---|
| Autopilot (recommended) | $0.10/cluster/hr (~$73/month) | 99.9% (Standard), 99.95% (regional) | Hands-off, fully managed K8s |
| Standard | $0.10/cluster/hr (~$73/month) | 99.5% (zonal), 99.95% (regional) | Custom node pools, advanced config |
| Free Tier | First cluster in a project free | 99.5% (zonal) | Dev/test single cluster |

### GKE Autopilot Node Pricing (pay per Pod resource requests)
| Resource | Cost |
|---|---|
| vCPU (per vCPU-hour) | $0.0585 |
| Memory (per GB-hour) | $0.00641 |
| Ephemeral storage (per GB-hour) | $0.000054 |
| Spot Pods (vCPU/hr) | ~70% discount off on-demand |
| Spot Pods (Memory GB/hr) | ~70% discount off on-demand |

### GKE Standard — Node Pricing (standard GCE VM rates)
| Node Pool | Machine Type | vCPU | RAM | Cost/hr |
|---|---|---|---|---|
| Burstable / Dev | e2-micro | 0.25 | 1 GB | $0.0084 |
| General (small) | e2-medium | 1 | 4 GB | $0.0336 |
| General (medium) | e2-standard-4 | 4 | 16 GB | $0.134 |
| General (large) | e2-standard-8 | 8 | 32 GB | $0.268 |
| Balanced (medium) | n2-standard-4 | 4 | 16 GB | $0.194 |
| Balanced (large) | n2-standard-8 | 8 | 32 GB | $0.388 |
| Memory-optimized | n2-highmem-8 | 8 | 64 GB | $0.493 |
| GPU (T4) | n1-standard-4 + T4 | 4+GPU | 15 GB | $0.48 |
| Spot instances | Various | — | — | ~60–91% off |

### GKE Features by Mode
| Feature | Autopilot | Standard |
|---|---|---|
| Node management | Fully managed | User-managed |
| Node pools | Not needed | Manual config |
| Pod security standards | Enforced (restricted) | Configurable |
| Bin packing | Automatic | Manual |
| Cluster autoscaler | Built-in | Optional |
| Node auto-provisioning | Built-in | Optional |
| Workload Identity | Included | Optional |
| Vertical Pod Autoscaler | Built-in | Optional |
| Binary Authorization | Supported | Supported |

### GKE Add-Ons & Features
| Feature | Cost |
|---|---|
| GKE Enterprise (formerly Anthos) | $0.25/vCPU/hr for managed nodes |
| GKE Gateway (API Gateway in K8s) | Load balancer rates |
| Config Sync (GitOps, Enterprise) | Enterprise |
| Policy Controller (OPA Gatekeeper, Enterprise) | Enterprise |
| Cloud Service Mesh (Istio, Enterprise) | Enterprise |
| Backup for GKE (per GiB protected/month) | $0.10 |

---

## Artifact Registry — Container & Package Repository

| Item | Free Tier | Paid Rate |
|---|---|---|
| Storage (per GB/month) | 0.5 GB/month | $0.10/GB |
| Network egress (same region) | Free | Free |
| Network egress (cross-region, per GB) | — | $0.01–$0.15/GB |
| Vulnerability scanning (Container Analysis, per image scanned) | — | $0.26/image |
| On-push scanning (per unique layer/month) | — | $0.26 |

### Supported Formats
Docker containers, Helm charts, Maven (Java), npm (Node.js), Python (PyPI), Go modules, Apt, Yum

### Key Features
- Native IAM access control
- Regional repositories (data residency)
- Multi-format support in same registry
- VPC Service Controls integration
- CMEK (customer-managed encryption keys)
- Integration with Cloud Build, GKE, Cloud Run
- Cleanup policies (auto-delete old images)

---

## Cloud Run — Container Platform (Serverless)

See GCP/06_serverless.md for full Cloud Run pricing.

| Quick Reference | Cost |
|---|---|
| vCPU-second (active) | $0.00002400 |
| GB-second (active) | $0.00000250 |
| Requests per million | $0.40 |
| Free: 2M requests, 360K GB-sec, 180K vCPU-sec/month | — |

---

## GKE Enterprise (formerly Anthos)

| Item | Cost |
|---|---|
| Managed cluster nodes (per vCPU/hr) | $0.25 |
| Attached clusters (non-GKE, per vCPU/hr) | $0.25 |
| Bare metal/VM clusters (per vCPU/hr) | $0.25 |

### Included in GKE Enterprise
- Config Sync (GitOps-based configuration management)
- Policy Controller (OPA/Gatekeeper enforcement)
- Cloud Service Mesh (Istio-based, mTLS, traffic management)
- Multi-cluster ingress
- Fleet management (manage multiple clusters across clouds)
- GKE on AWS, GKE on Azure (hybrid deployments)
- GKE on Bare Metal / VMware

---

## Container Decision Matrix

| Factor | GKE Autopilot | GKE Standard | Cloud Run | Cloud Functions |
|---|---|---|---|---|
| Container support | Yes | Yes | Yes | No (code only) |
| Server management | None | Node-level | None | None |
| Scale to zero | No (min 1 pod) | Configurable | Yes | Yes |
| Max scale | Very high | Very high | 1,000 instances | 3,000 instances |
| Startup latency | Seconds | Seconds | Milliseconds (warm) | Milliseconds |
| Pricing unit | Pod CPU/mem | VM instance | Request+CPU/mem | Request+GB-sec |
| Long-running jobs | Yes | Yes | Cloud Run Jobs | No |
| Stateful workloads | Yes (PV) | Yes (PV) | Volume mounts | No |
| Custom networking | Limited | Full VPC | VPC Direct | VPC Connector |
| Best For | Production K8s without node ops | Full K8s control | Event-driven containers | Simple event handlers |

---

## Cloud Build — CI/CD Build System

| Item | Free Tier | Paid Rate |
|---|---|---|
| Build minutes (per day) | 120 min/day | $0.003/build-minute |
| Build with custom machine (e2-highcpu-8) | — | $0.0096/min |
| Build with GPU (n1+V100) | — | $0.15/min |
| Stored build artifacts (Cloud Storage) | Cloud Storage rates | — |
| Triggers (GitHub, GitLab, Bitbucket, Cloud Source) | Free | Free |

### Key Features
- Fully managed, serverless
- Parallel steps, conditional steps
- Docker build + push to Artifact Registry
- Secret Manager integration (build-time secrets)
- Integration with GKE, Cloud Run, App Engine
- VPC connectivity (private pools)
- Binary Authorization (sign and verify images)

---

*Prices are us-central1 rates as of 2024. GKE cluster management fee is global.*
