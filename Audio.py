import pyttsx3
import PyPDF2
book = open('The-Secret-by-Rhonda-Byrne.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
n=int(input("Starting Page: "))
m=int(input("Ending Page: "))
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
for num in range(n,m):
    page = pdfReader.getPage(num)
    text = page.extractText()
    newVoiceRate = 110
    speaker.setProperty('rate', newVoiceRate)
    speaker.say(text)
    speaker.runAndWait()
    newVoiceRate = newVoiceRate + 50
    speaker.setProperty('rate', 125)
