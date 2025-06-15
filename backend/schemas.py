from pydantic import BaseModel # type: ignore

class UserCreate(BaseModel):
    username:str
    email:str
    password:str
    
class UserLogin(BaseModel):
    email:str
    password:str
    
class PDFStorageSchema(BaseModel):
    filename: str
    content: bytes  # for binary content

    class Config:
        orm_mode = True

class ChatRequest(BaseModel):
    prompt:str

class ChatResponse(BaseModel):
    text:str