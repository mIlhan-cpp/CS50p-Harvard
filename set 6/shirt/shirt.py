import sys
from PIL import Image,ImageOps
import os

if len(sys.argv)>3:
    sys.exit('too many args')
elif len(sys.argv)<3:
    sys.exit('too few args')
else:
    _, ext1 = os.path.splitext(sys.argv[1])
    _, ext2 = os.path.splitext(sys.argv[2])
    if ext1==ext2 :
            try:
                shirt = Image.open("shirt.png")
                photo=Image.open(sys.argv[1])
                photo = ImageOps.fit(photo, shirt.size)
                photo.paste(shirt,box=(0,0) , mask=shirt)
                photo.save(sys.argv[2],format=None)
            except FileNotFoundError:
                sys.exit("File invalid")
    else:
        sys.exit('Input and output have different extensions')