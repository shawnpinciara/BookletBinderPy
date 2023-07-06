# import module
from pdf2image import convert_from_path
import math
from PIL import Image
import os

#pdf name
pdf_name = 'DIY.pdf'

def a4_to_2_a5():
    images = convert_from_path(pdf_path=pdf_name,first_page=111+17,last_page=141+17)
    images = [image.rotate(-90,expand=True) for image in images]
    images_concat = []
    images_concat_inverse = []
    for i in range(len(images)-1):
        #TODO: sistemare in modo che vada di due in due
        if i%2==0:
            #print(i)
            im1 = images[i]
            im2 = images[i+1]
            dst = Image.new('RGB', (im1.width, im1.height * 2))
            dst.paste(im1, (0, 0))
            dst.paste(im2, (0, im1.height))
            dst.resize((595, 842))
            images_concat.append(dst)

    #reverse option
    imsave = Image.new('RGB', (im1.width, im1.height * 2))
    images_concat.append(dst)
    print(len(images_concat))
    for i in range((int(len(images_concat)/2)) -1):
        images_concat_inverse.append(images_concat[i])
        images_concat_inverse.append(images_concat[len(images_concat)-i-1].rotate(180,expand=True))
    images_concat = images_concat_inverse
    #END OF REVERSE OPTION
    
    imsave = Image.new('RGB', (im1.width, im1.height * 2))
    imsave.save('concat.pdf', save_all=True, append_images=images_concat)


a4_to_2_a5()