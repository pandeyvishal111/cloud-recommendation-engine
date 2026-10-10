# Azure — Serverless Factsheet

---

## Azure Functions — Serverless Compute

### Consumption Plan (Pay-per-execution)
| Item | Free Tier | Paid Rate |
|---|---|---|
| Executions (per million) | 1M/month free | $0.20 |
| Execution time (per GB-second) | 400,000 GB-s/month free | $0.000016 |
| Best For | Infrequent execution, cost-sensitive, event-driven |

### Premium Plan (always-warm, VNet integration)
| SKU | vCPU | RAM (GB) | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| EP1 | 1 | 3.5 | $0.173 | ~$125 | VNet, always-on, small |
| EP2 | 2 | 7 | $0.346 | ~$249 | Medium throughput |
| EP3 | 4 | 14 | $0.691 | ~$498 | High throughput, large memory |

Premium plan scales out automatically; minimum 1 always-warm instance required.

### App Service (Dedicated) Plan
Functions run on same App Service plans as web apps:

| Tier | vCPU | RAM | Cost/month |
|---|---|---|---|
| B1 (Basic) | 1 | 1.75 GB | ~$13 |
| B2 | 2 | 3.5 GB | ~$26 |
| B3 | 4 | 7 GB | ~$51 |
| S1 (Standard) | 1 | 1.75 GB | ~$69 |
| S2 | 2 | 3.5 GB | ~$139 |
| P1v3 (Premium v3) | 2 | 8 GB | ~$116 |
| P2v3 | 4 | 16 GB | ~$232 |
| P3v3 | 8 | 32 GB | ~$464 |

### Key Features
- Triggers: HTTP, Timer, Blob, Queue, Service Bus, Event Hub, Event Grid, Cosmos DB, IoT Hub
- Durable Functions (stateful orchestration — free beyond underlying compute)
- Max execution timeout: 10 min (Consumption), unlimited (Premium/Dedicated)
- VNet integration (Premium/Dedicated only)
- Cold start: Consumption plan (~1–5 sec); Premium plan: none

---

## Azure Logic Apps — Workflow Automation

### Consumption Plan
| Item | Free Tier | Paid Rate |
|---|---|---|
| Actions executed (per 10,000) | 4,000/month free | $0.25 |
| Trigger executions (per 10,000) | — | $0.25 |
| Standard connector actions (per 10,000) | — | $0.25 |
| Enterprise connector actions (per 10,000) | — | $1.00 |
| Data retention (per GB/month) | — | $0.12 |

### Standard Plan (single-tenant, VNet integration)
| SKU | vCPU | RAM | Cost/hr | Est. $/month |
|---|---|---|---|---|
| WS1 | 1 | 3.5 GB | $0.198 | ~$143 |
| WS2 | 2 | 7 GB | $0.396 | ~$285 |
| WS3 | 4 | 14 GB | $0.792 | ~$570 |

### Key Features
- 400+ built-in connectors (Salesforce, SAP, Office 365, Dynamics, etc.)
- Visual designer (no-code / low-code)
- Error handling, retry policies, parallel branches
- B2B capabilities (EDI, AS2, X12)
- Integration with Service Bus, Event Grid, Functions

---

## Azure Event Grid — Managed Event Routing

| Item | Free Tier | Paid Rate |
|---|---|---|
| Operations (first 100,000/month) | Free | $0.60/million |
| Events > 64 KB (billed per 64 KB chunk) | — | Multiple units |
| System topics (Azure service events) | Free | Free |
| Custom topics (per million operations) | — | $0.60 |
| Domain topics (per million operations) | — | $0.60 |
| Event Grid Namespaces — MQTT (per million) | — | $0.90 |
| Advanced filtering (per million evaluations) | — | $0.60 |

