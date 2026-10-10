from pydantic import BaseModel, Field
from typing import Optional


class UserRegistration(BaseModel):
    email: str
    password: str
    full_name: str
    company: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str


class RequirementInput(BaseModel):
    natural_language: str = Field(..., min_length=10)
    monthly_budget: Optional[str] = None
    compliance: Optional[str] = None
    concurrency: Optional[int] = 15
    region: Optional[str] = None
    workload_type: Optional[str] = None


class RecommendationResponse(BaseModel):
    provider: str
    fit_score: int
    architecture: str
    services: list[str]
    cost_estimate: dict
    tradeoffs: list[str]
    summary: str
