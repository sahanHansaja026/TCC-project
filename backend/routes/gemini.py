import logging
from urllib import response
from schemas import ChatRequest, ChatResponse
from fastapi import APIRouter, HTTPException, status # type: ignore

import google.generativeai as genai # type: ignore

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat_with_bot(request: ChatRequest):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(request.prompt)
        return ChatResponse(text=response.text)
    except Exception as e:
        logging.error(f"Gemini API error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error communicating with AI model: {e}"
        )