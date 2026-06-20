from fastapi import APIRouter, HTTPException

from app.models.schemas import ResumeAnalysisRequest, ResumeAnalysisResponse
from app.services.llm_service import LLMService

router = APIRouter(prefix="/analyze", tags=["Resume Analyzer"])

llm_service = LLMService()

@router.post("", response_model=ResumeAnalysisResponse)
def analyze_resume(request: ResumeAnalysisRequest):
    try:
        result = llm_service.analyze_resume(
            resume_text=request.resume_text, job_description=request.job_description
        )

        return ResumeAnalysisResponse(**result)

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
