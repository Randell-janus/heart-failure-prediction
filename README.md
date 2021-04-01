# Heart Failure Prediction
#### Machine learning Streamlit web app to predict mortality caused by Heart Failure
https://share.streamlit.io/randell-janus/heart-failure-prediction/main/app.py  
  
## Dataset Source  
The dataset is from Kaggle. The authors are Davide Chicco and Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16 (2020).  
  
## Web App Features  
* Sidebar Directory  
  * Explore Data  
    * About information on Heart Failure.  
    * Dataset exploration with selected pandas functions.
    * Multiselect box feature for specific column comparison.
    * Visualization area with customizable axes and plot types.
  * Predict Mortality  
    * User input features on sidebar (check boxes, radio buttons, sliders, and number inputs).   
    * Dataframe base on the user inputs.   
    * Conclusion button to predict the mortality. 
  * Citation
    * Dataset source
* Machine Learning Model
  * Random Forest Classifier  
  
## Predictor Values
* age
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
## Predicted Value
* DEATH_EVENT - If the patient deceased during the follow-up period (boolean)
    
