# GCP — Storage Factsheet

---

## Cloud Storage — Object Storage

### Storage Classes
| Storage Class | Min Duration | Retrieval Latency | Cost ($/GB/month) | Best For |
|---|---|---|---|---|
| Standard | None | Milliseconds | $0.020 | Frequently accessed, website content |
| Nearline | 30 days | Milliseconds | $0.010 | Monthly backups, data accessed ~once/month |
| Coldline | 90 days | Milliseconds | $0.004 | Quarterly archives, DR backups |
| Archive | 365 days | Milliseconds | $0.0012 | Long-term compliance, annual access |

### Multi-Region & Dual-Region Pricing
| Class | Multi-Region ($/GB/month) | Dual-Region ($/GB/month) |
|---|---|---|
| Standard | $0.026 | $0.023 |
| Nearline | $0.010 | $0.010 |
| Coldline | $0.007 | $0.006 |
| Archive | $0.0025 | $0.002 |

### Cloud Storage Operations
| Operation Type | Standard | Nearline | Coldline | Archive |
|---|---|---|---|---|
| Class A (write/list, per 10,000) | $0.05 | $0.10 | $0.10 | $0.50 |
| Class B (read, per 10,000) | $0.004 | $0.01 | $0.05 | $0.50 |
| Data retrieval (per GB) | Free | $0.01 | $0.02 | $0.05 |

### Data Transfer (Egress)
| Scenario | Cost |
|---|---|
| Inbound | Free |
| Same region (to GCE, GKE, Cloud Run) | Free |
| Multi-region within US | Free |
| Egress to internet (Americas/Europe, 0–1 TB/month) | $0.12/GB |
| Egress to internet (Americas/Europe, 1–10 TB/month) | $0.11/GB |
| Egress to internet (Americas/Europe, 10+ TB/month) | $0.08/GB |
| Egress to internet (Asia Pacific) | $0.15/GB |
| Cross-region (e.g., US to EU) | $0.01–$0.08/GB |
| Transfer to another GCP region | $0.01/GB |

### Key Features
- Versioning, object lifecycle management
- Retention policies (WORM compliance)
- Object holds (event-based, temporary)
- Uniform bucket-level access (IAM-only, no ACLs)
- Public Access Prevention
- HMAC keys for S3 interoperability
- Cloud Storage FUSE (mount as filesystem on GCE)
- Turbo replication (dual-region, 15-min RPO)
- Autoclass (auto-tiering based on access patterns)

---

## Persistent Disk — Block Storage

### Zonal Persistent Disk
| Type | Max IOPS | Throughput | Cost ($/GB/month) | Best For |
|---|---|---|---|---|
| Standard (HDD) | 3,000 read / 15,000 write | 400 MB/s | $0.040 | Cold data, backups |
| Balanced (SSD) | 80,000 | 1,200 MB/s | $0.100 | Most production workloads |
| SSD (Performance) | 100,000 | 1,200 MB/s | $0.170 | Databases, IOPS-intensive |
| Extreme | 120,000 | 2,400 MB/s | $0.125 + $0.003/IOPS/month | Highest IOPS requirements |

### Regional Persistent Disk (Multi-Zone HA)
| Type | Cost ($/GB/month) | Notes |
|---|---|---|
| Standard Regional | $0.080 | 2x single-zone; multi-zone HA |
| Balanced Regional | $0.200 | 2x single-zone |
| SSD Regional | $0.340 | 2x single-zone |

### Hyperdisk (Latest Gen, configurable IOPS/throughput)
| Type | Storage $/GB/month | IOPS $/IOPS/month | Throughput $/MB-s/month | Best For |
|---|---|---|---|---|
| Hyperdisk Balanced | $0.060 | $0.001 (above 3,000) | $0.098 (above 140) | Most workloads |
| Hyperdisk Extreme | $0.125 | $0.003 | — | Maximum IOPS |
| Hyperdisk Throughput | $0.022 | — | $0.024 (above 140) | High-throughput, low IOPS |
| Hyperdisk ML | $0.022 | — | $0.024 | ML training storage |

### Snapshots
| Item | Cost |
|---|---|
| Snapshot storage (per GB/month) | $0.026 |
| Snapshot retrieval | Free |
| Snapshot scheduling | Free |

---

## Filestore — Managed NFS

| Tier | Min Capacity | Max Capacity | Throughput | Cost ($/GB/month) | Best For |
|---|---|---|---|---|---|
| Basic HDD | 1 TB | 63.9 TB | 180 MB/s | ~$0.200 | General NFS, moderate throughput |
| Basic SSD | 2.5 TB | 63.9 TB | 480 MB/s | ~$0.740 | Low-latency NFS |
| Zonal (High Scale SSD) | 10 TB | 100 TB | 4.8 GB/s | ~$0.400 | High-throughput multi-client |
| Regional (High Scale SSD) | 10 TB | 100 TB | 4.8 GB/s | ~$0.480 | HA multi-zone NFS |
| Enterprise (Zonal) | 1 TB | 10 TB | 780 MB/s | ~$1.400 | Enterprise NFS, HA within zone |

### Filestore Additional Costs
| Item | Cost |
|---|---|
| Backups (per GB/month) | $0.10 |
| Snapshots (per GB/month) | $0.10 |
| Filestore Multi-share (per share) | No extra charge |

### Key Features
- NFSv3 (Basic/Zonal) / NFSv3 + NFSv4.1 (Regional/Enterprise)
- VPC peering support
- AD authentication (Enterprise tier)
- Multi-share within a Filestore instance (High Scale tiers)
- Best For: Lift-and-shift NFS workloads, GKE PersistentVolumes, rendering farms

---

## Cloud Storage Transfer Service

| Item | Cost |
|---|---|
| Data moved from on-premises sources | $0.10/GB (into Cloud Storage) |
| Data moved between cloud providers | $0.10/GB |
| Data moved between GCP regions/buckets | Free |
| Best For | Bulk data migration, recurring transfers from S3/Azure/on-prem |

---

## Google Cloud Backup and DR

| Item | Cost |
|---|---|
| Backup vault storage (per GB/month) | $0.023 |
| Backup management (per protected resource/month) | $1.50 |
| Backup for databases (per GB/month) | $0.10 |
| Long-term retention storage (per GB/month) | $0.004 |

### Supported Resources
Compute Engine VMs, Cloud SQL, GKE workloads, VMware workloads, SAP HANA, file systems.

---

*Prices are us-central1 (Iowa) rates as of 2024. Multi-region pricing applies to us, eu, and asia multi-regions.*
