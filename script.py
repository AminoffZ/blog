with open("public/tiff.tiff", "rb") as image:
  f = image.read()
  b = bytearray(f)
  print(' '.join(format(x, '02x') for x in b))
