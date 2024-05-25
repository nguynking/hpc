from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Extractive Question-Answering API", description="API to answer a question using provided context")

model_name = "quocviethere/xlmroberta-finetuned-squadv2"
qa_pipeline = pipeline('question-answering', model=model_name)

class QARequest(BaseModel):
    context: str
    question: str

@app.post("/answer", summary="Answer a new question given context")
def answer_question(request: QARequest) -> dict:
    answer = qa_pipeline(context=request.context, question=request.question)['answer']
    return {"answer": answer}