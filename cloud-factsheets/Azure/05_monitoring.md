# Azure — Monitoring & Observability Factsheet

---

## Azure Monitor — Core Observability Platform

### Metrics
| Item | Free Tier | Paid Rate |
|---|---|---|
| Platform metrics (Azure resource metrics) | Free | Free |
| Custom metrics (per million data points) | — | $0.31 |
| Custom metrics queries (per million) | — | $0.017 |
| Metrics API (per million calls) | — | $0.10 |
| Metrics alerts (per alert rule/month) | First 10 free | $0.10 |
| Multi-dimensional metrics alerts | First 10 free | $0.10 |
| Dynamic threshold alerts | — | $0.10/rule/month + $0.05/criteria/month |

### Log Analytics Workspace (Log Ingestion & Retention)
| Tier | Ingestion Cost ($/GB) | Retention |
|---|---|---|
| Pay-As-You-Go | $2.76/GB | 31 days free |
| Commitment Tier 100 GB/day | $2.00/GB (effective) | 31 days free |
| Commitment Tier 200 GB/day | $1.95/GB (effective) | 31 days free |
| Commitment Tier 300 GB/day | $1.84/GB (effective) | 31 days free |
| Commitment Tier 400 GB/day | $1.76/GB (effective) | 31 days free |
| Commitment Tier 500 GB/day | $1.68/GB (effective) | 31 days free |
| Commitment Tier 1,000 GB/day | $1.52/GB (effective) | 31 days free |
| Commitment Tier 2,000 GB/day | $1.37/GB (effective) | 31 days free |
| Commitment Tier 5,000 GB/day | $1.20/GB (effective) | 31 days free |

### Log Retention Beyond 31 Days
| Item | Cost |
|---|---|
| Interactive retention (31 days – 2 years, per GB/month) | $0.12 |
| Long-term archive (2–7 years, per GB/month) | $0.016 |

### Log Analytics Queries
| Item | Free Tier | Cost |
|---|---|---|
| Log Analytics queries | First 5 GB/month free | $2.76/GB |
| Basic Logs (low-touch, compliance, per GB) | — | $0.55/GB (ingestion) |
| Basic Logs queries (per GB scanned) | — | $0.0064 |
| Search Jobs (per GB scanned) | — | $0.0064 |
| Restore (per GB/day) | — | $0.13 |

---

## Application Insights — APM (Application Performance Monitoring)

Application Insights is a feature of Azure Monitor.

| Item | Free Tier | Paid Rate |
|---|---|---|
| Data ingestion | 5 GB/month per workspace free | $2.76/GB (via Log Analytics) |
| Data retention (beyond 90 days) | — | $0.12/GB/month |
| Availability tests (standard, per test/month) | 1 million pings free | $0.018/test/month |
| Availability tests (multi-step, per test/month) | — | $0.14/test/month |
| Smart Detection alerts | Free | Free |
| Profiler (per node/month) | — | Free for first 5 nodes, $2.88 per additional |
| Snapshot Debugger (per node/month) | — | Free |

### Key Features
- Distributed tracing (end-to-end request tracking)
- Live Metrics Stream
- Application Map (dependency visualization)
- Failure analysis, performance diagnosis
- User flows, funnels, retention analytics
- OpenTelemetry support

---

## Azure Monitor Alerts

| Alert Type | First 10 rules | Beyond 10 (per rule/month) |
|---|---|---|
| Metric alerts (static threshold) | Free | $0.10 |
| Metric alerts (dynamic thresholds) | Free | $0.10 + $0.05/criteria |
| Log search alerts | — | $1.50/rule/month |
| Activity Log alerts | Free | Free |
| Service Health alerts | Free | Free |

---

## Azure Advisor — Recommendations Engine

| Feature | Cost | Best For |
|---|---|---|
| Azure Advisor recommendations | Free | Cost, Security, Reliability, Operational Excellence, Performance |
| Advisor Score | Free | Overall posture scoring |
| Advisor workbooks (custom) | Free | Custom recommendation dashboards |

### Key Recommendation Categories
- **Cost**: Underutilized VMs, reserved instance opportunities, unused resources
- **Security**: MFA gaps, open ports, missing encryption
- **Reliability**: Single-instance VMs, no backup, replication gaps
- **Performance**: DB DTU utilization, slow queries, network bottlenecks
- **Operational Excellence**: Deprecated APIs, service health, quota limits

---

## Azure Service Health

| Feature | Cost | Best For |
|---|---|---|
| Azure Status (public status page) | Free | Global Azure outage visibility |
| Service Health (personalized) | Free | Events affecting your subscriptions |
| Resource Health | Free | Individual resource health |
| Health Alerts | Free | Alerts on service events, maintenance |

---

## Microsoft Defender for Cloud — Security Posture

### Free Tier
| Feature | Cost |
|---|---|
| Azure Security Benchmark assessment | Free |
| Secure Score | Free |
| Continuous assessment (Azure resources) | Free |
| Security recommendations | Free |

### Defender Plans (Enhanced Protection)
| Plan | Cost |
|---|---|
| Defender for Servers Plan 1 (per server/month) | $5 |
| Defender for Servers Plan 2 (per server/month) | $15 |
| Defender for SQL (Azure SQL, per server/month) | $15 |
| Defender for SQL (SQL Server on VMs, per server/month) | $15 |
| Defender for Storage (per storage account/month) | $10 |
| Defender for App Service (per App Service/month) | $15 |
| Defender for Key Vault (per 10K transactions/month) | $0.02 |
| Defender for Kubernetes (per core/month) | $2 |
| Defender for Container Registries (per image) | $0.29 |
| Defender for Resource Manager (per subscription/month) | $4 |
| Defender for DNS (per subscription/month) | $0.90 |
| Defender for Open-Source Relational DBs (per vCore/month) | $0.015 |
| Defender for Cosmos DB (per 100 RU/hr) | $0.007 |

---

## Azure Cost Management

| Feature | Cost | Best For |
|---|---|---|
| Azure Cost Management + Billing | Free | Analyze, monitor, optimize cloud spend |
| Cost alerts (budget alerts) | Free | Notify on spending thresholds |
| Azure Budgets | Free | Set cost/usage budgets with alerts |
| Cost allocation rules | Free | Distribute shared costs to subscriptions |
| Azure Reservations recommendations | Free | Identify savings with commitments |
| Cost export to Storage | Storage costs only | Automated cost data export |
| Power BI Cost Management connector | Free (Power BI costs apply) | Custom cost dashboards |

---

## Azure Monitor Workbooks

| Feature | Cost |
|---|---|
| Workbooks | Free |
| Workbook queries (via Log Analytics) | Log Analytics rates apply |

### Key Built-in Workbooks
- Performance, Failures, Usage (Application Insights)
- Dependency Analysis
- Change Analysis (infrastructure drift)
- VM Insights (VM performance maps)
- Container Insights (AKS monitoring)

---

*Prices are East US pay-as-you-go rates as of 2024. Log Analytics pricing is the dominant cost driver for Azure monitoring.*
