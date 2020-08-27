## Project Topic:
Handwritten Digit Recognition Using Convolutional Neural Network (Deep Learning)

## Objective:
Nowdays, Convolutional Neural Networks (CNNs) have become an emergent topic in machine learning. It has lead its importance in various different applications such as music and speech recognition, image processing, and sentence classification to name a few. We need to achieve high accuracy rate close to human brain’s neural network, to gain high accuracy as close to 100% as possible and minimization of the error rate. Various techniques have been proposed over the years to achieve these goals.

## Dataset Description:
MNIST Dataset The MNIST dataset, a subset of a larger set NIST, is a database of 70,000 handwritten digits, divided into 60,000 training examples and 10,000 testing samples. The images in the MNIST dataset are present in form of an array consisting of 28x28 values representing an image along with their labels. This is also the same in case of the testing images.
The data is stored in four files:

train-images-idx3-ubyte: training set images
train-labels-idx1-ubyte:training set labels
t10k-images-idx3-ubyte: test set images
t10k-labels-idx1-ubyte: test set labels
MNIST Dataset Format Analysis As you can see from above, the MNIST data is provided in a specific format. So, to be able to read the dataset it is first important to know that in what format the data is available to us. Both the Training and Testing images and labels have the first two columns consisting of the “Magic Number” and the number of items in the file.The magic number has its first two bytes equal to zero. This magic number is read as MSB first.
