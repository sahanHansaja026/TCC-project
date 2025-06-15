import io
from summary import summarize_with_sumy
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends # type: ignore
from sqlalchemy.orm import Session # type: ignore
import pdfplumber # type: ignore

from database import get_db
from models import PDFFile

router = APIRouter()

@router.post("/extract-text/")
async def extract_text_from_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        file_data = await file.read()

        # Save to DB
        pdf_entry = PDFFile(filename=file.filename, filedata=file_data)
        db.add(pdf_entry)
        db.commit()
        db.refresh(pdf_entry)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

    # Extract text from PDF in memory
    extract_text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_data)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extract_text += text + "\n"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Text extraction failed: {e}")

    word_count = len(extract_text.split())
    summary = summarize_with_sumy(extract_text)

    return {
        "text": extract_text,
        "word_count": word_count,
        "summary": summary
    }
