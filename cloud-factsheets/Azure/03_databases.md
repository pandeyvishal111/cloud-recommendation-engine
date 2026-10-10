# Azure — Databases Factsheet

---

## Azure SQL Database — Managed SQL Server

### vCore Purchasing Model
#### General Purpose (Provisioned)
| vCores | RAM (GB) | Est. $/month | Best For |
|---|---|---|---|
| 2 vCores | 10.4 | ~$374 | Small to medium apps |
| 4 vCores | 20.4 | ~$747 | Medium production |
| 8 vCores | 40.8 | ~$1,494 | High-traffic apps |
| 16 vCores | 81.6 | ~$2,988 | Large apps |
| 24 vCores | 122.4 | ~$4,483 | Very large apps |
| 32 vCores | 163.2 | ~$5,977 | Enterprise |
| 80 vCores | 408 | ~$14,943 | Largest |

#### Business Critical (includes high-availability replicas)
| vCores | RAM (GB) | Est. $/month | Best For |
|---|---|---|---|
| 4 vCores | 20.4 | ~$1,637 | Mission-critical low latency |
| 8 vCores | 40.8 | ~$3,275 | Business-critical apps |
| 16 vCores | 81.6 | ~$6,549 | Large critical workloads |
| 32 vCores | 163.2 | ~$13,099 | Very large critical |
| 80 vCores | 408 | ~$32,747 | Largest critical |

#### Hyperscale
| vCores | Storage | Est. $/month | Best For |
|---|---|---|---|
| 4 vCores | Up to 100 TB | ~$747 (compute) + $0.115/GB (storage) | Very large databases |
| 8 vCores | Up to 100 TB | ~$1,494 + storage | Databases that outgrow 4 TB |
| 16 vCores | Up to 100 TB | ~$2,988 + storage | Large-scale enterprise |

#### Serverless
| Config | Cost | Best For |
|---|---|---|
| 0.5–16 vCores (auto-scales) | $0.000267/vCore-second | Intermittent, unpredictable workloads |
| Min/max vCores | Configurable | Dev/test, apps with variable load |
| Auto-pause delay | Configurable (1 hr minimum) | Auto-pauses when idle (storage charged) |

### DTU Purchasing Model (legacy)
| Tier | DTUs | Storage | Est. $/month | Best For |
|---|---|---|---|---|
| Basic | 5 DTU | 2 GB | ~$5 | Dev/test only |
| Standard S0 | 10 DTU | 250 MB | ~$15 | Light workloads |
| Standard S2 | 50 DTU | 250 GB | ~$75 | Small production |
| Standard S4 | 200 DTU | 500 GB | ~$300 | Medium workloads |
| Standard S7 | 800 DTU | 1 TB | ~$600 | Large workloads |
| Standard S12 | 3,000 DTU | 1 TB | ~$1,470 | Highest standard |
| Premium P1 | 125 DTU | 500 GB | ~$465 | In-memory OLTP |
| Premium P2 | 250 DTU | 500 GB | ~$930 | High-perf production |
| Premium P4 | 500 DTU | 500 GB | ~$1,860 | Very large |
| Premium P11 | 1,750 DTU | 4 TB | ~$4,653 | Largest premium |

### Azure SQL Storage
| Item | Cost |
|---|---|
| General Purpose storage (per GB/month) | $0.115 |
| Business Critical storage (per GB/month) | $0.115 |
| Hyperscale storage (per GB/month) | $0.115 |
| Backup storage (RA-GRS, per GB/month) | $0.095 |

---

## Azure Database for PostgreSQL — Flexible Server

### Burstable Tier
| SKU | vCPU | RAM (GB) | Est. $/month | Best For |
|---|---|---|---|---|
| B1ms | 1 | 2 | ~$15 | Dev/test |
| B2s | 2 | 4 | ~$31 | Light workloads |
| B2ms | 2 | 8 | ~$58 | Small apps |
| B4ms | 4 | 16 | ~$116 | Medium dev |
| B8ms | 8 | 32 | ~$231 | Larger dev |
| B12ms | 12 | 48 | ~$347 | Heavy dev |
| B16ms | 16 | 64 | ~$463 | Very large dev |
| B20ms | 20 | 80 | ~$578 | Largest burstable |

### General Purpose Tier
| vCores | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|
| 2 | 8 | $0.188 | ~$135 | Small production |
| 4 | 16 | $0.376 | ~$271 | Web apps |
| 8 | 32 | $0.751 | ~$541 | App servers |
| 16 | 64 | $1.503 | ~$1,082 | High-traffic |
| 32 | 128 | $3.005 | ~$2,164 | Enterprise |
| 48 | 192 | $4.508 | ~$3,246 | Very large |
| 64 | 256 | $6.010 | ~$4,327 | Largest GP |

### Memory Optimized Tier
| vCores | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|
| 2 | 16 | $0.276 | ~$199 | Memory-intensive |
| 4 | 32 | $0.552 | ~$397 | Analytics |
| 8 | 64 | $1.104 | ~$795 | Large DBs |
| 16 | 128 | $2.208 | ~$1,590 | Enterprise DBs |
| 32 | 256 | $4.416 | ~$3,180 | SAP, large OLAP |
| 48 | 384 | $6.624 | ~$4,769 | Very large |
| 64 | 504 | $8.832 | ~$6,359 | Largest memory |

### Storage
| Item | Cost |
|---|---|
| Storage (per GB/month) | $0.115 |
| Backup (per GB/month) | $0.095 |

---

## Azure Database for MySQL — Flexible Server

