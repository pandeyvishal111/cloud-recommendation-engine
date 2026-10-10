# GCP — Compute Factsheet
> Compute Engine machine types, pricing tiers, and purchasing options.

---

## Machine Family Overview

| Family | Series | Category | Use Case |
|--------|--------|----------|----------|
| General Purpose | E2 | Cost-optimised | Dev/test, web apps |
| General Purpose | N2/N2D | Balanced | Production workloads |
| General Purpose | N1 | Legacy balanced | General production |
| General Purpose | T2D/T2A | Scale-out | Web serving, microservices |
| Compute Optimised | C2/C2D | High CPU | HPC, gaming, batch |
| Memory Optimised | M1/M2/M3 | High RAM | SAP HANA, large DBs |
| Accelerator Optimised | A2/A3 | GPU (A100) | ML training/inference |
| GPU (add-on) | NVIDIA T4/V100/K80 | GPU | ML, rendering |
| Storage Optimised | Z3 | High local SSD | NoSQL, data analytics |

---

## E2-Series — Cost Optimised (Best Value, Dev/Test)
| Machine Type | vCPU | RAM (GB) | Est. $/month | Best For |
|-------------|------|-----------|--------------|----------|
| e2-micro | 2 (shared) | 1 | ~$6.10 | Free tier, smallest |
| e2-small | 2 (shared) | 2 | ~$12.20 | Light workloads |
| e2-medium | 2 (shared) | 4 | ~$24.50 | Small apps |
| e2-standard-2 | 2 | 8 | ~$49 | Small production |
| e2-standard-4 | 4 | 16 | ~$97 | Web apps |
| e2-standard-8 | 8 | 32 | ~$194 | App servers |
| e2-standard-16 | 16 | 64 | ~$388 | Mid-scale |
| e2-standard-32 | 32 | 128 | ~$776 | Larger workloads |
| e2-highmem-2 | 2 | 16 | ~$68 | Memory-light apps |
| e2-highmem-4 | 4 | 32 | ~$136 | Memory workloads |
| e2-highmem-8 | 8 | 64 | ~$272 | Larger memory |
| e2-highmem-16 | 16 | 128 | ~$543 | High-memory |
| e2-highcpu-2 | 2 | 2 | ~$38 | CPU-heavy small |
| e2-highcpu-4 | 4 | 4 | ~$75 | Batch, gaming |
| e2-highcpu-8 | 8 | 8 | ~$150 | Compute-heavy |
| e2-highcpu-16 | 16 | 16 | ~$300 | Large compute |
| e2-highcpu-32 | 32 | 32 | ~$601 | Very large compute |

---

## N2-Series — Balanced Performance (Production)
| Machine Type | vCPU | RAM (GB) | Est. $/month | Best For |
|-------------|------|-----------|--------------|----------|
| n2-standard-2 | 2 | 8 | ~$67 | Production web apps |
| n2-standard-4 | 4 | 16 | ~$134 | App servers |
| n2-standard-8 | 8 | 32 | ~$268 | Mid-scale apps |
| n2-standard-16 | 16 | 64 | ~$536 | High-traffic apps |
| n2-standard-32 | 32 | 128 | ~$1,072 | Enterprise |
| n2-standard-48 | 48 | 192 | ~$1,608 | Large enterprise |
| n2-standard-64 | 64 | 256 | ~$2,144 | Very large |
| n2-standard-80 | 80 | 320 | ~$2,680 | Largest standard |
| n2-highmem-2 | 2 | 16 | ~$94 | Memory-intensive |
| n2-highmem-4 | 4 | 32 | ~$188 | Analytics |
| n2-highmem-8 | 8 | 64 | ~$376 | Databases |
| n2-highmem-16 | 16 | 128 | ~$752 | Large databases |
| n2-highmem-32 | 32 | 256 | ~$1,504 | Enterprise DBs |
| n2-highmem-48 | 48 | 384 | ~$2,257 | Very large memory |
| n2-highmem-64 | 64 | 512 | ~$3,009 | Largest memory |
| n2-highcpu-2 | 2 | 2 | ~$47 | CPU-heavy |
| n2-highcpu-4 | 4 | 4 | ~$94 | Batch |
| n2-highcpu-8 | 8 | 8 | ~$188 | Gaming |
| n2-highcpu-16 | 16 | 16 | ~$376 | HPC |
| n2-highcpu-32 | 32 | 32 | ~$751 | Large HPC |
| n2-highcpu-64 | 64 | 64 | ~$1,502 | Very large HPC |
| n2-highcpu-80 | 80 | 80 | ~$1,878 | Largest compute |

---

## C2-Series — Compute Optimised (Highest CPU Performance)
| Machine Type | vCPU | RAM (GB) | Est. $/month | Best For |
|-------------|------|-----------|--------------|----------|
| c2-standard-4 | 4 | 16 | ~$142 | Batch, HPC |
| c2-standard-8 | 8 | 32 | ~$284 | Gaming servers |
| c2-standard-16 | 16 | 64 | ~$568 | Scientific compute |
| c2-standard-30 | 30 | 120 | ~$1,065 | Large HPC |
| c2-standard-60 | 60 | 240 | ~$2,130 | Very large HPC |

