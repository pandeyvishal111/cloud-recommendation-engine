# GCP — Serverless Factsheet

---

## Cloud Functions — Event-Driven Functions

### Gen 2 Pricing (recommended, built on Cloud Run)

#### Compute (Invocation Time)
| Memory | CPU | Cost/100ms | Best For |
|---|---|---|---|
| 128 MB | 0.083 vCPU | $0.000000231 | Lightweight webhooks |
| 256 MB | 0.167 vCPU | $0.000000463 | Small event processing |
| 512 MB | 0.333 vCPU | $0.000000925 | Standard functions |
| 1 GB | 0.583 vCPU | $0.00000162 | Medium processing |
| 2 GB | 1 vCPU | $0.00000324 | CPU-intensive |
| 4 GB | 2 vCPU | $0.00000648 | Heavy compute |
| 8 GB | 2 vCPU | $0.0000130 | ML inference |
| 16 GB | 4 vCPU | $0.0000259 | Largest functions |
| 32 GB | 8 vCPU | $0.0000518 | Maximum scale |

#### Invocations & Free Tier
| Item | Free Tier | Paid Rate |
|---|---|---|
| Invocations | 2 million/month | $0.40/million |
| Compute (GB-seconds) | 400,000 GB-sec/month | $0.0000100/GB-sec |
| CPU (GHz-seconds) | 200,000 GHz-sec/month | $0.0000100/GHz-sec |
| Egress | 5 GB/month | Standard network rates |
| Concurrent requests (per function instance) | 1–1,000 | Configurable |

### Gen 1 Pricing (legacy)
| Item | Free Tier | Paid Rate |
|---|---|---|
| Invocations | 2 million/month | $0.40/million |
| Compute GB-seconds | 400,000 GB-sec/month | $0.0000100/GB-sec |
| CPU GHz-seconds | 200,000 GHz-sec/month | $0.0000100/GHz-sec |

### Key Features
- Supported runtimes: Node.js, Python, Go, Java, Ruby, PHP, .NET, Kotlin
- HTTP triggers, Pub/Sub triggers, Cloud Storage triggers, Eventarc triggers
- Minimum instances (avoid cold starts, billed continuously)
- Max instances (burst cap)
- VPC Connector (private network access)
- Secrets Manager integration
- Cloud Build for CI/CD deployment

---

## Cloud Run — Managed Container Platform (Serverless)

### Request-Based Billing (Consumption)
| Resource | Free Tier | Paid Rate |
|---|---|---|
| vCPU (per vCPU-second, active only) | 180,000 vCPU-sec/month | $0.00002400 |
| Memory (per GB-second, active only) | 360,000 GB-sec/month | $0.00000250 |
| Requests (per million) | 2 million/month | $0.40 |
| Idle minimum instances (vCPU-sec, always-on) | — | $0.00000240/vCPU-sec |
| Idle minimum instances (GB-sec) | — | $0.00000025/GB-sec |
| Egress | 1 GB/month | Standard network rates |

### Cloud Run Jobs
| Resource | Cost |
|---|---|
| vCPU (per vCPU-second) | $0.00002400 |
| Memory (per GB-second) | $0.00000250 |
| No per-request cost | — |

### Committed Use Discounts (Cloud Run)
| Commitment | Discount |
|---|---|
| 1-year | ~17% off on-demand |
| 3-year | ~37% off on-demand |

### Key Features
- Any container (any language, any binary)
- HTTPS endpoint auto-assigned
- Custom domains (HTTPS auto-managed)
- Concurrency: up to 1,000 requests per container instance
- Min/max instances (scale to zero, or keep warm)
- CPU always-on (for background tasks beyond request lifecycle)
- Traffic splitting (gradual rollout, canary deployments)
- Cloud Run Volume Mounts (Cloud Storage, Secrets, in-memory)
- VPC Direct (no connector required for private VPC)
- Cloud Run for Anthos (deploy to GKE or on-prem)

---

## Cloud Run — Always-On (Non-Serverless Option)
For predictable workloads needing continuous availability:

| Configuration | Cost | Best For |
|---|---|---|
| Minimum instances = 1 (1 vCPU, 512MB) | ~$30/month | Zero cold starts, low-traffic APIs |
| Minimum instances = 1 (2 vCPU, 1GB) | ~$60/month | Production services |

