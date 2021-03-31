import streamlit as st
import pandas as pd
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def app():
    st.sidebar.subheader('User Input Features')
    
    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
    X = df.drop('DEATH_EVENT', axis=1)
    y = df['DEATH_EVENT']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)
    
    def user_input_features():
        display = ("Male", "Female")
        options = list(range(len(display)))
        sex = st.sidebar.radio("Sex", options, format_func=lambda x: display[x])

        smoking = st.sidebar.checkbox('Smoking')
        if smoking:
            smoking = 1
        high_blood_pressure = st.sidebar.checkbox('Hypertensive')
        if high_blood_pressure:
            high_blood_pressure = 1
        diabetes = st.sidebar.checkbox('Diabetic')
        if diabetes:
            diabetes = 1
        anaemia = st.sidebar.checkbox('Anemic')
        if anaemia:
            anaemia = 1
            
        age = st.sidebar.slider('Age', 40, 95, 60)
        ejection_fraction = st.sidebar.slider('Ejection Fraction', 14, 80, 38)
        serum_sodium = st.sidebar.slider('Serum Sodium', 113, 148, 136)
        
        creatinine_phosphokinase = st.sidebar.number_input('Creatinine Phosphokinase', 23, 7861, 581)
        platelets = st.sidebar.number_input('Platelet Count', 25100.00, 850000.00, 263358.00, help='25100 < input < 850000')
        serum_creatinine = st.sidebar.number_input('Serum Creatinine', 0.5, 9.4, 1.3)
        time = st.sidebar.number_input('Follow-up period (Days)', 4, 285, 130)
        data = {'age': age,
                'anaemia': anaemia,
                'creatinine_phosphokinase': creatinine_phosphokinase,
                'diabetes': diabetes,
                'ejection_fraction': ejection_fraction,
                'high_blood_pressure': high_blood_pressure,
                'platelets': platelets,
                'serum_creatinine': serum_creatinine,
                'serum_sodium': serum_sodium,
                'sex': sex,
                'smoking': smoking,
                'time': time
                }
        features = pd.DataFrame(data, index=[0])
        return features

    user_data = user_input_features()
    st.subheader('**User Input parameters**')
    st.write(user_data)
    my_expander = st.beta_expander('Check dataset')
    with my_expander:
        st.write(df)
    
    classifier = RandomForestClassifier()
    classifier.fit(X_train, y_train)
    user_result = classifier.predict(user_data)
    
    st.title('')
    st.subheader('**Conclusion**')
    pred_button = st.button('Predict')
    if pred_button:
        if user_result[0] == 0:
            st.success('Patient survived during the follow-up period')
        else:
            st.error('Patient deceased during the follow-up period')
    
    
