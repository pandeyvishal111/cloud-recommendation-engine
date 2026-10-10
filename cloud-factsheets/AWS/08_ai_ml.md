# AWS — AI & Machine Learning Factsheet

---

## Amazon SageMaker — ML Platform

### Training Instance Types
| Instance | vCPU | RAM (GB) | GPU | Cost/hr | Best For |
|---|---|---|---|---|---|
| ml.c5.xlarge | 4 | 8 | — | $0.238 | CPU training, feature engineering |
| ml.c5.2xlarge | 8 | 16 | — | $0.476 | Larger CPU training |
| ml.c5.4xlarge | 16 | 32 | — | $0.952 | Batch inference |
| ml.m5.xlarge | 4 | 16 | — | $0.269 | General training |
| ml.m5.2xlarge | 8 | 32 | — | $0.538 | Medium-scale training |
| ml.g4dn.xlarge | 4 | 16 | 1x T4 | $0.736 | GPU inference, small training |
| ml.g4dn.2xlarge | 8 | 32 | 1x T4 | $1.052 | GPU training |
| ml.g4dn.12xlarge | 48 | 192 | 4x T4 | $5.478 | Large GPU training |
| ml.p3.2xlarge | 8 | 61 | 1x V100 | $3.825 | Deep learning training |
| ml.p3.8xlarge | 32 | 244 | 4x V100 | $14.688 | Distributed training |
| ml.p3.16xlarge | 64 | 488 | 8x V100 | $28.152 | Large distributed training |
| ml.p4d.24xlarge | 96 | 1,152 | 8x A100 | $32.773 | Very large model training |
| ml.trn1.2xlarge | 8 | 32 | 1x Trainium | $1.343 | Cost-efficient Trainium training |
| ml.trn1.32xlarge | 128 | 512 | 16x Trainium | $21.50 | Large Trainium training |
| ml.inf1.xlarge | 4 | 8 | 1x Inferentia | $0.228 | Cost-efficient ML inference |
| ml.inf2.xlarge | 4 | 16 | 1x Inferentia2 | $0.758 | High-perf inference |

### Hosting / Inference Instances
Same instance families as training (ml.c5, ml.m5, ml.g4dn, ml.inf1, ml.inf2, ml.p3).

| Endpoint Type | Cost | Best For |
|---|---|---|
| Real-time endpoints | Per instance-hr (same rates as training) | Low-latency predictions |
| Serverless Inference | $0.0200/GB + $0.000016/provisioned MB-s | Infrequent inference |
| Async Inference | Per instance-hr | Large payloads, long processing |
| Batch Transform | Per instance-hr | Offline bulk inference |
| Multi-Model Endpoints | Per instance-hr | Host thousands of models on one endpoint |

### SageMaker Studio & Notebooks
| Feature | Cost |
|---|---|
| SageMaker Studio (IDE) | Free to open; pay for notebook instances |
| ml.t3.medium notebook | $0.0582/hr |
| ml.t3.large notebook | $0.1046/hr |
| ml.m5.xlarge notebook | $0.269/hr |
| SageMaker Studio Lab | Free (limited GPU time) |
| SageMaker Experiments | Free |
| SageMaker Pipelines | Free (pay for underlying compute) |
| SageMaker Feature Store (online, per GB/month) | $0.25 |
| SageMaker Feature Store (offline, S3) | S3 rates |
| SageMaker Model Registry | Free |
| SageMaker Clarify (bias detection, per instance-hr) | Training instance rates |
| SageMaker Ground Truth (labeling, per object) | $0.08/object (text) |

---

## Amazon Bedrock — Foundation Models (Gen AI)

### Anthropic Claude Models (input / output per 1,000 tokens)
| Model | Input $/1K tokens | Output $/1K tokens | Best For |
|---|---|---|---|
| Claude 3 Haiku | $0.00025 | $0.00125 | Fast, low-cost tasks |
| Claude 3 Sonnet | $0.003 | $0.015 | Balanced intelligence |
| Claude 3 Opus | $0.015 | $0.075 | Most intelligent tasks |
| Claude 3.5 Sonnet | $0.003 | $0.015 | Advanced reasoning |
| Claude 3.5 Haiku | $0.0008 | $0.004 | Fast, affordable |

