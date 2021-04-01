import streamlit as st
import numpy as np
import pandas as pd 
import altair as alt

from PIL import Image
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(page_title='Heart Failure EDA')

st.title('Heart Failure Prediction')
st.subheader('This app uses the ***Random Forest Classifier***')
st.write('---')

st.sidebar.header('Directory')
app = st.sidebar.selectbox('', ['Explore Data', 'Predict Mortality', 'Citation'])

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

if app == 'Explore Data':
    about_expander = st.beta_expander('About',expanded=True)
    with about_expander:
        img = Image.open('heartattack.jpg')
        st.image(img)
        st.write("""
                Cardiovascular diseases (CVDs) are the **number 1 cause of death** globally, 
                taking an estimated 17.9 million lives each year, which accounts for 31 
                percent of all deaths worlwide. Heart failure is a common event caused 
                by CVDs and this dataset contains 12 features that can be used to predict 
                mortality by heart failure.
                """)

    st.subheader('**Explore the dataset**')
    col1, col2 = st.beta_columns(2)
    selectbox_options = col1.selectbox('Transform', ['Head','Tail', 
                                                        'Describe','Shape', 
                                                        'DTypes', 'Value Count'])
    if selectbox_options == 'Head':
        input_count = col2.number_input('Count', 5, 50, help='min=5, max=50')
        st.write(df.head(input_count))
    elif selectbox_options == 'Tail':
        input_count = col2.number_input('Count', 5, 50, help='min=5, max=50')
        st.write(df.tail(input_count))
    elif selectbox_options == 'Describe':
        st.write(df.describe())
    elif selectbox_options == 'Shape':
        st.write(df.head())
        st.write('Shape: ', df.shape)
    elif selectbox_options == 'DTypes':
        st.write(df.dtypes)
    
    st.write('---')
    numeric_df = df.select_dtypes(['float64', 'int64'])
    numeric_cols = numeric_df.columns

    st.subheader('**Filter columns with Multiselect**')
    st.write("""This feature is for comparing certain columns in the dataset.
                You may add only the columns you wish to compare and explore.
                """)
    feature_selection = st.multiselect('', options=numeric_cols)
    df_features = df[feature_selection]
    st.write(df_features)
    st.write('---')

    st.sidebar.subheader('Visualization Settings')
    y_axis = st.sidebar.selectbox('Select y-axis', ['age', 'ejection_fraction', 
                                                    'time'])
    x_axis = st.sidebar.selectbox('Select x-axis', ['platelets', 'creatinine_phosphokinase', 
                                                    'serum_creatinine', 'serum_sodium'])
    label = st.sidebar.selectbox('Select label', ['DEATH_EVENT', 'anaemia', 'diabetes', 
                                                    'high_blood_pressure', 'sex', 
                                                    'smoking'])
    st.subheader('**Visualization**')
    st.write("""Customize the x and y axis through the sidebar visualization settings. 
                You can also select binary features as labels which will be in the form 
                of a color.""")
    select_graph = st.sidebar.radio('Select Graph', ('point', 'bar', 'area', 'line'))

    col1, col2, col3 = st.beta_columns([.5,.5,1])
    graph_hgt = col1.slider('Height', 200, 600, 400, step=10)
    graph_wgt = col2.slider('Width',400, 800, 600, step=10)
        
    df = df.loc[(df.creatinine_phosphokinase < 800) & (df.platelets < 500000) & 
                (df.serum_creatinine < 2.2) & (df.age >= 40)]

    chart = alt.Chart(data=df, mark=select_graph).encode(alt.X(x_axis, scale=alt.Scale(zero=False)), 
                                                            alt.Y(y_axis, scale=alt.Scale(zero=False)),color=label).properties(
        height=graph_hgt,width=graph_wgt)
    st.write(chart)
    
    if y_axis == 'age' and x_axis == 'platelets' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had platelet count ranging from 150,000 - 300,000 and aged 58 - 75')
    elif y_axis == 'age' and x_axis == 'creatinine_phosphokinase' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had creatinine phosphokinase count ranging from 100 - 250 and aged 55 - 70')
    elif y_axis == 'age' and x_axis == 'serum_creatinine' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had serum creatinine count ranging from 1.2 - 1.9 and aged 50 - 75')
    elif y_axis == 'age' and x_axis == 'serum_sodium' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had serum sodium count ranging from 134 - 140 and aged 55 - 80')
    
    elif y_axis == 'ejection_fraction' and x_axis == 'platelets' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had platelet count ranging from 150,000 - 250,000 and ejection fraction count of 10 - 30') 
    elif y_axis == 'ejection_fraction' and x_axis == 'creatinine_phosphokinase' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had creatinine phosphokinase count ranging from 50 - 175 and ejection fraction count of 20 - 30') 
    elif y_axis == 'ejection_fraction' and x_axis == 'serum_creatinine' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had serum creatinine count ranging from 1.8 - 2 and ejection fraction count of 20 - 40') 
    elif y_axis == 'ejection_fraction' and x_axis == 'serum_sodium' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had serum_sodium count ranging from 134 - 138 and ejection fraction count of 20 - 40') 
        
    elif y_axis == 'time' and x_axis == 'platelets' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had platelet count ranging from 150,000 - 350,000 and a follow up time of less than 50 days') 
    elif y_axis == 'time' and x_axis == 'creatinine_phosphokinase' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had creatinine phosphokinase count ranging from 50 - 250, 550 - 600, and a follow up time of less than 50 days') 
    elif y_axis == 'time' and x_axis == 'serum_creatinine' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had serum creatinine count ranging from 0.9 - 1.5 and follow up time of less than 50 days') 
    elif y_axis == 'time' and x_axis == 'serum_sodium' and label == 'DEATH_EVENT':
        st.write('Majority of deceased patients had serum_sodium count ranging from 134 - 140 and follow up time of less than 100 days') 
        

elif app == 'Predict Mortality':
    st.sidebar.subheader('User Input Features')

    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
    X = df.drop('DEATH_EVENT', axis=1)
    y = df['DEATH_EVENT']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)

    def user_input_features():
        display = ("Female (0)", "Male (1)")
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
    st.subheader('**Conclusion:**')
    pred_button = st.button('Predict')
    if pred_button:
        if user_result[0] == 0:
            st.success('Patient survived during the follow-up period (0)')
        else:
            st.error('Patient deceased during the follow-up period (1)')

else:
    st.header('**References/Citation**')
    st.subheader('**Dataset**')
    st.write('The dataset is from user **Larxel** of Kaggle')
    st.write('Davide Chicco, Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16 (2020).')
