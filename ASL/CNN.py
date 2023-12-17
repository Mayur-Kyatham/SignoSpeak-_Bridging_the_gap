import pickle
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, model

# Load the dataset from the pickle file
with open('data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

data = np.array(data_dict['data'])
labels = np.array(data_dict['labels'])

# Convert labels to numerical values
label_to_index = {label: idx for idx, label in enumerate(set(labels))}
index_to_label = {idx: label for label, idx in label_to_index.items()}
numeric_labels = np.array([label_to_index[label] for label in labels])

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(data, numeric_labels, test_size=0.2, random_state=42)

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Reshape data for CNN input
x_train = x_train.reshape(x_train.shape[0], 21, 42, 1)
x_test = x_test.reshape(x_test.shape[0], 21, 42, 1)

# Define the CNN model
model = model.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(21, 42, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(len(set(labels)), activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# Save the trained model
model.save('hand_sign_cnn_model.h5')
