# Maternal Health Predictor Tool (MaternAI) – Data Documentation

MaternAI is an ML-powered application designed to predict maternal health risks. It classifies patients into different risk levels: High Risk, Mid Risk, and Low Risk. It also contains a web application based on Flask where users can input different values to predict risks.

## Data Sources and Collection Methods  

The dataset was sourced from Kaggle
🔗 [Maternal Health Risk Dataset](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data/data)  

It contains the following features:
- Age  
- Systolic and Diastolic Blood Pressure  
- Blood Sugar Levels  
- Body Temperature  
- Heart Rate  
- Risk Level (Low, Medium, High)  

## Preprocessing Steps  

To prepare the data for training, the following preprocessing steps were taken:

- **Handling Missing Values**: Checked for null/missing values and confirmed none existed.  
- **Outlier Removal**: Applied interquartile range (IQR) technique to identify and remove extreme outliers, particularly in heart rate and body temperature values.  
- **Categorical Encoding**: The `RiskLevel` categorical feature (`Low`, `Medium`, `High`) was encoded into numerical labels (`0`, `1`, `2`) using Label Encoding.  
- **Feature Scaling**: Standardization was applied using `StandardScaler` from scikit-learn to normalize the features.  
- **Data Splitting**: The cleaned dataset was split into training and test sets (80% training, 20% testing) to evaluate model performance.  

## 📈 Visualizations and Data Trends  

To better understand data trends and correlations between features, the following visualizations were created:

1. **Histogram of Age Distribution**  
   - Reveals a concentration of participants in the 20–35 age range, aligning with typical maternal ages.

2. **Boxplot of Blood Pressure by Risk Level**  
   - Shows that higher systolic and diastolic pressures are more commonly associated with medium and high-risk classifications.

3. **Scatter Plot of Heart Rate vs. Age**  
   - Displays a weak correlation but highlights some outliers with elevated heart rates in younger individuals.

4. **Bar Plot of Risk Level Frequency**  
   - Demonstrates that the dataset is fairly balanced across the three risk categories, allowing for effective supervised learning.

---

## 🗂 Files in This Section  

- `cleaned_maternal_health_data.csv`: Final cleaned dataset used for model training and prediction.  
- `visualizations/`: Folder (optional) containing saved PNG/JPEG plots showing histograms, scatter plots, and boxplots.  

---
