# 🧠 Brain Tumor Classification System

An end-to-end Machine Learning project utilizing a Convolutional Neural Network (CNN) to instantly classify brain MRI scans as either containing a **Tumor** or **No Tumor**. The model is deployed as a live web application, demonstrating a complete production-ready solution.

## 🚀 Live Demo

Experience the application and test your own MRI images:

**[Brain Tumor Classifier Live App](https://braintumorapplive.streamlit.app/)**

---

## 🛠️ Project Summary & My Role

| Category | Description |
| :--- | :--- |
| **Project Goal** | Achieve high-accuracy, rapid binary classification for brain MRI images. |
| **Model** | **Convolutional Neural Network (CNN)**, optimized with Batch Normalization and Dropout layers. |
| **Key Features** | Image Data Augmentation, Model Checkpointing, Real-Time Inference, Web Deployment. |

### My Role: Full-Stack ML Engineer (Metaphorical Description)

> I am a **Full-Stack ML Engineer** who builds, deploys, and manages the entire application, from the server infrastructure to the user interface. My core expertise lies in embedding the specialized **deep learning intelligence** at the heart of the system to deliver smart, self-contained solutions.

---

## 💻 Repository Structure

| File/Folder | Purpose |
| :--- | :--- |
| `app.py` | The main Streamlit script for the web application interface and model loading/prediction logic. |
| `BrainTumorClassifier.h5` | The final, 364MB trained Keras model, managed via Git LFS. |
| `requirements.txt` | Lists all necessary dependencies (`tensorflow`, `streamlit`, `numpy`, etc.) for deployment. |
| `BRAIN TUMOR CLASSIFICATION.ipynb` | Original Jupyter Notebook detailing data analysis, model training, and evaluation steps. |

---

## ☁️ How to Deploy (Streamlit Community Cloud)

This application was made live on the web in minutes using **Streamlit Community Cloud**—the recommended method for deploying Streamlit applications hosted on GitHub.

### 1. Requirements on GitHub

Ensure your GitHub repository contains these files at the root level, and that the large `.h5` model was pushed using **Git LFS**.

### 2. Deployment Steps

1.  Log in to the [Streamlit Community Cloud](https://streamlit.io/cloud) using your GitHub account.
2.  Click the **"New App"** button.
3.  Fill in the details:
    * **Repository:** Select your GitHub project repository.
    * **Branch:** Select the deployment branch (e.g., `main`).
    * **Main file path:** Ensure this is set to `app.py`.
4.  Click **"Deploy!"** Streamlit automatically clones the repo, installs packages from `requirements.txt`, handles the large LFS file, and launches the application.
