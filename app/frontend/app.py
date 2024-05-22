import gradio as gr
import requests

def classify_text(text):
    response = requests.post("http://api:8000/classify/", json={"text": text})
    return response.json()['classification']

iface = gr.Interface(
    fn=classify_text,
    inputs=gr.Textbox(lines=2, placeholder="Enter text here..."),
    outputs=gr.Label(num_top_classes=1),
    title="Text Classification",
    description="Classify text as Positive, Negative, or Neutral"
)

iface.launch(server_name="0.0.0.0", server_port=7860)

