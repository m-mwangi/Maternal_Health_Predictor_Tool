# Maternal Health Risk Predictor Tool (MaternAI)

MaternAI is a machine learning-powered application designed to predict maternal health risks. It classifies patients into one of three risk levels: **Low Risk**, **Mid Risk**, or **High Risk** based on clinical parameters.

## Features
- Predict maternal health risk based on input values
- ML model using Random Forest Classifier
- Simple Flask-based frontend
- Deployed and accessible online for testing

## How It Works
1. **User Interface**  
   The web interface allows users to input the following values:
   - Age
   - Systolic Blood Pressure
   - Diastolic Blood Pressure
   - Blood Sugar Levels
   - Body Temperature
   - Heart Rate
    
2. **Prediction**  
   The app sends user input to a deployed backend model, which returns a predicted **Risk Level**.

3. **Output**  
   The predicted risk level is displayed to the user.

## Deployed API (SwaggerUI)
https://maternai-api-m9q7.onrender.com/docs

## MaternAI Live Web Application
https://health-predictor-tool.onrender.com/

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, Flask
- **Backend**: Python, FastAPI, Scikit-learn
- **Model**: Random Forest Classifier
- **Deployment**: Render.com

## How to setup the project locally
### Prerequisites
Before you begin, make sure you have the following installed:

- Python 3.7+
- pip (Python's package installer)

### Download the Project
- Download the ZIP file of the project from Canvas.
- Extract the contents of the ZIP file to a location of your choice.

### Create a Virtual Environment
1. Open a terminal (or Command Prompt) in the extracted project folder.
2. Create a virtual environment by running:

   ```bash
   python -m venv venv

   source venv/bin/activate     # On Windows: venv\Scripts\activate

### Install Dependencies
```bash
pip install -r requirements.txt

```
### Launch the API locally
In the project root directory, run:
```bash
uvicorn app:app --reload
```
This will start the API locally on http://127.0.0.1:8000/docs

### Launch the Web App locally
Navigate to the front-end folder, then run this command:
```bash
python app.py
```
This will start the Web App locally on http://127.0.0.1:5000
