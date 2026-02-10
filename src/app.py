import streamlit as st  # type: ignore
import joblib  # type: ignore
import pandas as pd  # type: ignore

# List of columns exactly as they appeared during training
model_columns = [
    "radius_mean",
    "texture_mean",
    "smoothness_mean",
    "compactness_mean",
    "concave points_mean",
    "symmetry_mean",
    "fractal_dimension_mean",
    "radius_se",
    "texture_se",
    "smoothness_se",
    "compactness_se",
    "concave points_se",
    "symmetry_se",
    "fractal_dimension_se",
    "radius_worst",
    "texture_worst",
    "smoothness_worst",
    "compactness_worst",
    "concave points_worst",
    "symmetry_worst",
    "fractal_dimension_worst",
]

# 1. SETUP: Load Model AND Scaler 🛠️
try:
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")  # <--- NEW: Load the scaler
except Exception:
    # Fallback paths
    model = joblib.load("models/model.pkl")
    scaler = joblib.load("models/scaler.pkl")

st.set_page_config(
    page_title="Breast Cancer Diagnosis", page_icon="🎗️", layout="centered"
)

st.title("Breast Cancer Diagnostic Tool 🎗️")
st.markdown(
    """
This tool uses a machine learning model (**Logistic Regression**) to predict
whether a breast mass is **Benign** or **Malignant** based on cell nuclei
measurements.
"""
)

# 2. INTERFACE: Collect the 7 Key Features (Means)
st.subheader("Patient Data (Cell Nuclei Mean Values)")

col1, col2 = st.columns(2)

with col1:
    radius_mean = st.slider(
        "Radius",
        6.98,
        28.11,
        14.12,
        help="Mean of distances from center to points on the perimeter",
    )
    texture_mean = st.slider(
        "Texture", 9.71, 39.28, 19.29, help="Standard deviation of gray-scale "
        "values"
    )
    smoothness_mean = st.slider(
        "Smoothness",
        0.05,
        0.16,
        0.096,
        format="%.3f",
        help="Local variation in radius lengths",
    )
    compactness_mean = st.slider(
        "Compactness", 0.02, 0.35, 0.104, format="%.3f", help="Perimeter^2 / "
        "Area - 1.0"
    )

with col2:
    concave_points_mean = st.slider(
        "Concave Points",
        0.00,
        0.20,
        0.049,
        format="%.3f",
        help="Number of concave portions of the contour",
    )
    symmetry_mean = st.slider("Symmetry", 0.10, 0.30, 0.181, format="%.3f")
    fractal_dim_mean = st.slider(
        "Fractal Dimension",
        0.05,
        0.10,
        0.062,
        format="%.3f",
        help="Coastline approximation - 1",
    )

# 3. PRE-PROCESSING
input_data = {
    "radius_mean": radius_mean,
    "texture_mean": texture_mean,
    "smoothness_mean": smoothness_mean,
    "compactness_mean": compactness_mean,
    "concave points_mean": concave_points_mean,
    "symmetry_mean": symmetry_mean,
    "fractal_dimension_mean": fractal_dim_mean,
    # Standard Error (SE) features - Defaulting to mean
    "radius_se": 0.405,
    "texture_se": 1.216,
    "smoothness_se": 0.007,
    "compactness_se": 0.025,
    "concave points_se": 0.011,
    "symmetry_se": 0.020,
    "fractal_dimension_se": 0.003,
    # Worst features - Defaulting to mean
    "radius_worst": 16.269,
    "texture_worst": 25.677,
    "smoothness_worst": 0.132,
    "compactness_worst": 0.254,
    "concave points_worst": 0.114,
    "symmetry_worst": 0.290,
    "fractal_dimension_worst": 0.083,
}

# Ensure columns are in the EXACT same order as training
# (We dropped perimeter_*, area_*, and concavity_*)
expected_order = [
    "radius_mean",
    "texture_mean",
    "smoothness_mean",
    "compactness_mean",
    "concave points_mean",
    "symmetry_mean",
    "fractal_dimension_mean",
    "radius_se",
    "texture_se",
    "smoothness_se",
    "compactness_se",
    "concave points_se",
    "symmetry_se",
    "fractal_dimension_se",
    "radius_worst",
    "texture_worst",
    "smoothness_worst",
    "compactness_worst",
    "concave points_worst",
    "symmetry_worst",
    "fractal_dimension_worst",
]

features = pd.DataFrame([input_data])

# Reorder columns to match the scaler's expectation
features = features[expected_order]

# <--- NEW: Scale the features using the loaded scaler
features_scaled = scaler.transform(features)

# 4. PREDICTION
if st.button("Predict Diagnosis", type="primary"):
    # 1. Scale the data (returns a numpy array)
    features_scaled_array = scaler.transform(features)

    # 2. Convert back to DataFrame to put the names back!
    # (This silences the warning)
    features_scaled_df = pd.DataFrame(
        features_scaled_array, columns=features.columns
    )

    # 3. Predict using the DataFrame
    prediction = model.predict(features_scaled_df)[0]
    probability = model.predict_proba(features_scaled_df)[0][1]

    st.write("---")

    if prediction == 1:
        st.error("**Prediction: MALIGNANT (Cancerous)**")
        st.write(f"Confidence: **{probability:.1%}**")
        st.warning("⚠️ Recommendation: Urgent pathological "
                   "consultation required.")
    else:
        st.success("**Prediction: BENIGN (Non-Cancerous)**")
        st.write(f"Confidence: **{(1-probability):.1%}**")
        st.info("✅ Recommendation: Routine monitoring.")
