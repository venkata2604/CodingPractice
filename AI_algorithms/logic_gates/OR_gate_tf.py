import tensorflow as tf
import numpy as np

# input
X = np.array([
    [0,0], 
    [0,1], 
    [1,0],
    [0,0]
], dtype=np.float32)

# output
y = np.array([
    0,
    1,
    1,
    1
], dtype=np.float32)

# Model Architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=2, input_dim=2, activation='sigmoid' )
])
