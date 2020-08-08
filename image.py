from PIL import Image, ImageFilter

import os, pathlib, sys

departure_folder = sys.argv[1]
destination_folder = sys.argv[2]
resize_height = sys.argv[3]
resize_width = sys.argv[4]

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(departure_folder):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{departure_folder}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it.
  resize = img.resize((int(resize_height),int(resize_width)))
  resize.save(f'{destination_folder}/{clean_name}.png', 'png')

  print('all done!')




