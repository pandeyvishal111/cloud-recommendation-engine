# AWS — Compute Factsheet
> EC2 instance families, pricing tiers, and purchasing options.

---

## EC2 Instance Families

### General Purpose — T3 (Burstable, Dev/Test)
| Instance | vCPU | RAM (GB) | On-Demand ($/hr) | Est. $/month | Best For |
|----------|------|-----------|------------------|--------------|----------|
| t3.nano | 2 | 0.5 | $0.0052 | ~$3.75 | Micro services, smallest |
| t3.micro | 2 | 1 | $0.0104 | ~$7.50 | Dev/test, free-tier eligible |
| t3.small | 2 | 2 | $0.0208 | ~$15 | Light web servers |
| t3.medium | 2 | 4 | $0.0416 | ~$30 | Small apps, staging |
| t3.large | 2 | 8 | $0.0832 | ~$60 | Web apps, CMS |
| t3.xlarge | 4 | 16 | $0.1664 | ~$120 | Medium workloads |
| t3.2xlarge | 8 | 32 | $0.3328 | ~$240 | Larger web apps |

### General Purpose — M5 (Balanced Production)
| Instance | vCPU | RAM (GB) | On-Demand ($/hr) | Est. $/month | Best For |
|----------|------|-----------|------------------|--------------|----------|
| m5.large | 2 | 8 | $0.096 | ~$69 | Balanced production |
| m5.xlarge | 4 | 16 | $0.192 | ~$138 | App servers |
| m5.2xlarge | 8 | 32 | $0.384 | ~$277 | Mid-scale apps |
| m5.4xlarge | 16 | 64 | $0.768 | ~$553 | High-traffic APIs |
| m5.8xlarge | 32 | 128 | $1.536 | ~$1,106 | Enterprise applications |
| m5.12xlarge | 48 | 192 | $2.304 | ~$1,659 | Large enterprise |
| m5.16xlarge | 64 | 256 | $3.072 | ~$2,212 | Very large apps |
| m5.24xlarge | 96 | 384 | $4.608 | ~$3,318 | Largest general purpose |

### Compute Optimised — C5 (CPU-Heavy)
| Instance | vCPU | RAM (GB) | On-Demand ($/hr) | Est. $/month | Best For |
|----------|------|-----------|------------------|--------------|----------|
| c5.large | 2 | 4 | $0.085 | ~$61 | Batch processing |
| c5.xlarge | 4 | 8 | $0.170 | ~$122 | Gaming servers |
| c5.2xlarge | 8 | 16 | $0.340 | ~$245 | Scientific computing |
| c5.4xlarge | 16 | 32 | $0.680 | ~$490 | HPC, ML inference |
| c5.9xlarge | 36 | 72 | $1.530 | ~$1,102 | Intensive batch jobs |
| c5.18xlarge | 72 | 144 | $3.060 | ~$2,203 | Very large HPC |
| c5.24xlarge | 96 | 192 | $4.080 | ~$2,938 | Largest compute |

### Memory Optimised — R5 (RAM-Heavy)
| Instance | vCPU | RAM (GB) | On-Demand ($/hr) | Est. $/month | Best For |
|----------|------|-----------|------------------|--------------|----------|
| r5.large | 2 | 16 | $0.126 | ~$91 | In-memory caching |
| r5.xlarge | 4 | 32 | $0.252 | ~$181 | Real-time analytics |
| r5.2xlarge | 8 | 64 | $0.504 | ~$363 | SAP, large DBs |
| r5.4xlarge | 16 | 128 | $1.008 | ~$726 | High-memory apps |
| r5.8xlarge | 32 | 256 | $2.016 | ~$1,452 | In-memory databases |
| r5.12xlarge | 48 | 384 | $3.024 | ~$2,177 | Very large memory |
| r5.16xlarge | 64 | 512 | $4.032 | ~$2,903 | Enterprise SAP HANA |
| r5.24xlarge | 96 | 768 | $6.048 | ~$4,355 | Largest memory |

### Storage Optimised — I3/I4i (High I/O)
| Instance | vCPU | RAM (GB) | NVMe Storage | On-Demand ($/hr) | Best For |
|----------|------|-----------|-------------|------------------|----------|
| i3.large | 2 | 15.25 | 475 GB NVMe | $0.156 | NoSQL DBs |
| i3.xlarge | 4 | 30.5 | 950 GB NVMe | $0.312 | Elasticsearch |
| i3.2xlarge | 8 | 61 | 1.9 TB NVMe | $0.624 | High IOPS workloads |
| i3.4xlarge | 16 | 122 | 3.8 TB NVMe | $1.248 | Large NoSQL |
| i3.8xlarge | 32 | 244 | 6.4 TB NVMe | $2.496 | Very high IOPS |
| i3.16xlarge | 64 | 488 | 12.8 TB NVMe | $4.992 | Massive local storage |

