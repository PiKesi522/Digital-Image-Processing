from skimage import io       # 图像处理包pillow
import matplotlib.pyplot as plt    # 可视化窗口包

path = "C:\\Pics_Unit1\\BMP\\flower.bmp"

img_flower = io.imread(path)
# 参数为图像路径,读取图片

plt.imshow(img_flower)
plt.show()
# 展示画布


# 同理操作其他三张图片
path = "C:\\Pics_Unit1\\BMP\\boatssmall.bmp"
img_boats = io.imread(path)
path = "C:\\Pics_Unit1\\BMP\\fruits.bmp"
img_fruits = io.imread(path)
path = "C:\\Pics_Unit1\\BMP\\cornfield.bmp"
img_cornfield = io.imread(path)

plt.imshow(img_boats)
plt.show()
plt.imshow(img_fruits)
plt.show()
plt.imshow(img_cornfield)
plt.show()