from PIL import Image

img = Image.open("img.png")
w, h = img.size
newsize = (w // 2, h // 2)
newimg = img.resize(newsize)
newimg.save("halfimg.jpg")
newimg.thumbnail((128, 128))
newimg.save("_128img.png", "PNG")
newimg.show()
