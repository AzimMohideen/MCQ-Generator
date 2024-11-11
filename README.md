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
## Usage
- Go to the upload page.
- Select a PDF file that contains text-based notes or content.
- Choose the grade level for which you want the questions to be generated.
- Submit the form to generate and view the questions along with the answer key.

## Project Structure

```
project-folder/
├── app.py                 # Main Flask app code
├── templates/
│   └── index.html         # HTML template for upload form and results
├── static/
│   └── css/
│       └── styles.css     # CSS file for styling
├── uploads/               # Folder for uploaded PDF files
├── README.md              # Project overview, setup, and usage
├── requirements.txt       # List of required packages
└── .
```
- app.py - Main Flask application logic.
- templates/index.html - HTML form for uploading PDF and viewing questions.
- static/css/styles.css - CSS styles for the web application.
- uploads/ - Stores uploaded PDF files.
- README.md - Project documentation.
- requirements.txt - Required packages.

## API Key Setup

Make sure you have a valid Google Generative AI API key and configure it in app.py. You can get an API key by visiting the following link 'https://ai.google.dev/gemini-api/docs/api-key'

## Example

![Logo](https://github.com/AzimMohideen/MCQ-Generator/blob/main/image.png)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
- @Chorko C
- @KRISHNASAKTHIESWAR
- @bhrahmesh

