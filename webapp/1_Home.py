import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)


st.markdown(
    "<div style='text-align: center; padding: 50px; background-color: rgba(255, 255, 255, 0.7); border-radius: 10px;'><h1 style='font-size: 5em;'><em>Potato Disease Classification</em></h1></div>",
    unsafe_allow_html=True
)





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

.footer a {
    margin-left: 10px;
    text-decoration: none;
    color: black;
}

.footer a:hover {
    color: blue;
}
</style>

<div class="footer">
    <p align="right">
        <a href="https://www.linkedin.com/in/fadil-mohammed-347a0a231/" target="_blank">
            <img src="linkedin.png" alt="LinkedIn" width="20" height="20">
        </a>
        <a href="https://github.com/Fadil1212" target="_blank">
            <img src="github.png" alt="GitHub" width="20" height="20">
        </a>
        <a href="mailto:fadilmohammed208@gmail.com" target="_blank">
            <img src="gmail.png" alt="Gmail" width="20" height="20">
        </a>
        Developed by Fadil
    </p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
