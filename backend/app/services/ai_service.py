from __future__ import annotations

import re

from openai import AzureOpenAI

from app.config import settings


class AIRecommendationService:
    def __init__(self):
        self.endpoint = settings.AZURE_OPENAI_ENDPOINT
        self.api_key = settings.AZURE_OPENAI_API_KEY
        self.model = settings.AZURE_OPENAI_DEPLOYMENT or settings.AZURE_OPENAI_MODEL or "gpt-5.1"
        self.api_version = settings.AZURE_OPENAI_API_VERSION or "2025-04-01-preview"

    def build_prompt(self, data: dict) -> str:
        natural_language = data.get("natural_language", "")
        requirement_summary = f"\nUser requirement: {natural_language}\n"
        requirement_summary += f"Budget: {data.get('monthly_budget') or 'Not specified'}\n"
        requirement_summary += f"Compliance: {data.get('compliance') or 'General enterprise security'}\n"
        requirement_summary += f"Concurrency: {data.get('concurrency') or 15}\n"
        requirement_summary += f"Region: {data.get('region') or 'Global'}\n"
        requirement_summary += "\nAnalyze and recommend the best cloud architecture, provider fit, cost estimate, and trade-offs."
        return requirement_summary

    def generate(self, data: dict) -> dict:
        prompt = self.build_prompt(data)

        if not self.endpoint or not self.api_key:
            return {
                "status": "mocked",
                "prompt": prompt,
                "note": "Environment variables for Azure OpenAI are not configured. Mock response returned.",
            }

        try:
            client = AzureOpenAI(
                api_key=self.api_key,
                api_version=self.api_version,
                azure_endpoint=self.endpoint,
            )

            completion_kwargs = {
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a senior cloud architect. Extract functional and non-functional requirements and "
                            "recommend the best cloud provider, services, trade-offs, and cost estimates for the workload."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.2,
            }

            model_name = (self.model or "").lower()
            if re.search(r"gpt[-_]?5|gpt5\d|^o[1-9]", model_name):
                completion_kwargs["max_completion_tokens"] = 800
            else:
                completion_kwargs["max_tokens"] = 800

            response = client.chat.completions.create(**completion_kwargs)
            content = response.choices[0].message.content
            return {
                "status": "success",
                "model": self.model,
                "prompt": prompt,
                "response": content,
            }
        except Exception as exc:  # pragma: no cover - runtime integration failure fallback
            return {
                "status": "error",
                "prompt": prompt,
                "error": str(exc),
            }
