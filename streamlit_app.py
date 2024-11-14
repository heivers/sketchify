""" A streamlit app that transfers photos to sketches
Try it here: https://share.streamlit.io/heivers/sketchify"""

import cv2
import numpy as np
import streamlit as st
from PIL import Image
from camera_input_live import camera_input_live

st.write("""
         ## This Web App turns your video-feed into a sketch.
         \nGo Ahead and try:
         """
         )

image = camera_input_live()
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
