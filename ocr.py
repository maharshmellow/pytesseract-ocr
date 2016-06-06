import pytesseract
from PIL import Image

# extract the text
textFromImage = pytesseract.image_to_string(Image.open("test.png"))

print(textFromImage)
