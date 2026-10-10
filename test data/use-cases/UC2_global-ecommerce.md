# Use Case 2 — ShopSphere: Global E-Commerce Platform

## About the Customer

**Company:** ShopSphere Ltd.
**Industry:** Retail / E-Commerce
**Size:** 200 employees, $40M annual revenue

ShopSphere is an online retailer selling electronics and fashion. They are currently running their website on a single server in the US and it struggles during peak periods. They are expanding to serve customers in Europe and Asia and need a globally distributed setup that is fast everywhere, handles massive traffic spikes during events like Black Friday, and processes customer payments securely.

The VP of Engineering needs a cloud recommendation before the engineering team begins rebuilding the platform.

---

## Customer Questionnaire Responses

| Question | Customer's Answer |
|----------|------------------|
| What are you building? | A global e-commerce website — product catalogue, shopping cart, and online payment checkout for customers across 3 continents |
| How many users will use it at the same time? | Normally around 5,000 customers at the same time. During big sale events, this can jump to 25,000. |
| Where are your users located? | United States, Europe, and Asia Pacific — all three regions are important to us |
| What is your monthly cloud budget? | $12,000 per month |
| Do you have any compliance or legal requirements? | Yes — we process customer credit card payments online. Our finance team says we need PCI-DSS compliance for card payment security. |
| How important is uptime and reliability? | Critical — every minute we are down costs us sales. We need 99.99% uptime, especially during peak sale periods. |
| How sensitive is the data you will store? | High — customer payment card details and order history |
| Do you have a preferred cloud provider? | No preference — performance and payment security matter most to us |

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

- The compliance requirement is **PCI-DSS**
- The workload spans **three global regions** — the recommendation must address this
- The engine should address how it handles the 5× traffic spike during sale events
- Output must be in plain business language
