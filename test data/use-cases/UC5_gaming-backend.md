# Use Case 5 — ArenaX: Real-Time Multiplayer Gaming Backend

## About the Customer

**Company:** ArenaX Studios
**Industry:** Online Gaming
**Size:** 75 employees, venture-backed

ArenaX is launching a real-time multiplayer battle royale game. Players across three continents compete live against each other and any delay in the game server connection above 100 milliseconds ruins the experience and causes players to quit. The game is launching with 25,000 simultaneous players and the team expects to grow to 100,000 players within 12 months. Players need shared leaderboards that update in real time for every region.

The Head of Engineering needs a global cloud setup where every player — regardless of whether they are in New York, London, or Tokyo — gets the same fast, responsive experience.

---

## Customer Questionnaire Responses

| Question | Customer's Answer |
|----------|------------------|
| What are you building? | A global real-time multiplayer game server backend. Players in different countries play against each other and we need the connection to be fast for everyone, everywhere. |
| How many users will use it at the same time? | 25,000 players simultaneously at launch, growing to 100,000 within 12 months |
| Where are your users located? | United States, Europe, and Asia Pacific — all three regions matter equally |
| What is your monthly cloud budget? | $8,000 per month |
| Do you have any compliance or legal requirements? | None — this is a consumer gaming product. No financial data, no health data. |
| How important is uptime and reliability? | Extremely important. If the servers go down during a match, players immediately leave and may never come back. We need 99.99% uptime. |
| How sensitive is the data you will store? | Low — only player usernames, game scores, match history, and session data |
| Do you have a preferred cloud provider? | No preference — our number one priority is the lowest possible ping (delay) for players in all three regions simultaneously |

---

## What the Candidate Must Do

Run this customer profile through the UC48 recommendation engine and produce:

1. The recommended cloud provider with a fit score
2. The key cloud services the customer should use
3. An estimated monthly cost
4. Whether the budget is sufficient
5. An explanation of how global low-latency is achieved with this provider
6. A cost-saving tip
7. A runner-up provider option

---

## Evaluation Notes (for candidate)

- **No compliance requirements** — the compliance rule layer should not trigger
- The key differentiator between providers here is **global network performance** — the recommendation rationale must address this specifically
- The recommendation should mention how cross-region consistency (leaderboards) is handled
- A generic recommendation without addressing the latency requirement is considered incomplete
