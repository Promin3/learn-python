from PIL import Image


def makesketch(img, threshold):
    w, h = img.size
    img = img.convert('L')  # 图像转化灰度模式
    pix = img.load()  # 获取像素矩阵
    for x in range(w - 1):
        for y in range(h - 1):
            if abs(pix[x, y] - pix[x + 1, y + 1]) >= threshold:
                pix[x, y] = 0
            else:
                pix[x, y] = 255
    return img


img = Image.open("whu.jpg")
img = makesketch(img, 35)
img.show()
