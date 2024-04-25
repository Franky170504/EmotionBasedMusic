import os
import numpy as np
from keras.layers import Input, Dense
from keras.models import Model
from keras.utils import to_categorical

def load_data(data_dir):
    X = None  # Initialize X to None before data loading starts
    y = []  # Initialize y to an empty list for labels
    label = []
    dictionary = {}
    c = 0
    data_dir = os.path.join(data_dir,'data')
   
    for filename in os.listdir(data_dir):
        if filename.endswith(".npy") and not filename.startswith("labels"):
            data = np.load(os.path.join(data_dir, filename))
          
            # Handle first data file to determine size
            if X is None:
                size = data.shape[0]
                X = data.copy()  # Efficiently copy data using copy()
            else:
                X = np.concatenate((X, data))  # Concatenate subsequent data

            class_name = filename.split(".")[0]
            y.extend([class_name] * size) 
            label.append(class_name)
            dictionary[class_name] = c
            c += 1

    y = np.array([dictionary[class_name] for class_name in y], dtype="int32")
    y = to_categorical(y)
    return X, y, label, dictionary


def train_test_split(X, y, test_size=0.2):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)  # Set random state for reproducibility
    return X_train, X_test, y_train, y_test

def save_model(model, data_dir, label):
    models_dir = os.path.join(data_dir,'models')
    model.save(os.path.join(models_dir, "model.keras"))
    np.save(os.path.join(models_dir,"labels.npy"), np.array(label))

def main():
    data_dir = os.getcwd()  # Replace with your data directory path (use double backslashes for Windows)
    X, y, label, dictionary = load_data(data_dir)

    # Shuffle data for better training (optional)
    cnt = np.arange(X.shape[0])
    np.random.shuffle(cnt)
    X_new = X[cnt]  # Shuffle X based on shuffled indices
    y_new = y[cnt]  # Shuffle y based on shuffled indices
    
    X_train, X_test, y_train, y_test = train_test_split(X_new, y_new, test_size=0.2)  # Split shuffled data

    # Build the neural network model
    input_shape = X_train.shape[1]  # Get input shape from training data (corrected)
    ip = Input(shape=(input_shape,))
    m = Dense(512, activation="relu")(ip)
    m = Dense(256, activation="relu")(m)
    op = Dense(y.shape[1], activation="softmax")(m)  # Use y.shape[1] for dynamic output size
    model = Model(inputs=ip, outputs=op)
    model.compile(optimizer='rmsprop', loss="categorical_crossentropy", metrics=['acc'])
    model.fit(X_train, y_train, epochs=50)
    save_model(model, data_dir, label)

if __name__ == "__main__" :
    main()

