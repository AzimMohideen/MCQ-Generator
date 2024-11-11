import os
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import google.generativeai as genai
import re

# Define your Google API key here
GOOGLE_API_KEY = 'AIzaSyBAQPIeH0Zt-oiordrGN6hn_McKOlllu-A'

# Configure the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Instantiate the model
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files or 'grade' not in request.form:
            return 'No file or grade selected'
        
        file = request.files['file']
        grade = request.form['grade']
        
        if file.filename == '':
            return 'No selected file'

        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            pdf_text = read_pdf(file_path)
            questions_with_answers = generate_questions(pdf_text, grade)
            return render_template('index.html', pdf_text=pdf_text, questions_with_answers=questions_with_answers, selected_grade=grade)

    return render_template('index.html')

def read_pdf(file_path):
    pdf_text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            pdf_text += page.extract_text()
    return pdf_text

def generate_questions(text, grade):
    # Customize the prompt based on the selected grade
    if grade in ["7","8","9"]:
        base_prompt = (
            f"Create a set of Multiple Choice Questions (MCQs) for grade {grade} "
            f"based on the provided PDF, which includes notes from NCERT textbooks. "
            f"The questions should be of medium difficulty and cover a range of topics. "
            f"Each question should be clearly related to the material in the notes, with a focus on "
            f"comprehension and basic problem-solving skills. Additionally, provide the correct answers at the end:\n\n"
        )
    elif grade in ["10", "11", "12","University"]:
        base_prompt = (
            f"Create a set of Multiple Choice Questions (MCQs) for grade {grade} "
            f"based on the provided PDF, which includes notes from NCERT textbooks. "
            f"The questions should focus on real-time problems, critical thinking, and more complex MCQs. "
            f"These should include higher-level concepts, analytical reasoning, and application-based questions. "
            f"Also These questions need to be more complex and longer to understand with relative to the notes from the pdf(max 20 questions,min 12 questions)"
            f"Additionally, provide the correct answers at the end:\n\n"
        )
    else:
        base_prompt = (
            f"Create a set of Multiple Choice Questions (MCQs) for grade {grade} "
            f"based on the provided PDF, which includes notes from NCERT textbooks. "
            f"The questions should be appropriate for the selected grade level, covering basic to advanced topics as necessary. "
            f"Additionally, provide the correct answers at the end:\n\n"
        )
    
    response = model.generate_content(base_prompt + text)
    questions_with_answers = response.text.split("\n")  # Split the response into individual questions and answers
    return questions_with_answers

if __name__ == '__main__':
    app.run(debug=True)
