import cv2
import numpy as np

# Load the pre-trained model and the configuration file
net = cv2.dnn.readNetFromCaffe(
    'MobileNetSSD_deploy.prototxt.txt', 
    'MobileNetSSD_deploy.caffemodel'
)

# List of class labels MobileNet SSD was trained to detect
CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus",
    "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike",
    "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

# Load the input image
image = cv2.imread('train.jpg')
(h, w) = image.shape[:2]

# Preprocess the image: resize to 300x300 pixels and mean subtraction
blob = cv2.dnn.blobFromImage(
    cv2.resize(image, (300, 300)), 
    0.007843, 
    (300, 300), 
    127.5
)

# Set the processed image as the input to the network
net.setInput(blob)

# Perform forward pass to get the detections
detections = net.forward()

# Loop over the detections
for i in np.arange(0, detections.shape[2]):
    # Extract the confidence (i.e., probability) associated with the prediction
    confidence = detections[0, 0, i, 2]

    # Filter out weak detections by ensuring the confidence is greater than a threshold
    if confidence > 0.2:
        # Extract the index of the class label from the detections
        idx = int(detections[0, 0, i, 1])
        
        # Compute the (x, y)-coordinates of the bounding box for the object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        
        # Draw the prediction and the bounding box
        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
