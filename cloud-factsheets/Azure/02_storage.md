# Azure — Storage Factsheet

---

## Azure Blob Storage — Object Storage

### Storage Tiers
| Tier | Use Case | Cost ($/GB/month) — LRS | Min Duration |
|---|---|---|---|
| Hot | Frequently accessed data | $0.018 | None |
| Cool | Infrequently accessed (30+ days) | $0.01 | 30 days |
| Cold | Rarely accessed (90+ days) | $0.0045 | 90 days |
| Archive | Compliance, long-term backup | $0.00099 | 180 days |

### Redundancy Options (Hot tier price multipliers)
| Redundancy | Description | LRS Price ($/GB/month) | Best For |
|---|---|---|---|
| LRS (Locally Redundant) | 3 copies, 1 datacenter | $0.018 | Non-critical, cost-sensitive |
| ZRS (Zone Redundant) | 3 copies, 3 zones | $0.023 | High availability in a region |
| GRS (Geo Redundant) | 6 copies, 2 regions | $0.036 | Disaster recovery |
| RA-GRS (Read-Access GRS) | GRS + read secondary | $0.045 | DR with read access |
| GZRS (Geo Zone Redundant) | ZRS + geo-replication | $0.045 | Maximum HA + DR |
| RA-GZRS | GZRS + read secondary | $0.05625 | Maximum resiliency |

### Blob Operations Pricing
| Operation | Hot $/10,000 | Cool $/10,000 | Cold $/10,000 |
|---|---|---|---|
| Write (PUT, COPY, POST) | $0.05 | $0.10 | $0.18 |
| Read (GET, LIST, others) | $0.004 | $0.01 | $0.01 |
| Delete | Free | Free | Free |
| Data retrieval (per GB) | Free | $0.01 | $0.03 |

### Data Transfer (Egress)
| Scenario | Cost |
|---|---|
| Within same region | Free |
| Between Azure regions | $0.02/GB |
| To internet (first 5 GB/month) | Free |
| To internet (5 GB – 10 TB) | $0.087/GB |
| To internet (10 TB – 50 TB) | $0.083/GB |

### Key Features
- Azure Data Lake Storage Gen2 (hierarchical namespace on Blob)
- Blob versioning, soft delete, change feed
- Immutability policies (WORM)
- Lifecycle management (auto-tier/delete rules)
- Static website hosting
- Azure CDN integration

---

## Azure Managed Disks — Block Storage

### Standard HDD
| Disk Size | Max IOPS | Max Throughput | Cost/month | Best For |
|---|---|---|---|---|
| S4 (32 GB) | 500 | 60 MB/s | $1.54 | Dev/test, backups |
| S6 (64 GB) | 500 | 60 MB/s | $3.08 | Dev/test |
| S10 (128 GB) | 500 | 60 MB/s | $5.89 | Light workloads |
| S15 (256 GB) | 500 | 60 MB/s | $11.78 | Cold data |
| S20 (512 GB) | 500 | 60 MB/s | $20.38 | Archives |
| S30 (1,024 GB) | 500 | 60 MB/s | $37.63 | Large archives |
| S50 (4,096 GB) | 500 | 60 MB/s | $130.72 | — |

### Standard SSD
| Disk Size | Max IOPS | Max Throughput | Cost/month | Best For |
|---|---|---|---|---|
| E6 (64 GB) | 3,000 | 400 MB/s | $4.80 | Web servers, light production |
| E10 (128 GB) | 3,000 | 400 MB/s | $9.60 | Dev/test production |
| E15 (256 GB) | 3,000 | 400 MB/s | $19.20 | General workloads |
| E20 (512 GB) | 3,000 | 400 MB/s | $38.40 | Medium databases |
| E30 (1,024 GB) | 3,000 | 400 MB/s | $76.80 | Large apps |
| E50 (4,096 GB) | 3,000 | 400 MB/s | $268.80 | — |

