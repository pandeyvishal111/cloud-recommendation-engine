import logging

from fastapi import APIRouter, File, Query, UploadFile
from fastapi.responses import Response

from app.schemas import RequirementInput
from app.services.ai_service import AIRecommendationService
from app.services.blob_service import BlobStorageService
from app.services.comparison_service import RecommendationBuilder
from app.services.database_service import DatabaseService
from app.services.export_service import ExportService

router = APIRouter(tags=["recommendations"])
logger = logging.getLogger(__name__)


@router.post("/recommendations/build")
def build_recommendation(payload: RequirementInput):
    ai_service = AIRecommendationService()
    prompt = ai_service.build_prompt(payload.model_dump())
    recommendation = RecommendationBuilder.build(payload.model_dump())
    ai_status = ai_service.generate(payload.model_dump())
    return {
        "prompt": prompt,
        "recommendation": recommendation,
        "ai_status": ai_status,
    }


@router.post("/recommendations/save")
def save_recommendation(payload: dict):
    request_payload = dict(payload or {})
    user_email = request_payload.pop("user_email", "guest@example.com")
    title = request_payload.pop("title", "Saved recommendation")

    if "payload" in request_payload and isinstance(request_payload["payload"], dict):
        request_payload = request_payload["payload"]

    result = DatabaseService.save_search(
        user_email=user_email,
        title=title,
        payload=request_payload,
    )
    return result


@router.get("/recommendations/history")
def get_history(user_email: str | None = None):
    result = DatabaseService.list_searches(user_email=user_email)
    return {"history": result}


@router.post("/recommendations/export")
def export_recommendation(
    payload: dict,
    export_format: str = Query(default="csv", alias="format"),
) -> Response:
    """Generate and return a downloadable recommendation report."""
    extension = (export_format or "csv").lower()
    try:
        content, media_type = ExportService.export(payload, extension)
    except Exception:
        logger.exception("Recommendation export failed (format=%s)", extension)
        raise

    if extension == "excel":
        filename = "recommendation.xlsx"
    elif extension == "html":
        filename = "recommendation.html"
    elif extension == "pdf":
        filename = "recommendation.pdf"
    else:
        filename = "recommendation.csv"

    logger.info(
        "Recommendation export generated (format=%s, bytes=%d)",
        extension,
        len(content),
    )
    return Response(
        content=content,
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.post("/files/upload")
async def upload_file(file: UploadFile = File(...)):
    storage = BlobStorageService()
    content = await file.read()
    result = storage.upload_bytes(
        file_name=file.filename,
        content=content,
        container="recommendations",
    )
    return result
