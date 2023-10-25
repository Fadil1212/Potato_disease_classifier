import streamlit as st
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


MODEL = tf.keras.models.load_model("../saved_models/1")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

st.title("Potato Leaf Disease Prediction")


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = read_file_as_image(uploaded_file.read())
    st.write("Uploaded Image.")
    st.image(image, use_column_width=True)
    img_batch = np.expand_dims(image, 0)

    with st.spinner('Predicting...'):
        predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    st.write('Prediction:', predicted_class)
    st.write('Confidence:', f'{confidence * 100:.2f}%')





# Add the footer HTML code
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: black;
    text-align: right;
}
</style>

<div class="footer">
    <p align="right">
        <a href="https://www.linkedin.com/in/fadil-mohammed-347a0a231/">Developed by Fadil</a>
    </p>
</div>


"""

# Render the footer
st.markdown(footer, unsafe_allow_html=True)