### Premium SSD
| Disk Size | Max IOPS | Max Throughput | Cost/month | Best For |
|---|---|---|---|---|
| P6 (64 GB) | 240 | 25 MB/s | $9.60 | Small production |
| P10 (128 GB) | 500 | 100 MB/s | $19.71 | Production databases |
| P15 (256 GB) | 1,100 | 125 MB/s | $37.79 | High-perf apps |
| P20 (512 GB) | 2,300 | 150 MB/s | $73.22 | SQL Server |
| P30 (1,024 GB) | 5,000 | 200 MB/s | $135.17 | Large databases |
| P40 (2,048 GB) | 7,500 | 250 MB/s | $247.75 | Very large DBs |
| P50 (4,096 GB) | 7,500 | 250 MB/s | $495.50 | — |
| P60 (8,192 GB) | 16,000 | 500 MB/s | $942.08 | — |

### Premium SSD v2
| Feature | Details | Cost |
|---|---|---|
| Storage | Per GB/month | $0.12/GB |
| Provisioned IOPS (beyond 3,000 baseline) | Per IOPS/month | $0.005/IOPS |
| Provisioned throughput (beyond 125 MB/s) | Per MB/s/month | $0.12/MB/s |
| Best For | Mission-critical databases with dynamic IOPS needs |

### Ultra Disk
| Feature | Cost |
|---|---|
| Storage | $0.125/GB/month |
| Provisioned IOPS | $0.0065/IOPS/month |
| Provisioned throughput | $0.051/MB/s/month |
| VM reservation | $0.012–$0.018/vCPU/hr |
| Best For | Highest IOPS requirements (SAP HANA, Oracle, SQL Server) |

---

## Azure Files — Managed File Storage

### Tiers
| Tier | Protocol | Cost ($/GB/month) | Best For |
|---|---|---|---|
| Transaction Optimized | SMB / NFS | $0.060 | General file shares with variable access |
| Hot | SMB / NFS | $0.050 | Frequently accessed shares |
| Cool | SMB / NFS | $0.020 | Archiving, infrequently accessed |
| Premium (FileStorage) | SMB / NFS | $0.30/provisioned GB | Low-latency, enterprise apps, databases |

### Azure Files Operations
| Operation | Transaction Optimized | Hot | Cool |
|---|---|---|---|
| List / Create / Get (per 10,000) | $0.015 | $0.015 | $0.060 |
| Read (per 10,000) | $0.012 | $0.012 | $0.130 |
| Write (per 10,000) | $0.050 | $0.050 | $0.180 |
| Data retrieval (per GB) | Free | Free | $0.020 |

### Key Features
- Lift-and-shift Windows file share workloads
- Azure File Sync (cloud tiering, multi-site sync)
- Kerberos authentication (AD DS / Azure AD)
- SMBv3 encryption in transit

---

## Azure NetApp Files

| Service Level | Throughput per TB | Cost ($/TB/month) | Best For |
|---|---|---|---|
| Standard | 16 MB/s | ~$245 | General NFS workloads |
| Premium | 64 MB/s | ~$370 | Databases, ERP |
| Ultra | 128 MB/s | ~$490 | Latency-sensitive apps, SAP |

### Key Features
- Minimum 4 TB capacity pool
- Snapshot (instant, space-efficient)
- Cross-region replication
- NFS v3/v4.1, SMB 2.1/3.x, dual-protocol
- POSIX-compliant, NFSv4.1 ACLs

---

## Azure Backup

| Workload | Backup Storage Cost ($/GB/month) | Instance Cost |
|---|---|---|
| Azure VM (LRS) | $0.024 (first 50 GB free) | $5/protected instance/month (< 50 GB) |
| Azure VM (LRS, > 50 GB) | $0.024 | $10/protected instance/month |
| Azure Files | $0.020 | No instance cost |
| SQL Server in Azure VM | $0.024 | $0.009/backup-storage-GB |
| Azure Database for PostgreSQL | $0.024 | No instance cost |
| Azure Blobs (operational) | Free storage tier used | $5/protected storage account/month |

### Key Features
- Recovery Services Vault (centralized backup management)
- Application-consistent snapshots (VSS)
- Geo-redundant backup storage (GRS option)
- Soft delete (14-day accidental delete protection)
- Cross-region restore

---

*Prices are East US pay-as-you-go rates as of 2024.*
