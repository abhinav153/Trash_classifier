# Trash_classifier
Classification of trash images using Convolutional Neural nets


## Prior Research Work
## Dataset used
> [Trashnet](https://github.com/garythung/trashnet)
## Papers

> 1.[Classification of trash for recyclability status](http://cs229.stanford.edu/proj2016/report/ThungYang-ClassificationOfTrashForRecyclabilityStatus-report.pdf)<br>
> 2.[Smart trashnet : Waste localization](http://cs229.stanford.edu/proj2017/final-reports/5226723.pdf)<br>
> 3.[Classification of trashnet based on deeo learning models](https://ieeexplore.ieee.org/document/8622212)<br>
> 4.[A novel framework for trash classification using deep learning](https://ieeexplore.ieee.org/document/8930948)<br>

## Models
Following models were mostly used for trash classification on Trashnet

> 1. Densenet121
> 2. ResNext-101
> 3. Xception
> 4. MobileNetV2
> 5. Inception V4
> 6. R-CNN

In this project i used a [MobileNetV2](https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4) from tensorflow hub for classification

## Preprocessing
Data was augmented using computer vision python package to expand the dataset size , so that a better model could be trained
Following augementation operations were done
> 1. Rotation
> 2. Vertical Flip
> 3. Horizontal Flip
> 4. Channel Shift
> 5. Horizontal Shift
> 6. Vertical Shift



In this project , using transfer learning i trained my augmented dataset, across all this networks, adding the a final fully connected layer for classification .
The classification labels include
> 1.Trash<br>
> 2.Plastic<br>
> 3.Metal<br>
> 4.Paper<br>
> 5.Cardboard

## Usage 
Step 1. Clone the repository<br>
Step 2: Ensure dependencies are installed as given in requirement.txt file or make a virtualenv<br>
Step 3: To run the model for prediction , copy your image files to the prediction_image folder, and run<br>
> python predict.py

## Files
**data_augment.py** - Uses the images in dataset folder , augments them and saves them in the data_augmented folder<br>
**trash_classifier_MobileNetV2.ipynb** - Builds the model , and saves it in the saved_models folder<br>
**predict.py** - Runs the model, and prints the predictions of the model on the images stored in prediction_images folder<br>


## References
> [Complete Image Augmentation in OpenCV](https://towardsdatascience.com/complete-image-augmentation-in-opencv-31a6b02694f5)<br>
> [Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)
