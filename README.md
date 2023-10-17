# Air Writing using UWB Radar

## Dataset
<pre>
  2D-Range-Doppler Data
  2D-Range-Doppler Images
</pre>

## CNN-LSTM Architecture for Radar Signal Classification
<pre>CNN-LSTM_2D.ipynb</pre>
This CNN-LSTM architecture for radar signal classification consists of the following components:

* **CNN model:** The CNN model extracts spatial features from the input 2D range-Doppler images. It consists of four convolutional layers, each followed by a batch normalization layer and a ReLU activation function. After each convolutional layer, there is a max pooling layer to downsample the feature maps and reduce the number of parameters.
* **LSTM model:** The LSTM model learns the temporal relationships between the extracted spatial features. It consists of two LSTM layers, each with 128 and 64 hidden units, respectively. The output of the LSTM model is a 10-dimensional vector, which is the predicted probability distribution over the different radar signal classes.

The combined model is a sequential model that consists of the CNN model followed by the LSTM model. The output of the CNN model is reshaped into a sequence format and fed to the LSTM model.

The training process for the combined model is as follows:

1. The CNN model is trained independently on the 2D range-Doppler images.
2. The features extracted by the CNN model are reshaped into a sequence format and fed to the LSTM model.
3. The LSTM model is trained to predict the correct radar signal class for each sequence.

The following metrics are used to evaluate the performance of the model:

* **Accuracy:** The percentage of correctly classified radar signals.
* **Loss:** The categorical cross-entropy loss between the predicted and actual probability distributions of the radar signal classes.



