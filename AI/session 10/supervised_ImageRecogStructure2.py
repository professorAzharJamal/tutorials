import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Define a function to preprocess the input image
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Define a function to predict the breed of a cat or dog
def predict_breed(image_path):
    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    for _, label, probability in decoded_predictions:
        print(f"{label}: {probability:.2f}")

# Example usage
image_path = 'input_image_Dog.jpg'  # Change to the path of your image
print("Predicted breeds:")
predict_breed(image_path)
