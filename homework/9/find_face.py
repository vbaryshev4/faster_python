import cv2 as cv
import urllib.request
from PIL import Image
import os
import shutil

face_cascade = cv.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def crop_and_save(photo, where_to_save):
    crops_count = len(photo['faces_cords'])
    unique_crop_id = 1
    for cord in photo['faces_cords']:
        image = Image.open(photo['address'])
        left = cord[0]
        top = cord[1]
        width = cord[2]
        height = cord[3]
        cropped_img = image.crop((left, top, left + width, top + height))
        if cropped_img.size[0] >= 50:
            cropped_img.save(
                where_to_save + photo['photo_name'] + '__' + str(unique_crop_id) + '.' + photo['photo_format'],
                quality=85
                )
            if unique_crop_id < crops_count:
                unique_crop_id += 1

    return unique_crop_id


def get_faces(raw_photo_address):
    img = cv.imread(raw_photo_address)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_cords = face_cascade.detectMultiScale(gray, 1.3, 4)
    return faces_cords


def save_photo(link, raw_photo_address, photo_name):
    raw_photo_address = raw_photo_address + photo_name
    urllib.request.urlretrieve(link, raw_photo_address)
    return {
        'address': raw_photo_address,
        'faces_cords': None,
        'photo_name': photo_name.split('.')[0],
        'photo_format': photo_name.split('.')[1]
        }


def get_crops(user_and_links):
    vk_id = str(user_and_links[0])
    photos = user_and_links[1]
    root = '/Users/vbaryshev/Documents/Computer_Science/Kirill/faster_python/homework/9/VisionLabs/'
    crops = '/Users/vbaryshev/Documents/Computer_Science/Kirill/faster_python/homework/9/VisionLabs/{0}/'.format(vk_id)
    dump = '/Users/vbaryshev/Documents/Computer_Science/Kirill/faster_python/homework/9/VisionLabs/{0}/Photos/'.format(vk_id)
    adresses = {'root': root, 'photos': dump, 'crops': crops}

    if vk_id in os.listdir(adresses['root']):
        shutil.rmtree(adresses['crops'], ignore_errors=True)
    os.makedirs(adresses['photos'])


    saved_photos = [] # Контейнер с адресами фото и координатами кропов
    # Сохраняем фото на диск
    for link in photos:
        photo_name = link.split('/')[-1]
        try:
            result = save_photo(link, adresses['photos'], photo_name)
            saved_photos.append(result)
        except:
            continue

    # Читаем фото и определяем области кропов
    for foto in saved_photos:
        faces_cords = get_faces(foto['address'])
        if not isinstance(faces_cords, tuple):
            faces_cords = [tuple(i) for i in faces_cords]
            if len(faces_cords) > 5:
                faces_cords = faces_cords[0:5] # Сохраняем координаты первых пяти кропов
        foto.update({'faces_cords': faces_cords})

    # Сохраняем кропнутые фото
    photos_cropped_n_saved = 0
    for foto in saved_photos:
        if not isinstance(foto['faces_cords'], tuple):
            count = crop_and_save(foto, adresses['crops'])
            photos_cropped_n_saved += count

    # Удаляем папку с исходными фото, если кропов нет, то всю пользовательскую папку
    if photos_cropped_n_saved == 0:
        shutil.rmtree(adresses['crops'], ignore_errors=True)
    shutil.rmtree(adresses['photos'], ignore_errors=True)

    return {'user': vk_id, 'crops': photos_cropped_n_saved}


if __name__ == '__main__':
    vk_id = 6062193
    photos_links = ['https://pp.userapi.com/c633520/v633520193/16d65/mJ0AV4b2DJU.jpg', 'https://pp.userapi.com/3h2DB6f5P9g5YOMzo9CYwvk2x5KpZ539PMzGNg/LtuZRq6H8qM.jpg', 'https://pp.userapi.com/c617230/v617230193/322e/Y5RED45gvc8.jpg', 'https://pp.userapi.com/dfEdptxgU-MLLMDGerxbZbH4o49wMDKOHk7ZhA/MF2_yELk5bQ.jpg', 'https://pp.userapi.com/c625317/v625317193/1cc8c/XKi1cbY0OoU.jpg', 'https://pp.userapi.com/c625317/v625317193/1cc93/oQsw68Hy_co.jpg', 'https://pp.userapi.com/c625317/v625317193/1cc9d/dXqG3gUW5cg.jpg', 'https://pp.userapi.com/c631119/v631119193/42b12/0KTPgBQh7OQ.jpg', 'https://pp.userapi.com/c313326/v313326193/af4d/M3W9jDfvEbU.jpg', 'https://pp.userapi.com/c313326/v313326193/af54/zql7gJGaBiE.jpg', 'https://pp.userapi.com/c313326/v313326193/af5b/bwceEx0rCUA.jpg', 'https://pp.userapi.com/c313326/v313326193/af62/vT55BbSXVjE.jpg', 'https://pp.userapi.com/c313326/v313326193/af9a/6VRKRkTA_zc.jpg', 'https://pp.userapi.com/c608531/v608531193/4918/ftynLy5nh8A.jpg', 'https://pp.userapi.com/c608531/v608531193/491f/EJrNBT82q0I.jpg', 'https://pp.userapi.com/c614617/v614617193/106b1/FAeAkHKJCK4.jpg', 'https://pp.userapi.com/c614617/v614617193/11a02/djlTF8cjbqE.jpg', 'https://pp.userapi.com/c631119/v631119193/42b1b/7GcYnPmAqTQ.jpg', 'https://pp.userapi.com/c631119/v631119193/42b24/I4HooGUcLZk.jpg', 'https://pp.userapi.com/c320631/v320631193/4864/my2thuWW7dE.jpg', 'https://pp.userapi.com/c320631/v320631193/4882/-7KtnhMON40.jpg', 'https://pp.userapi.com/wDuzAHwdN0z7Gz6a5x9qW-Ubjjv7N32olMj7qQ/5AYrS7CTQuM.jpg', 'https://pp.userapi.com/SwYlhNDdmEG0tPxQEvKCiS8f2-xVNGUICixs2A/rVo8kGJakZ0.jpg', 'https://pp.userapi.com/c312531/v312531193/81a6/0aIGAQGp94I.jpg', 'https://pp.userapi.com/c313326/v313326193/aece/Q5THnTidJRI.jpg', 'https://pp.userapi.com/c313326/v313326193/aeec/Y5VTgdavfwA.jpg', 'https://pp.userapi.com/c313326/v313326193/aef6/bRGHEgIXFrE.jpg', 'https://pp.userapi.com/c313326/v313326193/af00/FNoT9VcCyZQ.jpg', 'https://pp.userapi.com/c313326/v313326193/af27/sgM6_Balr4Y.jpg', 'https://pp.userapi.com/c617230/v617230193/338e/PFD9b_Yj9CU.jpg', 'https://pp.userapi.com/c617230/v617230193/3398/R3IIzagInEQ.jpg', 'https://pp.userapi.com/c617624/v617624193/6945/rGlR1PHTFl0.jpg', 'https://pp.userapi.com/c617624/v617624193/694f/cWp-0692WdQ.jpg', 'https://pp.userapi.com/c617624/v617624193/6958/ti0yutl4jB8.jpg']
    result = get_crops(vk_id, photos_links)
    print(result)
