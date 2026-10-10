# Azure — Messaging & Streaming Factsheet

---

## Azure Service Bus — Enterprise Messaging

### Tiers
| Tier | Operations/month | Max Message Size | Topics | Geo-DR | VNet | Cost |
|---|---|---|---|---|---|---|
| Basic | Per million | 256 KB | No | No | No | $0.05/million ops |
| Standard | Per million | 256 KB | Yes | No | No | $0.10/million ops |
| Premium | Fixed capacity | 100 MB | Yes | Yes | Yes | Per Messaging Unit |

### Premium Tier — Messaging Units (MUs)
| Messaging Units | RAM | Est. $/month |
|---|---|---|
| 1 MU | 1 GB | ~$677 |
| 2 MU | 2 GB | ~$1,354 |
| 4 MU | 4 GB | ~$2,707 |
| 8 MU | 8 GB | ~$5,414 |
| 16 MU | 16 GB | ~$10,829 |

### Service Bus Standard — Operation Pricing
| Operations | Cost |
|---|---|
| First 13 million/month | Free |
| Per million operations beyond free | $0.10 |
| Brokered connections (per 100/month) | $0.10 |
| Relay hours (per 100/month) | $0.10 |

### Key Features
- Dead-letter queues
- Scheduled message delivery
- Message sessions (FIFO processing)
- Duplicate detection (5-min to 7-day window)
- Auto-forwarding between queues/topics
- Transactions (atomic operations across queues)
- Message deferral
- Geo-disaster recovery (Premium)
- Private endpoints (Premium)

---

## Azure Event Hubs — Real-Time Event Streaming

### Tiers
| Tier | Throughput | Max Partitions | Retention | Max Message Size | Best For |
|---|---|---|---|---|---|
| Basic | 1 TU = 1 MB/s in, 2 MB/s out | 32 | 1 day | 256 KB | Simple ingestion |
| Standard | 1 TU = 1 MB/s in, 2 MB/s out | 32 | 7 days | 256 KB | General streaming |
| Premium | 1 PU = 1 MB/s | 100 | 90 days | 1 MB | High-throughput, enterprise |
| Dedicated | Reserved capacity | 1,024 | 90 days | 1 MB | Predictable, largest scale |

### Standard Tier Pricing
| Item | Cost |
|---|---|
| Throughput Unit (TU), per hr | $0.028 |
| Est. $/month per TU (730 hr) | ~$20 |
| Ingress events (per million) | $0.028 |
| Extended retention (per GB/day beyond 1 day) | $0.01 |
| Event Hubs Capture (to Blob Storage, per hr) | $0.028/hr/namespace |
| Schema Registry (per schema group/month) | $0.01 |

### Premium Tier Pricing
| Item | Cost |
|---|---|
| Processing Unit (PU), per hr | $0.115 |
| Est. $/month per PU | ~$84 |
| Extended retention (per TB/month) | $0.015 |
| Capture | Included |
| Schema Registry | Included |

### Dedicated Tier Pricing
| Capacity Units (CU) | Reserved Capacity | Est. $/month |
|---|---|---|
| 1 CU | 1 GB/s ingress, 2 GB/s egress | ~$18,000 |

### Key Features
- Apache Kafka compatible (no code change for Kafka clients)
- Event Hubs Capture (automatic archival to Azure Blob Storage or ADLS Gen2)
- Schema Registry (Avro, JSON Schema)
- Partitioned consumer model (scale readers independently)
- Private endpoints, VNet integration (Standard+)
- Geo-disaster recovery (Standard+)

---

## Azure Event Grid — Managed Event Routing

### Pricing
| Item | Free Tier | Paid Rate |
|---|---|---|
| Operations (first 100,000/month) | Free | $0.60/million |
| Events > 64 KB (per 64 KB chunk, rounded up) | — | Billed as multiple operations |
| System topics (Azure service events) | Free | Free |
| Custom topics (per million operations) | — | $0.60 |
| Domain topics (per million operations) | — | $0.60 |
| Partner topics (per million operations) | — | $0.60 |
| Event Grid Namespaces — MQTT broker (per million) | — | $0.90 |
| Event Grid Namespaces — pull delivery (per million) | — | $0.40 |

### Key Features
- Push model (events pushed to subscribers)
- Pull model (via Event Grid Namespaces)
- MQTT broker (IoT scenarios)
- Retry with exponential backoff and dead-lettering
- Event subscriptions with filter rules
- Sources: Azure Blob, Resource Manager, Service Bus, Event Hubs, IoT Hub, partner apps
- Targets: Azure Functions, Logic Apps, Event Hubs, Service Bus, Webhooks, Storage Queues

---

## Azure Notification Hubs — Mobile Push Notifications

| Tier | Push Notifications | Active Devices | Cost |
|---|---|---|---|
| Free | 1M/month | 500 | Free |
| Basic | 10M/month | 200K | $10/month |
| Standard | Unlimited | Unlimited | $200/month |

### Supported Push Platforms
Apple APNs, Google FCM, Windows WNS, Amazon ADM, Baidu Cloud Push.

---

## Azure IoT Hub — IoT Device Management

### Tiers
| Tier | Messages/day (per unit) | Device Limit | Cloud-to-Device | Cost/unit/month |
|---|---|---|---|---|
| Free (F1) | 8,000 | 500 | No | Free |
| Basic B1 | 400,000 | Unlimited | No | $25 |
| Basic B2 | 6,000,000 | Unlimited | No | $250 |
| Basic B3 | 300,000,000 | Unlimited | No | $2,500 |
| Standard S1 | 400,000 | Unlimited | Yes | $25 |
| Standard S2 | 6,000,000 | Unlimited | Yes | $250 |
| Standard S3 | 300,000,000 | Unlimited | Yes | $2,500 |

### IoT Hub Additional Costs
| Item | Cost |
|---|---|
| Messages beyond daily quota (per million) | $0.70 |
| IoT Hub Device Update (per managed device/month) | $1.50 |
| Message enrichments | Free |
| Routing to Event Hubs | Event Hubs rates |
| File uploads (per file) | $0.06 |
| Azure IoT Edge (per device/month) | $5.00 |

### IoT Hub Device Provisioning Service (DPS)
| Item | Cost |
|---|---|
| Registration operations (per million) | $1.00 |
| Best For | Auto-provisioning IoT devices at scale |

### Key Features (Standard tier)
- Device twins (device shadow state)
- Direct methods (invoke device commands)
- Cloud-to-device messages
- Device streams
- IoT Hub message routing (multiple endpoints)
- Built-in Event Hub endpoint
- Per-device authentication (X.509, SAS tokens, TPM)

---

## Azure Web PubSub — Real-Time WebSocket Service

| Item | Free | Standard |
|---|---|---|
| Max connections | 20 concurrent | 1,000 per unit |
| Messages (per million) | 20,000/month free | $1.00 |
| Units | 1 (free) | $49/unit/month |

---

## Azure SignalR Service — Real-Time Communications

| Tier | Connections | Messages/unit/day | Cost/month |
|---|---|---|---|
| Free | 20 | 20,000 | Free |
| Standard 1 unit | 1,000 | 1,000,000 | $49 |
| Standard 2 units | 2,000 | 2,000,000 | $98 |
| Standard 5 units | 5,000 | 5,000,000 | $245 |

---

*Prices are East US pay-as-you-go rates as of 2024.*
