# Heart Failure Prediction
A Machine learning web app made with **Streamlit**
- https://share.streamlit.io/randell-janus/heart-failure-prediction/main/app.py  
- Deployed via [Streamlit Sharing](https://streamlit.io/sharing)

## About
Predicts mortality caused by Heart Failure with the use of a Random Forest Classifier model
  
### Dataset Source  
The dataset is from Kaggle. The authors are Davide Chicco and Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16 (2020).  

### Predictor Values
* age - Age of patient
* anaemia - Decrease of red blood cells or hemoglobin (boolean)  
* creatinine_phosphokinase - Level of the CPK enzyme in the blood (mcg/L)  
* diabetes - If the patient has diabetes (boolean)  
* ejection_fraction - Percentage of blood leaving the heart at each contraction (percentage)  
* high_blood_pressure - If the patient has hypertension (boolean)  
* platelets - Platelets in the blood (kiloplatelets/mL)  
* serum_creatinine - Level of serum creatinine in the blood (mg/dL)
* serum_sodium - Level of serum sodium in the blood (mEq/L)
* sex - male (1) or female (0) (binary)
* smoking - If the patient smokes or not (boolean)
* time - Follow-up period (days)  

### Predicted Value
* DEATH_EVENT - If the patient deceased during the follow-up period (boolean)

## Web App Features  
- Provides dataframe exploration
- Configurable visualization settings
- Interactive widgets for customizing predictor values

## Views
- Home page![](https://github.com/Randell-janus/heart-failure-prediction/blob/main/public/home.JPG)
- Data exploration![](https://github.com/Randell-janus/heart-failure-prediction/blob/main/public/data%20exploration.JPG)
- Data visualization![](https://github.com/Randell-janus/heart-failure-prediction/blob/main/public/visualization.JPG)
- Main page![](https://github.com/Randell-janus/heart-failure-prediction/blob/main/public/main.JPG)
