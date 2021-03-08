import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
book = open('<name of book>.pdf', 'rb') #enter name of pdf here
pdfReader = pyPDF.PdfFileReader(book)
for num in range(jo bhi number enter kia hai, pages):
    page =  pdfReader.getPage()#enter page number here from the pdf)
    text = page.extractText()#extracts text from page
    #put in whatever you want it to say at the start
    speaker.say('Hello this is SAROG')
    speaker.say(text)
    speaker.runAndWait()