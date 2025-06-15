# base.py
import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai

def configure_gemini():
    try:
        load_dotenv()  # Load from .env
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set.")
        genai.configure(api_key=api_key)
        logging.info("Gemini API configured successfully.")
    except Exception as e:
        logging.error(f"Error configuring Gemini API: {e}")
