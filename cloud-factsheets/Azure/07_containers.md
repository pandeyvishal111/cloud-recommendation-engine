# Azure — Containers Factsheet

---

## Azure Kubernetes Service (AKS)

### Cluster Tiers
| Tier | Cost | SLA | Best For |
|---|---|---|---|
| Free | Free | 99.5% (uptime SLO, not SLA) | Dev/test, learning |
| Standard | $0.10/cluster/hr (~$73/month) | 99.95% | Production workloads |
| Premium | $0.60/cluster/hr (~$432/month) | 99.95% + LTS (3 yr Kubernetes support) | Enterprise, regulated industries |

### Worker Nodes
AKS worker nodes are regular Azure VMs — you pay standard VM pricing:

| VM Series | vCPU | RAM | Est. $/month per node |
|---|---|---|---|
| D2s v3 | 2 | 8 GB | ~$70 |
| D4s v3 | 4 | 16 GB | ~$140 |
| D8s v3 | 8 | 32 GB | ~$280 |
| D16s v3 | 16 | 64 GB | ~$560 |
| E8s v3 | 8 | 64 GB | ~$384 |
| F8s v2 | 8 | 16 GB | ~$244 |
| B2ms | 2 | 8 GB | ~$58 | (burstable, dev/test) |

Spot node pools: up to 90% discount (interruptible).

### AKS Add-ons
| Add-on | Cost |
|---|---|
| Azure Monitor for containers | Log Analytics rates for data ingested |
| Azure Policy for AKS | Free |
| Ingress Application Gateway | Application Gateway rates |
| Open Service Mesh | Free |
| Dapr | Free |
| Azure Key Vault Secrets Store CSI | Key Vault rates |
| Confidential Computing (CVM nodes) | CVM VM rates |

### Key Features
- Managed control plane (free on Free tier, SLA on Standard/Premium)
- Auto-scaling (cluster autoscaler, KEDA)
- Node auto-provisioning (Karpenter-based, 2024)
- Multi-AZ node pools
- Private cluster (API server private IP)
- AAD integration, Azure RBAC for Kubernetes
- Azure CNI, kubenet, Cilium networking
- Windows node pools support
- AKS Automatic (fully-managed node pools, 2024)

---

## Azure Container Registry (ACR)

| Tier | Storage | Webhooks | Geo-replication | Cost/month | Best For |
|---|---|---|---|---|---|
| Basic | 10 GB | 2 | No | $5 | Dev/test |
| Standard | 100 GB | 10 | No | $20 | Small production |
| Premium | 500 GB | 500 | Yes (per replica) | $50 | Enterprise, multi-region |

### ACR Additional Costs
| Item | Cost |
|---|---|
| Additional storage (per GB/month) | $0.10 |
| Geo-replication (per replica/month) | $50 (Standard) / $100 (Premium replica) |
| Build tasks (per build minute) | $0.0001 |
| Data transfer OUT | Standard egress rates |
| Quarantine (vulnerability scan, per image) | $0.29/image (via Defender for Containers) |

### Key Features
- OCI-compliant (Docker images, Helm charts, WASM modules)
| Geo-replication for reduced latency and DR
- Private endpoints and VNet integration (Premium)
- Content trust (image signing with Notary)
- Repository-scoped permissions via tokens
- Automated image build with ACR Tasks
- Retention policies for unused images
- Connected registry (for disconnected environments)

---

## Azure Container Instances (ACI) — Serverless Containers

### Linux Containers
| Resource | Rate | Notes |
|---|---|---|
| vCPU (per second) | $0.0000120 | ~$0.043/vCPU-hr |
| Memory GB (per second) | $0.0000013 | ~$0.005/GB-hr |

### Windows Containers
| Resource | Rate | Notes |
|---|---|---|
| vCPU (per second) | $0.0000147 | ~$0.053/vCPU-hr |
| Memory GB (per second) | $0.0000016 | ~$0.006/GB-hr |

### ACI Example Costs (Linux, per month at 730 hrs)
| Config | vCPU | RAM | Est. $/month |
|---|---|---|---|
| Smallest | 0.5 | 0.5 GB | ~$17 |
| Small | 1 | 1 GB | ~$35 |
| Medium | 2 | 4 GB | ~$77 |
| Large | 4 | 8 GB | ~$154 |
| Very Large | 4 | 16 GB | ~$161 |

### Key Features
- No cluster setup — single-container deployment in seconds
- Per-second billing
- Public IP or VNet injection (private)
- Persistent storage via Azure Files mount
- GPU support (K80, P100, V100 — limited regions)
- Init containers, sidecar containers
- Restart policies (Always, OnFailure, Never)
- Best For: Burst capacity, CI/CD, scheduled jobs, event-driven tasks

---

## Azure Container Apps (Serverless — see also 06_serverless.md)

### Summary for Container Context
| Plan | Scale to Zero | VNet | Dapr | Best For |
|---|---|---|---|---|
| Consumption | Yes | Yes (per-app) | Yes | Event-driven, variable load |
| Dedicated | No (min instances) | Yes | Yes | Steady workloads, predictable cost |

### KEDA Scalers Supported
HTTP requests, Azure Service Bus, Azure Storage Queue, Kafka, RabbitMQ, Prometheus, Cron, CPU, Memory, and 50+ more.

---

## Azure Red Hat OpenShift (ARO)

| Component | Cost |
|---|---|
| OpenShift license (per cluster/hr) | $0.5808 (4-node) |
| Worker nodes | Standard Azure VM rates |
| 3 master nodes (included, managed) | Included in OpenShift fee |
| Minimum cluster (4 worker D8s v3 nodes, 1 hr) | ~$1.70/hr |
| Est. monthly (4 worker D8s v3) | ~$1,345 (ARO fee) + ~$1,120 (VM cost) |

### Key Features
- Fully managed OpenShift 4.x (Red Hat manages control plane)
- 99.95% SLA with multi-AZ
- Integrated with Azure Monitor, AAD, Key Vault
- Includes Red Hat CoreOS for worker nodes
- Automatic patching and updates
- Best For: Enterprises standardized on OpenShift/OCP

---

## AKS vs ACI vs Container Apps — Decision Guide

| Factor | AKS | ACI | Container Apps |
|---|---|---|---|
| Cluster management | Managed (control plane) | None | None |
| Scale to zero | No (min 1 node) | N/A (on-demand) | Yes (Consumption) |
| Kubernetes-native | Full K8s | No | Partial (KEDA/Dapr) |
| VNet integration | Yes | Yes (injection) | Yes |
| GPU support | Yes | Yes (limited) | No |
| Max container RAM | Node RAM | 16 GB | 4 GB (Consumption) |
| Per-second billing | No (VM-based) | Yes | Yes |
| Use case | Complex multi-service apps | Burst, CI jobs, isolated tasks | Microservices, event-driven |
| Cost at scale | Lower per workload | Higher | Medium |

---

*Prices are East US pay-as-you-go rates as of 2024.*
