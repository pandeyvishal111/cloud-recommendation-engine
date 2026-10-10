# AWS — Messaging & Streaming Factsheet

---

## Amazon SQS — Simple Queue Service

### Queue Types & Pricing
| Queue Type | First 1M/month | Beyond Free Tier | Best For |
|---|---|---|---|
| Standard Queue | Free | $0.40/million requests | At-least-once delivery, max throughput, ordering not required |
| FIFO Queue | Free | $0.50/million requests | Exactly-once processing, strict ordering |

### SQS Specifications
| Feature | Standard | FIFO |
|---|---|---|
| Max message size | 256 KB | 256 KB |
| Max retention period | 14 days | 14 days |
| Max visibility timeout | 12 hours | 12 hours |
| Throughput | Unlimited | 300 msg/sec (unbatched) / 3,000 msg/sec (batched) |
| Delivery guarantee | At-least-once | Exactly-once |
| Ordering | Best-effort | Strict per message group |

### SQS Extended Client Library
- Send messages up to 2 GB (stores payload in S3)
- S3 storage cost applies separately

### Key Features
- Dead-letter queues (DLQ) for failed messages
- Long polling (reduces empty responses — up to 20 seconds)
- Server-side encryption (SSE-KMS or SSE-SQS)
- VPC endpoints for private access
- Message deduplication (FIFO, 5-minute window)

---

## Amazon SNS — Simple Notification Service

### Delivery Pricing by Endpoint Type
| Endpoint Type | First 1M/month | Cost per million after |
|---|---|---|
| HTTP/HTTPS | Free | $0.60 |
| Email / Email-JSON | Free | $2.00 |
| Amazon SQS | Free | $0.50 |
| AWS Lambda | Free | $0.50 |
| Mobile Push — ADM, APNs, FCM | 1M free | $0.50 |
| SMS (US, per message) | 100 messages free | $0.00645 |
| Kinesis Data Firehose (per GB) | — | $0.19 |

### SNS FIFO Topics
| Item | Cost |
|---|---|
| API requests to FIFO topic (per million) | $0.50 |
| SQS FIFO deliveries (per million) | $0.50 |

### Key Features
- Fan-out: one publish → many subscribers
- Message filtering (subscription filter policies)
- FIFO topics for ordered, deduplicated delivery
- Message archiving (Kinesis Data Firehose)
- Dead-letter queues for failed deliveries
- Large message support (up to 256 KB)

---

## Amazon MQ — Managed Message Broker

### ActiveMQ Broker Pricing
| Instance | vCPU | RAM | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| mq.t3.micro | 2 | 1 GB | $0.027 | ~$19 | Dev/test |
| mq.m5.large | 2 | 8 GB | $0.302 | ~$218 | Small production |
| mq.m5.xlarge | 4 | 16 GB | $0.605 | ~$436 | Medium production |
| mq.m5.2xlarge | 8 | 32 GB | $1.209 | ~$870 | Large workloads |
| mq.m5.4xlarge | 16 | 64 GB | $2.419 | ~$1,742 | Very large |

### RabbitMQ Broker Pricing
| Instance | vCPU | RAM | Cost/hr | Est. $/month |
|---|---|---|---|---|
| mq.t3.micro | 2 | 1 GB | $0.027 | ~$19 |
| mq.m5.large | 2 | 8 GB | $0.302 | ~$218 |
| mq.m5.xlarge | 4 | 16 GB | $0.605 | ~$436 |

### Storage
| Type | Cost |
|---|---|
| EFS storage (ActiveMQ persistent) | $0.10/GB/month |
| EBS storage (RabbitMQ) | $0.10/GB/month |

### Key Features
- Protocols: AMQP, OpenWire, STOMP, MQTT, WebSocket (ActiveMQ); AMQP 0-9-1 (RabbitMQ)
- Active/standby deployment for HA
- Private networking via VPC
- Best For: migrating existing on-premises message broker workloads

---

## Amazon MSK — Managed Streaming for Apache Kafka

