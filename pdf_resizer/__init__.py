# This file is required to mark the pdf_resizer directory as a package.

# Import subpackages
from .gui import PDFResizerApp
from .resize import resize_pdf

# Define __all__ to specify which subpackages are exposed
__all__ = ['gui', 'resize']
