# import required module
from PIL import Image
from PIL import ImageEnhance
import os
 
# assign directory
directory = os.getcwd()
 
# iterate over files in that directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        #print(os.path.join(root, filename))
        f_name = os.path.join(root, filename)
        if filename.endswith(('.png', '.tga')):
            img = Image.open(f_name)
            img2 = img.convert("RGBA")
            converter = ImageEnhance.Color(img2)
            img3 = converter.enhance(1.35)
            converter2 = ImageEnhance.Brightness(img3)
            img4 = converter2.enhance(1.1)
            img4.save(f_name)