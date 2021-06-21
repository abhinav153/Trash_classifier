from flask import Flask,render_template,request,jsonify
import numpy as np
import cv2
import tensorflow as tf
import json


app = Flask(__name__)

def prediction(img,model):
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

@app.route('/')
def index_page():
	return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
	if request.method == "POST":
		#print('request data:',request.get_data())

		img_data = request.files['img']
		#print('image data:',type(img_data))
		#print('*****')
		#print('')


		#create byte string of img file
		img_byte_string = img_data.read()
		#print('type of data:',type(img_byte_string))
		#print('*****')
		#print('')

		#read byte string to form 1d array
		img_array = np.frombuffer(img_byte_string,dtype=np.uint8)
		#print("shape of array:",img_array.shape)
		#print(type(img_array))
		#print('*****')
		#print('')

		#ready array to form 3 dimensional array
		img = cv2.imdecode(img_array,cv2.IMREAD_COLOR)
		#print(img.shape)
		#print('*****')
		#print('')


		#display img
		#cv2.imshow("input image",img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

		
		#cv2.imshow("img",img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()


		#loading model net
		model_path = '../saved_models/MobileNetV2'
		model = tf.keras.models.load_model(model_path)
		#print(model)	

		class_predicted = prediction(img,model)
		data = {'class':class_predicted}

		return jsonify(data)

	


if __name__ == '__main__':
	app.run()