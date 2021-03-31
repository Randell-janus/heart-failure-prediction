import streamlit as st
from multiapp import MultiApp
from apps import prediction, cite, data

app = MultiApp()
st.set_page_config(page_title='Heart Failure EDA')
st.title('Heart Failure Prediction')
st.subheader('This app uses the ***Random Forest Classifier***')
#st.write('<== Check sidebar for Directory')
st.write('---')
st.sidebar.title('Directory')

app.add_app("Explore Data", data.app)
app.add_app("Predict Mortality", prediction.app)
app.add_app("Citation", cite.app)

app.run()
