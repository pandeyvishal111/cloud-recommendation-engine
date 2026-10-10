# GCP — Messaging & Streaming Factsheet

---

## Cloud Pub/Sub — Managed Messaging Service

### Pricing
| Item | Free Tier | Paid Rate |
|---|---|---|
| Data volume (first 10 GB/month) | 10 GB/month free | $0.04/GB |
| Data volume (10–50 TB/month) | — | $0.02/GB |
| Data volume (50–100 TB/month) | — | $0.01/GB |
| Data volume (100+ TB/month) | — | $0.006/GB |
| Snapshot storage (per GB/month) | — | $0.08/GB |
| Seek operations | — | Free |

### Message Retention
| Option | Cost |
|---|---|
| Default retention (7 days) | Included in data cost |
| Extended retention (up to 31 days, per GB-day) | $0.002/GB/day |

### Key Features
- At-least-once delivery guarantee
- Push and Pull delivery modes
- Dead-letter topics (max delivery attempts configurable)
- Message ordering (per ordering key)
- Exactly-once delivery (ordering + acknowledgment)
- BigQuery subscription (direct write to BQ table)
- Cloud Storage subscription (archive to GCS)
- Schema validation (Avro, Protocol Buffers)
- Message filtering (attribute-based)
- Message replay (within retention window)
- VPC Service Controls support
- CMEK encryption
- Global topics with regional endpoint support
- Best For: event-driven microservices, real-time analytics ingestion, log aggregation

---

## Cloud Tasks — Managed Async Task Queues

| Item | Free Tier | Paid Rate |
|---|---|---|
| Task operations (per million) | 1 million/month free | $0.40/million |

### Task Operation Types
Each of the following counts as one operation:
- Task creation
- Task delivery (attempt)
- Task deletion
- Task listing

### Key Features
- HTTP targets (any HTTPS endpoint, Cloud Run, Cloud Functions, App Engine)
- App Engine built-in targets
- Rate limiting per queue (dispatches/sec, max concurrent)
- Retry config (max attempts, min/max backoff, max doublings)
- Scheduled delivery (deliver at a specific future time, up to 30 days)
- Task deduplication (by task name within dedup window)
- Cloud Monitoring metrics per queue
- Best For: decoupling services, retryable background jobs, scheduled future execution

---

## Cloud Scheduler — Managed Cron Service

| Item | Free Tier | Paid Rate |
|---|---|---|
| Jobs (first 3/month/project) | 3 jobs/month | $0.10/job/month |

### Key Features
- Unix cron expression syntax
- Targets: HTTP/S endpoints, Pub/Sub topics, Cloud Tasks queues, App Engine
- OAuth2 / OIDC token for auth on HTTP targets
- Retry on failure (configurable count and interval)
- Time zone support (all IANA zones)
- Best For: periodic ETL jobs, report scheduling, cache warming, batch triggers

---

## Dataflow — Managed Apache Beam (Stream & Batch)

### Pricing
| Resource | Cost/hr |
|---|---|
| n1-standard-1 vCPU (per vCPU) | $0.056 |
| n1-standard-1 memory (per GB) | $0.003557 |
| GPU (NVIDIA T4, per GPU) | $0.35 |
| Streaming Engine (per vCPU) | $0.00521 additional |
| Shuffle service (batch, per GB shuffled) | $0.011 |
| Dataflow Prime (autoscaling, per DCU-hr) | $0.084 |
| Flex templates | Same compute rates |
| Spot/preemptible workers | ~70% off worker cost |

### Dataflow Free Tier
First 100 GB of data shuffled per month is free (batch jobs).

### Key Features
- Apache Beam SDK (Java, Python, Go)
- Unified model for batch and streaming
- Auto-scaling (worker count scales with backlog)
- Exactly-once processing (Streaming Engine)
- Side inputs, windowing, triggers (streaming)
- Templates (pre-built: Pub/Sub to BigQuery, GCS to BigQuery, etc.)
- Flexible resource scheduling (FlexRS, for batch — up to 40% savings)
- Regional endpoints
- Best For: ETL pipelines, real-time analytics, log processing, ML feature engineering

---

## Eventarc — Unified Event Routing

| Item | Free Tier | Paid Rate |
|---|---|---|
| Events from Cloud Audit Logs (per million) | 1 million/month | $0.40/million |
| Events from Pub/Sub (direct) | Pub/Sub rates | Pub/Sub rates |
| Advanced Pub/Sub pipeline events (per million) | — | $0.40/million |

### Key Features
- Pub/Sub-backed event delivery
- Sources: 90+ Google Cloud services via Cloud Audit Logs
- Targets: Cloud Run, Cloud Functions (Gen 2), GKE, Workflows
- CloudEvents standard compliance (portable event format)
- Retry with exponential backoff
- Dead-letter topics
- Filtering on event attributes
- Best For: event-driven architectures, replacing polling with push events

---

## Datastream — Change Data Capture (CDC)

### Pricing
| Data Volume | Cost per GB |
|---|---|
| First 100 GB/month | Free |
| 100 GB–10 TB/month | $0.50/GB |
| 10–100 TB/month | $0.45/GB |
| 100+ TB/month | $0.40/GB |

### Source Databases Supported
| Source | Protocol |
|---|---|
| Oracle | LogMiner |
| MySQL | Binary log (binlog) |
| PostgreSQL | Logical replication (pglogical) |
| SQL Server | Transaction log |
| Salesforce | Salesforce CDC |

### Destination Targets
Cloud Storage (Avro, JSON), BigQuery (real-time replication), Cloud Spanner

### Key Features
- Serverless (no infrastructure to manage)
- Low-latency replication (seconds to minutes)
- Schema change detection and handling
- Backfill (initial load + ongoing replication)
- Private connectivity (VPC peering, reverse SSH)
- Best For: real-time analytics on operational data, database migration, CDC pipelines

---

## Dataproc — Managed Hadoop/Spark

### Pricing (Dataproc premium on top of VM costs)
| Item | Cost |
|---|---|
| Dataproc surcharge (per vCPU/hr) | $0.010 |
| Dataproc surcharge (preemptible vCPU/hr) | $0.010 |
| VM compute (underlying GCE) | Standard GCE rates |
| Dataproc Serverless (per DCU-hr) | $0.075 |
| Dataproc Serverless memory (per GB-hr) | $0.008 |
| Dataproc on GKE | Dataproc surcharge + GKE node cost |

### Key Features
- Apache Spark, Hadoop, Flink, Hive, Pig, Presto on GCP
- Cluster autoscaling
- Dataproc Metastore (Hive metastore managed service)
- Custom image support
- Spot/Preemptible workers (secondary worker pools)
- Fast cluster startup (~90 seconds)
- Best For: ETL, batch analytics, ML pipelines, migrating on-prem Hadoop workloads

---

## Messaging & Streaming Decision Guide

| Requirement | Recommended Service |
|---|---|
| Simple async messaging, decoupling | Cloud Pub/Sub |
| Guaranteed ordered delivery | Pub/Sub (with message ordering) |
| Deferred/scheduled task execution | Cloud Tasks |
| Periodic cron-based triggers | Cloud Scheduler |
| Real-time stream processing (Apache Beam) | Dataflow |
| Event routing from GCP services | Eventarc |
| Database change data capture (CDC) | Datastream |
| Hadoop/Spark workloads | Dataproc |
| Dead-letter / retry patterns | Pub/Sub + Cloud Tasks |
| Fanout to multiple consumers | Pub/Sub (multiple subscriptions) |

---

*Prices are us-central1 / global rates as of 2024.*
