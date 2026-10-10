# GCP — AI & Machine Learning Factsheet

---

## Vertex AI — Unified ML Platform

### Training — Compute (per hr)
| Machine Type | vCPU | RAM | Cost/hr | Best For |
|---|---|---|---|---|
| n1-standard-4 | 4 | 15 GB | $0.19 | Small model training |
| n1-standard-8 | 8 | 30 GB | $0.38 | Medium training |
| n1-highmem-8 | 8 | 52 GB | $0.44 | Memory-intensive |
| a2-highgpu-1g (A100) | 12 | 85 GB | $3.67 | LLM fine-tuning |
| a2-highgpu-4g (4x A100) | 48 | 340 GB | $14.69 | Large model training |
| a2-highgpu-8g (8x A100) | 96 | 680 GB | $29.39 | Foundation model training |
| a3-highgpu-8g (8x H100) | 208 | 1872 GB | ~$98.32 | Largest LLMs |
| TPU v4 pod (per chip/hr) | — | — | $4.20/chip | TPU-optimized training |
| TPU v5 (per chip/hr) | — | — | $4.50/chip | Latest TPU generation |
| Preemptible/Spot training | Various | — | ~60–90% off | Cost-effective training |

### Prediction — Online Endpoints
| Machine Type | vCPU | RAM | Cost/hr | Best For |
|---|---|---|---|---|
| n1-standard-2 | 2 | 7.5 GB | $0.095 | Small inference |
| n1-standard-4 | 4 | 15 GB | $0.190 | Medium inference |
| n1-standard-8 | 8 | 30 GB | $0.380 | High-traffic APIs |
| n1-standard-16 | 16 | 60 GB | $0.760 | Large models |
| a2-highgpu-1g (A100) | 12 | 85 GB | $3.67 | GPU inference |
| g2-standard-4 (L4 GPU) | 4+L4 | 16 GB | $0.70 | Efficient GPU inference |
| Prediction requests (per 1,000) | — | $0.008 | — |

### Vertex AI Batch Prediction
| Item | Cost |
|---|---|
| Batch prediction (same VM rates, billed per usage) | VM type × usage hours |
| Spot pricing available | ~60% off |

### Vertex AI Model Garden
| Feature | Cost |
|---|---|
| Open models (Llama 3, Gemma, etc.) — self-deployed | Compute costs only |
| Google-served models (via API) | Per-token/request rates |
| Third-party models (via Model Garden) | Partner pricing |

### Vertex AI Feature Store
| Item | Free Tier | Paid Rate |
|---|---|---|
| Online serving (per node/hr) | — | $0.18 |
| Offline storage (per GB/month) | — | $0.023 |
| Batch ingestion (per GB) | — | $0.002 |

### Vertex AI Pipelines (ML workflow orchestration)
| Item | Cost |
|---|---|
| Pipeline run (per execution step) | $0.03/step |
| Storage (pipeline artifacts, Cloud Storage) | Cloud Storage rates |

### Vertex AI Experiments & Metadata
| Item | Cost |
|---|---|
| Metadata storage (per GB/month) | $0.10 |
| Artifact and lineage storage | $0.10/GB/month |

---

## Gemini API — Foundation Models

### Gemini 1.5 Pro
| Item | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| Standard (≤128K context) | $3.50 | $10.50 |
| Long context (>128K tokens) | $7.00 | $21.00 |
| Grounding with Google Search (per request, >1K/day) | $35.00/1K requests | — |

### Gemini 1.5 Flash
| Item | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| Standard (≤128K context) | $0.075 | $0.30 |
| Long context (>128K tokens) | $0.15 | $0.60 |

### Gemini 1.0 Pro
| Item | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| Text only | $0.50 | $1.50 |
| Multimodal (image/video) | $0.50 | $1.50 |

### Gemini Flash 8B (smallest, cheapest)
| Item | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| Standard | $0.0375 | $0.15 |

### Imagen (Image Generation)
| Model | Cost |
|---|---|
| Imagen 3 (per image) | $0.04 |
| Imagen 2 (per image) | $0.02 |
| Edit / upscale operations | $0.04 |

