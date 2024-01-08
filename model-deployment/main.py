from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
import flask

model = None
interpreter = None
input_index = None
output_index = None

class_names = ['Apple___Apple_scab',
               'Apple___Black_rot',
               'Apple___Cedar_apple_rust',
               'Apple___healthy',
               'Blueberry___healthy',
               'Cherry_(including_sour)___Powdery_mildew',
               'Cherry_(including_sour)___healthy',
               'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
               'Corn_(maize)___Common_rust_',
               'Corn_(maize)___Northern_Leaf_Blight',
               'Corn_(maize)___healthy',
               'Grape___Black_rot',
               'Grape___Esca_(Black_Measles)',
               'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
               'Grape___healthy',
               'Orange___Haunglongbing_(Citrus_greening)',
               'Peach___Bacterial_spot',
               'Peach___healthy',
               'Pepper,_bell___Bacterial_spot',
               'Pepper,_bell___healthy',
               'Potato___Early_blight',
               'Potato___Late_blight',
               'Potato___healthy',
               'Raspberry___healthy',
               'Soybean___healthy',
               'Squash___Powdery_mildew',
               'Strawberry___Leaf_scorch',
               'Strawberry___healthy',
               'Tomato___Bacterial_spot',
               'Tomato___Early_blight',
               'Tomato___Late_blight',
               'Tomato___Leaf_Mold',
               'Tomato___Septoria_leaf_spot',
               'Tomato___Spider_mites Two-spotted_spider_mite',
               'Tomato___Target_Spot',
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
               'Tomato___Tomato_mosaic_virus',
               'Tomato___healthy']

BUCKET_NAME = "elfailali-models"


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # Instantiates a client
    storage_client = storage.Client()
    # The name for the new bucket
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")


def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "models/model.h5",
            "/tmp/model.h5",
        )
        model = tf.keras.models.load_model("/tmp/model.h5")

    image = request.files["file"]

    IMAGE_SIZE = 250
    image = np.array(
        Image.open(image).convert("RGB").resize((IMAGE_SIZE, IMAGE_SIZE))  # image resizing
    )

    # image = image/255

    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)

    print("Predictions:", predictions)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    response = flask.jsonify({"predicted_class": predicted_class, "confidence": confidence})
    # return {"class": predicted_class, "confidence": confidence}
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')

    return response

