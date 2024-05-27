from fastapi import FastAPI, Depends
from pydantic import BaseModel
from transformers import pipeline
from sqlalchemy.orm import Session
from .models import ChatHistory, SessionLocal

app = FastAPI(title="Extractive Question-Answering API", description="API to answer a question using provided context")

model_name = "quocviethere/xlmroberta-finetuned-squadv2"
qa_pipeline = pipeline('question-answering', model=model_name)

class QARequest(BaseModel):
    context: str
    question: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/answer", summary="Answer a new question given context")
async def answer_question(request: QARequest, db: Session = Depends(get_db)) -> dict:
    answer = qa_pipeline(context=request.context, question=request.question)['answer']
    chat = ChatHistory(context=request.context, question=request.question, answer=answer)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return {"answer": answer}

@app.get("/history", summary="Get chat history")
async def get_history(db: Session = Depends(get_db)):
    history = db.query(ChatHistory).all()
    return history