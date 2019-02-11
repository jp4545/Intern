from PIL import Image
img_fle = "jp.jpg"
img = Image.open(img_fle)
print(img.size)