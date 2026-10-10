---
name: solution-architecture-design
description: Analyse a user use case, extract functional and technical requirements, and propose a practical architecture for the solution with trade-offs, components, security, scalability, and implementation guidance.
---

# Solution Architecture Design

Use this skill when a user wants help turning a business or technical use case into a solution architecture.

## Goal

Transform a problem statement, use case, or requirements brief into a clear architecture recommendation that includes:

- business and functional requirements
- technical requirements and constraints
- architecture overview
- components and responsibilities
- data flow and integrations
- security, compliance, and observability
- scalability, resilience, and performance expectations
- technology recommendations
- trade-offs and risks
- implementation roadmap or MVP-first plan

## Workflow

1. Understand the use case
   - Identify the user problem and business objective.
   - Extract functional requirements and business workflows.
   - Identify actors, users, systems, and integrations.

2. Capture non-functional requirements
   - Performance, latency, throughput, concurrency, availability, scale.
   - Security, identity, data protection, auditability, compliance.
   - Cost, maintainability, operability, and deployment expectations.

3. Ask targeted clarifying questions only if required
   - What are the primary user journeys?
   - What is the expected scale of users and transactions?
   - Are there compliance requirements such as HIPAA, PCI, SOC 2, GDPR, FedRAMP?
   - What systems or APIs need to integrate?
   - Is this greenfield or modernization?
   - What is the target deployment model: cloud-native, hybrid, or on-prem?

4. Produce a solution architecture
   - Recommend suitable architecture patterns, such as layered architecture, microservices, event-driven, modular monolith, or serverless-first.
   - Select a reasonable technology stack based on the problem, not just popular choices.
   - Explain component responsibilities and boundaries.
   - Include data storage, compute, integration, messaging, caching, search, and monitoring choices.

5. Validate against priorities
   - Check that the solution addresses business goals, cost, scale, and compliance.
   - Call out assumptions and trade-offs.
   - Propose an MVP and future-phase evolution.

## Output format

Always structure the response as:

### 1. Problem Summary
- Business objective
- Key constraints

### 2. Functional Requirements
- User journeys
- Core features
- Integrations

### 3. Non-Functional Requirements
- Performance
- Security
- Scalability
- Reliability
- Compliance
- Cost

### 4. Recommended Architecture
- High-level architecture overview
- Major components
- Deployment model
- Data flow

### 5. Technology Recommendations
- Frontend, backend, database, messaging, caching, AI, observability, infrastructure
- Reason for each choice

### 6. Security and Compliance
- Identity and access
- Secrets management
- Encryption
- Audit logging
- Data residency and privacy controls

### 7. Scalability and Resilience
- Horizontal scaling plan
- Load balancing and failover
- Queueing and async processing
- Caching strategy

### 8. Trade-offs and Risks
- What was prioritized
- What is intentionally deferred
- Risks and mitigation

### 9. Recommended MVP and Next Phases
- Phase 1: MVP
- Phase 2: scale and automation
- Phase 3: optimization and advanced features

## Quality bar

- Prefer practical and balanced decisions over theoretical architecture.
- Base recommendations on the actual constraints in the use case.
- Highlight assumptions explicitly.
- Tie architecture choices to business needs and cost profile.
- Keep the design understandable to both technical and non-technical stakeholders.

## Example reasoning patterns

- If the problem is a customer-facing application with moderate concurrency, prefer a modular monolith or layered app with clear service boundaries before a full microservices decomposition.
- If the use case includes bursty workloads or event-based processing, consider queue-based async workflows and autoscaling.
- If there is strict compliance or sensitive data, prioritize identity controls, encryption, audit logs, and least-privilege access.
- If the problem requires AI features, integrate a managed LLM API and keep prompt orchestration, caching, and guardrails separate from core domain logic.
- If the requirement is low-latency global access, prioritize regional deployment, CDN, caching, and data locality decisions early.

## Do not do

- Do not recommend a complex architecture without a clear need.
- Do not ignore security, performance, and compliance requirements.
- Do not propose a stack without explaining why it fits the use case.
- Do not present vague recommendations; always explain trade-offs and operational implications.

## Final instruction

Design the architecture as a decision-oriented recommendation, not a generic template. Use the user’s requirements to justify each choice and emphasize what matters most for this specific use case.
