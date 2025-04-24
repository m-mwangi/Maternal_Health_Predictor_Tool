from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.secret_key = "your_secret_key"

FASTAPI_PREDICT_URL = "https://maternai-api-m9q7.onrender.com/predict"

# Ensure upload directory exists
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction_message = None
    form_data = {}

    if request.method == 'POST':
        form_data = request.form.to_dict()

        try:
            input_data = {
                "Age": float(form_data.get("Age", 0)),
                "SystolicBP": float(form_data.get("SystolicBP", 0)),
                "DiastolicBP": float(form_data.get("DiastolicBP", 0)),
                "BS": float(form_data.get("BS", 0)),
                "BodyTemp": float(form_data.get("BodyTemp", 0)),
                "HeartRate": float(form_data.get("HeartRate", 0))
            }

            response = requests.post(FASTAPI_PREDICT_URL, params=input_data)
            if response.status_code == 200:
                prediction_result = response.json().get("Predicted Risk Level", "Unknown result")
                prediction_message = f"Predicted Risk: {prediction_result}"
            elif response.status_code == 422:
                prediction_message = "Error: Invalid input data. Please check your values."
            else:
                prediction_message = f"Error: API returned {response.status_code}"

        except Exception as e:
            prediction_message = f"Error: {str(e)}"

    return render_template('predict.html', form_data=form_data, prediction_message=prediction_message)

@app.route('/preprocess')
def preprocess():
    return render_template('preprocess.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
