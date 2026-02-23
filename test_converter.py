from converter import images_to_pdf, text_to_pdf
from PIL import Image
import os

def create_dummy_image(filename):
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save(filename)

def create_dummy_text(filename):
    with open(filename, 'w') as f:
        f.write("Hello World\nThis is a test text file.")

def test_conversion():
    print("Setting up test files...")
    img_file = "test_image.jpg"
    txt_file = "test_text.txt"
    create_dummy_image(img_file)
    create_dummy_text(txt_file)

    print("Testing Image to PDF...")
    img_pdf = "output_image.pdf"
    success, msg = images_to_pdf([img_file], img_pdf)
    if success and os.path.exists(img_pdf):
        print("PASS: Image to PDF conversion successful.")
    else:
        print(f"FAIL: Image to PDF conversion failed. {msg}")

    print("Testing Text to PDF...")
    txt_pdf = "output_text.pdf"
    success, msg = text_to_pdf(txt_file, txt_pdf)
    if success and os.path.exists(txt_pdf):
        print("PASS: Text to PDF conversion successful.")
    else:
        print(f"FAIL: Text to PDF conversion failed. {msg}")

    # Cleanup
    print("Cleaning up...")
    try:
        os.remove(img_file)
        os.remove(txt_file)
        os.remove(img_pdf)
        os.remove(txt_pdf)
    except Exception as e:
        print(f"Cleanup warning: {e}")

if __name__ == "__main__":
    test_conversion()
