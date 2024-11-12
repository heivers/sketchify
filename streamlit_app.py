""" A streamlit app that transfers photos to sketches
Try it here: https://share.streamlit.io/heivers/sketchify"""

import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.write("""
         ## This Web App turns a color jpg into a sketch.
         \nGo Ahead and try:
         """
         )

image = st.file_uploader("Upload an Image", type=['jpg', 'jpeg', 'png',])
if image:
    st.image(image)
    img = Image.open(image)
    img_gray = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
    img_blend = cv2.divide(img_gray, img_blur, scale=256)
    sketch = Image.fromarray(img_blend)
    if sketch.mode != "RGB":
        sketch = sketch.convert("RGB")
    st.image(sketch)
