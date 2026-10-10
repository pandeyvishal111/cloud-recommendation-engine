# AWS — Monitoring & Observability Factsheet

---

## Amazon CloudWatch

### Metrics
| Tier | Cost | Included |
|---|---|---|
| Basic Monitoring (EC2/EBS default metrics) | Free | 5-minute granularity |
| Detailed Monitoring (1-minute granularity) | $0.30/metric/month | EC2, EBS, others |
| Custom Metrics | $0.30/metric/month | First 10,000 metrics |
| High-Resolution Custom Metrics (10s/30s/1s) | $0.30/metric/month | Standard price applies |
| Metric Math / Metric Streams | Included / $0.003/1,000 metric updates | — |

### CloudWatch Logs
| Item | Cost |
|---|---|
| Log data ingestion (per GB) | $0.50 |
| Log data archival/storage (per GB/month) | $0.03 |
| Log data transfer to S3 (export) | $0.13/GB |
| Logs Insights (per GB queried) | $0.005 |
| Live tail (per hour) | $0.01 |
| Cross-account log subscription | Standard delivery charges |

### CloudWatch Alarms
| Item | Cost |
|---|---|
| Standard alarm (per alarm/month) | $0.10 |
| High-resolution alarm (10s resolution) | $0.30/alarm/month |
| Composite alarms | $0.50/alarm/month |
| Metric Insights alarms | $0.30/alarm/month |

### CloudWatch Dashboards
| Item | Cost |
|---|---|
| First 3 dashboards (up to 50 metrics each) | Free |
| Additional dashboards (per dashboard/month) | $3.00 |

### CloudWatch Synthetics (Canaries)
| Item | Cost |
|---|---|
| Canary runs (per run) | $0.0012 |
| Best For | Endpoint monitoring, UI testing, broken link detection |

### CloudWatch RUM (Real User Monitoring)
| Item | Cost |
|---|---|
| Per 100,000 RUM events | $1.00 |
| Best For | Frontend performance, user experience monitoring |

### CloudWatch Evidently (Feature Flags & A/B Testing)
| Item | Cost |
|---|---|
| Events analyzed (per 100,000) | $0.0075 |
| Feature evaluation (per 1 million evaluations) | $1.00 |

---

## AWS X-Ray — Distributed Tracing

| Item | Free Tier | Paid Rate |
|---|---|---|
| Traces recorded (per million) | 100,000/month free | $5.00 |
| Traces retrieved (per million) | 1,000,000/month free | $0.50 |
| Traces scanned (per million) | 1,000,000/month free | $0.50 |

### Key Features
- Service maps for visualizing microservice dependencies
- Root cause analysis for latency/errors
- Integration with Lambda, ECS, EKS, API Gateway, SNS, SQS
- X-Ray Insights: ML-based anomaly detection

---

## AWS CloudTrail — API Audit Logging

| Item | Free Tier | Paid Rate |
|---|---|---|
| Management events (one trail per region) | Free | — |
| Additional management event copies (per 100,000 events) | — | $2.00 |
| Data events — S3 (per 100,000 events) | — | $0.10 |
| Data events — Lambda (per 100,000 invocations) | — | $0.10 |
| CloudTrail Lake (event data store ingestion, per GB) | — | $2.75 |
| CloudTrail Lake (query per TB scanned) | — | $0.005 |
| CloudTrail Insights (per 100,000 events analyzed) | — | $0.35 |

### Key Features
- 90-day event history (free) in console
- Delivers logs to S3, CloudWatch Logs, or CloudTrail Lake
- Integrity validation (log file hashing)
- Organization-wide trail for multi-account auditing

---

## AWS Config — Resource Configuration Compliance

| Item | Free Tier | Paid Rate |
|---|---|---|
| Configuration items recorded (per item) | — | $0.003 |
| Config rules evaluations (per rule evaluation) | — | $0.001 |
| Conformance pack evaluations (per eval) | — | $0.001 |
| Query (per GB queried via advanced queries) | — | $0.0025 |

### Key Features
- Continuous resource inventory and change tracking
- Pre-built rule library (150+ managed rules)
- Custom rules via Lambda
- Automatic remediation via Systems Manager
- Conformance packs (CIS, PCI-DSS, HIPAA baselines)

---

## AWS Health — Service & Account Events

| Feature | Cost | Best For |
|---|---|---|
| AWS Health Dashboard (Service Health) | Free | Public AWS service status |
| AWS Personal Health Dashboard | Free | Events affecting your specific account |
| AWS Health API (Business/Enterprise Support only) | Requires Support plan | Programmatic event monitoring |

---

## AWS Cost Explorer & Cost Management

| Feature | Cost | Best For |
|---|---|---|
| Cost Explorer | Free | Visualize and analyze spend trends |
| Cost Explorer API (per request) | $0.01 | Programmatic cost data retrieval |
| AWS Budgets (first 2 budgets) | Free | Spend alerts |
| AWS Budgets (additional, per budget/month) | $0.02 | Cost and usage budgets |
| Budget Actions | $0.10/action/month | Auto-stop resources on budget breach |
| AWS Cost & Usage Report | Free (S3 storage charged) | Granular billing data |
| Savings Plans recommendations | Free | Right-sizing suggestions |

---

## AWS Trusted Advisor

| Feature | Support Plan Required | Cost |
|---|---|---|
| Core checks (7 checks) | Free (Basic/Developer) | Free |
| Full checks (500+ checks) | Business or Enterprise Support | Included in support plan |
| Trusted Advisor Priority | Enterprise Support | Included |

### Key Check Categories
- Cost Optimization, Performance, Security, Fault Tolerance, Service Limits, Operational Excellence

---

## AWS Compute Optimizer

| Feature | Cost | Best For |
|---|---|---|
| Compute Optimizer (basic) | Free | EC2, Auto Scaling, Lambda, EBS, ECS on Fargate |
| Enhanced Infrastructure Metrics (per resource/month) | $0.0003360 | 3-month lookback instead of 14 days |
| Commercial Software (per resource/month) | $0.0015 | SQL Server on EC2 recommendations |

### Key Features
- ML-driven rightsizing recommendations
- Reduces over-provisioning (cost) and under-provisioning (performance)
- Identifies idle resources
- Integrates with Cost Explorer

---

*Prices are US East (N. Virginia) rates as of 2024.*
