from PIL import Image
import os


image1 = Image.open('pup1.jpg')
image1.convert(mode='L').save('pup2_mod.jpg')



#To make a image rotate

#image1 = Image.open('pup1.jpg')
#image1.rotate(90).save('pup1_mod.jpg')


# For Thumbnail and making the Images 300 by 300 pixels
#size_300 = (300,300)

#for f in os.listdir('.'):
#  if f.endswith('.jpg'):
#    i = Image.open(f)
#    fn, fext = os.path.splitext(f)
    
#    i.thumbnail(size_300)
#    i.save('300/{}_300{}'.format(fn, fext))




