from io import BytesIO

import streamlit as st
from PIL import Image
from rembg import remove

st.set_page_config(layout="wide", page_title="Thought AI image background remover")

st.write("Thought AI Image background remover")
st.write(
    
    "upload and download high quality images for free."
)
hide_st_style = """
<style>
#MainMenu {visibility: hidden; display: none;}
footer {visibility: hidden;}
header {display: none; visibility: hidden}
.css-fblp2m {display:none;}
.css-fblp2m {display: none;}
<style>
img, s
img, s .css-1vencpc {
    position: relative;
    top: 2px;
    background-color: rgb(38, 39, 48);
    z-index: 999991;
    min-width: 244px;
    max-width: 550px;
    transform: none;
    transition: transform 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s;
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
st.sidebar.write("Upload and download ")

# Create the columns
col1, col2 = st.columns(2)

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Package the transform into a function
def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Background Removed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\\n")
    st.sidebar.download_button(
        "Download image", convert_image(fixed), "fixed.png", "image/png"
    )

# Create the file uploader
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Fix the image!
if my_upload is not None:
    fix_image(upload=my_upload)
