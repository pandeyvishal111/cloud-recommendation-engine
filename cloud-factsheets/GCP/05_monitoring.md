# GCP — Monitoring & Observability Factsheet

---

## Cloud Monitoring — Metrics & Alerting

### Metrics Pricing
| Item | Free Tier | Paid Rate |
|---|---|---|
| Google Cloud metrics (all built-in) | Free | Free |
| Custom metrics (per metric/month, first 250) | First 250 free | $0.10/metric |
| Custom metrics (next 750) | — | $0.10/metric |
| Custom metrics (beyond 1,000) | — | $0.05/metric |
| Prometheus metrics (per million samples/month, first 50M) | First 50M free | $0.15/million |
| External metrics (AWS CloudWatch, Datadog, etc.) | — | $0.15/million samples |

### Alerting & Dashboards
| Item | Cost |
|---|---|
| Alerting policies | Free |
| Uptime checks (first 3 million results/month) | Free |
| Uptime checks (per million beyond 3M) | $0.30 |
| Dashboards | Free |
| Monitoring groups | Free |

### Key Features
- 1,000+ pre-built Google Cloud metrics
- Integration with Prometheus (managed collection)
- Multi-cloud metrics (AWS, Azure via agents)
- SLO (Service Level Objectives) monitoring
- Error budget tracking
- Custom dashboards (chart builder, JSON editing)
- Synthetic monitors (uptime checks: HTTP, TCP, HTTPS)
- Notification channels: email, SMS, PagerDuty, OpsGenie, Slack, webhooks
- Alerting: condition-based, MQL-based, log-based

---

## Cloud Logging — Log Management

### Log Ingestion
| Tier | Free Tier | Paid Rate |
|---|---|---|
| Default log bucket (_Default) | First 50 GB/month free | $0.01/GB after |
| User-defined log buckets | First 50 GB/month free | $0.01/GB after |
| Storage beyond retention period | — | $0.01/GB/month |
| Log Analytics (BigQuery-linked buckets) | — | BigQuery storage rates |

### Log Retention
| Bucket | Default Retention | Extended Retention |
|---|---|---|
| _Required (Admin Activity, System Events) | 400 days | Not configurable |
| _Default (all other logs) | 30 days | Up to 3,650 days ($0.01/GB/month) |
| User-defined buckets | 30 days (configurable) | $0.01/GB/month for extended |

### Log Routing & Exports
| Item | Cost |
|---|---|
| Log sinks to Cloud Storage | Free (storage costs apply) |
| Log sinks to BigQuery | Free (BQ ingestion costs apply) |
| Log sinks to Pub/Sub | Free (Pub/Sub costs apply) |
| Log sinks to Splunk (via Pub/Sub) | Pub/Sub rates |

### Key Features
- Structured logging (JSON payloads)
- Log-based metrics (convert log entries to metrics)
- Log-based alerts (alert when log pattern matched)
- Log Explorer (query, filter, live tail)
- Log Analytics (SQL queries over logs using BigQuery)
- Log views (IAM-controlled access to log subsets)
- Data Access audit logs (track who accesses what)

---

## Cloud Trace — Distributed Tracing

| Item | Free Tier | Paid Rate |
|---|---|---|
| Trace spans ingested (first 2.5M/month) | Free | $0.20/million |
| Trace spans retrieved (first 25M/month) | Free | $0.02/million |
| Trace data retention | 30 days | — |

### Key Features
- Automatic trace collection (App Engine, Cloud Run, Cloud Functions)
- OpenTelemetry and OpenCensus compatible
- Latency analysis and breakdown
- Integration with Cloud Logging (jump from trace to logs)
- Trace waterfall diagrams
- 99th percentile latency analysis

---

## Cloud Profiler — Continuous CPU/Memory Profiling

| Item | Cost |
|---|---|
| Profiling (all supported languages) | Free |
| Profile data retention | 30 days |

### Supported Languages
Go, Java, Node.js, Python, Ruby

---

## Error Reporting

| Item | Cost |
|---|---|
| Error events (all volumes) | Free |
| Error data retention | 30 days |

### Key Features
- Automatic grouping of similar errors
- First-occurrence tracking
- Stack trace analysis
- Integration with Cloud Logging and Cloud Monitoring
- Supported: App Engine, Cloud Functions, Cloud Run, GCE (via Logging agent)

---

## Active Assist — Intelligent Recommendations

| Service | Cost |
|---|---|
| VM rightsizing recommendations | Free |
| Committed Use Discount (CUD) recommendations | Free |
| IAM recommendations (unused permissions) | Free |
| Firewall recommendations | Free |
| Idle resource identification | Free |
| GKE rightsizing recommendations | Free |

---

## Google Cloud Cost Management

| Feature | Cost |
|---|---|
| Cloud Billing reports | Free |
| Budgets and alerts | Free |
| Cost breakdowns (project, service, label) | Free |
| BigQuery export (detailed billing data) | BigQuery storage/query rates |
| Cost recommendations (Recommender API) | Free (first N calls/project/month) |
| Committed Use Discount analysis | Free |
| Saved views and custom reports | Free |

### Key Features
- Real-time spend tracking
- Budget alerts (% of budget or actual amount)
- Label-based cost attribution
- Committed Use Discount purchase and tracking
- Flat-rate slot purchase analysis (BigQuery)
- Billing export to BigQuery for custom analytics
- Cost allocation tags (labels)

---

## Cloud Debugger (Deprecated — replaced by snapshot debugger)

Use **Cloud Trace** and **Cloud Profiler** for new workloads.

---

## Ops Agent — Unified Monitoring & Logging Agent

| Item | Cost |
|---|---|
| Agent installation and management | Free |
| System metrics collection | Free (first 250 custom metrics) |
| Log forwarding | Logging costs apply |

### Supported Platforms
- GCE VMs (Linux: all major distros; Windows Server)
- GKE nodes
- On-premises servers (via hybrid connectivity)

---

*Prices are us-central1 / global rates as of 2024.*
