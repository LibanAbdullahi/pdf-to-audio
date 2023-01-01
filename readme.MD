# Convert PDF to Speech using Python

Learn how to convert a PDF file to speech using Python. We will be using three libraries: PyPDF3, pyttsx3, and pdfplumber.

- Prerequisites
  Before you begin, make sure you have the following libraries installed on your computer:

PyPDF3
pyttsx3
pdfplumber

- You can install these libraries using pip, the Python package manager. Simply open a terminal or command prompt and enter the following command:

pip install PyPDF3 pyttsx3 pdfplumber

# Steps

- Import the necessary libraries into your Python script.

import PyPDF3
import pyttsx3
import pdfplumber

- Specify the name of the PDF file that you want to read and convert to speech.

file = 'story.pdf'

- Open the PDF file in read-binary mode and create a PDF file reader object using PyPDF3.

book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

- Use the numPages attribute of the PDF file reader object to get the total number of pages in the PDF file.

pages = pdfReader.numPages
Create an empty string called finalText that will be used to store the text from all the pages of the PDF file.

finalText = ""

- Use pdfplumber to open the PDF file and iterate over each page in the file. For each page, extract the text using the extract_text() method and append it to the finalText string.

with pdfplumber.open(file) as pdf:
for i in range(0, pages):
page = pdf.pages[i]
text = page.extract_text()
finalText += text

- After you have extracted the text from all the pages, initialize the pyttsx3 engine and use the save_to_file() method to save the text as an MP3 file.

engine = pyttsx3.init()
engine.save_to_file(finalText, 'lorem.mp3')

Use the say() and runAndWait() methods of the pyttsx3 engine to speak the text out loud.

engine = pyttsx3.init()
engine.say(finalText)
engine.runAndWait()

# Conclusion

Congratulations! You have successfully converted a PDF file to speech using Python.

I hope you found this tutorial helpful.

If you have any questions or need further clarification, feel free to ask.

Thank you for following along!
