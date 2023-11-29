import cv2
import numpy as np
import tensorflow as tf

# Path to your pre-trained emotion detection model
MODEL_PATH = 'model.h5' 
IMAGE_PATH = 'test/data/images/FALSE_0.jpg'

# Load the TensorFlow model
model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(image_path):
    """
    Preprocess the image to fit the input requirements of the model.
    This typically includes resizing and normalization.
    Adjust this function based on your model's requirements.
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (48, 48))  # Resize based on your model's input size
    image = image / 255.0  # Normalizing
    image = np.expand_dims(image, axis=0)  # Adding batch dimension
    return image

def predict_emotion(processed_image):
    """
    Predict the emotion from the processed image using the model.
    """
    prediction = model.predict(processed_image)
    return np.argmax(prediction, axis=1)

def decode_prediction(prediction):
    """
    Decode the prediction to a human-readable emotion.
    Adjust this function based on the output of your model.
    """
    emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
    return emotions[prediction[0]]

# Process the image
processed_image = preprocess_image(IMAGE_PATH)

# Predict the emotion
prediction = predict_emotion(processed_image)

# Decode the prediction
emotion = decode_prediction(prediction)

# Display the result
print(f"Detected Emotion: {emotion}")
