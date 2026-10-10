---
name: cloud-offering-analysis
description: Analyze AWS, Azure, and GCP cloud offerings, compare pricing models and feature fit for a given workload, and recommend the best provider based on technical and business requirements.
---

# Cloud Offering Analysis

Use this skill when the user needs help comparing cloud providers or evaluating the best-fit services for a workload.

## Goal

Assess available services across AWS, Azure, and GCP and compare them against the requirements in a use case. The output should help determine:

- which provider is the best fit
- which services are appropriate for the workload
- expected pricing patterns and monthly cost ranges
- key feature differences and trade-offs
- compliance and operational considerations
- a recommendation with reasoning and confidence level

## Inputs to consider

- workload type and expected usage pattern
- number of users / concurrency / throughput
- compliance needs
- data sensitivity and retention requirements
- latency sensitivity
- region or geographic distribution
- budget constraints
- preferred architecture style
- requirements for compute, storage, DB, networking, AI, monitoring, security, and integration

## Workflow

1. Identify workload categories
   - Compute-heavy, database-heavy, storage-heavy, analytics, AI/ML, real-time, secure enterprise, low-latency global workloads, serverless-first, etc.

2. Map requirements to provider services
   - Compute: EC2, ECS, EKS, Lambda, Azure VM, AKS, Azure Functions, GCE, GKE, Cloud Run
   - Storage: S3, EBS, EFS, Azure Blob, Azure Disk, Azure Files, Cloud Storage, Persistent Disk
   - Databases: RDS, Aurora, DynamoDB, Azure SQL, Cosmos DB, PostgreSQL/MySQL managed services, Cloud SQL, Spanner, Bigtable
   - Networking: VPC, ALB, CloudFront, Azure VNet, Load Balancer, GCP VPC, Cloud Load Balancing
   - Security/compliance: IAM, Key Vault, Azure AD, Cloud IAM, Security Center / Defender / WAF equivalents
   - Observability: CloudWatch, Azure Monitor, Cloud Logging / Monitoring
   - AI services: Azure OpenAI, Bedrock, Vertex AI, Azure AI services

3. Compare provider fit
   - Evaluate alignment between workload and provider strengths.
   - Consider ease of implementation, ecosystems, maturity, networking, global footprint, and operational fit.
   - Consider cost sensitivity and option flexibility.

4. Compare price drivers
   - Compute type and instance tier
   - Storage class and IOPS/performance profile
   - Data transfer and egress
   - Managed service pricing and region differences
   - Database capacity and backup costs
   - Load balancing and networking costs
   - Monitoring, log retention, and idle costs
   - Managed AI service usage and token or compute pricing

5. Explain feature differences
   - Which provider offers stronger integration with a given ecosystem
   - Which provider is preferable for managed services
   - Which provider offers cheaper or simpler options for the specific workload
   - Which provider is stronger for compliance, global reach, or developer productivity

6. Recommend the best provider and service mix
   - Recommend one provider as best fit
   - Include runner-up provider if close
   - Include a short rationale for each
   - Flag if a cheaper option sacrifices flexibility or compliance

## Output format

Always respond with:

### 1. Workload Summary
- business objective
- important workload characteristics
- key constraints

### 2. Provider Comparison
Create a concise comparison table with fields such as:
- Provider
- Best-fit services
- Strengths
- Weaknesses
- Estimated cost profile
- Compliance fit
- Best use case

### 3. Recommended Provider
- Best-fit provider
- Confidence level
- Fit score or ranking
- Why it wins for this workload

### 4. Service Recommendations
- Compute service(s)
- Database service(s)
- Storage service(s)
- Networking services
- Security identities / secrets
- Monitoring / logging
- AI or integration services if needed

### 5. Cost Estimate
- Monthly estimate range for the architecture
- Cost drivers and assumptions
- Budget fit assessment

### 6. Risks and Trade-offs
- What is optimized for this use case
- What may be more expensive or harder elsewhere
- Risks such as vendor lock-in, egress charges, or region constraints

### 7. Final Recommendation
- short executive summary
- one-line recommendation

## Comparison criteria

Use these criteria to judge provider fit:

- workload fit
- performance profile
- geographic reach
- price efficiency
- compliance fit
- operational simplicity
- developer experience
- ecosystem alignment
- service maturity

## Practical guidance

- Prefer cost-effective managed services where the workload is standard and not highly custom.
- Prefer provider-native security and compliance features when requirements are strict.
- For real-time or global workloads, evaluate latency, regional availability, and network cost.
- For AI-enabled platforms, compare model access, integration maturity, and data handling policies.
- For enterprise workloads, prioritize security posture, governance, and support options.

## Do not do

- Do not claim exact production pricing without assumptions clearly stated.
- Do not ignore data transfer, availability zone, and region differences.
- Do not treat all workloads as identical.
- Do not recommend a provider without showing why it matches the workload and constraints.

## Final instruction

Use business-friendly language where possible, but include enough technical reasoning for architecture decisions. The recommendation should be grounded in actual cloud service categories and realistic cost drivers rather than generic marketing statements.
