# AWS — Databases Factsheet

---

## Amazon RDS — Relational Database Service
Engines: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2

### RDS PostgreSQL / MySQL — Instance Tiers (Multi-AZ price)
| Instance | vCPU | RAM (GB) | Single-AZ $/month | Multi-AZ $/month | Best For |
|---|---|---|---|---|---|
| db.t3.micro | 2 | 1 | ~$14 | ~$29 | Dev/test |
| db.t3.small | 2 | 2 | ~$21 | ~$42 | Dev/test |
| db.t3.medium | 2 | 4 | ~$35 | ~$70 | Small apps |
| db.t3.large | 2 | 8 | ~$70 | ~$141 | Light production |
| db.t3.xlarge | 4 | 16 | ~$141 | ~$282 | Medium apps |
| db.t3.2xlarge | 8 | 32 | ~$282 | ~$565 | Larger workloads |
| db.m5.large | 2 | 8 | ~$107 | ~$214 | Production |
| db.m5.xlarge | 4 | 16 | ~$214 | ~$428 | High-traffic apps |
| db.m5.2xlarge | 8 | 32 | ~$428 | ~$856 | Enterprise apps |
| db.m5.4xlarge | 16 | 64 | ~$856 | ~$1,713 | Large databases |
| db.m5.8xlarge | 32 | 128 | ~$1,713 | ~$3,426 | Very large production |
| db.r5.large | 2 | 16 | ~$140 | ~$281 | Memory-intensive |
| db.r5.xlarge | 4 | 32 | ~$281 | ~$563 | Analytics databases |
| db.r5.2xlarge | 8 | 64 | ~$563 | ~$1,126 | SAP, OLAP |
| db.r5.4xlarge | 16 | 128 | ~$1,126 | ~$2,252 | Very large DBs |
| db.r5.8xlarge | 32 | 256 | ~$2,252 | ~$4,505 | Largest memory DBs |

### RDS Storage
| Type | Cost | Notes |
|---|---|---|
| gp3 SSD (General Purpose) | $0.115/GB/month | 3,000 IOPS baseline free |
| gp2 SSD (legacy) | $0.115/GB/month | 3 IOPS/GB baseline |
| io1 Provisioned IOPS SSD | $0.125/GB + $0.10/IOPS/month | Up to 256,000 IOPS |
| Magnetic (legacy) | $0.10/GB/month | Legacy workloads |
| Automated backups | Free (up to DB size) | Beyond: $0.095/GB/month |
| Snapshot storage | $0.095/GB/month | Beyond free tier |

---

## Amazon Aurora — Cloud-Native Database

| Edition | Compatibility | Storage Cost | ACU Cost | Best For |
|---|---|---|---|---|
| Aurora MySQL | MySQL 5.7 / 8.0 | $0.10/GB/month | $0.10/ACU-hr | MySQL workloads needing higher availability |
| Aurora PostgreSQL | PostgreSQL 13–15 | $0.10/GB/month | $0.10/ACU-hr | PostgreSQL with auto-scaling |
| Aurora Serverless v2 | MySQL / PostgreSQL | $0.10/GB/month | $0.12/ACU-hr | Variable / intermittent workloads |
| Aurora Global Database | MySQL / PostgreSQL | $0.10/GB/month | Standard + $0.20/million replicated writes | Multi-region reads / DR |
| Aurora I/O Optimized | MySQL / PostgreSQL | $0.225/GB/month | $0.22/ACU-hr | High I/O workloads (saves on I/O charges) |

### Aurora I/O Cost (Standard config)
| Item | Cost |
|---|---|
| I/O requests | $0.20/million |
| Storage (auto-grows in 10 GB increments) | $0.10/GB/month |
| Backtrack (per change record) | $0.012/million |

---

## Amazon DynamoDB — NoSQL (Key-Value & Document)

### Capacity Modes
| Mode | Write Cost | Read Cost | Best For |
|---|---|---|---|
| On-Demand | $1.25/million WRU | $0.25/million RRU | Unpredictable or spiky traffic |
| Provisioned | $0.00065/WCU/hour | $0.00013/RCU/hour | Steady, predictable traffic |

### DynamoDB Additional Costs
| Feature | Cost |
|---|---|
| Storage (first 25 GB/month) | Free |
| Storage (beyond 25 GB) | $0.25/GB/month |
| DynamoDB Accelerator (DAX) — dax.t3.small | $0.050/hr (~$36/month) | In-memory caching |
| DAX — dax.r5.large | $0.269/hr (~$194/month) | Production caching |
| Global Tables (replicated writes) | $1.875/million WRU | Multi-region replication |
| DynamoDB Streams | $0.02/million read request units | Change data capture |
| Point-in-time recovery | $0.20/GB/month | PITR enabled tables |
| DynamoDB export to S3 | $0.10/GB exported | Data analysis |

---

## Amazon ElastiCache — In-Memory Database

