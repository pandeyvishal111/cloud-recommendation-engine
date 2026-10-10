# GCP — Databases Factsheet

---

## Cloud SQL — Managed Relational Database
Engines: MySQL, PostgreSQL, SQL Server

### Shared Core (Dev/Test)
| Tier | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| db-f1-micro (shared) | Shared | 0.6 | $0.010 | ~$7 | Minimal dev/test |
| db-g1-small (shared) | Shared | 1.7 | $0.034 | ~$25 | Light dev workloads |

### Standard (Dedicated vCPU)
| Tier | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| db-n1-standard-1 | 1 | 3.75 | $0.097 | ~$70 | Small apps |
| db-n1-standard-2 | 2 | 7.5 | $0.193 | ~$139 | Small production |
| db-n1-standard-4 | 4 | 15 | $0.387 | ~$279 | Medium apps |
| db-n1-standard-8 | 8 | 30 | $0.773 | ~$557 | High-traffic |
| db-n1-standard-16 | 16 | 60 | $1.546 | ~$1,113 | Large apps |
| db-n1-standard-32 | 32 | 120 | $3.093 | ~$2,227 | Enterprise |
| db-n1-standard-64 | 64 | 240 | $6.185 | ~$4,453 | Largest standard |
| db-n1-standard-96 | 96 | 360 | $9.278 | ~$6,680 | Very large |

### High Memory
| Tier | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| db-n1-highmem-2 | 2 | 13 | $0.226 | ~$163 | Memory-intensive small |
| db-n1-highmem-4 | 4 | 26 | $0.451 | ~$325 | Analytics |
| db-n1-highmem-8 | 8 | 52 | $0.902 | ~$650 | Large databases |
| db-n1-highmem-16 | 16 | 104 | $1.804 | ~$1,299 | Very large DBs |
| db-n1-highmem-32 | 32 | 208 | $3.607 | ~$2,597 | Enterprise DBs |
| db-n1-highmem-64 | 64 | 416 | $7.214 | ~$5,194 | SAP / large analytics |
| db-n1-highmem-96 | 96 | 624 | $10.821 | ~$7,791 | Largest memory |

### Cloud SQL Storage
| Type | Cost |
|---|---|
| SSD storage (per GB/month) | $0.170 |
| HDD storage (per GB/month) | $0.090 |
| Backup storage (per GB/month) | $0.080 |
| HA (Regional Instance) | ~2x single-zone price |

### Key Features
- Automatic storage increase
- Read replicas (cross-region available)
- Automated backups (up to 7 days, configurable)
- PITR (point-in-time recovery, up to 7 days)
- Private IP (VPC) / Public IP
- IAM database authentication (PostgreSQL)
- Cloud SQL Auth Proxy for secure connections

---

## AlloyDB for PostgreSQL — High-Performance PostgreSQL

| Config | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| 2 vCPU, 16 GB | 2 | 16 | $0.437 | ~$315 | Small production |
| 4 vCPU, 32 GB | 4 | 32 | $0.876 | ~$631 | Medium production |
| 8 vCPU, 64 GB | 8 | 64 | $1.752 | ~$1,261 | High-traffic apps |
| 16 vCPU, 128 GB | 16 | 128 | $3.504 | ~$2,523 | Large apps |
| 32 vCPU, 256 GB | 32 | 256 | $7.008 | ~$5,046 | Enterprise apps |
| 64 vCPU, 512 GB | 64 | 512 | $14.016 | ~$10,092 | Largest |

### AlloyDB Storage & Additional Costs
| Item | Cost |
|---|---|
| Storage (per GB/month) | $0.130 |
| Network egress | Standard GCP egress rates |
| Cross-region read replicas | ~2x primary region cost |
| AlloyDB Omni (self-managed on-prem) | Software license negotiated |

### Key Features
- 4x faster reads and 2x faster writes vs standard PostgreSQL
- 99.99% HA SLA (built-in HA, no failover configuration needed)
- Separated compute and storage (auto-scale storage)
- In-memory columnar cache (real-time analytics alongside OLTP)
- AI/ML integration (pgvector, LLM-based query advisor)
- Fully PostgreSQL compatible

---

## Cloud Spanner — Globally Distributed Relational DB

| Component | Cost | Notes |
|---|---|---|
| Processing Units (PU) — minimum 100 PU | $0.90/100 PU/hr | ~$657/month per 100 PU (1 node) |
| Storage | $0.30/GB/month | — |
| Free operations tier | 10 GB storage free | (within 90-day trial) |
| Multi-region config | ~3x single-region cost | 3 read-write replicas |

### Spanner Compute Reference
| Scale | Processing Units | Est. Compute $/month |
|---|---|---|
| Dev/test | 100 PU (minimum) | ~$657 |
| Small production | 300 PU | ~$1,971 |
| Medium production | 1,000 PU (1 node) | ~$6,570 |
| Large production | 3,000 PU | ~$19,710 |
| Enterprise | 10,000 PU | ~$65,700 |

### Key Features
- Horizontally scalable, globally consistent (external consistency)
- 99.999% SLA (multi-region config)
- Automatic sharding and rebalancing
- ACID transactions globally
- Change streams (real-time CDC)
- IAM row-level security
- Best For: global financial systems, inventory, gaming leaderboards requiring strong consistency

