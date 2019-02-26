# ITTTS-Image-To-Text-To-Speech
This is a project for helping the people who are visually challenging. The OCR will help to recognize the character from an image with back ground with the help of Auto Encoder algorithm, then it will speech out the content
The project is to convert the image to speech. An image is processed and segmented to identify the characters in the image. Then the characters are combined to form words and save it as a text file. This text file is converted to speech. We have divided the project into four sub parts : image is pre-processed, segmented to extract the images of characters, then characters are recognized and combined , then the text is translated then converted into speech.
Language translation: For language translation, we used model built on RNN (Recurrent Neural Network). As the final model, we used encoder- decoder implemented with the help Embedding layer as the top most layer and then the accuracy was enhanced using Bidirectional LSTM.

Image to text: For image to text, we used CNN (Convoluted Neural Network).
Through the results we analyzed that our model was highly biased. Thus, we used tanh with Leaky Relu as our activation function. Our model comprised of 3 Fully convoluted layers, then 2 hidden layers and then a softmax for classifying 62 classes.

We have used the following architectures 

Image to text

Convolution 2d: This layer creates a convolution kernel that is covolved with the layer input to produce a tensor of outputs. If use_bias is true, a bias vector is created and added to the outputs. Finally, if activation is not Non, it is applied to the outputs as well.
 
Max Pooling: This is a form of non-linear down-sampling. There are several non-linear functions to implement pooling among which max pooling is the most common. It partitions the input image into a set of non-overlapping rectangles and, for each such sub-region, outputs the maximum.


Activation Function (Tanh, Relu, Sigmoid, Leaky Relu): We have used the combination of Leaky Relu and Tanh because our model was very highly biased.

Flatten: We need to convert the output of the convolutional part of the CNN into a 1D feature vector, to be used by the ANN part of it. This operation is called flattening. It gets the output of the convolutional layers, flattens all its structure to create a single long feature vector to be used by the dense layer for the final classification.


Page no :6
Dropout: It is a regularization technique for reducing overfitting in neural networks by preventing complex co-adaptations on training data. It is a very efficient way of performing model averaging with neural networks. The term "dropout" refers to dropping out units (both hidden and visible) in a neural network. 

Character Segmentation
C# (.exe): In c# we have made an exe file to segment the characters

Language Translation 

LSTM:  LSTMs are explicitly designed to avoid the long-term dependency problem.
GRU: Gated recurrent units (GRUs) are a gating mechanism in recurrent neural networks and their performance on polyphonic music modeling and speech signal modeling was found to be similar to that of long short-term memory (LSTM).

Bi-directional RNN: BRNNs were introduced to increase the amount of input information available to the network but have limitations on the input data flexibility, as they require their input data to be fixed.

Embedding layer: embedding layers can be used to embed many more things than just words.

Encoder and Decoder: The encoder-decoder architecture for recurrent neural networks is the standard neural machine translation method that rivals and, in some cases, outperforms classical statistical machine translation methods.

Text to Speech

GTTS: This is google-text-to-speech which is used to convert the text to speech.

PYgame: Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.



