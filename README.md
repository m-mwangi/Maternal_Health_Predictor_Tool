# Maternal Health Predictor Tool – Data Documentation

## 📊 Cleaned Dataset  
The cleaned dataset used in this project is included as `cleaned_maternal_health_data.csv` in the `/backend/models/` folder.

---

## 📥 Data Sources and Collection Methods  

The dataset used was sourced from the [Maternal Health Risk Data Set on Kaggle](https://www.kaggle.com/datasets/andrewmvd/maternal-health-risk-data). It contains clinical and physiological information relevant to maternal health risk prediction.

The original dataset includes features such as:

- Age  
- Systolic and Diastolic Blood Pressure  
- Blood Sugar Levels  
- Body Temperature  
- Heart Rate  
- Risk Level (Low, Medium, High)  

This dataset was downloaded directly from Kaggle and used under its open-source license for educational purposes.

---

## 🧹 Preprocessing Steps  

To prepare the data for modeling, the following preprocessing steps were taken:

- **Missing Value Handling**: Checked for null/missing values and confirmed none existed.  
- **Outlier Removal**: Applied interquartile range (IQR) technique to identify and remove extreme outliers, particularly in heart rate and blood pressure values.  
- **Categorical Encoding**:  
  - The `RiskLevel` categorical feature (`Low`, `Medium`, `High`) was encoded into numerical labels (`0`, `1`, `2`) using Label Encoding.  
- **Feature Scaling**:  
  - Standardization (z-score scaling) was applied using `StandardScaler` from scikit-learn to normalize features such as age, blood pressure, sugar levels, and heart rate.  
- **Data Splitting**:  
  - The cleaned dataset was split into training and test sets (80% training, 20% testing) to evaluate model performance.  

---

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
