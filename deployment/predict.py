import streamlit as st
import numpy as np
from keras.models import load_model
import tensorflow as tf
from PIL import Image

# Load model
model = load_model('model1.h5')

# Define class names
class_names = ["Beagle", "Boxer", "Bulldog", "Dachshund", 'German_Shepherd', "Golden_Retriever", "Labrador_Retriever", "Poodle", "Rottweiler", "Yorkshire_Terrier"]

def run():
    st.title("Dog Breed Classifier")
    st.write("Upload an image of a dog and the model will predict the breed!")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Convert the file to an open image
        image = Image.open(uploaded_file)
        
        # Display the image
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        
        
        # Preprocess the image
        img = image.resize((110, 110))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        img_batch = img_batch / 255.0

        # Predict
        prediction_inf = model.predict(img_batch)
        result_max_proba = prediction_inf.argmax(axis=-1)[0]
        result_class = class_names[result_max_proba]

        # Display results
        st.write(f'Class Name: {result_class}')

if __name__ == "__main__":
    run()
