 🌿 Plant Disease Detection using VGG16

A deep learning project that classifies plant leaf images into 39 disease classes using a fine-tuned VGG16 model. This web app is deployed using Streamlit and helps farmers, researchers, and plant enthusiasts detect plant diseases from images.

---

## 📁 Dataset

* **Source:** [Plant Leaves Dataset for Plant Disease Prediction (Kaggle)](https://www.kaggle.com/datasets/ziac007/plant-leaves-dataset-for-plant-disease-prediction)
* **Classes:** 39
* **Images:** 50,000+ high-quality leaf images categorized by disease and healthy status.
* **Structure:**

  ```
  ├── dataset/
      ├── class_1/
      ├── class_2/
      ├── ...
      └── class_39/
  ```

---

## 🧠 Model Architecture

* **Base Model:** VGG16 (pre-trained on ImageNet)
* **Modifications:**

  * Top layers removed
  * Custom dense layers added for classification
  * Fine-tuning enabled on upper VGG16 layers
* **Input Size:** 224x224 RGB
* **Augmentation:** ImageDataGenerator with rotation, zoom, shear, horizontal flip
* **Balancing:** Class weights used to handle class imbalance

---

## 📈 Training Insights

* **Optimizer:** Adam
* **Loss Function:** Categorical Crossentropy
* **Epochs:** \~20 (based on tuning)
* **Validation Accuracy:** \~93%
* **Augmentation Techniques:**

  * Random Flip
  * Random Rotation
  * Rescale
  * Zoom

---

## 🚀 Deployment

### 🌐 Streamlit App

You can interact with the model via a Streamlit web app. It allows you to upload a leaf image and get a prediction instantly.

### 🛠 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/plant-disease-detection.git
cd plant-disease-detection

# 2. Create virtual environment & activate
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run streamlit_app.py
```

### 🗂 Required Files

* `plant_disease_model_vgg16.keras` — Trained Keras model
* `streamlit_app.py` — App UI and prediction logic
* `requirements.txt` — Python dependencies

---

## 🖼️ Sample Predictions

| Input Image | Predicted Disease   |
| ----------- | ------------------- |
| 🍃 Leaf 1   | Apple Scab          |
| 🍃 Leaf 2   | Tomato Mosaic Virus |

---

## 📦 Requirements

* Python 3.8+
* TensorFlow
* Streamlit
* Pillow
* NumPy
* Pandas
* Altair

Or install all with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Acknowledgments

* VGG16 model from [Keras Applications](https://keras.io/api/applications/)
* Dataset by Zia Ullah from [Kaggle](https://www.kaggle.com/datasets/ziac007/plant-leaves-dataset-for-plant-disease-prediction)
* Streamlit community for easy deployment




