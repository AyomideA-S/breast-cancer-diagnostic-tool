![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-97.4%25-green)

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

* Ayomide Ayodele-Soyebo (<midesuperbest@gmail.com>) - Model Develeopment, Model Deployment, D&D Team
* Heba Hamzat (<hamzathebaoyin@gmail.com>) - EDA
* M'MONI AFUMBA Jason (<afumbajason@gmail.com>) - Model Evaluation
* Owoeye Olajumoke Prestige (<owoeyejummie@gmail.com>) - Feature Engineering, D&D Team
* Popoola Eninlaloluwa Sharon (<popoolaeninlaloluwa@gmail.com>) - Feature Engineering
* Sidiq Abdulkadir Akanbi (<sidiqabdulkadir05@gmail.com>) - EDA
* Zainab Salman (<zainabadebisi007@gmail.com>) - EDA, Model Training, D&D Team (Research-based Report)
* Dabuo Jacob Ngmenlanaa (<d.ja84@yahoo.com>) - Model Deployment, Report Editing
Built as part of the Data Science Capstone Project for the **Awibi Medtech Learning Initiative 2025**.
