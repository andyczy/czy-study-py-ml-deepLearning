# encoding:UTF-8
# czy study ocr

try:
    import pytesseract as pyact
    from PIL import Image
except ImportError:
    print("Import Error !") 
    raise  SystemExit

img=Image.open("e://c.png")
text= pyact.image_to_string(img)
print(text)