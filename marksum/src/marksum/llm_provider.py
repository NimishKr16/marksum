import os
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Setup Gemini once
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def summarize_with_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()