import streamlit as st

st.title("Project Description")
st.write("I have developed an AI-powered web application for diagnosing plant diseases, specifically focusing on potato diseases like early blight and late blight. These diseases significantly impact potato quality and yield. Manually identifying these leaf diseases is time-consuming and arduous. To address this, I created a web app that utilizes artificial intelligence to classify potato leaf diseases.")
st.write("The core of our application is a Convolutional Neural Network (CNN) architecture, a type of deep learning model. To train the model, I initially gathered a dataset from Kaggle. However, due to the dataset's small size, I employed a technique called Data Augmentation. This process increased the dataset's size and helped prevent overfitting, ultimately enhancing the model's performance.")
st.write("Through diligent training and fine-tuning, the deep learning model achieved an impressive test accuracy of 97%. This accuracy makes our application a reliable tool for identifying and classifying potato leaf diseases, providing farmers with crucial insights to enhance crop management and yield.")
st.image("healthy.jpg", caption="Healthy", use_column_width=False, width=200)
st.image("early.jpg", caption="Early Blight", use_column_width=False, width=200)
st.image("late.jpg", caption="Late Blight", use_column_width=False, width=200)

# Use Local CSS File

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
st.markdown(footer, unsafe_allow_html=True)