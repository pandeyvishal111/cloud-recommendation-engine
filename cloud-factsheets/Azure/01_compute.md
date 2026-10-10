# Azure — Compute Factsheet
> Azure Virtual Machine series, pricing tiers, and purchasing options.

---

## VM Series Overview

| Series | Category | Use Case |
|--------|----------|----------|
| B | Burstable General Purpose | Dev/test, low-traffic apps |
| D/Ds | General Purpose | Balanced production workloads |
| E/Es | Memory Optimised | Databases, in-memory caching |
| F/Fs | Compute Optimised | Batch, gaming, ML inference |
| G/Gs | Memory + Storage | Very large databases |
| H | High Performance Compute | Scientific simulations |
| L | Storage Optimised | NoSQL, data warehousing |
| M | Very Large Memory | SAP HANA, very large DBs |
| N (NC/ND/NV) | GPU | ML training, rendering, inference |

---

## B-Series — Burstable (Dev/Test)
| Size | vCPU | RAM (GB) | Est. $/month | Best For |
|------|------|-----------|--------------|----------|
| B1ls | 1 | 0.5 | ~$3.80 | Smallest workloads |
| B1s | 1 | 1 | ~$7.30 | Micro apps, free-tier eligible |
| B1ms | 1 | 2 | ~$14.60 | Light dev workloads |
| B2s | 2 | 4 | ~$29.20 | Small apps |
| B2ms | 2 | 8 | ~$58.40 | Medium dev workloads |
| B4ms | 4 | 16 | ~$116.80 | Dev environments |
| B8ms | 8 | 32 | ~$233.60 | Larger dev workloads |
| B12ms | 12 | 48 | ~$350 | Heavy dev |
| B16ms | 16 | 64 | ~$467 | Large dev/test |
| B20ms | 20 | 80 | ~$584 | Very large burstable |

---

## Dv3/Dsv3-Series — General Purpose (Balanced Production)
| Size | vCPU | RAM (GB) | Est. $/month | Best For |
|------|------|-----------|--------------|----------|
| D2s v3 | 2 | 8 | ~$70 | Small production apps |
| D4s v3 | 4 | 16 | ~$140 | Web servers |
| D8s v3 | 8 | 32 | ~$280 | App servers |
| D16s v3 | 16 | 64 | ~$560 | Mid-scale apps |
| D32s v3 | 32 | 128 | ~$1,120 | High-traffic apps |
| D48s v3 | 48 | 192 | ~$1,680 | Large enterprise |
| D64s v3 | 64 | 256 | ~$2,240 | Enterprise apps |

## Dv5/Dsv5-Series — General Purpose (Latest Gen)
| Size | vCPU | RAM (GB) | Est. $/month | Best For |
|------|------|-----------|--------------|----------|
| D2s v5 | 2 | 8 | ~$68 | Modern production |
| D4s v5 | 4 | 16 | ~$136 | Web servers |
| D8s v5 | 8 | 32 | ~$272 | App servers |
| D16s v5 | 16 | 64 | ~$544 | High-traffic |
| D32s v5 | 32 | 128 | ~$1,088 | Enterprise |
| D64s v5 | 64 | 256 | ~$2,175 | Very large |
| D96s v5 | 96 | 384 | ~$3,263 | Largest general purpose |

---

## Ev3/Esv3-Series — Memory Optimised
| Size | vCPU | RAM (GB) | Est. $/month | Best For |
|------|------|-----------|--------------|----------|
| E2s v3 | 2 | 16 | ~$96 | In-memory caching |
| E4s v3 | 4 | 32 | ~$192 | Real-time analytics |
| E8s v3 | 8 | 64 | ~$384 | Large databases |
| E16s v3 | 16 | 128 | ~$768 | SAP workloads |
| E32s v3 | 32 | 256 | ~$1,536 | Enterprise memory |
| E48s v3 | 48 | 384 | ~$2,304 | Very large memory |
| E64s v3 | 64 | 432 | ~$2,688 | SAP HANA medium |

## Ev5/Esv5-Series — Memory Optimised (Latest Gen)
| Size | vCPU | RAM (GB) | Est. $/month | Best For |
|------|------|-----------|--------------|----------|
| E2s v5 | 2 | 16 | ~$92 | Memory-intensive small |
| E4s v5 | 4 | 32 | ~$184 | Analytics |
| E8s v5 | 8 | 64 | ~$368 | Databases |
| E16s v5 | 16 | 128 | ~$736 | SAP |
| E32s v5 | 32 | 256 | ~$1,473 | Enterprise DBs |
| E64s v5 | 64 | 512 | ~$2,946 | Very large DBs |
| E96s v5 | 96 | 672 | ~$4,025 | Largest memory |

---

## Fsv2-Series — Compute Optimised
| Size | vCPU | RAM (GB) | Est. $/month | Best For |
|------|------|-----------|--------------|----------|
| F2s v2 | 2 | 4 | ~$61 | Batch processing |
| F4s v2 | 4 | 8 | ~$122 | Gaming servers |
| F8s v2 | 8 | 16 | ~$244 | ML inference |
| F16s v2 | 16 | 32 | ~$488 | HPC workloads |
| F32s v2 | 32 | 64 | ~$976 | Large-scale compute |
| F48s v2 | 48 | 96 | ~$1,464 | Very large compute |
| F72s v2 | 72 | 144 | ~$2,196 | Maximum compute |

