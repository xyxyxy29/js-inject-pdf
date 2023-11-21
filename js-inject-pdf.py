import sys
from PyPDF2 import PdfWriter, PdfReader

def add_javascript(pdf_path, javascript_code, new_pdf_path):
    output = PdfWriter()
    ipdf = PdfReader(open(pdf_path, 'rb'))

    for i in range(len(ipdf.pages)):
        page = ipdf.pages[i]
        output.add_page(page)

    output.add_js(javascript_code)

    output_path = new_pdf_path
    with open(output_path, 'wb') as f:
        output.write(f)

    return output_path

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <pdf_path> <new_pdf_path> <javascript_code>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    new_pdf_path = sys.argv[2]
    javascript_code = sys.argv[3]

    output_path = add_javascript(pdf_path, javascript_code, new_pdf_path)
    print(f"Modified PDF saved to: {output_path}")