### GPU / Accelerated — P3 (ML Training)
| Instance | vCPU | RAM (GB) | GPU | VRAM | On-Demand ($/hr) | Est. $/month |
|----------|------|-----------|-----|------|------------------|--------------|
| p3.2xlarge | 8 | 61 | 1x V100 | 16 GB | $3.06 | ~$2,203 |
| p3.8xlarge | 32 | 244 | 4x V100 | 64 GB | $12.24 | ~$8,813 |
| p3.16xlarge | 64 | 488 | 8x V100 | 128 GB | $24.48 | ~$17,626 |
| p3dn.24xlarge | 96 | 768 | 8x V100 | 256 GB | $31.212 | ~$22,473 |

### GPU — G4dn (ML Inference / Graphics)
| Instance | vCPU | RAM (GB) | GPU | On-Demand ($/hr) | Est. $/month |
|----------|------|-----------|-----|------------------|--------------|
| g4dn.xlarge | 4 | 16 | 1x T4 | $0.526 | ~$379 |
| g4dn.2xlarge | 8 | 32 | 1x T4 | $0.752 | ~$541 |
| g4dn.4xlarge | 16 | 64 | 1x T4 | $1.204 | ~$867 |
| g4dn.8xlarge | 32 | 128 | 1x T4 | $2.264 | ~$1,630 |
| g4dn.12xlarge | 48 | 192 | 4x T4 | $3.912 | ~$2,817 |
| g4dn.16xlarge | 64 | 256 | 1x T4 | $4.528 | ~$3,260 |

### High Performance Computing — Hpc6a
| Instance | vCPU | RAM (GB) | Network | On-Demand ($/hr) | Best For |
|----------|------|-----------|---------|------------------|----------|
| hpc6a.48xlarge | 96 | 384 | 100 Gbps EFA | $2.88 | Tightly coupled HPC |

---

## EC2 Purchasing Options

| Option | Discount vs On-Demand | Commitment | Notes |
|--------|----------------------|------------|-------|
| On-Demand | — | None | Pay by the second |
| 1-yr Reserved (No Upfront) | ~30% | 1 year | Monthly payments |
| 1-yr Reserved (Partial Upfront) | ~33% | 1 year | Part upfront + monthly |
| 1-yr Reserved (All Upfront) | ~37% | 1 year | Best 1-yr rate |
| 3-yr Reserved (All Upfront) | ~55% | 3 years | Best long-term rate |
| Compute Savings Plans | ~30–66% | 1 or 3 years | Flexible, applies to Fargate & Lambda too |
| EC2 Instance Savings Plans | ~72% max | 1 or 3 years | Locked to family/region |
| Spot Instances | up to 90% | None | Interruptible, 2-min warning |
| Dedicated Hosts | On-Demand rate | None / 1 or 3 yr | BYOL, compliance |
| Dedicated Instances | +10% on-demand | None | Physical isolation |

---

## Auto Scaling
| Feature | Details |
|---------|---------|
| EC2 Auto Scaling Groups | Scale by CPU, memory, custom metrics |
| Target Tracking | Maintain specific metric (e.g., 70% CPU) |
| Step Scaling | Step rules based on alarm thresholds |
| Scheduled Scaling | Scale based on time (e.g., business hours) |
| Predictive Scaling | ML-based — forecasts demand |
| Warm Pools | Pre-initialised instances for fast scale-out |
| Cost | Free — you pay only for EC2 instances launched |

---

## AWS Lightsail — Simplified VMs (Small Business / Starter)
| Plan | vCPU | RAM | SSD | Transfer | $/month |
|------|------|-----|-----|----------|---------|
| $5 | 2 | 0.5 GB | 20 GB | 1 TB | $5 |
| $7 | 2 | 1 GB | 40 GB | 2 TB | $7 |
| $12 | 2 | 2 GB | 60 GB | 3 TB | $12 |
| $20 | 2 | 4 GB | 80 GB | 4 TB | $20 |
| $40 | 4 | 8 GB | 160 GB | 5 TB | $40 |
| $80 | 4 | 16 GB | 320 GB | 6 TB | $80 |
| $160 | 8 | 32 GB | 640 GB | 7 TB | $160 |

---

## AWS Batch — Managed Batch Computing
| Component | Cost |
|-----------|------|
| AWS Batch service | Free (pay for underlying EC2/Fargate) |
| EC2 (on-demand) | Standard EC2 rates |
| EC2 (Spot) | Spot rates (up to 90% saving) |
| Fargate (per vCPU-hr) | $0.04048 |
| Fargate (per GB-hr) | $0.004445 |

---

## AWS Lambda — Serverless Compute
| Component | Free Tier | Paid Rate |
|-----------|-----------|-----------|
| Requests | 1M/month free | $0.20/million |
| Duration (x86, per GB-second) | 400,000 GB-s/month free | $0.0000166667 |
| Duration (Arm/Graviton2) | 400,000 GB-s/month free | $0.0000133334 |
| Provisioned Concurrency (per GB-hr) | — | $0.000004646 |

*Prices are US East (N. Virginia) on-demand rates as of 2024.*
