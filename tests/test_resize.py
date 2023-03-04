import os
import tempfile
import unittest
from pdf_resizer.resize import resize_pdf

class TestResizePDF(unittest.TestCase):
    def test_resize_pdf(self):
        # Create a temporary input file
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_input:
            tmp_input.write(b"Hello, World!")
            tmp_input.flush()

            # Create a temporary output file
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_output:
                # Resize the PDF file
                resize_pdf(tmp_input.name, tmp_output.name)

                # Check that the output file exists
                self.assertTrue(os.path.exists(tmp_output.name))

                # Check that the output file is not empty
                self.assertGreater(os.path.getsize(tmp_output.name), 0)

                # Check that the output file is smaller than the input file
                self.assertLess(os.path.getsize(tmp_output.name), os.path.getsize(tmp_input.name))

            # Delete the output file
            os.remove(tmp_output.name)

        # Delete the input file
        os.remove(tmp_input.name)

if __name__ == "__main__":
    unittest.main()
