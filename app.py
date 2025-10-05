import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the model
model = load_model("BrainTumorClassifier.h5")

st.title("🧠 Brain Tumor Prediction App")
st.write("Upload an MRI scan and the model will predict if it has a tumor.")

uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Resize to match model input
    img = image.load_img(uploaded_file, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Add batch dimension and normalize

    # Predict
    prediction = model.predict(img_array)[0][0]

    st.image(img, caption="Uploaded MRI", use_container_width=True)

    if prediction > 0.5:
        st.error("Tumor Detected ⚠️")
    else:
        st.success("No Tumor ✅")
