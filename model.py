from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

def model_keras(modelYolu, labelYolu, gorselYolu):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Check if the model file exists
    if not os.path.isfile(modelYolu):
        raise FileNotFoundError(f"No file found at {modelYolu}")
    
    # Check if the label file exists
    if not os.path.isfile(labelYolu):
        raise FileNotFoundError(f"No file found at {labelYolu}")

    # Load the model
    model = load_model(modelYolu, compile=False)

    # Load the labels
    class_names = open(labelYolu, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Load and preprocess the image
    image = Image.open(gorselYolu).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return ("Class:", class_name.strip(), "Confidence Score:", confidence_score)

# Example usage
model_path = "FİLA ROAD MODEL H5"
label_path = "FİLA ROAD LABELS"
image_path = "path_to_your_image.jpg"

try:
    result = model_keras(model_path, label_path, image_path)
    print(result)
except FileNotFoundError as e:
    print(e)
