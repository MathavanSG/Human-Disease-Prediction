import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image
model=keras.models.load_model("Disease_predicition.h5")

disease={'BA- cellulitis': 0,
 'BA-impetigo': 1,
 'FU-athlete-foot': 2,
 'FU-nail-fungus': 3,
 'FU-ringworm': 4,
 'PA-cutaneous-larva-migrans': 5,
 'VI-chickenpox': 6,
 'VI-shingles': 7}
st.title("Human Disease Image Prediction")

uploaded_image=st.file_uploader('Upload an image of your defected region',type=["jpg","png","jpeg"])
if uploaded_image is not None:
    img=Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image")


    if st.button('Predict'):
        img_resized = img.resize((223, 223))
        img_array = image.img_to_array(img_resized)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        prediction = model.predict(img_array)
        predicted_class_index = np.argmax(prediction)
        predicted_class = list(disease.keys())[predicted_class_index]
        st.write(f"Prediction: {predicted_class}")


