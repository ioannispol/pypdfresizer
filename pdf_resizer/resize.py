import PyPDF2

def resize_pdf(input_file, output_file):
    """Resize the PDF file by compressing its images."""

    # Create a PDF object from the input file
    pdf = PyPDF2.PdfFileReader(input_file)

    # Create a PDF writer object to save the output
    writer = PyPDF2.PdfFileWriter()

    # Loop over each page in the input PDF
    for page_num in range(pdf.getNumPages()):
        # Get the current page object
        page = pdf.getPage(page_num)

        # Compress any images on the page
        page.compressContentStreams()

        # Add the compressed page to the output PDF
        writer.addPage(page)

    # Write the output PDF to a file
    with open(output_file, "wb") as f:
        writer.write(f)