## C2D-Series — Compute Optimised (AMD EPYC)
| Machine Type | vCPU | RAM (GB) | Est. $/month | Best For |
|-------------|------|-----------|--------------|----------|
| c2d-standard-2 | 2 | 8 | ~$61 | Small compute |
| c2d-standard-4 | 4 | 16 | ~$122 | Batch |
| c2d-standard-8 | 8 | 32 | ~$244 | Gaming |
| c2d-standard-16 | 16 | 64 | ~$488 | HPC |
| c2d-standard-32 | 32 | 128 | ~$976 | Large HPC |
| c2d-standard-56 | 56 | 224 | ~$1,708 | Very large HPC |
| c2d-standard-112 | 112 | 448 | ~$3,415 | Largest compute |

---

## M1/M2/M3-Series — Memory Optimised (SAP HANA)
| Machine Type | vCPU | RAM (GB) | Est. $/month | Best For |
|-------------|------|-----------|--------------|----------|
| m1-megamem-96 | 96 | 1,433 | ~$6,300 | Large SAP HANA |
| m1-ultramem-40 | 40 | 961 | ~$4,800 | Medium SAP HANA |
| m1-ultramem-80 | 80 | 1,922 | ~$9,500 | Large SAP HANA |
| m1-ultramem-160 | 160 | 3,844 | ~$19,000 | Very large HANA |
| m2-ultramem-208 | 208 | 5,888 | ~$22,000 | Largest memory |
| m2-megamem-416 | 416 | 5,888 | ~$25,000 | Maximum memory |
| m3-ultramem-32 | 32 | 976 | ~$5,400 | Medium HANA (latest) |
| m3-ultramem-64 | 64 | 1,952 | ~$10,800 | Large HANA (latest) |
| m3-ultramem-128 | 128 | 3,904 | ~$21,600 | Very large (latest) |

---

## A2-Series — Accelerator Optimised (NVIDIA A100 GPU)
| Machine Type | vCPU | RAM (GB) | GPU | VRAM | Est. $/month | Best For |
|-------------|------|-----------|-----|------|--------------|----------|
| a2-highgpu-1g | 12 | 85 | 1x A100 | 40 GB | ~$2,950 | ML training |
| a2-highgpu-2g | 24 | 170 | 2x A100 | 80 GB | ~$5,900 | Large training |
| a2-highgpu-4g | 48 | 340 | 4x A100 | 160 GB | ~$11,800 | Distributed training |
| a2-highgpu-8g | 96 | 680 | 8x A100 | 320 GB | ~$23,600 | Very large models |
| a2-megagpu-16g | 96 | 1,360 | 16x A100 | 640 GB | ~$47,200 | Largest training |
| a2-ultragpu-1g | 12 | 170 | 1x A100 80GB | 80 GB | ~$3,800 | Memory-heavy ML |

## A3-Series — Accelerator Optimised (NVIDIA H100 GPU, Latest)
| Machine Type | vCPU | RAM (GB) | GPU | VRAM | Est. $/month | Best For |
|-------------|------|-----------|-----|------|--------------|----------|
| a3-highgpu-8g | 208 | 1,872 | 8x H100 | 640 GB | ~$98,000 | Largest generative AI |

---

## GCP Pricing Options
| Option | Discount | Commitment | Notes |
|--------|----------|------------|-------|
| On-Demand | — | None | Per-second billing |
| Sustained Use Discount (SUD) | Up to 30% | None (automatic) | Auto-applied for >25% of month |
| 1-yr Committed Use (Resource) | ~37% | 1 year | Specific machine type |
| 3-yr Committed Use (Resource) | ~55% | 3 years | Best rate |
| 1-yr Committed Use (Spend) | ~17% | 1 year | Flexible across types |
| Spot VMs | Up to 91% | None | Interruptible, <30s notice |
| Preemptible VMs (legacy) | Up to 80% | None | 24-hr max runtime |
| Sole-tenant nodes | On-Demand | None / 1 or 3 yr | Physical isolation, BYOL |

> **Sustained Use Discount**: Unlike AWS/Azure, GCP automatically discounts VMs used for more than 25% of a billing month — no reservation needed.

---

## Cloud Run — Serverless Containers
| Component | Free Tier | Paid Rate |
|-----------|-----------|-----------|
| vCPU-seconds | 180,000/month | $0.000024/vCPU-s |
| Memory GB-seconds | 360,000/month | $0.0000025/GB-s |
| Requests | 2M/month | $0.40/million |
| Minimum instances | — | $0.000024/vCPU-s (idle) |

## Cloud Functions — Serverless Functions
| Component | Free Tier | Paid Rate |
|-----------|-----------|-----------|
| Invocations | 2M/month | $0.40/million |
| Compute (per GB-second) | 400,000 GB-s | $0.0000025 |
| Compute (per GHz-second) | 200,000 GHz-s | $0.0000100 |

---

## GCP Batch — Managed Batch Computing
| Component | Cost |
|-----------|------|
| Batch service | Free |
| Underlying VMs | Standard Compute Engine rates |
| Spot VM option | Up to 91% saving |
| Preemptible VM option | Up to 80% saving |

---

## Always Free Tier
| Resource | Free Amount |
|----------|------------|
| e2-micro instance | 1 instance per month (US regions) |
| HDD persistent disk | 30 GB |
| Snapshot storage | 5 GB |
| Cloud Run | 180,000 vCPU-s + 2M requests/month |
| Cloud Functions | 2M invocations/month |

*Prices are approximate us-central1 on-demand rates as of 2024. SUD applied automatically for eligible instances.*
