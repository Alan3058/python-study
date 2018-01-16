import argparse

from skimage import io, color, transform

# 字符越多，体现的颜色更丰富
asciis = '@#$%&*OMWomwqxbnmkpPNBQTYULASDF()2345789ertyfdvcXCVPOYH{}!_+-=?/\|><,.`~:;" '


# 灰度转字符
def convertChar(gray):
    try:
        return asciis[int(gray * len(asciis)) - 1]
    except Exception as e:
        print(gray)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='file', default='zoro.jpg')
    args = parser.parse_args()
    fileName = args.file
    # 图片灰度化
    grayimg = color.rgb2gray(io.imread(fileName))
    # 图片缩放
    image = transform.resize(grayimg, output_shape=(int(grayimg.shape[0] * 80 / grayimg.shape[1]), 80))
    height, width = image.shape
    temp = ''
    for i in range(height):
        for j in range(width):
            temp += convertChar(image[i, j])
        temp = temp + "\n"
    print(temp)
    with open("output.txt", 'w') as f:
        f.write(temp)
