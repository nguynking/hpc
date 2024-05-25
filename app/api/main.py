from fastapi import FastAPI
from transformers import pipeline

app = FastAPI(title="Extractive Question-Answering API", description="API to answer a question using provided context")

# Load the model using Hugging Face's pipeline
model_name = "quocviethere/xlmroberta-finetuned-squadv2"
qa_pipeline = pipeline('question-answering', model=model_name)

@app.post("/answer", summary="Answer a new question give context")
def answer_question(context: str, question: str) -> dict:
    answer = qa_pipeline(context=context, question=question)['answer']
    return {"answer": answer}