from pydantic import BaseModel, Field

class ResumeAnalysisRequest(BaseModel):
    resume_text: str = Field(
        ...,
        min_length=50,
        description="Extracted text from candidate resume"
    )

    job_description: str = Field(
        ...,
        min_length=50,
        description="Job description provided by recruiter"
    )

class ResumeAnalysisResponse(BaseModel):
    match_score: int

    strengths: list[str]

    missing_skills: list[str]

    recommendations: list[str]