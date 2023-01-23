import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os

from settings import DEFAULT_CONFIDENCE_THRESHOLD, DEMO_IMAGE, MODEL, PROTOTXT


st.title("Object Editing app")
img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])


if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))



st.image(
    image, caption=f"Processed image", use_column_width=True,
)


