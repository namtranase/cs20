""" Assigment 1 - Problem 2: Linear regression.
"""
import os
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import utils

matplotlib.use("Agg")
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
DATA_FILE = "data/birth_life_2010.txt"

# Step 1: read in data from the .txt file
data, n_samples = utils.read_birth_life_data(DATA_FILE)

# Using placeholder to hold TODO: using dataset of tf will results speed up!
# Step 2: create placeholders for X (birth rate) and Y (life expectancy)
# Remember both X and Y are scalars with type float
# X, Y = None, None

X = tf.placeholder(tf.float32, name="images")
Y = tf.placeholder(tf.float32, name="labels")

# Step 3: create weight and bias, initialized to 0.0
# Make sure to use tf.get_variable
# w, b = None, None
w = tf.get_variable(name="weights", initializer=tf.constant(0.0))
b = tf.get_variable(name="bias", initializer=tf.constant(0.0))

# Step 4: build model to predict Y
# e.g. how would you derive at Y_predicted given X, w, and b
# Y_predicted = None
Y_predicted = w * X + b

# Step 5: use the square error as the loss function
# loss = None
# loss = tf.square(Y - Y_predicted, name='loss')
# Using huber loss here


def huber_loss(labels, predictions, delta=14.0):
    residual = tf.abs(labels - predictions)

    def f1():
        return 0.5 * tf.square(residual)

    def f2():
        return delta * residual - 0.5 * tf.square(delta)

    return tf.cond(residual < delta, f1, f2)


loss = huber_loss(Y, Y_predicted)

# Step 6: using gradient descent with learning rate of 0.001 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

start = time.time()

# Create a filewriter to write the model's graph to TensorBoard
writer = tf.summary.FileWriter("./graphs/linreg", tf.get_default_graph())
with tf.Session() as sess:
    # Step 7: initialize the necessary variables, in this case, w and b
    sess.run(tf.global_variables_initializer())
    # Step 8: train the model for 100 epochs
    for i in range(100):
        total_loss = 0
        for x, y in data:
            # Execute train_op and get the value of loss.
            # Don't forget to feed in data for placeholders
            # _, loss = ########## TO DO ############
            _, loss_ = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
            total_loss += loss_

        print("Epoch {0}: {1}".format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer.close()

    # Step 9: output the values of w and b
    # w_out, b_out = None, None
    w_out, b_out = sess.run([w, b])

print("Took: %f seconds" % (time.time() - start))

# uncomment the following lines to see the plot
plt.plot(data[:, 0], data[:, 1], "bo", label="Real data")
plt.plot(data[:, 0], data[:, 0] * w_out + b_out, "r", label="Predicted data")
plt.legend()
plt.savefig("assignments/results/q2_linreg.png")