---

## Firestore — NoSQL Document Database

| Component | Free Tier | Paid Rate |
|---|---|---|
| Document reads (per million) | 50,000/day free | $0.06 |
| Document writes (per million) | 20,000/day free | $0.18 |
| Document deletes (per million) | 20,000/day free | $0.02 |
| Storage (per GB/month) | 1 GB free | $0.18 |
| Network egress (per GB) | 10 GB/month free | Standard GCP rates |

### Key Features
- Real-time listeners (push updates to clients)
- Offline support (client SDKs)
- Native mobile/web SDKs (iOS, Android, Web, Flutter)
- Automatic scaling (serverless)
- Multi-region option (higher cost, higher availability)
- Firestore vs Datastore mode (Firestore native recommended for new apps)
- Security rules (document-level access control)

---

## Bigtable — Wide-Column NoSQL Database

### Node Types
| Node Type | Cost/hr | Est. $/month per node | Best For |
|---|---|---|---|
| SSD production (minimum 3 nodes) | $0.65 | ~$473 | Low-latency, high-throughput |
| HDD production (minimum 3 nodes) | $0.16 | ~$117 | Large, rarely-accessed data |
| SSD development (1 node) | $0.65 | ~$473 | Dev/test (no replication) |
| HDD development (1 node) | $0.16 | ~$117 | Dev/test |
| Autoscaling | Min/max nodes defined | Based on usage | Variable workloads |

### Bigtable Storage
| Type | Cost |
|---|---|
| SSD storage (per GB/month) | $0.170 |
| HDD storage (per GB/month) | $0.026 |
| Backup storage (per GB/month) | $0.026 |

### Key Features
- Apache HBase compatible API
- Sub-10ms read/write latency at scale
- Linear horizontal scaling
- Multi-cluster routing (load balancing / failover)
- Application profiles (traffic routing policies)
- Best For: IoT telemetry, financial data, ad-tech, time-series

---

## Memorystore — In-Memory Database

### Redis
| Tier | Size | Cost/GB/hr | Est. $/month (10 GB) | Best For |
|---|---|---|---|---|
| Basic | 1–300 GB | $0.049/GB/hr | ~$36/GB | Dev/test, single instance |
| Standard (HA) | 1–300 GB | $0.098/GB/hr | ~$72/GB | Production, HA with replica |

### Redis Cluster (High Scale)
| Size | Shards | Est. $/month | Best For |
|---|---|---|---|
| 5 GB (1 shard) | 1 | ~$254 | Small cluster |
| 50 GB (1 shard) | 1 | ~$2,540 | Medium cluster |
| 500 GB (10 shards) | 10 | ~$25,400 | Large cluster |

### Memcached
| Tier | Cost/GB/hr | Best For |
|---|---|---|
| Standard | $0.049/GB/hr | Simple key-value caching, horizontal scale |

### Key Features
- Redis 6.x / 7.x supported
- Persistence (RDB/AOF — Redis only)
- Private IP only (VPC peering required)
- Read replicas (Standard tier)
- Auto failover (Standard tier)
- Maintenance windows configurable
- IAM access control + TLS in transit

---

## BigQuery — Serverless Data Warehouse

### Compute Pricing
| Model | Cost | Best For |
|---|---|---|
| On-Demand (per TB queries) | $6.25/TB | Infrequent, ad hoc queries |
| Standard Edition Slots (per slot-hr) | $0.04 | Consistent query workloads |
| Enterprise Edition Slots (per slot-hr) | $0.06 | Larger teams, BI workloads |
| Enterprise Plus Edition Slots (per slot-hr) | $0.10 | Advanced features, CMEK, BI Engine |
| Flex Slots (100-slot blocks, per hr) | $4.00/100 slots | Short-term capacity bursts |

### Storage Pricing
| Type | Cost ($/GB/month) | Notes |
|---|---|---|
| Active Storage | $0.020 | Modified in last 90 days |
| Long-Term Storage | $0.010 | Not modified for 90+ days (auto) |
| Streaming inserts (per GB) | $0.010 | Real-time ingestion |
| Storage API reads (per TB) | $1.10 | BigQuery Storage Read API |

### BigQuery ML (BQML)
| Feature | Cost |
|---|---|
| Model creation (per TB processed by query) | $6.25 (on-demand rate) |
| Prediction (per TB) | $6.25 (on-demand rate) |
| AutoML tables training (per node-hr) | $19.32 |

### Key Features
- Fully serverless — no cluster/server management
- Standard SQL (ANSI 2011 compliant)
- Federated queries (Cloud Storage, Bigtable, Drive, Cloud SQL)
- BigQuery Omni (multi-cloud — AWS, Azure)
- BigQuery ML (in-database ML)
- Built-in geospatial analytics (GEOGRAPHY type)
- Row/column-level security
- Data sharing marketplace
- Connected Sheets (Google Sheets integration)
- BI Engine (in-memory analytics up to 100 GB)

---

*Prices are us-central1 rates as of 2024. BigQuery on-demand pricing applies to the US multi-region.*
