import gradio as gr
import requests

# def classify_text(text):
#     response = requests.post("http://api:8000/classify/", json={"text": text})
#     return response.json()['classification']

# Define a function that the interface will use
def answer_question(context, question):
    response = requests.post("http://api:8000/answer/", json={"context": context, "question": question})
    return response.json()['answer']

# iface = gr.Interface(
#     fn=classify_text,
#     inputs=gr.Textbox(lines=2, placeholder="Enter text here..."),
#     outputs=gr.Label(num_top_classes=1),
#     title="Text Classification",
#     description="Classify text as Positive, Negative, or Neutral"
# )

# Create the Gradio interface
iface = gr.Interface(fn=answer_question,
                     inputs=[
                         gr.Textbox(lines=7, placeholder="Enter the context here...", label="Context"),
                         gr.Textbox(placeholder="Enter your question here...", label="Question")
                     ],
                     outputs=gr.Textbox(label="Answer"),
                     title='UEH-QA',
                     description='Creating safe AGI that benefits all of humanity.',
                     examples=examples)

iface.launch(server_name="0.0.0.0", server_port=7860)

