import sys
import argparse
import tkinter as tk
from gui import PDFResizerApp
from resize import resize_pdf

def parse_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description="Resize a PDF file.")
    parser.add_argument("input_file", help="the input PDF file")
    parser.add_argument("output_file", help="the output PDF file")
    return parser.parse_args()

def main():
    # Parse the command line arguments
    args = parse_args()

    # Resize the PDF file
    resize_pdf(args.input_file, args.output_file)

if __name__ == "__main__":
    # Run the GUI if no command line arguments are provided
    if len(sys.argv) == 1:
        root = tk.Tk()
        app = PDFResizerApp(root)
        root.mainloop()
    # Otherwise, run the command line interface
    else:
        main()
