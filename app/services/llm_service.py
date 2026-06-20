import json
import os

from dotenv import load_dotenv
from google import genai

from app.prompts.analyzer_prompt import build_analysis_prompt

load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        self.client = genai.Client(api_key=api_key)

    def analyze_resume(self, resume_text: str, job_description: str) -> dict:

        prompt = build_analysis_prompt(
            resume_text=resume_text, job_description=job_description
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt, config=genai.types.GenerateContentConfig(response_mime_type="application/json")
        )

        content = response.text

        try:
            return json.loads(content)

        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON returned by Gemini:\n{content}")