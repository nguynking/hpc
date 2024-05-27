import time
import gradio as gr
import requests

def answer_question(context, question):
    response = requests.post(
        "http://api:8000/answer", 
        json={"context": context, "question": question}
    )
    return response.json().get('answer', 'No answer returned')

def get_history(retries=5, delay=2):
    for i in range(retries):
        try:
            response = requests.get("http://api:8000/history")
            history = response.json()
            formatted_history = [
                (entry['id'], entry['context'], entry['question'], entry['answer'])
                for entry in history
            ]
            return formatted_history
        except requests.exceptions.ConnectionError:
            if i < retries - 1:
                time.sleep(delay)
                continue
            else:
                return []

def update_chat(context, question):
    answer = answer_question(context, question)
    history = get_history()
    formatted_history = ""
    for entry in history:
        formatted_history += f"""
        <div class="chat-message">
            <div class="chat-question">Q: {entry[2]}</div>
            <div class="chat-answer">A: {entry[3]}</div>
        </div>
        """
    return formatted_history

examples = [
    ["Tính đến tháng 6/2023, Vườn ươm Viện Đổi mới sáng tạo đã ươm tạo gần 100 dự án khởi nghiệp, trong đó có 19 dự án thành lập công ty, hơn 7600 người tham dự các hoạt động và tổng giá trị đầu tư mạo hiểm đạt 350.000 USD.", 
     "Tổng giá trị đầu tư mạo hiểm của Vườn ươm Viện Đổi mới sáng tạo là bao nhiêu?"],
    ["""Vị trí của UEH trên các Bảng xếp hạng trong nước và quốc tế:

Top 860 Đại học thế giới về Bền vững theo QS World University Ranking Sustainability 2024;

Top 301+ trong BXH các Trường Đại học tốt nhất Châu Á (Theo BXH QS châu Á) (2024);

Top 301 - 400 Đại học đóng góp cho 17 mục tiêu phát triển bền vững của Liên Hợp Quốc (Theo BXH THE Impact Ranking) (2023)

Top 01 trong các trường kinh tế, kinh doanh và luật và Top 7 trường đại học tốt nhất Việt Nam (Theo BXH Webometrics) (02/2023);

Top 298 trong BXH quốc tế các cơ sở nghiên cứu (SCImago) khu vực châu Á;

Top 05 trường đại học công bố quốc tế uy tín nhiều nhất Việt Nam (2020);

Top 01 trường đại học công bố quốc tế uy tín nhiều nhất Việt Nam trong lĩnh vực kinh tế, kinh doanh (2020);

Top 25 đại học tốt nhất thế giới đóng góp cho sự phát triển nghề nghiệp suốt đời (Theo BXH U-Multirank) (2016, 2017, 2018 2020);
Top 10 trường đại học công bố quốc tế uy tín nhiều nhất Việt Nam (2019);

Top 100 Trường đào tạo Thạc sĩ tốt nhất thế giới (Theo BXH Eduniversal) (2018);

Top 1000 Trường đào tạo kinh doanh tốt nhất thế giới (Theo BXH Eduniversal) từ năm 2014;

Thành tích của UEH và các tổ chức chính trị - xã hội trực thuộc UEH:

Huân chương Độc lập hạng Nhất năm 2021

Huân chương Độc lập hạng Nhì năm 2010

Danh hiệu Anh hùng Lao động năm 2006

Huân chương Độc lập hạng Ba năm 2001

Huân chương Lao động hạng Ba năm 2000 về thành tích đền ơn đáp nghĩa và công tác xã hội từ thiện

Huân chương Lao động hạng Nhất năm 1996 (cho 2 trường cũ: Đại học Kinh tế TP. Hồ Chí Minh và Đại học Tài chính - Kế toán TP.HCM)

Huân chương Lao động hạng Nhì năm 1991 (cho 2 trường cũ: Đại học Kinh tế TP. Hồ Chí Minh và Đại học Tài chính - Kế toán TP.HCM)

Huân chương Lao động hạng Ba năm 1986 (cho 2 trường cũ: Đại học Kinh tế TP. Hồ Chí Minh và Đại học Tài chính - Kế toán TP.HCM)

Huân chương Độc lập hạng Ba năm 2011 cho Công đoàn trường

Huân chương Lao động hạng Nhất năm 2006 cho Công đoàn trường

Huân chương Lao động hạng Nhì năm 2001 cho Công đoàn trường

Huân chương Lao động hạng Ba năm 1996 cho Công đoàn trường

Huân chương Lao động hạng Nhì năm 2003 cho Đoàn Thanh niên trường

Huân chương Lao động hạng Ba năm 1997 cho Đoàn Thanh niên trường

Huân chương Lao động hạng Ba năm 2006 cho Hội Sinh viên trường

Cờ thi đua Chính phủ năm 2020, tập thể đã hoàn thành xuất sắc nhiệm vụ công tác năm học 2019-2020, dẫn đầu phong trào thi đua yêu nước của Bộ Giáo dục và Đào tạo

Cờ thi đua Chính phủ năm 2016, đơn vị đã hoàn thành xuất sắc toàn diện nhiệm vụ công tác, dẫn đầu phong trào thi đua yêu nước năm 2015 của Bộ GD&ĐT

Cờ thi đua Chính phủ năm 2014, đơn vị đã hoàn thành xuất sắc toàn diện nhiệm vụ công tác, dẫn đầu phong trào thi đua yêu nước năm 2013 của Bộ GD&ĐT

Cờ thi đua Chính phủ năm 2011, đơn vị đã hoàn thành xuất sắc, toàn diện nhiệm vụ công tác, dẫn đầu phong trào thi đua yêu nước của ngành GD&ĐT năm học 2009-2010
Cờ "Đơn vị Tiên tiến xuất sắc" của Bộ GD&ĐT, đơn vị đạt thành tích xuất sắc tiêu biểu năm học 1999 - 2000

Cờ thi đua của Bộ Giáo dục và Đào tạo trong các năm 2008, 2010, 2013, 2014, 2015, 2016, 2017, 2018 về thành tích đơn vị xuất sắc tiêu biểu

Cờ thi đua Bộ Công an, đơn vị đã có thành tích trong phong trào toàn dân bảo vệ an ninh quốc phòng năm 2013

Cờ truyền thống của UBND TP. Hồ Chí Minh, đơn vị có thành tích xuất sắc trong việc đào tạo và phát triển nguồn nhân lực nhân kỷ niệm 25 năm thành lập (1976-2001), 30 năm thành lập (1976-2006), 35 năm thành lập (1976-2011) và 40 năm thành lập (1976-2016)

Danh hiệu Điển hình tiên tiến trong phong trào thi đua yêu nước ngành Giáo dục giai đoạn 2010-2015

Nhiều Bằng khen của Bộ GD&ĐT; Bộ Tài chính; Bộ Khoa học và Công nghệ; Bộ Văn hóa, Thể thao và Du lịch; Bộ Thông tin và Truyền thông; UBND TP. Hồ Chí Minh; các UBND tỉnh: Bà Rịa - Vũng Tàu, Bạc Liêu, Bến Tre, Bình Thuận, Cần Thơ, Đồng Nai, Đồng Tháp, Lâm Đồng, Phú Yên, Quảng Ngãi, Vĩnh Long cho đơn vị có thành tích xuất sắc trong công tác giảng dạy, nghiên cứu khoa học và chuyển giao công nghệ, đào tạo nguồn nhân lực …; hoạt động vì sự tiến bộ phụ nữ, phong trào văn hóa, văn nghệ, ký túc xá sinh viên đạt chuẩn văn hóa; công tác quân sự, an ninh quốc phòng, công tác sĩ quan biệt phái…

Thành tích của cá nhân và tập thể thuộc UEH:

03 cá nhân được Chủ tịch nước tặng Huân chương Lao động hạng Nhì

20 cá nhân được Chủ tịch nước tặng Huân chương Lao động hạng Ba

37 cá nhân và 11 tập thể được tặng Bằng khen của Thủ tướng Chính phủ

344 cá nhân và 98 tập thể được tặng Bằng khen của Bộ trưởng Bộ Giáo dục và Đào tạo

46 cá nhân và 3 tập thể được tặng Bằng khen của Bộ trưởng Bộ Tài chính

02 cá nhân được tặng Bằng khen của Bộ Công an

06 cá nhân được tặng Bằng khen của Bộ Thông tin và Truyền thông

102 cá nhân và 15 tập thể được tặng Bằng khen của UBND TP. Hồ Chí Minh

Ngoài ra, rất nhiều cá nhân của trường được trao tặng Huy chương và Kỷ niệm chương: “Vì sự nghiệp giáo dục”, “Vì sự nghiệp Tài chính Việt Nam”, “Vì sự nghiệp khoa học và công nghệ”, “Vì sự nghiệp xây dựng tổ chức Công đoàn”, “Vì thế hệ trẻ”, “Vì sự nghiệp ngành Tổ chức Nhà nước”, “Vì sự nghiệp báo chí Việt Nam”, “Bảo vệ An ninh Tổ quốc” …; Huy hiệu thành phố Hồ Chí Minh; Danh hiệu điển hình tiên tiến trong phong trào thi đua yêu nước ngành giáo dục.""",
 "UEH xếp hạng bao nhiêu theo QSRanking?"]
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

    # Load initial chat history when the interface loads
    initial_history = get_history()
    initial_chat = ""
    for entry in initial_history:
        initial_chat += f"""
        <div class="chat-message">
            <div class="chat-question">Q: {entry[2]}</div>
            <div class="chat-answer">A: {entry[3]}</div>
        </div>
        """
    
    if not initial_chat:
        initial_chat = "<div class='chat-message'><div class='chat-question'>No chat history available.</div></div>"

    chat_box.value = initial_chat

    submit_button.click(fn=update_chat, inputs=[context_input, question_input], outputs=chat_box)
    
    gr.Examples(
        examples=examples,
        inputs=[context_input, question_input],
        elem_id="examples"
    )

demo.launch(server_name="0.0.0.0", server_port=7860)