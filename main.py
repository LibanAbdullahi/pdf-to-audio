import PyPDF3
import pyttsx3
import pdfplumber

file = 'eng.pdf'


book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)


pages = pdfReader.numPages


finalText = ""


with pdfplumber.open(file) as pdf:
    for i in range(pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

        engine = pyttsx3.init()
        engine.save_to_file(finalText, 'test.mp3')

        engine = pyttsx3.init()
        engine.runAndWait()
