# MCQ Generator Application Using LangChain and HuggingFace Hub API

MCQ Generator with Streamlit is a web application that allows users to upload PDF or text files, specify the number of questions, subject, and tone, and generate multiple-choice questions (MCQs) based on the provided input. The application utilizes Hugging Face API open source language models for natural language processing and provides feedback on the complexity of the generated quiz.

**To run this application:**

* Download this repo and install prerequisite libraries using the command pip install -r requirements.txt
* Run the command streamlit run streamlitapp.py to run the application.
* P.S: You will need to provide your own HUGGING_FACE_TOKEN in the mcqGen.py file.

## Features
* **File Upload:** Users can upload PDF or text files containing the text from which MCQs will be generated.
* **Dynamic Inputs:** Users can specify the number of questions, subject, and tone for the generated MCQs.
* **Real-time Feedback:** Provides real-time feedback on the complexity of the generated quiz and suggests improvements.
* **Tabular Display:** Displays the generated MCQs in a tabular format for easy readability.

## Prerequisites
* Python 3.x
* Streamlit library
* Langchain library
* HUGGING_FACE_TOKEN

## Installation
1. Clone the repository:

   ` git clone https://github.com/4darsh-Dev/mcqgen.git `
    
   
2 Install the required dependencies:

   `pip install -r requirements.txt`

3. Set up environment variables:

    + Create a .env file in the root directory.

    + Add your OpenAI API key to the .env file:

        `HF_API_TOKEN=YOUR_TOKEN_HERE`
      
4. Install the local package in the virtual environment:

   `python setup.py install`

## Demo


COMING SOON...

## Usage

1. Run the Streamlit application:

   `streamlit run main.py`
2. Access the application in your web browser.

3. Upload a PDF or text file, specify the number of questions, subject, and tone, and click the "Create MCQs" button.

4. View the generated MCQs and the review feedback provided.

## Logging

* All logs are stored in the `logs` directory.
* Each log file is named with a timestamp indicating when it was created.

