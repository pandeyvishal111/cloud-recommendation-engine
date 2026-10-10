# AWS — Serverless Factsheet

---

## AWS Lambda — Serverless Functions

### Request Pricing
| Tier | Cost |
|---|---|
| Requests (first 1M/month) | Free |
| Requests beyond free tier | $0.20/million requests |

### Duration Pricing (x86 architecture)
| Memory | Cost per GB-second | Notes |
|---|---|---|
| 128 MB – 10,240 MB | $0.0000166667/GB-s | 400,000 GB-s free/month |

### Duration Pricing (Arm / Graviton2 — 20% cheaper)
| Memory | Cost per GB-second |
|---|---|
| 128 MB – 10,240 MB | $0.0000133334/GB-s |

### Provisioned Concurrency
| Item | Cost |
|---|---|
| Provisioned concurrency (per GB-hour) | $0.000004646 |
| Provisioned concurrency requests (per GB-second) | $0.0000097192 |
| Best For | Latency-sensitive apps needing cold-start elimination |

### Lambda Memory → Duration Reference
| Memory | Max Duration | Typical Use |
|---|---|---|
| 128 MB | 15 min | Lightweight functions |
| 512 MB | 15 min | General processing |
| 1,769 MB | 15 min | 1 vCPU equivalent |
| 3,008 MB | 15 min | CPU-intensive tasks |
| 10,240 MB | 15 min | Memory-heavy processing |

### Key Features
- Up to 10 GB memory, 15-minute timeout, 10 GB /tmp storage
- Concurrent execution limit: 1,000 (default, can request increase)
- Container image support (up to 10 GB)
- Lambda URLs (built-in HTTPS endpoint — free)
- Event source mapping: Kinesis, DynamoDB Streams, SQS, Kafka

---

## Amazon API Gateway

### REST API
| Tier | Cost per million API calls |
|---|---|
| First 333 million/month | $3.50 |
| Next 667 million/month | $2.80 |
| Next 19 billion/month | $2.38 |
| Over 20 billion/month | $1.51 |
| Cache memory (per hr, 0.5 GB) | $0.020 |
| Cache memory (per hr, 1.6 GB) | $0.038 |
| Cache memory (per hr, 6.1 GB) | $0.200 |
| Cache memory (per hr, 13.5 GB) | $0.295 |

### HTTP API (Cheaper, fewer features)
| Tier | Cost per million API calls |
|---|---|
| First 300 million/month | $1.00 |
| Over 300 million/month | $0.90 |

### WebSocket API
| Item | Cost |
|---|---|
| Messages (per million) | $1.00 |
| Connection minutes (per million) | $0.25 |

### Key Features
- Throttling, request validation, usage plans, API keys
- Stages and deployment canary releases
- Private APIs via VPC endpoints
- Integration with Lambda, HTTP backends, AWS services

---

## AWS Step Functions — Workflow Orchestration

| Workflow Type | Cost | Best For |
|---|---|---|
| Standard Workflows | $0.025/1,000 state transitions | Long-running, auditable, exactly-once |
| Express Workflows (per million) | $1.00/million workflow executions + $0.00001/GB-second duration | High-volume, short-duration (<5 min) |
| Free tier | 4,000 state transitions/month | — |

### Key Features
- Visual workflow designer
- Error handling, retries, catch blocks built-in
- Supports 200+ AWS service integrations
- Wait for callback / heartbeat / events
- Up to 1 year execution duration (Standard)
- Audit logs via CloudWatch

---

## Amazon EventBridge — Serverless Event Bus

| Item | Free Tier | Paid Rate |
|---|---|---|
| Custom events published (per million) | — | $1.00 |
| Third-party events (per million) | — | $1.00 |
| AWS service events | Free | Free |
| Schema Registry (per policy/month) | Free (first 5 million events) | $0.10/million |
| EventBridge Pipes (per million events) | — | $0.40 |
| Scheduler invocations (per million) | 14 million free | $1.00 |
| Cross-account event delivery | Standard rates | — |

---

## Amazon SQS — Managed Message Queues

| Queue Type | Cost per million requests | Best For |
|---|---|---|
| Standard Queue (first 1M/month) | Free | At-least-once delivery, high throughput |
| Standard Queue (beyond free tier) | $0.40 | High-volume asynchronous processing |
| FIFO Queue (first 1M/month) | Free | Exactly-once, ordered processing |
| FIFO Queue (beyond free tier) | $0.50 | Financial, inventory, sequenced workflows |

### SQS Specifications
| Spec | Standard | FIFO |
|---|---|---|
| Max message size | 256 KB | 256 KB |
| Max retention | 14 days | 14 days |
| Throughput | Unlimited | 3,000 msg/sec (batching) |
| Long polling | Yes | Yes |
| Extended client (S3 payload) | Up to 2 GB | Up to 2 GB |

---

## Amazon SNS — Managed Pub/Sub

| Endpoint Type | First 1M deliveries | Cost per million after |
|---|---|---|
| HTTP/S | Free | $0.60 |
| Email/Email-JSON | Free | $2.00 |
| SQS | Free | $0.50 |
| Lambda | Free | $0.50 |
| SMS (US, per message) | — | $0.00645 |
| Mobile push (per million) | 1M free | $0.50 |
| Kinesis Data Firehose (per GB) | — | $0.19 |

### Key Features
- Fan-out pattern: 1 publisher → many subscribers
- Message filtering at subscription level
- FIFO topics for ordered delivery
- Message archiving, replay

---

## AWS Fargate — Serverless Containers

| Resource | Per vCPU-Hour | Per GB-Hour |
|---|---|---|
| Linux (x86_64) | $0.04048 | $0.004445 |
| Linux (ARM64 / Graviton) | $0.03238 | $0.00356 |
| Windows (Server 2019) | $0.09148 | $0.01005 |

### Fargate Example Costs
| Task Config | Est. $/month (730 hr) |
|---|---|
| 0.25 vCPU, 0.5 GB (smallest) | ~$9.60 |
| 0.5 vCPU, 1 GB | ~$19.20 |
| 1 vCPU, 2 GB | ~$38.00 |
| 2 vCPU, 4 GB | ~$76.00 |
| 4 vCPU, 8 GB | ~$151.00 |
| 8 vCPU, 16 GB | ~$302.00 |
| 16 vCPU, 120 GB | ~$724.00 |

### Key Features
- No cluster/node management
- Per-second billing (60-second minimum)
- Works with ECS and EKS
- Fargate Spot for cost savings (up to 70%)
- Network modes: awsvpc only

---

*Prices are US East (N. Virginia) rates as of 2024.*
