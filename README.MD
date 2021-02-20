pip install PyPDF2
pip install tempfile

pip install pdf2image
Mac users will have to install poppler for Mac. (http://macappstore.org/poppler/)

pip install img2pdf

from PyPDF2 import PdfFileReader, PdfFileWriter
from os.path import join
from tempfile import TemporaryDirectory
from pdf2image import convert_from_path # https://pypi.org/project/pdf2image/
from img2pdf import convert # https://pypi.org/project/img2pdf/

# put here your pdf to convert to horizontal and grayscale

#### Example: showpd.pdf

run:

python index.py

then this will create 2 files

- test_rotated.pdf (file rotated with original color)
- Gray_PDF.pdf (file rotated with gray scale)
