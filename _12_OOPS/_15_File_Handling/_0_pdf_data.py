import PyPDF2
pdfFileObj = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("Pages:", pdfReader.numPages)

for p_no in range(0, pdfReader.numPages):
    print("****** Content of Page ******:", p_no)
    p_data = pdfReader.getPage(p_no)
    # algorithm
    print("Content: ", p_data.extractText())
pdfFileObj.close()