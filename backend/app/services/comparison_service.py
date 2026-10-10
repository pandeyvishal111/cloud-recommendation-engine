from __future__ import annotations


class RecommendationBuilder:
    @staticmethod
    def build(data: dict) -> dict:
        text = (data.get("natural_language") or "").lower()
        workload = data.get("workload_type") or (
            "web application" if "app" in text or "portal" in text else "cloud workload"
        )
        budget = data.get("monthly_budget") or "$5000"
        compliance = data.get("compliance") or "General enterprise security"
        concurrency = data.get("concurrency") or 15
        region = data.get("region") or "United States"

        is_ai = any(keyword in text for keyword in ["ai", "gen ai", "llm", "openai", "chatbot", "ml"])
        is_data = any(keyword in text for keyword in ["analytics", "data lake", "warehouse", "etl", "reporting"])
        is_high_compliance = any(keyword in text for keyword in ["hipaa", "fedramp", "pci", "sox", "compliance", "audit", "security"])
        is_api = any(keyword in text for keyword in ["api", "service", "microservice", "backend"])

        if is_ai:
            best_provider = "Azure"
            fit_score = 95
            service_picks = [
                "Azure Container Apps",
                "Azure Database for PostgreSQL",
                "Azure Blob Storage",
                "Azure Monitor",
                "Azure OpenAI",
                "Azure Key Vault",
                "Azure Front Door",
            ]
            if "openai" in text:
                service_picks.append("Azure OpenAI GPT deployment")
        elif is_data:
            best_provider = "GCP"
            fit_score = 90
            service_picks = [
                "Cloud SQL or BigQuery",
                "Cloud Storage",
                "Dataflow or Pub/Sub",
                "Monitoring and Logging",
                "IAM and Security",
            ]
        elif is_high_compliance:
            best_provider = "Azure"
            fit_score = 94
            service_picks = [
                "Azure App Service or AKS",
                "Azure Database for PostgreSQL",
                "Azure Blob Storage",
                "Azure Monitor",
                "Azure Policy",
                "Azure Key Vault",
                "Azure Firewall",
            ]
        elif is_api:
            best_provider = "AWS"
            fit_score = 88
            service_picks = [
                "Amazon ECS or Lambda",
                "Amazon RDS",
                "S3",
                "CloudWatch",
                "API Gateway",
                "Shield or WAF",
            ]
        else:
            best_provider = "Azure"
            fit_score = 92
            service_picks = [
                "Azure App Service or Container Apps",
                "Azure Database for PostgreSQL",
                "Azure Blob Storage",
                "Azure Monitor",
                "Azure OpenAI",
                "Azure Key Vault",
            ]

        if "react" in text or "frontend" in text:
            service_picks.insert(0, "Azure Static Web Apps")

        if "postgres" in text or "database" in text:
            service_picks.append("Managed PostgreSQL")

        service_level_breakdown = [
            {
                "service": "Managed web/API runtime",
                "provider": best_provider,
                "monthly_estimate": "$180 - $420",
                "details": "Runs the application layer and handles incoming traffic and business logic.",
            },
            {
                "service": "Managed database",
                "provider": best_provider,
                "monthly_estimate": "$90 - $350",
                "details": "Stores transactional, reporting, and operational data securely.",
            },
            {
                "service": "Blob/object storage",
                "provider": best_provider,
                "monthly_estimate": "$25 - $180",
                "details": "Stores documents, media, logs, and backups at low cost.",
            },
            {
                "service": "Monitoring and alerting",
                "provider": best_provider,
                "monthly_estimate": "$40 - $220",
                "details": "Provides uptime, performance, and compliance monitoring.",
            },
        ]

        if is_ai:
            service_level_breakdown.insert(1, {
                "service": "AI inference layer",
                "provider": best_provider,
                "monthly_estimate": "$250 - $1200",
                "details": "Covers model hosting, embeddings, and orchestration for AI workloads.",
            })

        if is_high_compliance:
            service_level_breakdown.append({
                "service": "Security & policy controls",
                "provider": best_provider,
                "monthly_estimate": "$30 - $180",
                "details": "Adds enterprise identity, policy, and audit controls for regulated environments.",
            })

        similar_services = [
            {
                "service": "AWS equivalent stack",
                "provider": "AWS",
                "monthly_estimate": "$220 - $600",
                "comparison": "Strong breadth and maturity, but typically more configuration overhead.",
            },
            {
                "service": "GCP equivalent stack",
                "provider": "GCP",
                "monthly_estimate": "$210 - $580",
                "comparison": "Strong analytics tooling and simplicity, especially for data-heavy workloads.",
            },
        ]

        monthly_base = 1200
        if "ai" in text or "openai" in text:
            monthly_base = 2200
        elif "data" in text or "analytics" in text:
            monthly_base = 1800
        elif "hipaa" in text or "fedramp" in text:
            monthly_base = 2600

        low = monthly_base
        high = monthly_base + (concurrency * 18) + 1500
        if best_provider == "GCP":
            low = max(1100, monthly_base - 150)
            high = max(high, low + 1800)
        elif best_provider == "AWS":
            low = max(1200, monthly_base)
            high = max(high, low + 1800)

        cost_estimate = {
            "monthly_estimate": f"${low:,} - ${high:,}",
            "assumptions": {
                "budget": budget,
                "concurrency": concurrency,
                "region": region,
                "workload": workload,
                "compliance": compliance,
            },
            "comparison": {
                "AWS": f"${max(1200, low):,} - ${max(high, low + 1600):,}",
                "Azure": f"${max(1100, low - 100):,} - ${max(high, low + 1800):,}",
                "GCP": f"${max(1000, low - 200):,} - ${max(high, low + 2000):,}",
            },
        }

        tradeoffs = [
            f"{best_provider} best matches the requested workload pattern and compliance posture.",
            "The alternative cloud providers remain viable for broader ecosystem or analytics-heavy use cases.",
            "Cost and operational complexity will vary most with concurrency, compliance controls, and AI feature usage.",
        ]

        if is_ai:
            tradeoffs[0] = "Azure is strongest here due to its managed AI services and enterprise integration."
        elif is_data:
            tradeoffs[0] = "GCP is attractive for large-scale analytics pipelines and data-intensive operations."
        elif is_api:
            tradeoffs[0] = "AWS offers broad platform choice and mature API infrastructure for service-oriented workloads."

        summary = (
            f"For a {workload} serving {concurrency} concurrent users in {region}, with {compliance} requirements and a budget of {budget}, "
            f"{best_provider} is the best fit because it aligns with the workload profile, service needs, and operational constraints."
        )

        return {
            "provider": best_provider,
            "fit_score": fit_score,
            "architecture": (
                "A modular application with managed platform services, secure identity controls, and cloud-native data and AI components selected to match the stated workload."
            ),
            "services": service_picks,
            "service_level_breakdown": service_level_breakdown,
            "similar_services": similar_services,
            "cost_estimate": cost_estimate,
            "tradeoffs": tradeoffs,
            "summary": summary,
        }
