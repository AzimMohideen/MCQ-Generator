# PDF-Based MCQ Generator

This project is a Flask web application that generates grade-specific multiple-choice questions (MCQs) based on the contents of a PDF. It uses Google Generative AI's Gemini model to create questions with varying difficulty levels, depending on the selected grade.

## Features

- Upload a PDF and generate MCQs.
- Select from multiple grade levels (below grade 6 to university).
- MCQs are generated based on difficulty appropriate to the selected grade level.
- Integration with Google Generative AI's Gemini model.

## Installation

### Prerequisites

- Python 3.6+
- [Google Generative AI API Key](https://cloud.google.com/docs/authentication/api-keys)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2.Install the dependencies:
```
pip install -r requirements.txt
```
3.Configure your Google API key:
```
GOOGLE_API_KEY = 'your-google-api-key-here'
```
4.Run the application:
```
python app.py
```
