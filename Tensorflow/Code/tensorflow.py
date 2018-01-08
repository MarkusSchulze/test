'''
Created on 08.01.2018

@author: Maggi
'''
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))