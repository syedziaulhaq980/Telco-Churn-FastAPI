# 📊 Telco Customer Churn Prediction API

A production-style **Machine Learning REST API** for predicting customer churn probability using **XGBoost** and **FastAPI**.

The project takes customer information through an API request, processes the input using the same preprocessing pipeline used during model training, and returns the predicted churn class, churn probability, and decision threshold.

---

## 🚀 Live API

**Live API:**
https://telco-churn-fastapi-1.onrender.com/

**Interactive API Documentation:**
https://telco-churn-fastapi-1.onrender.com/docs

**Health Check:**
https://telco-churn-fastapi-1.onrender.com/health

---

## 🎯 Project Objective

Customer churn is an important business problem for telecom companies.

The objective of this project is to build a machine learning system that can:

* Predict whether a customer is likely to churn
* Estimate the customer's churn probability
* Expose the trained ML model through a REST API
* Accept real-time customer information
* Return structured JSON predictions
* Provide an API health-check endpoint
* Deploy the ML application to the cloud

---

## 🏗️ Project Architecture

```text
Customer
   │
   ▼
FastAPI REST API
   │
   ▼
Pydantic Input Validation
   │
   ▼
Pandas DataFrame
   │
   ▼
Saved ML Pipeline
   │
   ├── Preprocessing
   └── XGBoost Model
   │
   ▼
Churn Probability
   │
   ▼
Decision Threshold = 0.30
   │
   ▼
JSON Response
```

---

## 🛠️ Technologies Used

### Programming

* Python

### Machine Learning

* XGBoost
* Scikit-learn
* Pandas
* NumPy
* Joblib

### API Development

* FastAPI
* Pydantic
* Uvicorn

### Development Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

### Deployment

* Render

---

## 📂 Project Structure

```text
Telco-Churn-FastAPI/
│
├── app/
│   └── main.py
│
├── data/
│   ├── 1.ipynb
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   └── telco_churn_model.pkl
│
├── notebooks/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Dataset

The project uses the **Telco Customer Churn** dataset.

The dataset contains customer information such as:

* Customer demographics
* Tenure
* Contract type
* Internet service
* Payment method
* Monthly charges
* Total charges
* Additional services
* Churn status

The API accepts **19 raw customer features**.

### Input Features

```text
gender
SeniorCitizen
Partner
Dependents
tenure
PhoneService
MultipleLines
InternetService
OnlineSecurity
OnlineBackup
DeviceProtection
TechSupport
StreamingTV
StreamingMovies
Contract
PaperlessBilling
PaymentMethod
MonthlyCharges
TotalCharges
```

---

# 🤖 Machine Learning Model

The project uses **XGBoost** for binary classification.

The trained model is saved using **Joblib** and loaded by the FastAPI application.

The saved pipeline includes the required preprocessing and machine learning steps, allowing the API to receive raw customer information.

### Prediction Threshold

The API uses a classification threshold of:

```text
0.30
```

If:

```text
Churn Probability >= 0.30
```

the customer is classified as:

```text
Churn
```

Otherwise:

```text
No Churn
```

### Why a 0.30 Threshold?

The threshold was intentionally reduced from the standard `0.50` threshold to increase the model's ability to identify potential churners.

This creates a trade-off between precision and recall.

---

# 📈 Model Performance

The production model was evaluated using a **0.30 classification threshold**.

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 76.44% |
| Precision | 53.93% |
| Recall    | 77.01% |
| F1 Score  | 63.44% |
| ROC-AUC   | 84.60% |

The threshold was selected with greater emphasis on identifying customers who may churn.

---

# ⚡ FastAPI Endpoints

## 1. Root Endpoint

```http
GET /
```

Example response:

```json
{
  "message": "Telco Customer Churn Prediction API is running"
}
```

---

## 2. Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

This endpoint verifies that the API is running and that the trained model has successfully loaded.

---

## 3. Churn Prediction

```http
POST /predict
```

The endpoint accepts customer information in JSON format.

### Example Request

```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.35,
  "TotalCharges": 844.20
}
```

### Example Response

```json
{
  "prediction": 1,
  "prediction_label": "Churn",
  "churn_probability": 0.6821,
  "threshold": 0.3
}
```

---

# 🧪 API Testing

The API was tested locally using:

```text
GET  /
GET  /health
POST /predict
```

The prediction generated through FastAPI was also compared with the probability generated directly from the saved machine learning model.

Example:

```text
Model probability ≈ 0.6821
API probability   ≈ 0.6821
```

This confirms that the API is using the expected trained model and preprocessing pipeline.

---

# 💻 Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/syedziaulhaq980/Telco-Churn-FastAPI.git
```

```bash
cd Telco-Churn-FastAPI
```

---

## 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start the FastAPI Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 5. Open Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically provides interactive Swagger/OpenAPI documentation, allowing the prediction API to be tested directly from the browser.

---

# ☁️ Deployment

The application is deployed as a **Render Web Service**.

### Production Build Command

```bash
pip install -r requirements.txt
```

### Production Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Deployment Flow

```text
GitHub Repository
       │
       ▼
     Render
```
