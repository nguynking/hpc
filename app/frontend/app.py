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
    gr.HTML("""
    <style>
    .container { max-width: 800px; margin: auto; padding: 20px; font-family: Arial, sans-serif; }
    .chat-box { border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin-bottom: 20px; height: 400px; overflow-y: auto; }
    .chat-input { margin-top: 10px; margin-bottom: 20px; }
    .chat-message { padding: 10px; border-bottom: 1px solid #eee; }
    .chat-message:last-child { border-bottom: none; }
    .chat-question { font-weight: bold; }
    .chat-answer { margin-top: 5px; }
    </style>
    """)
    
    gr.Markdown("""
    <div class="container">
        <h1>Question Answering Chat</h1>
        <p>Enter your question and context to get answers using our advanced model.</p>
    </div>
    """)
    
    chat_box = gr.HTML(value="<div id='chat-box-content'></div>", elem_id="chat-box")
    
    context_input = gr.Textbox(lines=5, placeholder="Enter the context here...", label="Context", elem_id="context")
    question_input = gr.Textbox(placeholder="Enter your question here...", label="Question", elem_id="question")
    submit_button = gr.Button("Send", elem_id="get-answer")

    def update_chat(context, question, current_chat):
        answer = answer_question(context, question)
        new_message = f"""
        <div class="chat-message">
            <div class="chat-question">Q: {question}</div>
            <div class="chat-answer">A: {answer}</div>
        </div>
        """
        updated_chat = current_chat + new_message
        return updated_chat
    
    submit_button.click(fn=update_chat, inputs=[context_input, question_input, chat_box], outputs=chat_box)
    
    gr.Examples(
        examples=examples,
        inputs=[context_input, question_input],
        elem_id="examples"
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
