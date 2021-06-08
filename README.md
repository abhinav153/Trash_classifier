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

## Preprocessing
Data was augmented using computer vision python package to expand the dataset size , so that a better model could be trained
Following augementation operations were done
> 1. Rotation
> 2. Brightness
> 3. Vertical Flip
> 4. Horizontal Flip
> 5. Channel Shift
> 6. Horizontal Shift
> 7. Vertical Shift

## Models
Following modesl were mostly used for trash classification on Trashnet
Convolutional nets used so far
> 1>Densenet121
> 2>ResNext-101
> 3>Xception
> 4>MobileNet
> 5>Inception V4
> 6> R-CNN

In this project , using transfer learning i trained my augmented dataset, across all this networks, adding the same set of fully connected layers across all networks .
Using these networks as a ensemble , predictions for class of image will be made, and the model parameters would be tuned for best accuracy.


## References
> [Complete Image Augmentation in OpenCV](https://towardsdatascience.com/complete-image-augmentation-in-opencv-31a6b02694f5)
