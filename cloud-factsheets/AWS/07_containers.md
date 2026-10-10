# AWS — Containers Factsheet

---

## Amazon EKS — Managed Kubernetes

### Cluster Pricing
| Item | Cost | Notes |
|---|---|---|
| EKS Cluster (per hr) | $0.10 | ~$73/month per cluster |
| EKS Distro | Free | Self-managed Kubernetes |
| EKS Anywhere | Free software, hardware cost | On-premises Kubernetes |

### Worker Nodes
Worker nodes are standard EC2 instances — you pay EC2 prices for the underlying instances.

| Node Group Type | Cost | Best For |
|---|---|---|
| Self-Managed Nodes | EC2 rate only | Full control |
| Managed Node Groups | EC2 rate only (EKS manages lifecycle) | Simplified ops |
| Fargate Profiles | $0.04048/vCPU-hr + $0.004445/GB-hr | Serverless pods |
| Karpenter (open source) | Free tool, EC2 rates | Just-in-time node provisioning |

### EKS Add-ons (optional, managed)
| Add-on | Cost |
|---|---|
| Amazon VPC CNI | Free |
| CoreDNS | Free |
| kube-proxy | Free |
| AWS Load Balancer Controller | Free |
| EBS CSI Driver | Free |
| GuardDuty EKS Runtime Monitoring | GuardDuty pricing |

### Key Features
- Kubernetes 1.24–1.29+ supported
- Managed control plane (etcd, API server, scheduler)
- Multi-AZ control plane by default
- EKS Auto Mode (fully managed nodes, 2024)
- Integrates with IAM, ALB, CloudWatch, X-Ray, ECR

---

## Amazon ECS — Elastic Container Service

### ECS Pricing
| Launch Type | Cost | Best For |
|---|---|---|
| EC2 Launch Type | EC2 instance rates only | Cost control, custom AMIs, GPU workloads |
| Fargate Launch Type | $0.04048/vCPU-hr + $0.004445/GB-hr | No node management |
| Fargate Spot | ~70% cheaper than Fargate | Fault-tolerant batch workloads |

### ECS Control Plane
- **Free** — ECS cluster, task definitions, service definitions all free
- You pay only for the underlying compute (EC2 or Fargate)

### ECS Service Connect
| Item | Cost |
|---|---|
| Service Connect | Free |
| Underlying data transfer | Standard VPC rates |

### Key Features
- AWS-native orchestrator (tight AWS integration)
- Task definitions (CPU/memory, Docker image, port mappings)
- Service auto-scaling, rolling deployments, blue/green via CodeDeploy
- ECS Anywhere (on-premises containers)
- No Kubernetes overhead

---

## Amazon ECR — Elastic Container Registry

| Feature | Free Tier | Paid Rate |
|---|---|---|
| Storage (private repositories) | 500 MB/month | $0.10/GB/month |
| Data transfer OUT to EC2 (same region) | Free | Free |
| Data transfer OUT to internet | First 1 GB free | $0.09/GB |
| Data transfer to other AWS regions | — | $0.02/GB |
| ECR Public (images stored) | 50 GB free | $0.10/GB/month |
| ECR Public (data transfer OUT) | 500 GB/month free | $0.09/GB |

### Key Features
- OCI-compliant (Docker images, Helm charts)
- Image vulnerability scanning (Basic free, Enhanced via Inspector)
- Image tag immutability
- Lifecycle policies (auto-delete old images)
- Cross-region and cross-account replication
- Pull-through cache from Docker Hub, Quay, GitHub GHCR

---

## AWS App Runner — Fully Managed Container Service

| Resource | Cost |
|---|---|
| vCPU (active, per vCPU-hr) | $0.064 |
| Memory (active, per GB-hr) | $0.007 |
| vCPU (paused, per vCPU-hr) | $0.0064 |
| Memory (paused, per GB-hr) | $0.0007 |
| Automatic deployments | $1.00/month per service (if enabled) |

### App Runner Instance Sizes
| Config | vCPU | Memory | Est. $/month (always on) |
|---|---|---|---|
| 0.25 vCPU, 0.5 GB | 0.25 | 0.5 GB | ~$12 |
| 0.5 vCPU, 1 GB | 0.5 | 1 GB | ~$23 |
| 1 vCPU, 2 GB | 1 | 2 GB | ~$46 |
| 2 vCPU, 4 GB | 2 | 4 GB | ~$93 |
| 4 vCPU, 8 GB | 4 | 8 GB | ~$185 |

### Key Features
- Deploy from ECR image or source code (GitHub)
- Zero infrastructure management
- Built-in auto-scaling (scales to zero when paused)
- Custom domains with free TLS
- VPC connector for private resource access
- Best For: web apps and APIs without Kubernetes complexity

---

## AWS Fargate (Detailed)

### vCPU and Memory Combinations
Fargate requires specific vCPU → memory combinations:

| vCPU | Allowed Memory |
|---|---|
| 0.25 | 0.5, 1, 2 GB |
| 0.5 | 1–4 GB (1 GB increments) |
| 1 | 2–8 GB (1 GB increments) |
| 2 | 4–16 GB (1 GB increments) |
| 4 | 8–30 GB (1 GB increments) |
| 8 | 16–60 GB (4 GB increments) |
| 16 | 32–120 GB (8 GB increments) |

### Fargate Spot (significant savings)
| Architecture | Spot vCPU-hr | Spot GB-hr |
|---|---|---|
| x86_64 | ~$0.01289 | ~$0.00141 |
| ARM64 | ~$0.01031 | ~$0.00113 |

> Fargate Spot can be interrupted with 2-minute warning — best for batch, CI runners, non-critical workloads.

---

## AWS Batch — Managed Batch Computing (Container-based)

| Item | Cost |
|---|---|
| AWS Batch service | Free |
| EC2 (on-demand jobs) | Standard EC2 rates |
| EC2 Spot (batch jobs) | Spot rates (up to 90% saving) |
| Fargate jobs (vCPU-hr) | $0.04048 |
| Fargate jobs (GB-hr) | $0.004445 |
| Fargate Spot jobs | ~70% cheaper |

### Key Features
- Job queues with priorities
- Compute environments (EC2, Spot, Fargate)
- Array jobs and multi-node parallel jobs
- AWS Step Functions integration
- Best For: genomics, rendering, ML preprocessing, ETL

---

*Prices are US East (N. Virginia) rates as of 2024.*
