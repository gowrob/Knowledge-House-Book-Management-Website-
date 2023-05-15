import pyttsx3         ##importing pyttsx3 package
import PyPDF2          ##importing PyPDF2 package

book = open('oop_python.pdf','rb')    ##opening the book in binary reading mode(REadable Binary)

pdf_reader = PyPDF2.PdfFileReader(book)    ##accessing the book with PyPDF2

number_of_pages = pdf_reader.numPages     ##finding out total number of pages


engine = pyttsx3.init()             ##initializing pyttsx3

for n in range (7,number_of_pages):
    page = pdf_reader.getPage(n)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()