---

## Eventarc — Unified Event Routing

| Item | Free Tier | Paid Rate |
|---|---|---|
| Event delivery (Cloud Audit Logs events) | 1 million/month | $0.40/million |
| Custom event delivery (Pub/Sub based) | Pub/Sub free tier | Pub/Sub rates |
| Workflows event delivery | — | Workflows rates |

### Key Features
- Source: 90+ Google services via Cloud Audit Logs
- Source: Custom events via Pub/Sub
- Targets: Cloud Run, Cloud Functions, GKE, Workflows
- CloudEvents standard (portable event format)
- Retry and dead-letter queue support

---

## Cloud Tasks — Managed Async Task Queues

| Item | Free Tier | Paid Rate |
|---|---|---|
| Task operations (per million) | 1 million/month | $0.40/million |

### Key Features
- HTTP targets (any endpoint, including Cloud Run, App Engine)
- App Engine targets (native App Engine queue)
- Scheduled future delivery (up to 30 days ahead)
- Rate limiting (dispatches per second, concurrent dispatches)
- Retry configuration (max attempts, backoff, deadline)
- Deduplication (task ID reuse within window)
- Best For: offloading slow API calls, retry-safe background processing, fan-out

---

## Cloud Scheduler — Managed Cron Jobs

| Item | Free Tier | Paid Rate |
|---|---|---|
| Jobs (first 3/month free) | 3 jobs/month | $0.10/job/month |

### Key Features
- Cron syntax scheduling (Unix cron)
- Targets: HTTP, Pub/Sub, Cloud Tasks, App Engine
- OAuth2 / OIDC authentication for HTTP targets
- Retry on failure (configurable)
- Time zone support
- Best For: ETL pipelines, report generation, cache warming, scheduled API calls

---

## API Gateway — Managed API Gateway for Serverless

| Item | Free Tier | Paid Rate |
|---|---|---|
| API calls (first 2 million/month) | Free | $3.00/million |

### Key Features
- Backends: Cloud Functions, Cloud Run, App Engine
- OpenAPI 2.0 spec (Swagger)
- Authentication: API keys, JWT, Google ID tokens
- Usage plans and quota management
- Cloud Logging and Cloud Monitoring integration
- Best For: exposing serverless backends as managed APIs

---

## Workflows — Serverless Orchestration

| Item | Free Tier | Paid Rate |
|---|---|---|
| Internal steps (first 5,000/month) | Free | $0.01/1,000 steps |
| External HTTP steps | — | $0.025/1,000 steps |

### Key Features
- YAML/JSON workflow definitions
- Connectors to 100+ Google and third-party APIs
- Built-in error handling and retries
- Parallel steps (concurrent branch execution)
- Subworkflows (reusable components)
- Integration with Eventarc (event-driven workflows)
- Long-running execution (up to 1 year)
- Best For: microservices orchestration, multi-step data pipelines, approval flows

---

## App Engine — Platform as a Service (PaaS)

### Standard Environment (auto-scaling, ms startup)
| Instance Class | Memory | CPU | Cost/hr |
|---|---|---|---|
| F1 (free) | 256 MB | 600 MHz | Free up to 28 hr/day |
| F2 | 512 MB | 1.2 GHz | $0.05 |
| F4 | 1 GB | 2.4 GHz | $0.10 |
| F4_1G | 2 GB | 2.4 GHz | $0.20 |
| B1 (backend) | 256 MB | 600 MHz | $0.05 |
| B2 | 512 MB | 1.2 GHz | $0.10 |
| B4 | 1 GB | 2.4 GHz | $0.20 |
| B8 | 2 GB | 4.8 GHz | $0.40 |

### Flexible Environment (custom runtimes, Docker)
Priced same as GCE VMs (N1 instance pricing) with 10% premium.

### Key Features (Standard)
- Scale to zero (no cost when idle)
- No Docker required (managed runtimes)
- Traffic splitting, A/B testing
- Cron jobs, task queues (built-in)
- Best For: web apps with variable traffic, rapid prototyping

---

*Prices are us-central1 / global rates as of 2024.*
