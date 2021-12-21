# import PIL
# from PIL import Image
# from tkinter.filedialog import *

# # file_path=askopenfilenames()
# file_path=input()
# img = PIL.Image.open(file_path)
# myHeight,myWidth = img.size

# img=img.resize((myHeight,myWidth),PIL.Image.ANTIALIAS)
# save_path=asksaveasfile()

# img.save(save_path+"_compressed.JPG")


from PIL import Image
import os

path = input()
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if item == '.jpg':
            continue
        if os.path.isfile(path+item):
            image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)
            size = image.size

            new_image_height = 0.5
            new_image_width = int(size[1] / size[0] * new_image_height)
            print("Here")
            image = image.resize((new_image_height, new_image_width), Image.ANTIALIAS)
            image.save(file_path + "_small" + extension, 'JPEG', quality=90)

print("hHere")
resize()