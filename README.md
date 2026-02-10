# Breast Cancer Diagnostic Tool 🎗️

## Project Overview

This project uses Machine Learning to classify breast cancer tumors as **Benign** or **Malignant** based on cell nuclei measurements from the Wisconsin Breast Cancer Diagnostic Dataset.

## Key Features

* **Clinical Focus:** Prioritizes **Recall** (Sensitivity) to minimize false negatives (missed cancer cases).
* **Champion Model:** Logistic Regression with optimized feature selection.
  * **Accuracy:** 97.37%
  * **False Negatives:** Only 2 cases (out of 114 test patients).
* **Deployment:** Containerized web application using **Streamlit** and **Docker**.

## Project Structure

* `src/app.py`: The web application script.
* `Breast_Cancer_Classification_Model.ipynb`: The research notebook (Data cleaning, EDA, Model training).
* `Dockerfile`: Configuration for building the container.
* `model.pkl` & `scaler.pkl`: The trained model and data scaler.

## How to Run (Local)

1. **Clone the repository/folder.**
2. **Build the Docker Image:**

    ```bash
    docker build -t breast-cancer-app .
    ```

3. **Run the Container:**

    ```bash
    docker run -p 8501:8501 breast-cancer-app
    ```

4. **Access the App:** Open `http://localhost:8501` in your browser.

## Contributors

* Ayomide Ayodele-Soyebo - Model Develeopment, Model Deployment, D&D Team
* [Teammate Name]
* [Teammate Name]
