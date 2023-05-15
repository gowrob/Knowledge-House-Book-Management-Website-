import pyttsx3                          ##importing pyttsx3 package

import PyPDF2                           ##importing PyPDF2 package

book = open('oop_python.pdf', 'rb')     ##opening the book in binary reading mode
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()