from PIL import Image, ImageFilter

#checking the current working directory
# import os
# print(os.getcwd())

#the following reads the contents of the jpeg file
# with open("./ZTM/pokedex/Pokedex/pikachu.jpg", "rb") as img2:
#     print(img2)

#the following prints out the whole jpeg information and creates a representation of the image in memory
img = Image.open("./Pokedex/pikachu.jpg")
filtered_img = img.filter(ImageFilter.BLUR)

#turns picture into grey scale
filtered_img = img.convert("L")
filtered_img.save("./pokedex/grey.png")

#resizing
resize = filtered_img.resize((300,300))

#rotating
crooked = filtered_img.rotate(90)

#cropping
box = (100, 100, 400, 400) #needs to be a tuple
crop = filtered_img.crop(box)

#will pop a window to show image immediately
# filtered_img.show()
# crooked.show()
# resize.show()
crop.show()

#png supports all kinds of filter unlike jpeg