### Broker Instance Types
| Instance | vCPU | RAM (GB) | Cost/hr | Est. $/month (per broker) | Best For |
|---|---|---|---|---|---|
| kafka.t3.small | 2 | 2 | $0.0616 | ~$44 | Dev/test |
| kafka.m5.large | 2 | 8 | $0.2160 | ~$156 | Small production |
| kafka.m5.xlarge | 4 | 16 | $0.4320 | ~$311 | Medium production |
| kafka.m5.2xlarge | 8 | 32 | $0.8640 | ~$622 | Large streaming |
| kafka.m5.4xlarge | 16 | 64 | $1.7280 | ~$1,244 | High-throughput |
| kafka.m5.8xlarge | 32 | 128 | $3.4560 | ~$2,489 | Very large |
| kafka.m5.12xlarge | 48 | 192 | $5.1840 | ~$3,733 | Largest |

**Note:** Minimum 3 brokers recommended for production (multiply by 3 for cluster cost).

### MSK Storage
| Item | Cost |
|---|---|
| Provisioned EBS storage (per GB/month) | $0.10 |
| MSK Tiered Storage (S3 offload, per GB/month) | $0.0230 |

### MSK Serverless
| Item | Cost |
|---|---|
| Cluster capacity (per VCU-hr) | $0.75 |
| Storage (per GB/month) | $0.10 |
| Best For | Variable or unpredictable Kafka workloads |

### Key Features
- Apache Kafka 2.6 – 3.5+
- Multi-AZ replication (3 AZs)
- MSK Connect (Kafka Connect managed)
- MSK Replicator (cross-region replication)
- IAM authentication, TLS in transit, encryption at rest

---

## Amazon Kinesis Data Streams

| Item | Cost | Best For |
|---|---|---|
| Shard-hour (provisioned) | $0.015/shard-hr | Predictable throughput |
| PUT Payload Unit (per million, 25KB each) | $0.014 | Data ingestion |
| Extended retention (7–365 days, per shard-hr) | $0.023 | Long-term stream retention |
| Enhanced fan-out (per shard-hr) | $0.015 | Multiple parallel consumers |
| Enhanced fan-out (per GB retrieved) | $0.013 | Low-latency dedicated consumers |

### Kinesis Serverless (On-Demand mode)
| Item | Cost |
|---|---|
| Data written (per GB) | $0.08 |
| Data read (per GB) | $0.03 |
| Best For | Variable / unpredictable stream traffic |

### Shard Capacity Reference
| Shard count | Write (MB/s) | Write (records/s) | Read (MB/s) |
|---|---|---|---|
| 1 | 1 | 1,000 | 2 |
| 10 | 10 | 10,000 | 20 |
| 100 | 100 | 100,000 | 200 |

---

## Amazon Kinesis Data Firehose — Delivery Streams

| Item | Free Tier | Paid Rate |
|---|---|---|
| Data ingested (per GB, first 500 TB/month) | — | $0.029 |
| Data ingested (next 1.5 PB/month) | — | $0.025 |
| Data format conversion (per GB) | — | $0.018 |
| Dynamic partitioning (per GB) | — | $0.02 |
| VPC delivery (per GB) | — | $0.01 |

### Key Features
- Destinations: S3, Redshift, OpenSearch, Splunk, HTTP endpoints, Datadog, New Relic
- Auto-scaling (no shards to manage)
- Buffer interval (60–900 seconds) or size (1–128 MB)
- Data transformation via Lambda

---

## Amazon Kinesis Data Analytics (MSK → Apache Flink)

| Item | Cost |
|---|---|
| Kinesis Processing Unit (KPU) per hr | $0.11 |
| 1 KPU = 1 vCPU + 4 GB RAM | — |
| Durable application storage (per GB/month) | $0.10 |
| Running applications overhead (per KPU-hr) | $0.11 |

---

## Amazon EventBridge — Event Bus

| Item | Free Tier | Paid Rate |
|---|---|---|
| AWS service events (default bus) | Free | Free |
| Custom events (per million) | — | $1.00 |
| Third-party SaaS events (per million) | — | $1.00 |
| Cross-account / cross-region events | Standard rates | — |
| EventBridge Pipes (per million events processed) | — | $0.40 |
| EventBridge Scheduler (per million invocations) | 14M/month free | $1.00 |
| Schema Registry (per policy/month) | 5M events free discovery | $0.10/million |
| Archive & replay (per GB stored/month) | — | $0.10 |

### Key Features
- 90+ native AWS service integrations as event sources
- 35+ AWS services as targets
- Content-based routing with pattern rules
- Schema discovery, registry, code binding generation
- Best For: decoupled event-driven architectures, SaaS integrations

---

*Prices are US East (N. Virginia) rates as of 2024.*
