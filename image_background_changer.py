from PIL import Image

img = Image.open('unnamed.png')
img = img.convert('RGB')

datas = img.getdata()

new_image_data = []
for item in datas:
    new_image_data.append(item)

    if item == (255, 255, 255):   #This is to change any color with white background
        new_image_data.append((128, 128, 128)) #to gray color
    else:
        new_image_data.append(item)

img.putdata(new_image_data)
img.save('new.png')
img.show()
                       
