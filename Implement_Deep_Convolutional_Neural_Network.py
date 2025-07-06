# import tensorflow as tf
# import numpy as np
# from tensorflow.keras import layers, models

# def build_cnn(input_shape=(28, 28, 1), num_classes=10):
#     model = models.Sequential([
#         layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape),
#         layers.MaxPooling2D(pool_size=(2, 2)),
#         layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
#         layers.MaxPooling2D(pool_size=(2, 2)),
#         layers.Flatten(),
#         layers.Dense(128, activation='relu'),
#         layers.Dense(num_classes, activation='softmax')
#     ])
#     return model

# # Load and preprocess MNIST dataset
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# x_train = x_train[..., np.newaxis] / 255.0
# x_test = x_test[..., np.newaxis] / 255.0

# # Build and compile model
# cnn_model = build_cnn()
# cnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# # Train the model (run for 1 epoch for simplicity)
# cnn_model.fit(x_train, y_train, epochs=1, validation_data=(x_test, y_test))


import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# CNN Model
def build_cnn():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Load, Preprocess, Train (1 epoch)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train[..., np.newaxis] / 255.0
x_test = x_test[..., np.newaxis] / 255.0
model = build_cnn()
model.fit(x_train, y_train, epochs=1, validation_data=(x_test, y_test))
