from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/classify/")
def classify_text(request: TextRequest):
    classes = ['Positive', 'Negative', 'Neutral']
    classification = random.choice(classes)
    return {"classification": classification}

