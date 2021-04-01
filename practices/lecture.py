import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

###############################################################################
# a = tf.constant(2)
# b = tf.constant(3)
# x = tf.add(a, b)

# with tf.Session() as sess:
#     print(sess.run(x))
###############################################################################

###############################################################################
# a = tf.constant(2, name="a")
# b = tf.constant(3, name="b")
# x = tf.add(a, b, name="add")

# writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())
# with tf.Session() as sess:
#     print(sess.run(x))
# writer.close()
###############################################################################

###############################################################################
# a = tf.constant([2, 2], name="a")
# b = tf.constant([[0, 1], [2, 3]], name="b")
# x = tf.multiply(a, b, name="mul")
# with tf.Session() as sess:
#     print(sess.run(x))
###############################################################################

###############################################################################
# a = tf.constant([2, 2], name="a")
# b = tf.constant([[0, 1], [2, 3]], name="b")
# x = tf.multiply(a, b, name="mul")
# with tf.Session() as sess:
#     print(sess.run(x))
###############################################################################

###############################################################################
# a = tf.constant([2, 2], name='a')
# b = tf.constant([[0, 1], [2, 3]], name='b')

# with tf.Session() as sess:
#     print(sess.run(tf.div(b, a)))
#     print(sess.run(tf.divide(b, a)))
#     print(sess.run(tf.truediv(b, a)))
#     print(sess.run(tf.floordiv(b, a)))
#     # print(sess.run(tf.realdiv(b, a)))
#     print(sess.run(tf.truncatediv(b, a)))
#     print(sess.run(tf.floor_div(b, a)))
###############################################################################

###############################################################################
# test_list = [b"apple", b"peach", b"grape"] 
# a = tf.zeros_like(test_list)
# b = tf.ones_like(test_list) # This is error!
# with tf.Session() as sess:
#     print(sess.run(a))
###############################################################################

###############################################################################
# s = tf.Variable(2, name="scalar")
# m = tf.Variable([[0, 1], [2, 3]], name="matrix")
# W = tf.Variable(tf.zeros([748, 10]))
# # Better way below!
# s = tf.get_variable("scalar", initializer=tf.constant(2)) 
# m = tf.get_variable("matrix", initializer=tf.constant([[0, 1], [2, 3]]))
# W = tf.get_variable("big_matrix", shape=(784, 10), initializer=tf.zeros_initializer())
# with tf.Session() as sess:
#     sess.run(W.initializer)
#     print(W.eval())
# Why using Variable: tf.Variable is a class with many ops
###############################################################################