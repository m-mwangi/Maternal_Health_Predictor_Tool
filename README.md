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

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Flask
- **Backend**: Python, FastAPI, Scikit-learn
- **Model**: Random Forest Classifier
- **Deployment**: Render.com


## 
