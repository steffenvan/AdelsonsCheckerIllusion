from PIL import Image
from resizeimage import resizeimage
import os

folder = "/home/besterma/ETH/Neural_Systems/AdelsonsCheckerIllusion/illusionApp/Screenshots/"
fileList = os.listdir(folder)
for file in (fileList):
    print(file)
    with open(os.path.join(folder, file), 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [500, 500])
            cover.save(os.path.join(folder, file), image.format)