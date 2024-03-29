import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Function to recognize cats, dogs, and tigers in an image
def recognize_animals(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # MobileNetV2 input size
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    predictions = decode_predictions(preds, top=3)[0]  # Get top 3 predictions
    
    # Filter out predictions for cats, dogs, and tigers
    cat_predictions = [pred for pred in predictions if 'cat' in pred[1]]
    dog_predictions = [pred for pred in predictions if 'dog' in pred[1]]
    tiger_predictions = [pred for pred in predictions if 'tiger' in pred[1]]
    
    return cat_predictions, dog_predictions, tiger_predictions

# Main function
def main():
    # Load input image
    image_path = 'input_image.jpg'

    # Recognize cats, dogs, and tigers
    cat_predictions, dog_predictions, tiger_predictions = recognize_animals(image_path)

    # Display the predictions
    print("Cat Predictions:")
    for pred in cat_predictions:
        print(f"{pred[1]}: {pred[2]*100:.2f}%")

    print("\nDog Predictions:")
    for pred in dog_predictions:
        print(f"{pred[1]}: {pred[2]*100:.2f}%")
        
    print("\nTiger Predictions:")
    for pred in tiger_predictions:
        print(f"{pred[1]}: {pred[2]*100:.2f}%")

if __name__ == "__main__":
    main()