### Amazon Titan Models
| Model | Input $/1K tokens | Output $/1K tokens | Best For |
|---|---|---|---|
| Titan Text Lite | $0.0003 | $0.0004 | Simple tasks |
| Titan Text Express | $0.0008 | $0.0016 | General text generation |
| Titan Text Premier | $0.0005 | $0.0015 | Complex generation |
| Titan Embeddings V2 | $0.00002/1K tokens | — | Semantic search, RAG |
| Titan Multimodal Embeddings | $0.0006/image | — | Image search |

### Meta Llama Models
| Model | Input $/1K tokens | Output $/1K tokens |
|---|---|---|
| Llama 3 8B Instruct | $0.0003 | $0.0006 |
| Llama 3 70B Instruct | $0.00265 | $0.0035 |
| Llama 3.1 405B Instruct | $0.00532 | $0.016 |

### Stability AI (Image Generation)
| Model | Cost per image |
|---|---|
| Stable Diffusion XL 1.0 (512x512) | $0.018 |
| Stable Diffusion XL 1.0 (1024x1024) | $0.036 |

### Bedrock Features Pricing
| Feature | Cost |
|---|---|
| Knowledge Bases (vector store queries, per 1K) | $0.01 |
| Bedrock Agents (per 1K input tokens) | Same as underlying model |
| Model Evaluation (per response) | $0.10 |
| Guardrails (per 1K units processed) | $0.75 |
| Fine-tuning (training tokens, per 1K) | $0.004 |

---

## Amazon Rekognition — Computer Vision

| Feature | Free Tier | Paid Rate |
|---|---|---|
| Image analysis (per 1,000 images) | 5,000 images/month free | $1.00 (first 1M) / $0.80 (next 9M) |
| Video analysis (per minute) | 1,000 min/month free | $0.10 (first 1M min) |
| Face search (per 1,000 images) | 5,000/month free | $1.00 |
| Face storage (per face/month) | 1,000 faces free | $0.01/1,000 faces |
| Custom Labels training (per hr) | — | $1.00 |
| Custom Labels inference (per hr) | — | $4.00 |

---

## Amazon Comprehend — NLP

| Feature | Free Tier | Paid Rate |
|---|---|---|
| Entity recognition (per 100 characters) | 50K units/month free | $0.0001 (first 10M units) |
| Sentiment analysis (per 100 characters) | 50K units/month free | $0.0001 |
| Key phrase extraction | 50K units/month free | $0.0001 |
| Language detection | 50K units/month free | $0.0001 |
| Custom classification training (per document) | — | $0.0004 |
| Custom NER (per unit) | — | $0.0005 |

---

## Amazon Transcribe — Speech to Text

| Feature | Free Tier | Paid Rate |
|---|---|---|
| Standard (per second of audio) | 60 min/month free | $0.024/min |
| Medical (per second of audio) | — | $0.0750/min |
| Call Analytics (per minute) | — | $0.02 |
| Real-time streaming (per second) | — | $0.000085/second |

---

## Amazon Translate — Text Translation

| Feature | Free Tier | Paid Rate |
|---|---|---|
| Standard (per character) | 2M characters/month free | $0.000015/character |
| Active Custom Translation (per character) | — | $0.000060/character |
| Batch translation (per character) | — | $0.000015/character |

---

## Amazon Textract — Document AI

| Feature | Free Tier | Paid Rate |
|---|---|---|
| Detect Document Text (per page) | 1,000 pages/month free | $0.0015 |
| Analyze Document (Forms/Tables, per page) | 1,000 pages/month free | $0.050 |
| Analyze Document (Queries, per page) | — | $0.050 |
| Analyze Expense (invoices/receipts, per page) | 1,000 pages/month free | $0.010 |
| Analyze ID (per page) | — | $0.050 |

---

## Amazon Polly — Text to Speech

| Feature | Free Tier | Paid Rate |
|---|---|---|
| Standard voices (per 1M characters) | 5M characters/month free (12 months) | $4.00 |
| Neural voices (per 1M characters) | 1M characters/month free (12 months) | $16.00 |
| Long-form voices (per 1M characters) | — | $100.00 |

---

*Prices are US East (N. Virginia) rates as of 2024. Bedrock pricing varies by region and may change frequently.*
