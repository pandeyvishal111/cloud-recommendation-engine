# Use Case 4 — FedDocs: Federal Government Document Portal

## About the Customer

**Agency:** U.S. Department of Infrastructure Services *(fictionalised)*
**Industry:** Federal Government
**Size:** 500 federal employees across 12 agencies

This federal government agency is replacing an ageing on-premise document system with a modern cloud-hosted portal. Government employees from 12 different agencies will use it to upload, search, and share official documents and government forms. The system will handle Controlled Unclassified Information (CUI) — sensitive government records, though not classified as secret or top secret.

The IT Director has been given a $5,000/month cloud budget. Their agency's security and legal teams have issued a hard requirement: **FedRAMP High authorisation is mandatory**. No exceptions will be made.

The IT Director has heard that GCP BigQuery is excellent for analytics and has mentioned a preference for GCP during the intake conversation.

---

## Customer Questionnaire Responses

| Question | Customer's Answer |
|----------|------------------|
| What are you building? | A secure online portal where government employees from multiple agencies can upload, search, and share official government documents |
| How many users will use it at the same time? | Around 500 federal employees spread across 12 agencies — mostly during regular US business hours |
| Where are your users located? | United States only — the system must stay on US government-dedicated infrastructure |
| What is your monthly cloud budget? | $5,000 per month |
| Do you have any compliance or legal requirements? | Yes — FedRAMP High authorisation is mandatory. This is a hard requirement from our agency's cybersecurity office. It cannot be waived. |
| How important is uptime and reliability? | Very important — government employees rely on this during business hours. We need 99.9% uptime. |
| How sensitive is the data you will store? | High — Controlled Unclassified Information (CUI). Data must never leave US government-dedicated infrastructure. |
| Do you have a preferred cloud provider? | We have heard good things about GCP for analytics and our IT Director would prefer GCP if possible |

---

## What the Candidate Must Do

Run this customer profile through the UC48 recommendation engine and produce:

1. The recommended cloud provider with a fit score
2. The key cloud services the customer should use
3. An estimated monthly cost
4. Whether the budget is sufficient
5. All compliance flags and required steps before go-live
6. A clear explanation of why the customer's preferred provider (GCP) cannot be used
7. A runner-up provider option

---

## Evaluation Notes (for candidate)

- This use case **tests the compliance rule layer** — FedRAMP High must trigger GCP exclusion
- The customer explicitly prefers GCP — the engine must override this preference and explain why
- The recommendation must come from the eligible provider list only (AWS GovCloud or Azure Government)
- Failing to exclude GCP is a **critical failure** of the compliance rule layer
