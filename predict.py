import tensorflow as tf
import cv2

def prediction(img):
	#rescaling image
	img = img/255

	#converting to tensor
	tensor_img = tf.convert_to_tensor(img,dtype=tf.float32)

	#resizing image
	tensor_img = tf.image.resize(tensor_img,[224,224])
	tensor_img = tensor_img[tf.newaxis,...,]

	class_names = ['cardboard','metal','paper','plastic','trash']

	#predicting image
	return class_names[model.predict(tensor_img).argmax()]


if __name__ == '__main__':


	#loading model net
	model_path = 'saved_models/MobileNetV2'
	model = tf.keras.models.load_model(model_path)	

	#loading image
	image_path = 'dataset_augmented/plastic/plastic_10.jpg'
	img = cv2.imread(image_path)

	#predicting image
	print(prediction(img))
	