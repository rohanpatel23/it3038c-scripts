# Lab 7

I also decided to use the plugin called Pillow for my Python Script.

To get started you first want to install Pillow
  
The command is
```  
pip install pillow 
```
You can now find any image you would like to edit, in my script I used a picture of a dog I found on google.

The line of code below is how you would make an image blackand white. The name of your image would go in the (pup1.jpg)

```
from PIL import Image
import os


#Black and White Image

image1 = Image.open('pup1.jpg')
image1.convert(mode='L').save('pup2_mod.jpg')
```
The code below is to make an image rotate 90 degress. 

```
from PIL import Image
import os

#To make a image rotate

#image1 = Image.open('pup1.jpg')
#image1.rotate(90).save('pup1_mod.jpg')
```

Finally to make a thumbnail and save it to a folder you can use a for loop to edit multiple pictures ending with jpg

```
from PIL import Image
import os

# For Thumbnail and making the Images 300 by 300 pixels
#size_300 = (300,300)

#for f in os.listdir('.'):
#  if f.endswith('.jpg'):
#    i = Image.open(f)
#    fn, fext = os.path.splitext(f)
    
#    i.thumbnail(size_300)
#    i.save('300/{}_300{}'.format(fn, fext))
```
