# AWS — Storage Factsheet

---

## Amazon S3 — Object Storage

### Storage Classes
| Storage Class | Min Duration | Retrieval | Cost ($/GB/month) | Best For |
|---|---|---|---|---|
| S3 Standard | None | Instant | $0.023 | Frequently accessed data, web content |
| S3 Intelligent-Tiering | None | Instant | $0.023 (active) / $0.0125 (infrequent) / $0.004 (archive) | Unknown or changing access patterns |
| S3 Standard-IA | 30 days | Instant | $0.0125 | Backups accessed monthly |
| S3 One Zone-IA | 30 days | Instant | $0.01 | Reproducible infrequent data |
| S3 Glacier Instant Retrieval | 90 days | Milliseconds | $0.004 | Archive with instant access |
| S3 Glacier Flexible Retrieval | 90 days | 1–12 hours | $0.0036 | Long-term archive |
| S3 Glacier Deep Archive | 180 days | Up to 12 hours | $0.00099 | 7–10 year compliance archive |

### S3 Request Pricing
| Request Type | Cost per 1,000 |
|---|---|
| PUT, COPY, POST, LIST | $0.005 |
| GET, SELECT, all others | $0.0004 |
| Lifecycle transitions | $0.01 |
| S3 Select (data scanned per GB) | $0.002 |

### S3 Data Transfer
| Scenario | Cost |
|---|---|
| Data IN from internet | Free |
| Data OUT to internet (first 1 GB/month) | Free |
| Data OUT to internet (up to 10 TB) | $0.09/GB |
| Data OUT to internet (next 40 TB) | $0.085/GB |
| Data OUT to internet (next 100 TB) | $0.07/GB |
| Data OUT to internet (150 TB+) | $0.05/GB |
| S3 Transfer Acceleration | +$0.04–$0.08/GB |
| Data transfer to CloudFront | Free |

### Key Features
- Versioning, replication (cross-region, same-region)
- Event notifications → Lambda/SQS/SNS
- S3 Object Lock (WORM compliance)
- S3 Inventory, Analytics, Storage Lens
- Block Public Access (default on)
- SSE-S3, SSE-KMS, SSE-C encryption

---

## Amazon EBS — Block Storage (for EC2)

| Volume Type | Max IOPS | Max Throughput | Cost | Best For |
|---|---|---|---|---|
| gp3 (General Purpose SSD) | 16,000 | 1,000 MB/s | $0.08/GB/month + $0.005/provisioned IOPS (above 3,000) | Most workloads, boot volumes |
| gp2 (General Purpose SSD, legacy) | 16,000 (burst) | 250 MB/s | $0.10/GB/month | Legacy workloads |
| io2 Block Express (Provisioned IOPS SSD) | 256,000 | 4,000 MB/s | $0.125/GB + $0.065/IOPS | Mission-critical databases |
| io1 (Provisioned IOPS SSD) | 64,000 | 1,000 MB/s | $0.125/GB + $0.065/IOPS | Databases requiring high IOPS |
| st1 (Throughput HDD) | 500 | 500 MB/s | $0.045/GB/month | Big data, log processing |
| sc1 (Cold HDD) | 250 | 250 MB/s | $0.015/GB/month | Cold data, infrequent access |

### EBS Snapshots
| Item | Cost |
|---|---|
| Snapshot storage (US East) | $0.05/GB/month |
| Snapshot restore | Free |
| Fast Snapshot Restore (per AZ enabled) | $0.75/hour |

### Key Features
- Encrypted at rest (AES-256)
- Multi-Attach (io1/io2 only, up to 16 instances)
- Elastic Volumes — resize without downtime
- Point-in-time snapshots to S3
- Available within single AZ only

---

## Amazon EFS — Managed File Storage (NFS)

| Storage Class | Cost ($/GB/month) | Best For |
|---|---|---|
| EFS Standard | $0.30 | Multi-AZ, frequently accessed shared storage |
| EFS Standard-IA (Infrequent Access) | $0.025 | Multi-AZ, infrequently accessed |
| EFS One Zone | $0.16 | Single-AZ, frequently accessed |
| EFS One Zone-IA | $0.013 | Single-AZ, infrequently accessed |

### EFS Additional Costs
| Item | Cost |
|---|---|
| Provisioned Throughput (per MB/s) | $6.00/month |
| Bursting Throughput | Included |
| Data transfer OUT to EC2 (same AZ) | Free |
| Data transfer OUT to EC2 (cross-AZ) | $0.01/GB |

### Key Features
- Elastic — scales to petabytes automatically
- NFSv4.1/4.0 protocol
- Lifecycle management (auto-tiering to IA)
- Encryption at rest and in transit
- POSIX-compliant
- Multi-AZ (Standard) or Single-AZ

---

## Amazon FSx — Managed File Systems

| Service | Protocol | Base Cost | Best For |
|---|---|---|---|
| FSx for Windows File Server | SMB | $0.013/GB/month (HDD) / $0.23/GB/month (SSD) | Windows apps, Active Directory integration |
| FSx for Lustre (Scratch) | Lustre | $0.14/GB/month | HPC, temporary ML training storage |
| FSx for Lustre (Persistent) | Lustre | $0.145/GB/month | Persistent HPC, ML workloads |
| FSx for NetApp ONTAP | NFS, SMB, iSCSI | $0.16/GB/month (SSD) | Enterprise multiprotocol workloads |
| FSx for OpenZFS | NFS | $0.09/GB/month (SSD) | Linux workloads, data migration from on-prem |

### FSx for Windows Additional Costs
| Component | Cost |
|---|---|
| Storage (SSD, 32–65,536 GB) | $0.23/GB/month |
| Storage (HDD, 2,000–65,536 GB) | $0.013/GB/month |
| Throughput capacity (per MBps) | $2.20/month (HDD) |
| Backup storage | $0.05/GB/month |

---

## AWS Backup

| Feature | Cost |
|---|---|
| Backup storage (US East, per GB/month) | $0.05 |
| Restore | Free |
| Backup data transferred cross-region | $0.02/GB |
| Warm tier storage (advanced) | $0.012/GB/month |
| Cold tier storage (advanced) | $0.004/GB/month |

### Resources Supported
EC2 (AMI), EBS, RDS, DynamoDB, EFS, FSx, Aurora, DocumentDB, Neptune, S3, Storage Gateway, VMware Cloud on AWS.

---

*Prices are US East (N. Virginia) rates as of 2024.*
