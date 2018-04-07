import cntk as C
# import cntk.tests.test_utils
from cntk.layers import Sequential, Dense, For, np
import argparse
import numpy as np
import sys
import os
import cntk as C
from cntk.train import Trainer, minibatch_size_schedule
from cntk.io import MinibatchSource, CTFDeserializer, StreamDef, StreamDefs, INFINITELY_REPEAT
from cntk.device import cpu, try_set_default_device
from cntk.learners import adadelta, learning_parameter_schedule_per_sample
from cntk.ops import relu, element_times, constant
from cntk.layers import Dense, Sequential, For
from cntk.losses import cross_entropy_with_softmax
from cntk.metrics import classification_error
from cntk.train.training_session import *
from cntk.logging import ProgressPrinter, TensorBoardProgressWriter

# The inputs are:
# pot size
# call size
# percentage of hands that will win
# chip count of opponent
# the total aggressiveness of the opponent
# Current chip count

input_dim = 6
num_output_classes = 1
num_hidden_layers = 3
hidden_layers_dim = 6


# The input variable (representing 1 observation, in our example of age and size) x, which
# in this case has a dimension of 2.
#
# The label variable has a dimensionality equal to the number of output classes in our case 2.

input = C.input_variable(input_dim)
label = C.input_variable(num_output_classes)

# Instantiate the feedforward classification model
def linear_layer(input_var, output_dim):
    input_dim = input_var.shape[0]

    weight = C.parameter(shape=(input_dim, output_dim))
    bias = C.parameter(shape=(output_dim))

    return bias + C.times(input_var, weight)

def dense_layer(input_var, output_dim, nonlinearity):
    l = linear_layer(input_var, output_dim)

    return nonlinearity(l)

def fully_connected_classifier_net(input_var, num_output_classes, hidden_layer_dim,
                                   num_hidden_layers, nonlinearity):

    h = dense_layer(input_var, hidden_layer_dim, nonlinearity)
    for i in range(1, num_hidden_layers):
        h = dense_layer(h, hidden_layer_dim, nonlinearity)

    return linear_layer(h, num_output_classes)

deepNeuralNetwork = fully_connected_classifier_net(input, num_output_classes, hidden_layers_dim,
                                   num_hidden_layers, C.sigmoid)