### Embeddings API
| Model | Input (per 1M tokens) |
|---|---|
| text-embedding-004 | $0.025 |
| text-multilingual-embedding-002 | $0.025 |

### Free Tier (Gemini API via Vertex AI)
- Limited free usage available in Google AI Studio (not Vertex AI)
- Vertex AI: no free tier; billing required

---

## Document AI — Intelligent Document Processing

| Processor Type | Cost (per page) | Best For |
|---|---|---|
| Document OCR | $1.50/1,000 pages | Text extraction from PDFs/images |
| Form Parser | $65/1,000 pages | Structured form extraction |
| Invoice Parser | $65/1,000 pages | Invoice field extraction |
| Receipt Parser | $65/1,000 pages | Receipt processing |
| ID Document Parser | $65/1,000 pages | Passport, driver's license |
| Contract DocAI | Custom pricing | Contract analysis |
| Custom Extractor (trained) | $65/1,000 pages | Custom document types |

### Free Tier
1,000 pages/month free for most processors.

---

## Cloud Vision API — Image Analysis

| Feature | Free Tier | Cost per 1,000 units |
|---|---|---|
| Label detection | 1,000/month | $1.50 |
| OCR (text detection) | 1,000/month | $1.50 |
| Safe search detection | 1,000/month | $1.50 |
| Face detection | 1,000/month | $1.50 |
| Landmark detection | 1,000/month | $1.50 |
| Logo detection | 1,000/month | $1.50 |
| Object localization | 1,000/month | $1.50 |
| Image properties | 1,000/month | $1.50 |
| Web entity detection | 1,000/month | $3.50 |
| Document text detection | 1,000/month | $1.50 |

---

## Cloud Natural Language API — NLP

| Feature | Free Tier | Cost per 1,000 units |
|---|---|---|
| Syntax analysis | 5,000/month | $0.50 |
| Entity analysis | 5,000/month | $1.00 |
| Sentiment analysis | 5,000/month | $1.00 |
| Entity sentiment analysis | 5,000/month | $2.00 |
| Content classification | 5,000/month | $2.00 |
| Moderation analysis | — | $2.00 |

---

## Cloud Speech-to-Text API

| Tier | Cost per 60 seconds |
|---|---|
| Standard (phone/video audio, ≤60 min/month free) | $0.006 |
| Premium (enhanced models) | $0.009 |
| Medical model | $0.049 |
| Chirp 2 (latest model, per second) | $0.000333 |
| Real-time streaming | Same rates as speech recognition |
| Data logging opt-out | Standard rates |
| Chirp streaming | $0.000333/sec |

---

## Cloud Text-to-Speech API

| Voice Type | Cost per 1 million characters |
|---|---|
| Standard voices | $4.00 |
| WaveNet voices | $16.00 |
| Neural2 voices | $16.00 |
| Studio voices | $160.00 |
| Free tier (per month) | 4 million chars (Standard), 1 million chars (WaveNet/Neural2) |

---

## Cloud Translation API

| Item | Cost |
|---|---|
| Translation (per million characters) | $20.00 |
| Language detection (per million characters) | $20.00 |
| Translation V3 (same rates, batch support) | $20.00 |
| AutoML Translation (custom model inference, per million chars) | $80.00 |
| Free tier (per month) | 500,000 characters/month |

---

## AI Summary — Model Selection Guide

| Use Case | Recommended Service | Cost Tier |
|---|---|---|
| LLM inference (fast, cheap) | Gemini 1.5 Flash | $$ |
| LLM inference (complex tasks) | Gemini 1.5 Pro | $$$ |
| Custom model training | Vertex AI Training | $$–$$$$ |
| Custom model serving | Vertex AI Prediction | $$–$$$ |
| Image understanding | Cloud Vision API | $ |
| Document extraction | Document AI | $$ |
| Speech processing | Speech-to-Text API | $ |
| Text analysis | Natural Language API | $ |
| Translation | Cloud Translation API | $$ |

---

*Prices are us-central1 / global rates as of 2024.*
