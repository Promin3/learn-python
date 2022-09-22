from PIL import Image
from PIL import ImageFilter

img = Image.open("whu.jpg")
print(img.format, img.mode)
newimg = img.rotate(90, expand=True)
newimg.show()
newimg = img.transpose(Image.FLIP_LEFT_RIGHT)
newimg = img.transpose(Image.FLIP_TOP_BOTTOM)
newimg = img.filter(ImageFilter.EMBOSS)  # 浮雕效果
newimg.show()
newimg = img.filter(ImageFilter.BLUR)  # 模糊效果
newimg.show()
newimg = img.filter(ImageFilter.CONTOUR)  # 轮廓效果
newimg.show()
newimg = img.filter(ImageFilter.EDGE_ENHANCE)  # 边框增强
newimg.show()
newimg = img.filter(ImageFilter.SMOOTH)  # 平滑效果
newimg.show()
