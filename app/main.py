from fastapi import FastAPI

from app.api.analyzer import router as analyzer_router

app = FastAPI(
    title="Resume Analyzer",
    description="Analyze resumes against job descriptions using OpenAI and FastAPI.",
    version="1.0.0",
)

@app.get("/")
def health_check():
    return {"status": "healthy", "application": "LLM Resume Analyzer"}

app.include_router(analyzer_router)
