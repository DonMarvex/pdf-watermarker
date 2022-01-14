import PyPDF2

document = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(document.getNumPages()):
    page = document.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)


# Additional Notes
# Another method to open the file
# with open('wtr.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
