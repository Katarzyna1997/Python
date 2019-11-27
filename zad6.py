import os
from PIL import Image

IMGS_DIR = 'obrazy'

images_names = os.listdir(IMGS_DIR)
for name in images_names:
    new_name = name.split('.')[0] + '.png'
    Image.open(os.path.join(IMGS_DIR, name))\
         .save(os.path.join(IMGS_DIR, new_name))
