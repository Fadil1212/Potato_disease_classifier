import streamlit as st

def display_contacts():
    st.title("Contacts Page")
    # Add content for the Contacts page
    st.write("Welcome to the Contacts Page!")



st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/fadilmohammed208@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; margin-top: 6px; margin-bottom: 16px; resize: vertical;" required>
    <input type="email" name="email" placeholder="Your email" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; margin-top: 6px; margin-bottom: 16px; resize: vertical;" required>
    <textarea name="message" placeholder="Your message here" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; margin-top: 6px; margin-bottom: 16px; resize: vertical;"></textarea>
    <button type="submit" style="background-color: #04AA6D; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

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