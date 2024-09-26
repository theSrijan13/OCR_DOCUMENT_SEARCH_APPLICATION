# OCR Web Application for English and Hindi Text
This web application allows users to upload an image containing both English and Hindi text, performs Optical Character Recognition (OCR) on the image, and displays the extracted text. The app is built using Streamlit and uses the EasyOCR library for text extraction.

## Features
Upload an image in .jpg, .jpeg, or .png format.
Extract text from the image, supporting both Hindi and English.
Display the extracted text in the browser.

## Demo
You can try the live demo here.

## Setup Instructions
1. Prerequisites
Before running the app locally, ensure you have the following installed:

Python 3.7+
pip (Python package manager)
2. Clone the Repository
First, clone the repository to your local machine:

git clone https://github.com/yourusername/ocr-app.git
cd ocr-app

3. Create a Virtual Environment (optional but recommended)
To avoid conflicts with other projects, create and activate a virtual environment:

## Create a virtual environment
python -m venv venv

## Activate the virtual environment (Windows)
venv\Scripts\activate

## Activate the virtual environment (macOS/Linux)
source venv/bin/activate
4. Install Dependencies
Install all the required Python libraries by running the following command:

pip install -r requirements.txt
If you need to generate the requirements.txt file manually, you can run:

pip freeze > requirements.txt

Running the Web Application Locally
Once all dependencies are installed, you can start the Streamlit app by running:

streamlit run app.py
This will open a new tab in your default web browser with the URL:

https://ocrdocumentsearchapplication-jmsefdbnjrg99fnufjnqrx.streamlit.app/
From there, you can upload an image and see the extracted text.

## Deployment to Streamlit Cloud
You can easily deploy the app to Streamlit Cloud to make it accessible online.

1. Prepare the Project for Deployment
Ensure your repository contains the following files:

app.py: The main script for your Streamlit app.
requirements.txt: The list of required Python libraries (as mentioned earlier).
README.md: This file for documentation (optional but recommended).

2. Push Your Code to GitHub
If you haven’t already, push your code to GitHub:
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/ocr-app.git
git push -u origin main
3. Deploy to Streamlit Cloud
Go to Streamlit Cloud.
Sign in with your GitHub account.
Click New App.
Select the repository where your project is stored.
Choose the branch (main) and select the Python file (app.py).
Click Deploy.
Once deployed, you’ll be given a URL where the app is live and accessible to anyone.

4. Post-Deployment
After deploying, you can share the live URL with others to try the OCR app.

## Technologies Used
Streamlit: Web framework to build the UI and serve the application.
EasyOCR: Library for performing Optical Character Recognition (OCR).
Pillow: Python Imaging Library for image processing.
Numpy: For image format conversion to numpy arrays.

## Troubleshooting
Image Not Loading Properly: Ensure the uploaded image is in .jpg, .jpeg, or .png format.
OCR Accuracy: The accuracy of the OCR depends on the quality of the image and the fonts used in the text. Ensure the image is clear for better results.

