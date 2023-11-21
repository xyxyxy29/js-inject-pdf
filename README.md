# js-inject-pdf

This Python script leverages the PyPDF2 library to add custom JavaScript code to an existing PDF file. The purpose of this tool is to enable users to embed JavaScript functionality into PDF documents, enhancing interactivity and automation within the PDF environment.

## Usage
To use the script, follow the command-line syntax below:

```bash
python script.py <pdf_path> <new_pdf_path> <javascript_code>
<pdf_path>: Path to the input PDF file.
<new_pdf_path>: Path to the output PDF file with injected JavaScript.
<javascript_code>: The JavaScript code to be added to the PDF.
```

Example
```bash
python script.py input.pdf output.pdf "app.alert('Hello, PDF!');"
```

## Dependencies
Make sure you have the required Python libraries installed:

`pip install PyPDF2`

## Notes
This script uses PyPDF2 to manipulate PDF files.
Ensure that the provided JavaScript code is compatible with PDF standards.
The modified PDF will be saved to the specified <new_pdf_path>.

## Disclaimer
Use this tool responsibly and respect legal and ethical guidelines when adding JavaScript to PDF files. Be aware that not all PDF viewers support JavaScript, and the behavior may vary across different platforms.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the PyPDF2 developers for their library.
