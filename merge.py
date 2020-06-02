from PIL import Image
import numpy as np
import wget

fg_image_url = str(input("Enter URL: "))
bg_image_url = fg_image_url.replace("png", "jpg")

fg_image = wget.download(fg_image_url)
bg_image = wget.download(bg_image_url)

img = Image.open(fg_image)
background = Image.open(bg_image)

background.paste(img, (0, 0), img)

out = str(input("Enter file name: "))
out = out+'.png'

background.save(out, "PNG")

image_for_pdf = Image.open(out)
im1 = image_for_pdf.convert('RGB')
pdf_out = out+'.pdf'
im1.save(pdf_out)

num_pages = num_pages-1
