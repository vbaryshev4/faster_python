import numpy as np
import cv2 as cv
import urllib.request
from PIL import Image
import os
import shutil

face_cascade = cv.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def get_crops(vk_id, photos):
	
	result = []
	path = '/Users/vbaryshev/Documents/Computer_Science/Kirill/faster_python/homework/9/VisionLabs/{0}/photos/'.format(vk_id)
	
	try:
		os.makedirs(path)	
	except FileExistsError:
		shutil.rmtree(path, ignore_errors=True)
		return {'user': vk_id, 'crops': 0}

	for link in photos:
		photo = link.split('/')[-1]
		photo_address = "/Users/vbaryshev/Desktop/VisionLabs/{0}/photos/{1}".format(vk_id, photo)
		urllib.request.urlretrieve(link, photo_address)
		try:
			img = cv.imread(photo_address)
			gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray, 1.3, 4)
		except...:
			continue
		if not isinstance(faces, tuple):
			faces = [tuple(i) for i in faces]
			unique_crop_id = 0
			for face in faces:
				if unique_crop_id == 6:
					continue
				image = Image.open(photo_address)
				left = face[0]
				top = face[1]
				width = face[2]
				height = face[3]
				cropped_img = image.crop((left, top, left+width, top+height))
				if cropped_img.size[0] >= 50:
					crops_address = photo_address.replace('/photos', '')
					result.append({'crop':cropped_img, 'address': '{0}_{1}.jpg'.format(crops_address, unique_crop_id)})
					unique_crop_id += 1
	
	
	if len(result) == 0 or len(result) > 300:
		path = path.replace('/photos','') 
		shutil.rmtree(path, ignore_errors=True)
		return {'user': vk_id, 'crops': 0}
	
	else:
		for i in result:
			print(i, i['crop'], i['address'])
			i['crop'].save(i['address'], quality=100)
		shutil.rmtree(path, ignore_errors=True)
		return {'user': vk_id, 'crops': len(result)}
