# Maternal Health Risk Predictor Tool (MaternAI) – Data Documentation

MaternAI is an ML-powered application designed to predict maternal health risks. It classifies patients into different risk levels: High Risk, Mid Risk, and Low Risk. It also contains a web application based on Flask where users can input different values to predict risks.

## Data Sources and Collection Methods  

The dataset was sourced from Kaggle
🔗 [Maternal Health Risk Dataset](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data/data)  

## Key Variables
- Age - This is the age in years when a woman is pregnant.
- Systolic Blood Pressure - The upper value of Blood Pressure in mmHg.
- Diastolic Blood Pressure - Lower value of Blood Pressure in mmHg.
- Blood Sugar Levels - Measured in terms of molar concentration, mmol/L.
- Body Temperature - Measured in Fahrenheit.
- Heart Rate - A normal resting heart rate in beats per minute.
- Risk Level - Predicted Risk Intensity Level during pregnancy, considering the previous attributes. Categorized as either 'High Risk', 'Low Risk', or 'Mid Risk'.

## Preprocessing Steps  
To prepare the data for training, the following preprocessing steps were taken:

- Handling Missing Values - Checked for null/missing values and confirmed none existed.  
- Outlier Removal - Applied interquartile range (IQR) technique to identify and remove extreme outliers, particularly in heart rate and body temperature values.  
- Categorical Encoding - The `RiskLevel` categorical feature (`Low`, `Medium`, `High`) was encoded into numerical labels (`0`, `1`, `2`) using Label Encoding.  
- Feature Scaling - Standardization was applied using `StandardScaler` from scikit-learn to normalize the features.  
- Data Splitting - The cleaned dataset was split into training, validation, and test sets to evaluate model performance.  

## Visualizations  

To better understand data trends and correlations between features, the following visualizations were created:

1. **Correlation Heatmap**
   - Displays the correlation between various features in the dataset.
   - There is a positive correlation between the input variables and the output variable.
   - The strongest one is in Blood Sugar with 0.58, and the weakest correlation is in Body Temperature and Heart Rate with values of 0.14 and 0.18, respectively.
   - Systolic BP and Diastolic BP are strongly correlated with a value of 0.8. As Systolic BP increases, Diastolic BP also tends to increase.

3. **Boxplots**  
   - Show the distribution of key numerical variables (e.g., blood pressure, heart rate) and help identify outliers.  
   - Illustrate how some features vary across different risk levels.

4. **Pair Plots**  
   - Provide a grid of scatter plots for each feature combination, color-coded by risk level.  
   - Help visualize feature clustering and separability by class.

5. **Histogram**
   - It enabled us to see the class distribution, ensuring that there was no class imbalance.