---

## Lsv2-Series — Storage Optimised
| Size | vCPU | RAM (GB) | NVMe Storage | Est. $/month | Best For |
|------|------|-----------|-------------|--------------|----------|
| L8s v2 | 8 | 64 | 1.92 TB | ~$553 | NoSQL databases |
| L16s v2 | 16 | 128 | 3.84 TB | ~$1,107 | Elasticsearch |
| L32s v2 | 32 | 256 | 7.68 TB | ~$2,213 | Large NoSQL |
| L48s v2 | 48 | 384 | 11.52 TB | ~$3,320 | Very large storage |
| L64s v2 | 64 | 512 | 15.36 TB | ~$4,427 | Maximum storage |
| L80s v2 | 80 | 640 | 19.2 TB | ~$5,534 | Highest local storage |

---

## M-Series — Very Large Memory (SAP HANA)
| Size | vCPU | RAM (GB) | Est. $/month | Best For |
|------|------|-----------|--------------|----------|
| M8ms | 8 | 218.75 | ~$1,646 | Medium SAP HANA |
| M16ms | 16 | 437.5 | ~$3,293 | SAP HANA |
| M32ms | 32 | 875 | ~$6,586 | Large SAP HANA |
| M64ms | 64 | 1,750 | ~$13,172 | Very large HANA |
| M128ms | 128 | 3,892 | ~$26,344 | Largest HANA |
| M192ims v2 | 192 | 4,096 | ~$40,000 | Hyperscale HANA |

---

## NC/ND/NV-Series — GPU
| Size | vCPU | RAM (GB) | GPU | VRAM | Est. $/month | Best For |
|------|------|-----------|-----|------|--------------|----------|
| NC6s v3 | 6 | 112 | 1x V100 | 16 GB | ~$2,200 | ML training |
| NC12s v3 | 12 | 224 | 2x V100 | 32 GB | ~$4,400 | Large training |
| NC24s v3 | 24 | 448 | 4x V100 | 64 GB | ~$8,800 | Distributed training |
| ND40rs v2 | 40 | 672 | 8x V100 | 256 GB | ~$22,000 | Very large ML |
| NC4as T4 v3 | 4 | 28 | 1x T4 | 16 GB | ~$379 | ML inference |
| NC8as T4 v3 | 8 | 56 | 1x T4 | 16 GB | ~$541 | Medium inference |
| NC16as T4 v3 | 16 | 110 | 1x T4 | 16 GB | ~$867 | Larger inference |
| NC64as T4 v3 | 64 | 440 | 4x T4 | 64 GB | ~$3,460 | Large inference |
| NV6 | 6 | 56 | 1/2 M60 | 8 GB | ~$730 | Virtual desktop |
| NV12 | 12 | 112 | 1x M60 | 8 GB | ~$1,460 | Remote visualisation |
| NV24 | 24 | 224 | 2x M60 | 16 GB | ~$2,920 | Heavy visualisation |

---

## Azure Purchasing / Pricing Options
| Option | Discount | Commitment | Notes |
|--------|----------|------------|-------|
| Pay-as-you-go | — | None | Billed per second |
| 1-yr Reserved (No Upfront) | ~30% | 1 year | Monthly payments |
| 1-yr Reserved (All Upfront) | ~35–40% | 1 year | Single payment |
| 3-yr Reserved (All Upfront) | ~50–60% | 3 years | Best rate |
| Spot VMs | up to 90% | None | Evictable on 30-sec notice |
| Azure Hybrid Benefit | up to 49% | Existing license | Windows Server / SQL Server BYOL |
| Dev/Test Pricing | up to 55% | Dev/Test subscription | Windows VMs at Linux rates |
| Azure Savings Plan for Compute | ~15–17% | 1 or 3 years | Flexible across VM families |

---

## Azure Functions — Serverless Compute
| Component | Free Tier | Paid Rate |
|-----------|-----------|-----------|
| Executions | 1M/month free | $0.20/million |
| Execution time (per GB-s) | 400,000 GB-s/month free | $0.000016 |
| Premium plan (EP1, 1 vCPU, 3.5 GB) | — | $0.173/hr |
| Premium plan (EP2, 2 vCPU, 7 GB) | — | $0.346/hr |
| Premium plan (EP3, 4 vCPU, 14 GB) | — | $0.691/hr |

---

## Azure Container Instances (ACI) — Serverless Containers
| Resource | Cost |
|----------|------|
| vCPU (per second) | $0.000012 |
| Memory GB (per second) | $0.0000013 |
| Linux containers (1 vCPU, 1 GB, 1hr) | ~$0.050 |
| Windows containers (1 vCPU, 1 GB, 1hr) | ~$0.060 |

---

## Azure Virtual Machine Scale Sets
| Feature | Details |
|---------|---------|
| Cost | Free — pay only for underlying VMs |
| Scaling | Metric-based, schedule-based, predictive |
| Min/Max instances | Configurable |
| Scale-in policy | Newest / oldest / closest to upgrade domain |
| Spot VM support | Yes |
| Availability zones | Yes |

*Prices are approximate East US pay-as-you-go rates as of 2024.*
