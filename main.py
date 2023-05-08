import pytesseract
from PIL import Image

# Screenshot to txt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Open image and extract text using pytesseract
image = Image.open("screenshot.png")
text = pytesseract.image_to_string(image)


# Write the text to a .txt file
with open("output.txt", "w") as f:
    f.write(text)
