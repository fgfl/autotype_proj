import pdfminer.pdfparser as PDFPaser
import pdfminer.pdfdocument as PDFDocument
import pdfminer.pdfpage as PDFPage
import pdfminer.pdfpage as PDFTextExtractionNotAllowed
import pdfminer.pdfinterp as PDFResourceManager
import pdfminer.pdfinterp as PDFPageInterpreter
import pdfminer.pdfdevice as PDFDevice

f_name = 'test.pdf'

# Open a PDF file.
fp = open('test.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser, password)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
device = PDFDevice(rsrcmgr)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)



