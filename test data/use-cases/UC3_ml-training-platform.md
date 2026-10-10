# Use Case 3 — NeuralForge: AI Model Training Platform

## About the Customer

**Company:** NeuralForge AI
**Industry:** Artificial Intelligence
**Size:** 18 engineers, seed-funded startup

NeuralForge is an AI research startup where teams of engineers train large machine learning models for computer vision and natural language tasks. Their researchers submit training jobs that run anywhere from 8 to 72 hours on large datasets. The jobs do not run all day, every day — they are submitted in batches, mostly during working hours. If a job gets interrupted, the team can restart it from a saved checkpoint, so they do not need guaranteed uptime for every moment of every job.

The CTO wants the most powerful GPU compute available for the lowest possible cost, with as little infrastructure to manage as possible.

---

## Customer Questionnaire Responses

| Question | Customer's Answer |
|----------|------------------|
| What are you building? | A cloud workspace where our AI researchers can train large machine learning models and store results. We need powerful GPU machines and a place to manage and track our experiments. |
| How many users will use it at the same time? | 20 researchers — they submit jobs throughout the day but do not all run jobs simultaneously |
| Where are your users located? | United States |
| What is your monthly cloud budget? | $15,000 per month |
| Do you have any compliance or legal requirements? | None — this is a purely private research environment with no personal or regulated data |
| How important is uptime and reliability? | Moderate — we run batch jobs and can restart from a saved checkpoint if something is interrupted. We would rather save money than pay for guaranteed uptime. |
| How sensitive is the data you will store? | Low — proprietary research datasets only, no personal data |
| Do you have a preferred cloud provider? | No preference — we want the best GPU performance per dollar. We use PyTorch and TensorFlow and want to avoid managing servers ourselves. |

---

## What the Candidate Must Do

Run this customer profile through the UC48 recommendation engine and produce:

1. The recommended cloud provider with a fit score
2. The key cloud services the customer should use (including the specific GPU type)
3. An estimated monthly cost
4. Whether the budget is sufficient
5. A cost-saving tip relevant to their batch job pattern
6. A runner-up provider option

---

## Evaluation Notes (for candidate)

- **No compliance requirements** — the engine should not apply any compliance rule layer here
- The customer explicitly says they can tolerate interruptions — this is a hint that spot / preemptible compute is appropriate
- GPU type and generation should be part of the recommendation rationale
- The cost estimate should reflect realistic spot/preemptible pricing, not full on-demand
