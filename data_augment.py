'''
Run this file to augment the original image files , so that the new dataset is created which is bigger than 
original dataset
Bigger the dataset for neural nets better would the model run
'''

import glob
import cv2
import random
import numpy as np


def rotation(img, angle):
    angle = int(random.uniform(-angle, angle))
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), angle, 1)
    img = cv2.warpAffine(img, M, (w, h))
    return img
def brightness(img, low, high):
    value = random.uniform(low, high)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype = np.float64)
    hsv[:,:,1] = hsv[:,:,1]*value
    hsv[:,:,1][hsv[:,:,1]>255]  = 255
    hsv[:,:,2] = hsv[:,:,2]*value 
    hsv[:,:,2][hsv[:,:,2]>255]  = 255
    hsv = np.array(hsv, dtype = np.uint8)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return img

def vertical_flip(img, flag):
    if flag:
        return cv2.flip(img,0)
    else:
        return img
def horizontal_flip(img, flag):
    if flag:
        return cv2.flip(img,1)
    else:
        return img
def channel_shift(img, value):
    value = int(random.uniform(-value, value))
    img = img + value
    img[:,:,:][img[:,:,:]>255]  = 255
    img[:,:,:][img[:,:,:]<0]  = 0
    img = img.astype(np.uint8)
    return img

def fill(img, h, w):
    img = cv2.resize(img, (h, w), cv2.INTER_CUBIC)
    return img
        
def horizontal_shift(img, ratio=0.0):
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    w, h = img.shape[:2]
    to_shift = w*ratio
    if ratio > 0:
        img = img[:, :int(w-to_shift), :]
    if ratio < 0:
        img = img[:, int(-1*to_shift):, :]
    img = fill(img, h, w)
    return img

def vertical_shift(img, ratio=0.0):
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    w, h = img.shape[:2]
    to_shift = h*ratio
    if ratio > 0:
        img = img[:int(h-to_shift), :, :]
    if ratio < 0:
        img = img[int(-1*to_shift):, :, :]
    img = fill(img, h, w)
    return img


if __name__ == '__main__':
	'''
	for every image in each category we perform augment operations in the order
	1. Rotation
	2. Brightness
	3. Vertical Flip
	4. Horizontal Flip
	5. Channel Shift
	6. Horizontal Shift
	7. Vertical SHift
	'''
	categories = glob.glob('dataset/*')
	print('pls wait until the all augmentation operations are done')

	for category in categories:
		i=1
		save_file = 'dataset_augmented/'+category.split('/')[-1] +'/'+category.split('/')[-1]
		print('current category under processing:',save_file)
		image_paths = glob.glob(category+'/*')
		for image_path in image_paths:
			#print(image_path)
			img = cv2.imread(image_path)
			cv2.imwrite(save_file+'_'+str(i)+'.jpg',img)
			for operation in range(1,8):
				img_rotation = rotation(img,180)
				cv2.imwrite(save_file+'_'+str(i+1)+'.jpg',img_rotation)

				img_vertical_flip = vertical_flip(img,1)
				cv2.imwrite(save_file+'_'+str(i+2)+'.jpg',img_vertical_flip)

				img_horizontal_flip = horizontal_flip(img,1)
				cv2.imwrite(save_file+'_'+str(i+3)+'.jpg',img_horizontal_flip)

				img_channel_shift = channel_shift(img,100)
				cv2.imwrite(save_file+'_'+str(i+4)+'.jpg',img_channel_shift)

				img_horizontal_shift = horizontal_shift(img,0.5)
				cv2.imwrite(save_file+'_'+str(i+5)+'.jpg',img_horizontal_shift)

				img_vertical_shift = vertical_shift(img,0.4)
				cv2.imwrite(save_file+'_'+str(i+6)+'.jpg',img_vertical_shift)

			i+=7
	print('Done!!!!')
  	
     


    		       
    

