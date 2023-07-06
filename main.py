# import module
from pdf2image import convert_from_path
#import ffmpeg
import math
from PIL import Image
import os
#pdf name
pdf_name = 'test.pdf'

# from pdf to images
images = convert_from_path(pdf_name)
images = [image.rotate(-90,expand=True) for image in images]
images_concat = []
#creare dei pattern di riarrangiamento delle immagini
print(len(images))
for i in range(len(images)-1):
    #TODO: sistemare in modo che vada di due in due
    print(i)
    im1 = images[i]
    im2 = images[i+1]
    dst = Image.new('RGB', (im1.width, im1.height * 2))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    images_concat.append(dst)
    # dst.save(str(i)+'concat.jpg')
    # images[i].save('images_from_pdf/im'+ str(i) +'.jpg', 'JPEG')

# #images[0].save('im0.jpg', 'JPEG')
# #images[1].save('im1.jpg', 'JPEG')
# im1 = Image.open('im0.jpg').rotate(-90,expand=True).save('im1_r.jpg')
# im2 = Image.open('im1.jpg').rotate(-90,expand=True).save('im2_r.jpg')
# im1 = Image.open('im1_r.jpg')
# im2 = Image.open('im2_r.jpg')

# def get_concat_v(im1, im2):
#     dst = Image.new('RGB', (im1.width, im1.height * 2))
#     dst.paste(im1, (0, 0))
#     dst.paste(im2, (0, im1.height))
#     return dst

# get_concat_v(im1, im2).save('concat_v.jpg')
# #im1 = ffmpeg.input(images[0])
# #im2 = ffmpeg.input(images[1])
# #ffmpeg.filter([im1,im2],"scale=120:-1,tile=2x1").output("out.jpg").run()

# def a4_to_2_a5():
    
#     print('ok')