Same tier structure as PostgreSQL Flexible Server:
- Burstable: B1ms ($15/month) → B20ms ($578/month)
- General Purpose: 2–64 vCores ($135 – $4,327/month)
- Memory Optimized: 2–64 vCores ($199 – $6,359/month)
- Storage: $0.115/GB/month

---

## Azure Cosmos DB — Globally Distributed NoSQL

### APIs Supported
| API | Use Case |
|---|---|
| NoSQL (Core) | Document store (JSON) |
| MongoDB | MongoDB compatible |
| Cassandra | Wide-column / CQL |
| Gremlin | Graph database |
| Table | Key-value store |
| PostgreSQL (Citus) | Distributed relational |

### Capacity Modes
| Mode | RU/s Cost (manual) | Best For |
|---|---|---|
| Provisioned Throughput | $0.008/100 RU/hr ($5.84/100 RU/month) | Steady workloads |
| Autoscale | $0.016/100 RU/hr (scaled value) | Variable traffic |
| Serverless | $0.282/million RUs | Dev/test, infrequent access |

### Cosmos DB Storage & Replication
| Item | Cost |
|---|---|
| Storage (per GB/month) | $0.25 |
| Analytical store (per GB/month) | $0.028 |
| Backup storage (per GB/month) | $0.10 |
| Multi-region writes (additional per 100 RU/hr) | $0.016 |
| Geo-redundant reads (per region beyond 1) | Regional read RU cost |

---

## Azure Cache for Redis

| Tier | Cache Size | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|
| Basic C0 | 250 MB | $0.017 | ~$12 | Dev/test |
| Basic C1 | 1 GB | $0.055 | ~$40 | Dev/test |
| Basic C2 | 6 GB | $0.110 | ~$79 | Small dev |
| Basic C3 | 13 GB | $0.226 | ~$163 | Medium dev |
| Standard C0 | 250 MB | $0.034 | ~$24 | Small production |
| Standard C1 | 1 GB | $0.109 | ~$78 | Small apps |
| Standard C2 | 6 GB | $0.219 | ~$158 | Medium apps |
| Standard C3 | 13 GB | $0.453 | ~$326 | Larger apps |
| Standard C4 | 26 GB | $0.906 | ~$653 | Large apps |
| Standard C5 | 53 GB | $1.767 | ~$1,272 | Very large |
| Standard C6 | 120 GB | $3.557 | ~$2,561 | Enterprise |
| Premium P1 | 6 GB | $0.608 | ~$438 | Enterprise features |
| Premium P2 | 13 GB | $1.215 | ~$875 | Geo-replication |
| Premium P3 | 26 GB | $2.430 | ~$1,750 | Large enterprise |
| Premium P4 | 53 GB | $4.861 | ~$3,500 | Very large enterprise |
| Premium P5 | 120 GB | $9.722 | ~$7,000 | Largest premium |

### Key Features (Premium tier)
- Redis Cluster (shard across multiple nodes)
- Geo-replication (active-active or active-passive)
- Private endpoint support
- Virtual network injection
- Data persistence (RDB/AOF)
- Azure Active Directory authentication

---

## Azure Synapse Analytics — Data Warehouse & Analytics

### Dedicated SQL Pool (formerly SQL Data Warehouse)
| DWU | Compute Cost/hr | Est. $/month | Best For |
|---|---|---|---|
| DW100c | $1.51 | ~$1,087 | Small DWH |
| DW200c | $3.02 | ~$2,174 | Medium DWH |
| DW300c | $4.53 | ~$3,262 | — |
| DW500c | $7.55 | ~$5,436 | — |
| DW1000c | $15.10 | ~$10,872 | Large DWH |
| DW2000c | $30.20 | ~$21,744 | — |
| DW5000c | $75.50 | ~$54,360 | Enterprise DWH |
| DW6000c | $90.60 | ~$65,232 | — |
| DW30000c | $453 | ~$326,160 | Largest |

### Serverless SQL Pool
| Item | Cost |
|---|---|
| Data processed (per TB) | $5.00 |
| Best For | Ad hoc queries over data lake |

### Apache Spark Pool
| Node Size | vCPU | RAM | Cost/hr (per node) |
|---|---|---|---|
| Small | 4 | 32 GB | $0.295/vCore-hr |
| Medium | 8 | 64 GB | $0.295/vCore-hr |
| Large | 16 | 128 GB | $0.295/vCore-hr |
| XLarge | 32 | 256 GB | $0.295/vCore-hr |
| XXLarge | 64 | 512 GB | $0.295/vCore-hr |

### Synapse Data Integration (Pipelines)
| Item | Cost |
|---|---|
| Data Integration Unit-hour (DIU-hr) | $0.25 |
| Pipeline runs (per run) | $1.00/1,000 |

---

## Azure Database for MariaDB

| vCores | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|
| Basic 1 | 1 | 2 | $0.034 | Dev/test |
| Basic 2 | 2 | 4 | $0.068 | Small apps |
| GP 2 | 2 | 10 | $0.188 | Production |
| GP 4 | 4 | 20 | $0.376 | Medium apps |
| GP 8 | 8 | 40 | $0.751 | Large apps |
| GP 16 | 16 | 80 | $1.503 | Enterprise |
| MO 2 | 2 | 20 | $0.276 | Memory-intensive |
| MO 4 | 4 | 40 | $0.552 | Analytics |

> **Note:** Azure Database for MariaDB is being retired. Migration to Azure Database for MySQL or Azure Database for PostgreSQL is recommended.

---

*Prices are East US pay-as-you-go rates as of 2024.*
