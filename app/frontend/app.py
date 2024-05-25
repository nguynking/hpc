import gradio as gr
import requests

def answer_question(context, question):
    response = requests.post(
        "http://api:8000/answer", 
        json={"context": context, "question": question}
    )
    return response.json().get('answer', 'No answer returned')

examples = [
    ["Tính đến tháng 6/2023, Vườn ươm Viện Đổi mới sáng tạo đã ươm tạo gần 100 dự án khởi nghiệp, trong đó có 19 dự án thành lập công ty, hơn 7600 người tham dự các hoạt động và tổng giá trị đầu tư mạo hiểm đạt 350.000 USD.", 
     "Tổng giá trị đầu tư mạo hiểm của Vườn ươm Viện Đổi mới sáng tạo là bao nhiêu?"]
]

iface = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Textbox(lines=7, placeholder="Enter the context here...", label="Context"),
        gr.Textbox(placeholder="Enter your question here...", label="Question")
    ],
    outputs=gr.Textbox(label="Answer"),
    title='UEH-QA',
    description='Creating safe AGI that benefits all of humanity.',
    examples=examples
)

iface.launch(server_name="0.0.0.0", server_port=7860)