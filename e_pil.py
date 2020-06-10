#https://pillow.readthedocs.io/en/latest/

from PIL import Image

file="tom.png"
image=Image.open(file)
print(image)

import inspect
print("The type of the image is " + str(type(image)))
print(inspect.getmro(type(image)))
#image.show()


#copy
#image.save("msi_recruitment.png")
import PIL

from PIL import ImageFilter
image=image.convert('RGB') 
blurred_image=image.filter(PIL.ImageFilter.BLUR)
#blurred_image.show()
print("{}x{}".format(image.width, image.height))

#image.crop((0,0,190,150)).show()


from PIL import ImageDraw
drawing_object=ImageDraw.Draw(image)
#drawing_object.rectangle((50,0,190,150), fill = None, outline ='red')
#image.show()



from PIL import ImageEnhance
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(0, 10):
    images.append(enhancer.enhance(i/10))

#print(images)


first_image=images[0]
from PIL import Image
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width,10*first_image.height))

current_location = 0
for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (0, current_location) )
    # And update the current_location counter
    current_location=current_location+450

# This contact sheet has gotten big: 4,500 pixels tall! Lets just resize this sheet for display. We can do
# this using the resize() function. This function just takes a tuple of width and height, and we'll resize
# everything down to the size of just two individual images
contact_sheet = contact_sheet.resize((160,900) )
# Now lets just display that composite image
#contact_sheet.show()



contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

# Now, lets iterate over our images. Except, we don't want to both with the first one, because it is
# just solid black. Instead we want to just deal with the images after the first one, and that should
# give us nine in total
for img in images[1:]:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width


contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.show()