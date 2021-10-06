import io
import pdfrw
from pdfrw import PdfReader

pdf = PdfReader('test.pdf')
print(pdf)