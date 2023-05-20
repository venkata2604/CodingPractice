import numpy as np
import tensorflow as tf
import datetime


# Input and output data
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
], dtype=np.float32)

y = np.array([
    0,
    1,
    1,
    0
], dtype=np.float32)

# Define the Model 
model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, input_dim=2, activation='sigmoid'), 
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# compile the model 
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1), loss=tf.keras.losses.MeanSquaredError(), metrics=['mse', 'binary_accuracy'])

# Summary Print
print(model.summary())

# Adding tensorboard logs
log_dir = "../logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Train the model in the XOR data
history = model.fit(X,y,batch_size = 1, epochs=500, callbacks=[tensorboard_callback])

#Predict the XOR outputs
predictions = model.predict(X)

# Print the predicted outputs
for i in range(len(X)):
    print(f"Input: {X[i]} XOR Output: {1 if predictions[i][0] >= 0.5 else 0}")
