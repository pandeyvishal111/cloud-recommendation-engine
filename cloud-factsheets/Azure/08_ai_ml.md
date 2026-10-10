# Azure — AI & Machine Learning Factsheet

---

## Azure Machine Learning — ML Platform

### Compute Clusters (Training)
| VM Size | vCPU | RAM | GPU | Cost/hr | Best For |
|---|---|---|---|---|---|
| Standard_DS3_v2 | 4 | 14 GB | — | $0.27 | CPU training, small |
| Standard_DS4_v2 | 8 | 28 GB | — | $0.54 | CPU training, medium |
| Standard_DS5_v2 | 16 | 56 GB | — | $1.09 | CPU training, large |
| Standard_NC6s_v3 | 6 | 112 GB | 1x V100 | $3.06 | GPU training |
| Standard_NC12s_v3 | 12 | 224 GB | 2x V100 | $6.12 | Large GPU training |
| Standard_NC24s_v3 | 24 | 448 GB | 4x V100 | $12.24 | Distributed training |
| Standard_ND40rs_v2 | 40 | 672 GB | 8x V100 | $22.03 | Large model training |
| Standard_NC4as_T4_v3 | 4 | 28 GB | 1x T4 | $0.53 | Cost-efficient inference |
| Standard_ND96amsr_A100_v4 | 96 | 900 GB | 8x A100 | $32.77 | Largest model training |

### Compute Instances (Notebooks / Development)
| Size | vCPU | RAM | GPU | Cost/hr |
|---|---|---|---|---|
| Standard_DS11_v2 | 2 | 14 GB | — | $0.15 |
| Standard_DS12_v2 | 4 | 28 GB | — | $0.31 |
| Standard_DS3_v2 | 4 | 14 GB | — | $0.27 |
| Standard_DS5_v2 | 16 | 56 GB | — | $1.09 |
| Standard_NC6 | 6 | 56 GB | 1x K80 | $0.90 |
| Standard_NC6s_v3 | 6 | 112 GB | 1x V100 | $3.06 |

### Azure ML Service Costs
| Feature | Cost | Best For |
|---|---|---|
| Azure ML Studio workspace | Free | Managed ML IDE |
| Automated ML (per experiment run-hr) | Compute rate only | No-code model training |
| Pipelines (per step) | Compute rate only | ML workflow orchestration |
| MLflow experiments tracking | Free | Experiment logging |
| Model Registry | Free | Model versioning |
| Dataset storage (Azure Blob/ADLS) | Storage rates | Training data |
| Managed Feature Store (per record/month) | $0.10/100K records | Reusable ML features |
| Real-time inference endpoints | VM/ACI rates | Online serving |
| Batch inference | VM rates | Offline bulk scoring |
| Responsible AI dashboard | Free | Model fairness/explainability |

---

## Azure OpenAI Service — Foundation Models (Gen AI)

> **Note:** Azure OpenAI pricing matches OpenAI API pricing. Input and output tokens are charged separately.

### GPT-4o Models
| Model | Input (per 1M tokens) | Output (per 1M tokens) | Best For |
|---|---|---|---|
| gpt-4o | $5.00 | $15.00 | Multimodal, most capable |
| gpt-4o-mini | $0.15 | $0.60 | Fast, cost-efficient |
| gpt-4o (with vision) | $5.00 + $0.00765/image | $15.00 | Image + text understanding |

### GPT-4 Models
| Model | Input (per 1M tokens) | Output (per 1M tokens) | Best For |
|---|---|---|---|
| gpt-4 (8K context) | $30.00 | $60.00 | Complex reasoning |
| gpt-4 (32K context) | $60.00 | $120.00 | Long documents |
| gpt-4-turbo | $10.00 | $30.00 | Balanced capability |
| gpt-4-32k | $60.00 | $120.00 | Extended context |

### GPT-3.5 Models
| Model | Input (per 1M tokens) | Output (per 1M tokens) | Best For |
|---|---|---|---|
| gpt-3.5-turbo (4K) | $1.50 | $2.00 | General tasks, lower cost |
| gpt-3.5-turbo (16K) | $3.00 | $4.00 | Longer context tasks |
| gpt-3.5-turbo-instruct | $1.50 | $2.00 | Completion tasks |

### Embedding Models
| Model | Cost (per 1M tokens) | Best For |
|---|---|---|
| text-embedding-3-small | $0.02 | Cost-efficient RAG |
| text-embedding-3-large | $0.13 | High-quality embeddings |
| text-embedding-ada-002 | $0.10 | Legacy embeddings |

