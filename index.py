from PyPDF2 import PdfFileReader, PdfFileWriter
from os.path import join
from tempfile import TemporaryDirectory
from pdf2image import convert_from_path # https://pypi.org/project/pdf2image/
from img2pdf import convert # https://pypi.org/project/img2pdf/

def convert_to_grayscale(path):
    with TemporaryDirectory() as temp_dir: # Saves images temporarily in disk rather than RAM to speed up parsing
        # Converting pages to images
        print("++++ Parsing pages to grayscale images. This may take a while +++++")
        images = convert_from_path(
            path,
            output_folder=temp_dir,
            grayscale=True,
            fmt="jpeg",
            thread_count=4
        )

        image_list = list()
        for page_number in range(1, len(images) + 1):
            path = join(temp_dir, "page_" + str(page_number) + ".jpeg")
            image_list.append(path)
            images[page_number-1].save(path, "JPEG") # (page_number - 1) because index starts from 0

        with open("Gray_PDF.pdf", "bw") as gray_pdf:
            gray_pdf.write(convert(image_list))


def rotate_pages(pdf_path, path_rotated, degrees):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file, strict=False)
        pdf_writer = PdfFileWriter()

        for page_num in range(pdf_reader.numPages):
            pdf_page = pdf_reader.getPage(page_num).rotateClockwise(degrees)
            pdf_writer.addPage(pdf_page)

        with open(path_rotated, "wb") as pdf_file_rotated:
            pdf_writer.write(pdf_file_rotated)

    convert_to_grayscale(path_rotated)

if __name__ == '__main__':
    path = 'showpdf.pdf'
    path_rotated = 'test_rotated.pdf'
    rotate_pages(path, path_rotated, 90)