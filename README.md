# Digit-recognition-using-Neural-networks

## PROBLEM DEFINITION
Handwritten Digit Recognition is one of the most fundamental problems in designing practical
recognition system. Immediate applications of the digit recognition techniques include, address
code reading, vehicle’s number plate and bank check processing etc

**Steps:**  
1. Install requirements
```python
pip install -r requirements.txt
```
2. Predict the output
```python
python testing_input.py  
```

## Screenshots  
![GUI](1.PNG)  

![Enter a number](2.PNG)  

![Output](3.PNG)  

## OBJECTIVES
* To provide an easy user interface to input the object image.
* User should be able to save the image.
* System should be able to pre-process the given input to suppress the background.
* System should recognize digit present in the image and display them to the user.


#### Dataset: [MNIST](http://yann.lecun.com/exdb/mnist/)  
The MNIST problem is a dataset developed by Yann LeCun, Corinna Cortes and Christopher
Burges for evaluating machine learning models on the handwritten digit classification problem.

## Implementation
**Training**
1. Split the data set into a training set and a test set. Normally the training set is larger than the
test set. Often the desired outputs have to be normalized to the range [0: 1] since the sigmoid
function only returns values in this range. The input patterns do not have to be normalized.
2. Initialize all weights, including all biases if any, to small random values (normally in the range
of -1 to +1).
3. Forward propagation of the first input pattern of the training set from the input layer over the
hidden layer(s) to the output layer, where each neuron sums the weighted inputs, passes them
through the non-linearity and passes this weighted sum to the neurons in the next layer.
4. Calculation of the difference between the actual output of each output neuron and its
corresponding desired output. This is the error associated with each output neuron.
5. Back propagating this error through each connection by using the Backpropagation learning
rule and thus determining the amount each weight has to be changed in order to decrease the
error at the output layer.
6. Correcting each weight by its individual weight update.
7. Presenting and forward propagating the next input pattern. Repeat steps 3-7 until a certain
stopping criterion is reached, for example that the error falls below a predefined value. The one-
time presentation of the entire set of training patterns to the net constitutes a training epoch.

**Testing**  
1. After terminating the training phase the trained net is tested with new, unseen patterns from the
test data set.
2. The patterns are forward propagated, using the weights now available from training,
and the error at the output layer is determined (no weight-update is performed!). 
3. If performance is sufficiently good, the net is ready-for- use. If not, it has to be retrained with the same patterns
and parameters or something has to be changed (e.g. number of hidden neurons, additional input
patterns, different kinds of information contained in the input patterns).
4. It is also important that the net not be "over trained": if it is trained for too many epochs it starts "memorizing" the
training patterns and can no longer recognize patterns other than those it was explicitly trained for. 
5. This effect can be compared to the over fitting of a discretely sampled function. 
6. In summary the goal of training a neural network is that it is able to generalize. This means that it only
extracts some important features of the data and thus also classifies slightly differing patterns to
belong to the same class. This also provides robustness in the presence of noise

**Preprocessing**  
The purpose of preprocessing is to discard irrelevant information in the input data that can
negatively affect the recognition. This concerns speed and accuracy. Preprocessing usually
consists of scaling, binarization, normalization.

**Predication**  
The digit in the image is predicted and displayed.




