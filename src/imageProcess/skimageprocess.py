from skimage import io, transform, data, data_dir, color, exposure


def info():
    img = data.coffee()
    print(img.shape)
    # red 通道图层
    imgshow(img[:, :, 0])
    # green 通道图层
    imgshow(img[:, :, 1])
    # blue 通道图层
    imgshow(img[:, :, 2])
    # 裁剪图片
    imgshow(img[50:150, 50:150, :])
    # 遮罩图片
    copyImg = img.copy()
    rows, cols, channels = copyImg.shape
    for x in range(rows // 2):
        for y in range(cols // 2):
            copyImg[x, y, :] = 1
    imgshow(copyImg)


# transform使用
def transformUse():
    img = data.coffee()
    # 缩小图片
    img8080 = transform.resize(img, (80, 80))
    imgshow(img8080)
    # 缩小到原来的一半
    imgrescale = transform.rescale(img, 0.5)
    imgshow(imgrescale)
    # 逆时针旋转
    imgrotate = transform.rotate(img, 60)
    imgshow(imgrotate)
    # 高斯图片
    imgs = transform.pyramid_gaussian(img, downscale=2)
    for image in imgs:
        imgshow(image)


# 批处理图片
def batchProcess():
    def toGray(file):
        return color.rgb2gray(io.imread(file))

    images = io.ImageCollection(data_dir + "/*.png", load_func=toGray)
    print(len(images))
    for image in images:
        imgshow(image)


# color使用
def colorUse():
    img = data.coffee()
    imgshow(color.rgb2gray(img))
    imgshow(color.gray2rgb(color.rgb2gray(img)))


# exposure使用
def exposureUse():
    img = data.coffee()
    # 对比度调整
    imgshow(img)
    imgshow(exposure.adjust_gamma(img, 0.2))
    imgshow(exposure.adjust_gamma(img, 2))


def imgshow(img):
    io.imshow(img)
    io.show()


if __name__ == '__main__':
    # info()
    # transformUse()
    # batchProcess()
    # colorUse()
    exposureUse()
