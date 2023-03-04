import tkinter as tk
from tkinter import filedialog
from resize import resize_pdf

class PDFResizerApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF Resizer")

        self.input_label = tk.Label(master, text="Select PDF file to resize:")
        self.input_label.pack()

        self.input_button = tk.Button(master, text="Choose file", command=self.select_input_file)
        self.input_button.pack()

        self.output_label = tk.Label(master, text="Save resized PDF as:")
        self.output_label.pack()

        self.output_button = tk.Button(master, text="Choose file", command=self.select_output_file)
        self.output_button.pack()

        self.resize_button = tk.Button(master, text="Resize PDF", command=self.resize_pdf)
        self.resize_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.input_file = None
        self.output_file = None

    def select_input_file(self):
        """Open a file dialog to select the input PDF file."""
        self.input_file = filedialog.askopenfilename(title="Select PDF file to resize")

    def select_output_file(self):
        """Open a file dialog to select the output PDF file."""
        self.output_file = filedialog.asksaveasfilename(title="Save resized PDF as",
                                                        defaultextension=".pdf")

    def resize_pdf(self):
        """Resize the PDF file and display the status message."""
        if self.input_file and self.output_file:
            resize_pdf(self.input_file, self.output_file)
            self.status_label.config(text="PDF successfully resized!")
        else:
            self.status_label.config(text="Please select input and output files.")

def main():
    root = tk.Tk()
    app = PDFResizerApp(root)
    root.mainloop()
