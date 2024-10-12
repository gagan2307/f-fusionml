# image_classifier.py

import os
import sys
import numpy as np
import tensorflow as tf
import joblib
import logging
import warnings

# Suppress TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow INFO, WARNING, and ERROR messages
logging.getLogger('tensorflow').setLevel(logging.FATAL)

# Suppress all warnings
warnings.filterwarnings('ignore')

# Configure stdout and stderr to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def preprocess_image(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def make_prediction(img_path):
    img_array = preprocess_image(img_path)
    # Suppress progress bar by setting verbose=0
    predictions = model.predict(img_array, verbose=0)
    predicted_class = np.argmax(predictions, axis=1)
    predicted_class_name = class_names[predicted_class[0]]
    return predicted_class_name

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No image file path provided.", file=sys.stderr)
        sys.exit(1)

    img_path = sys.argv[1]

    if not os.path.exists(img_path):
        print(f"Error: Image file {img_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the model and additional data from the script's directory
    model_path = os.path.join(script_dir, 'modelweth.h5')
    data_path = os.path.join(script_dir, 'additional_data_weth.pkl')

    # Load the model
    model = tf.keras.models.load_model(model_path)

    # Load additional data
    additional_data = joblib.load(data_path)
    class_names = additional_data['class_names']

    try:
        predicted_class_name = make_prediction(img_path)
        print(predicted_class_name)  # Output prediction to stdout
    except Exception as e:
        print(f"Error during prediction: {e}", file=sys.stderr)
        sys.exit(1)
