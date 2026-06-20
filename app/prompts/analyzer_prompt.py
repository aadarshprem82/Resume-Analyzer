def build_analysis_prompt(resume_text: str, job_description: str) -> str:
    prompt = f"""
You are an experienced Technical Recruiter and ATS evaluation system.

Analyze the candidate resume against the provided job description.

Your tasks:

1. Calculate a match score between 0 and 100.
2. Identify candidate strengths.
3. Identify missing skills or experience.
4. Provide practical recommendations to improve suitability.

Return ONLY raw JSON.

Do not use markdown.
Do not use triple backticks.
Do not add explanations.

Schema:

{{
  "match_score": 0,
  "strengths": [],
  "missing_skills": [],
  "recommendations": []
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    return prompt
