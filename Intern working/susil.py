from PIL import Image
from pylab import *
pil = array(Image.open('jj.jpg'))
figure()
hist(pil.flatten(),128)
show()
