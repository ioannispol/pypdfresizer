import PyPDF2
import tkinter as tk
from tkinter import filedialog

def resize_pdf():
    # Get input and output file names from the UI
    input_file = filedialog.askopenfilename(title="Select PDF file to resize")
    output_file = filedialog.asksaveasfilename(title="Save resized PDF as",
                                               defaultextension=".pdf")

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

    # Show message box indicating successful resize
    tk.messagebox.showinfo(title="PDF Resizer", message="PDF successfully resized!")

# Create UI window
root = tk.Tk()
root.title("PDF Resizer")

# Create UI elements
input_label = tk.Label(root, text="Select PDF file to resize:")
input_label.pack()

input_button = tk.Button(root, text="Choose file", command=resize_pdf)
input_button.pack()

output_label = tk.Label(root, text="Save resized PDF as:")
output_label.pack()

output_button = tk.Button(root, text="Choose file", command=resize_pdf)
output_button.pack()

resize_button = tk.Button(root, text="Resize PDF", command=resize_pdf)
resize_button.pack()

# Run UI loop
root.mainloop()