### Image Generation (DALL·E)
| Model | Quality | Size | Cost per image |
|---|---|---|---|
| DALL·E 3 | Standard | 1024×1024 | $0.040 |
| DALL·E 3 | Standard | 1024×1792 / 1792×1024 | $0.080 |
| DALL·E 3 | HD | 1024×1024 | $0.080 |
| DALL·E 3 | HD | 1024×1792 / 1792×1024 | $0.120 |

### Azure OpenAI Provisioned Throughput
| Provisioned Throughput Units (PTU) | Use Case |
|---|---|
| Per PTU/hour | $0.94–$2.00/hr depending on model |
| Best For | Predictable latency at scale, high-volume apps |

### Key Azure OpenAI Features
- Private endpoint (VNet integration)
- Data privacy (inputs not used for training)
- Azure AD authentication
- Content filtering (configurable)
- On-your-data (RAG with Azure AI Search)
- Fine-tuning (GPT-3.5-turbo, GPT-4 — per token charged separately)

---

## Azure AI Services (Cognitive Services)

### Azure AI Vision
| Feature | Free Tier | Paid Rate |
|---|---|---|
| Image analysis (per 1,000 transactions) | 5,000/month free | $1.00 (first 1M) |
| Read OCR (per 1,000 pages) | 5,000/month free | $1.50 |
| Custom Vision training (per hour) | 1 hr free | $0.75 |
| Custom Vision prediction (per 1,000 calls) | 10,000 free | $2.00 |
| Face API (per 1,000 calls) | 30,000/month free | $1.00 |
| Spatial Analysis (per camera) | — | $0.004/hr |

### Azure AI Speech
| Feature | Free Tier | Paid Rate |
|---|---|---|
| Speech to Text (per audio hour) | 5 hrs/month free | $1.00 |
| Neural Text to Speech (per 1M chars) | 0.5M/month free | $16.00 |
| Speech Translation (per audio hour) | 5 hrs/month free | $2.50 |
| Custom Speech (per audio hour training) | — | $0.90 |
| Speaker Recognition (per 1,000 transactions) | — | $1.00 |

### Azure AI Language
| Feature | Free Tier | Paid Rate |
|---|---|---|
| Sentiment Analysis (per 1,000 text records) | 5,000/month free | $2.00 |
| Named Entity Recognition | 5,000/month free | $2.00 |
| Language Detection | 5,000/month free | $0.50 |
| Text Summarization | 5,000/month free | $2.00 |
| Conversational Language Understanding | — | $2.00/1K text records |
| Custom NER training (per hour) | 1 hr free | $3.00 |

### Azure AI Translator
| Feature | Free Tier | Paid Rate |
|---|---|---|
| Text translation (per million characters) | 2M chars/month free | $10.00 |
| Document translation (per million characters) | — | $15.00 |
| Custom Translator (per million characters) | — | $40.00 |

### Azure AI Document Intelligence (Form Recognizer)
| Feature | Free Tier | Paid Rate |
|---|---|---|
| Prebuilt models (per 1,000 pages) | 500 pages/month free | $1.50 |
| Custom models training (per page) | 500 pages/month free | $0.60 |
| Custom models prediction (per 1,000 pages) | 500 pages/month free | $1.50 |
| Layout (per 1,000 pages) | 500 pages/month free | $1.50 |
| Invoice model (per 1,000 pages) | 500 pages/month free | $1.50 |

---

## Azure AI Search — Vector Search & RAG

| Tier | Replicas | Partitions | Cost/hr | Est. $/month | Best For |
|---|---|---|---|---|---|
| Free | 1 | 1 | Free | Free (3 indexes, 50 MB) | Dev/test |
| Basic | 3 max | 1 | $0.101 | ~$73 | Small production |
| Standard S1 | 12 max | 12 max | $0.336 | ~$242 | Medium search |
| Standard S2 | 12 max | 12 max | $1.344 | ~$968 | Large search |
| Standard S3 | 12 max | 12 max | $2.688 | ~$1,936 | Very large |
| Storage Optimized L1 | 12 max | 12 max | $2.688 | ~$1,936 | Large indexes |
| Storage Optimized L2 | 12 max | 12 max | $5.376 | ~$3,871 | Largest indexes |

### Semantic Ranker (AI-enhanced relevance)
| Item | Free | Paid |
|---|---|---|
| Semantic queries (per month) | 1,000/month free | $1.00/1,000 queries |

---

## Azure Bot Service

| Tier | Cost |
|---|---|
| Free (Standard channels) | Free (unlimited messages) |
| Premium channels (per 1,000 messages) | $0.50 |
| Direct Line Speech (per audio hour) | Speech rates apply |

---

*Prices are East US pay-as-you-go rates as of 2024. OpenAI model pricing changes frequently — verify at azure.microsoft.com/pricing.*
