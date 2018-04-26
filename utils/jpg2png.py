import os
import sys
from PIL import Image

filename = sys.argv[-1] 

im = Image.open(filename)
im.save(filename[:-3]+"png")