### Key Features
- Publish-subscribe model at cloud scale
- Retry with exponential backoff (24-hour delivery guarantee)
- Dead-letter queues
- Filtering at subscription level
- CloudEvents 1.0 schema support
- Sources: Azure services (Blob, Resource Manager, Service Bus, AKS), custom apps, partner events

---

## Azure Service Bus — Enterprise Messaging

| Tier | Features | Operations (per million) | Best For |
|---|---|---|---|
| Basic | Queues only, no topics | $0.05 | Simple queue scenarios |
| Standard | Queues + Topics, variable throughput | $0.10 | General messaging |
| Premium | Dedicated capacity, geo-DR, VNet | Fixed per messaging unit | Enterprise, predictable performance |

### Premium Tier Messaging Units
| Messaging Units | Est. $/month |
|---|---|
| 1 MU (1 GB RAM) | ~$677 |
| 2 MU (2 GB RAM) | ~$1,354 |
| 4 MU (4 GB RAM) | ~$2,707 |
| 8 MU (8 GB RAM) | ~$5,414 |

### Service Bus Specifications
| Feature | Basic | Standard | Premium |
|---|---|---|---|
| Max message size | 256 KB | 256 KB | 100 MB |
| Queues | Yes | Yes | Yes |
| Topics/Subscriptions | No | Yes | Yes |
| Message lock | 5 min | 5 min | 5 min |
| Max message TTL | 14 days | 14 days | 14 days |
| Geo-disaster recovery | No | No | Yes |
| VNet integration | No | No | Yes |
| Sessions (FIFO) | No | Yes | Yes |
| Dead-letter queues | Yes | Yes | Yes |
| Duplicate detection | No | Yes | Yes |
| SLA | 99.9% | 99.9% | 99.9% |

---

## Azure API Management — API Gateway

| Tier | Features | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|
| Consumption | Serverless, pay-per-call | $0.000035/call (first 1M free) | Variable | Serverless APIs, dev/test |
| Developer | Full features, no SLA | $0.07 | ~$50 | Non-prod testing |
| Basic | Basic features, 99.95% SLA | $0.19 | ~$137 | Small production |
| Standard | Mid-scale, 99.95% SLA, external cache | $0.95 | ~$684 | Medium production |
| Premium | Multi-region, VNet, 99.99% SLA | $3.82 | ~$2,750 | Enterprise production |

### Consumption Tier Details
| Item | Free | Paid |
|---|---|---|
| API calls | 1M/month | $0.035/10,000 calls |
| Self-hosted gateway | Not available | — |
| Built-in cache | Yes | Yes |

### Key Features
- Developer portal (API documentation, testing)
- Rate limiting, quotas, IP filtering
- OAuth 2.0, JWT, subscription keys
- Caching, request/response transformation
- Backend circuit breaker
- Azure Monitor + Application Insights integration

---

## Azure Container Apps — Serverless Containers

### Consumption Plan
| Resource | Free Tier | Paid Rate |
|---|---|---|
| vCPU-seconds | 180,000/month | $0.000024/vCPU-s |
| Memory GB-seconds | 360,000/month | $0.0000030/GB-s |
| Requests | 2M/month | $0.40/million |

### Dedicated Plan (always-on)
| Profile | vCPU | RAM | Cost/hr |
|---|---|---|---|
| Dedicated D4 | 4 | 16 GB | $0.26 |
| Dedicated D8 | 8 | 32 GB | $0.52 |
| Dedicated D16 | 16 | 64 GB | $1.04 |
| Dedicated D32 | 32 | 128 GB | $2.08 |

### Key Features
- Scale to zero automatically (Consumption)
- KEDA (Kubernetes-based Event Driven Autoscaling)
- Dapr integration (distributed application runtime)
- VNet integration, private endpoints
- Built-in ingress (HTTPS, HTTP/2, gRPC)
- Sidecar container support
- Blue/green and canary deployments
- No Kubernetes cluster to manage

---

*Prices are East US pay-as-you-go rates as of 2024.*
