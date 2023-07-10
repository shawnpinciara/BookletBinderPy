# import module
from pdf2image import convert_from_path
import math
from PIL import Image
import os

#pdf name
pdf_name = './src/Booklet.pdf'

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
    # imsave = Image.new('RGB', (im1.width, im1.height * 2))
    # images_concat.append(dst)
    # print(len(images_concat))
    # for i in range((int(len(images_concat)/2)) -1):
    #     images_concat_inverse.append(images_concat[i])
    #     images_concat_inverse.append(images_concat[len(images_concat)-i-1].rotate(180,expand=True))
    # images_concat = images_concat_inverse
    #END OF REVERSE OPTION   
    imsave = Image.new('RGB', (im1.width, im1.height * 2))
    imsave.save('concat.pdf', save_all=True, append_images=images_concat)

def single_booklet(images_array):
    final_images_arr = []
    for i in range(0,int(len(images_array)/2)):
        print(i)
        if i%2==0:
            im1 = images_array[i]
            im2 = images_array[len(images_array)-1-i]
        else:
            im2 = images_array[i]
            im1 = images_array[len(images_array)-1-i]
        dst = Image.new('RGB', (images_array[0].width, images_array[0].height * 2))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        dst.resize((595, 842))
        final_images_arr.append(dst)
    # print(final_images_arr)
    return final_images_arr

def booklet(pliques_len,total_pages_of_book):
    images_concat = []
    if total_pages_of_book % 10!=0:
        total_pages_of_book += 10-(total_pages_of_book%10)
    und = 0;
    while (und < total_pages_of_book):
        images = convert_from_path(pdf_path=pdf_name,first_page=und,last_page=und+10)
        images = [image.rotate(90,expand=True) for image in images]
        #int(len(images)/pliques_len)
        #TODO: gestire il caso in cui non è un multiplo di 10
        #SE le pagine finali sono meno di 10: aggiungi pagine bianche sino ad arrivare ad un multiplo di due
        ind = 0
        while(ind < 20):
            um = images[ind:ind+10] 
            ima = single_booklet(um)
            for im in ima:
                images_concat.append(im)
            ind += 10
        und+=10
    

    imsave = Image.new('RGB', (images[0].width, images[0].height * 2))
    imsave.save('concat.pdf', save_all=True, append_images=images_concat)



booklet(10,23)
#a4_to_2_a5()