# Use Case 48 — CloudSelect: Customized Cloud Services Recommendation Engine

## About the Customer

**Company:** CloudSelect Advisory
**Industry:** Cloud Consulting / SaaS Platform
**Size:** 30 employees, growing digital-first business

CloudSelect Advisory helps businesses evaluate cloud services before they commit to a provider. The company wants to launch a web application that lets users describe their workload, compare AWS, Azure, and GCP service options, and receive AI-assisted recommendations for compute, storage, databases, networking, and cost. The platform will also keep a history of searches and let users export their recommendations for sharing with stakeholders.

The product team is looking for a cloud-ready recommendation engine that is secure, flexible, and easy for non-technical buyers to use. They expect the platform to support a growing user base while remaining simple enough for business users to complete a form and understand the results.

---

## Customer Questionnaire Responses

| Question | Customer's Answer |
|----------|------------------|
| What are you building? | A web application that helps businesses choose the best cloud services based on workload requirements, compliance needs, and budget. It compares AWS, Azure, and GCP recommendations for compute, storage, databases, networking, and related services. |
| How many users will use it at the same time? | About 15 concurrent users at launch, with expected growth as more users adopt the recommendation engine. |
| Where are your users located? | Primarily United States and Europe, with future expansion into Asia Pacific. |
| What is your monthly cloud budget? | $5,000 per month for hosting and operating the recommendation platform itself. |
| Do you have any compliance or legal requirements? | Yes — the application must protect user data and support audit logging. For client workloads, the recommendation engine should clearly flag requirements such as security and compliance considerations, including HIPAA, SOC 2, or regulated workloads. |
| How important is uptime and reliability? | Very important. The application should be available and responsive for regular business usage, with strong reliability and backup of user search data. |
| How sensitive is the data you will store? | Moderate to high. The application stores user profile information, workload questionnaires, search history, and recommendation outputs. It must protect this data and maintain logs for accountability. |
| Do you have a preferred cloud provider? | No preference. The platform should compare all three major providers and recommend the best fit based on the inputs and cost. |

---

## What the Candidate Must Do

Run this customer profile through the UC48 recommendation engine and produce:

1. The recommended cloud provider with a fit score
2. The key cloud services the customer should use
3. An estimated monthly cost for the recommendation platform
4. Whether the budget is sufficient
5. The recommended architecture pattern for the platform
6. The compliance and security controls that must be included
7. A runner-up provider option

---

## Evaluation Notes (for candidate)

- The platform is not just a cost calculator — it must recommend cloud services based on workload, compliance, and business inputs.
- The recommendation should account for multi-cloud comparison across AWS, Azure, and GCP.
- Security and audit logging are critical requirements and should be explicitly called out.
- The workload is moderate, but the system must still be scalable and support increasing user demand.
- The recommendation should emphasize ease of use for non-technical users who are completing the intake questionnaire.
- The system must support search history, recommendations, and report export in a business-friendly format.
- Evidence of performance and concurrent-user support should be incorporated into the recommendation rationale.
