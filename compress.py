import io
import math
import sys
import numpy as np
from PIL import Image
from tkinter.filedialog import *

def compress_image(im, target):
   """Save the image as JPEG with the given name at best quality that makes less than "target" bytes"""
   # Min and Max quality
   Qmin, Qmax = 0, 96
   # Highest acceptable quality found
   Qacc = -1

   while Qmin <= Qmax:
      m = math.floor((Qmin + Qmax) / 2)

      # Encode into memory and get size
      buffer = io.BytesIO()
      im.save(buffer, format="JPEG", quality=m)
      s = str(buffer.getbuffer().nbytes)
      print(s)
      if s <= target:
         Qacc = m
         Qmin = m + 1
      elif s > target:
         Qmax = m - 1

   # Write to disk at the defined quality
   if Qacc > -1:

            im.save(f"Compressed_new.jpg", format="JPEG", quality=Qacc)
   else:
      print("ERROR: No acceptble quality factor found", file=sys.stderr)

# file=askopenfilename()
# im=Image.open(file)
# compress_image(im,500000)