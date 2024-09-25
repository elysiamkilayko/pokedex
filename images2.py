from PIL import Image, ImageFilter

img = Image.open("./ZTM/pokedex/sheep.jpg")
print(img.size)

img.thumbnail((400,1000)) #thumbnail modifies the original image and does not return a new image
img.save("./ZTM/pokedex/thumbnail.png")

# img.show()
print(img.size)