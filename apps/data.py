import streamlit as st
import pandas as pd
import altair as alt 

def app():
    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
    about_expander = st.beta_expander('About',expanded=True)
    with about_expander:
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
                                                     'DTypes', 'Default'])
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
    else:
        st.write(df.sort_index())
        
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
        
    df = df.loc[(df.creatinine_phosphokinase < 800) & (df.platelets < 500000) 
        & (df.serum_creatinine < 2.2) & (df.age >= 40)]
    
    chart = alt.Chart(data=df, mark=select_graph).encode(alt.X(x_axis, scale=alt.Scale(zero=False)), 
                                                         alt.Y(y_axis, scale=alt.Scale(zero=False)),color=label).properties(
        height=graph_hgt,width=graph_wgt)
    st.write(chart)
    
    
    
    
        
    