### Redis Instances
| Node Type | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| cache.t3.micro | 2 | 0.5 | $0.017 | ~$12 | Dev/test |
| cache.t3.small | 2 | 1.37 | $0.034 | ~$24 | Small caches |
| cache.t3.medium | 2 | 3.09 | $0.068 | ~$49 | Small apps |
| cache.r6g.large | 2 | 13.07 | $0.166 | ~$120 | Session store |
| cache.r6g.xlarge | 4 | 26.32 | $0.333 | ~$240 | High-traffic cache |
| cache.r6g.2xlarge | 8 | 52.82 | $0.665 | ~$479 | Large cache |
| cache.r6g.4xlarge | 16 | 105.81 | $1.330 | ~$958 | Very large cache |
| cache.r6g.8xlarge | 32 | 209.55 | $2.656 | ~$1,912 | Enterprise cache |
| cache.r6g.12xlarge | 48 | 317.77 | $3.990 | ~$2,873 | Largest cache |

### Memcached Instances
| Node Type | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| cache.t3.micro | 2 | 0.5 | $0.017 | ~$12 | Dev/test |
| cache.m6g.large | 2 | 6.38 | $0.131 | ~$94 | Simple caching |
| cache.m6g.xlarge | 4 | 12.93 | $0.261 | ~$188 | Medium workloads |
| cache.m6g.2xlarge | 8 | 25.05 | $0.522 | ~$376 | High-traffic apps |

---

## Amazon Redshift — Data Warehouse

### RA3 Node Types (Managed Storage)
| Node Type | vCPU | RAM (GB) | Managed Storage | Cost/node/hr | Est. $/node/month | Best For |
|---|---|---|---|---|---|---|
| ra3.xlplus | 4 | 32 | Up to 32 TB | $1.086 | ~$782 | Small data warehouses |
| ra3.4xlarge | 12 | 96 | Up to 128 TB | $3.26 | ~$2,347 | Medium warehouses |
| ra3.16xlarge | 48 | 384 | Up to 128 TB | $13.04 | ~$9,389 | Large enterprise DWH |

### Redshift Serverless
| Item | Cost |
|---|---|
| RPU (Redshift Processing Unit) per hour | $0.36/RPU-hr |
| Base capacity | 32 RPUs minimum |
| Storage | $0.024/GB/month |
| Best For | Intermittent analytics, variable workloads |

### Redshift Additional Costs
| Item | Cost |
|---|---|
| Concurrency Scaling (per second) | $0.0013/second |
| Spectrum (data scanned in S3, per TB) | $5.00 |
| Backup (beyond free allocation) | $0.024/GB/month |

---

## Amazon DocumentDB — MongoDB-Compatible

| Instance | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| db.t3.medium | 2 | 4 | $0.076 | ~$55 | Dev/test |
| db.r5.large | 2 | 16 | $0.277 | ~$199 | Small production |
| db.r5.xlarge | 4 | 32 | $0.554 | ~$399 | Medium apps |
| db.r5.2xlarge | 8 | 64 | $1.108 | ~$798 | Large apps |
| db.r5.4xlarge | 16 | 128 | $2.216 | ~$1,596 | Very large apps |
| db.r6g.2xlarge | 8 | 64 | $0.964 | ~$694 | Graviton cost savings |

### DocumentDB Storage & I/O
| Item | Cost |
|---|---|
| Storage | $0.10/GB/month |
| I/O | $0.20/million requests |
| Backup (beyond retention window) | $0.021/GB/month |

---

## Amazon Neptune — Graph Database

| Instance | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| db.t3.medium | 2 | 4 | $0.082 | ~$59 | Dev/test |
| db.r5.large | 2 | 16 | $0.295 | ~$212 | Small graph apps |
| db.r5.xlarge | 4 | 32 | $0.590 | ~$425 | Medium graph apps |
| db.r5.2xlarge | 8 | 64 | $1.180 | ~$850 | Knowledge graphs |
| db.r5.4xlarge | 16 | 128 | $2.360 | ~$1,699 | Large graph workloads |

### Neptune Storage
| Item | Cost |
|---|---|
| Storage | $0.10/GB/month |
| I/O | $0.20/million requests |
| Serverless Neptune (NCU-hr) | $0.12/NCU-hr |

---

## Amazon Timestream — Time-Series Database

| Component | Cost | Notes |
|---|---|---|
| Write (per million events) | $0.50 | Up to 1 KB each |
| Memory store queries (per GB scanned) | $0.036 | Recent data, fast |
| Magnetic store queries (per GB scanned) | $0.01 | Historical data |
| Memory store storage (per GB/hr) | $0.036 | Data in hot tier |
| Magnetic store storage (per GB/month) | $0.03 | Long-term storage |

### Key Features
- Serverless, auto-scales
- Purpose-built for IoT, DevOps, industrial telemetry
- SQL query interface
- Built-in time-series analytics functions
- Integrates with Grafana, Apache Kafka, Kinesis

---

*Prices are US East (N. Virginia) on-demand rates as of 2024. Multi-AZ pricing approximately doubles compute cost.*
