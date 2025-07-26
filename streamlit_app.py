
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# تحميل النموذج
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("/content/plant_disease_model_v2.keras")

model = load_model()

st.title("🌱 Plant Disease Detection")
st.write("Upload a plant leaf image to detect the disease.")

# رفع الصورة
uploaded_file = st.file_uploader("Upload a plant image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # تجهيز الصورة للتنبؤ
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # التنبؤ
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    st.write(f"*Predicted Class:* {class_index}")
    st.write(f"*Confidence:* {confidence:.2f}%")
