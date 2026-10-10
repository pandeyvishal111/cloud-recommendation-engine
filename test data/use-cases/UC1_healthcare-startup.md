# Use Case 1 — HealthTrack: Patient Health Portal

## About the Customer

**Company:** HealthTrack Inc.
**Industry:** Digital Healthcare
**Size:** 45 employees, Series A startup

HealthTrack is a digital health startup that wants to build an online patient portal. Their platform will allow patients to log in securely, view their medical records, book doctor appointments, check lab test results, and send messages to their care team. They already have two hospital networks signed up as clients and need the platform live within 6 months.

The CTO has come to the recommendation engine with no prior cloud experience and needs guidance on which cloud provider to use and what it will cost.

---

## Customer Questionnaire Responses

| Question | Customer's Answer |
|----------|------------------|
| What are you building? | A secure web portal where patients can access their health records, book appointments, and view lab results |
| How many users will use it at the same time? | Around 300 — a mix of patients and doctors logging in throughout the day |
| Where are your users located? | United States only |
| What is your monthly cloud budget? | $2,500 per month |
| Do you have any compliance or legal requirements? | Yes — we store patient health records and our legal team confirmed we need HIPAA compliance. This is mandatory before we go live. |
| How important is uptime and reliability? | Very important — if the system goes down, patients cannot access their health information. We need at least 99.9% uptime. |
| How sensitive is the data you will store? | Very high — we store Protected Health Information (PHI) including diagnoses, medication history, and lab results |
| Do you have a preferred cloud provider? | No preference — we want whatever is best and most cost-effective for our situation |

---

## What the Candidate Must Do

Run this customer profile through the UC48 recommendation engine and produce:

1. The recommended cloud provider with a fit score
2. The key cloud services the customer should use
3. An estimated monthly cost
4. Whether the budget is sufficient
5. Any compliance steps the customer must take before going live
6. A runner-up provider option

---

## Evaluation Notes (for candidate)

- The compliance requirement here is **HIPAA**
- The output must be in plain business language — this customer is not a cloud engineer
- The recommendation must include what the customer needs to do about compliance, not just which provider to pick
