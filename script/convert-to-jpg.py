from PIL import Image
import os
import pathlib

for img_file in pathlib.Path('../datasets').glob('**/*.jfif'):
  path = os.path.splitext(img_file)[0]
  img = Image.open(img_file)
  
  img.save(path+".jpg",'JPEG', optimize=True, quality=70)
  os.remove(img_file)

for img_file in pathlib.Path('../datasets').glob('**/*.jpeg'):
  path = os.path.splitext(img_file)[0]
  img = Image.open(img_file)
  
  img.save(path+".jpg",'JPEG', optimize=True, quality=70)
  os.remove(img_file)
