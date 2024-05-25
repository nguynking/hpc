import gradio as gr
import requests

def answer_question(context, question):
    response = requests.post(
        "http://api:8000/answer", 
        json={"context": context, "question": question}
    )
    return response.json().get('answer', 'No answer returned')

def get_history():
    response = requests.get("http://api:8000/history")
    history = response.json()
    # Ensure the data is in the correct format for Gradio Dataframe component
    formatted_history = [
        (entry['id'], entry['context'], entry['question'], entry['answer'])
        for entry in history
    ]
    return formatted_history

examples = [
    ["Tính đến tháng 6/2023, Vườn ươm Viện Đổi mới sáng tạo đã ươm tạo gần 100 dự án khởi nghiệp, trong đó có 19 dự án thành lập công ty, hơn 7600 người tham dự các hoạt động và tổng giá trị đầu tư mạo hiểm đạt 350.000 USD.", 
     "Tổng giá trị đầu tư mạo hiểm của Vườn ươm Viện Đổi mới sáng tạo là bao nhiêu?"]
]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            context = gr.Textbox(lines=7, placeholder="Enter the context here...", label="Context")
            question = gr.Textbox(placeholder="Enter your question here...", label="Question")
            answer = gr.Textbox(label="Answer")
            btn = gr.Button("Get Answer")
            btn.click(fn=answer_question, inputs=[context, question], outputs=answer)
            
        with gr.Column():
            chat_history = gr.Dataframe(headers=["ID", "Context", "Question", "Answer"], label="Chat History")
            btn_history = gr.Button("Load History")
            btn_history.click(fn=get_history, inputs=[], outputs=chat_history)

    gr.Examples(
        examples=examples,
        inputs=[context, question]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)