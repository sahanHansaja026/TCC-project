import logging
from base import configure_gemini
from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from database import engine
import models

from routes import user,pdf,gemini

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
configure_gemini()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Include the user router
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(pdf.router)
app.include_router(gemini.router)