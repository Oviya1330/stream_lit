import streamlit as st
import  pandas as pd 
st.title('ML app 😒')

st.info('This is a ML app')

with st.expander('Data'):
  st.write('**Raw data**')
  
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
  st.write('**X**')
  X =df.drop('species',axis=1)
  X
  st.write('**Y**')
  Y = df.species
  Y
with st.expander('Data viz'):
  st.scatter_chart(data=df, x= 'bill_length_mm', y= 'body_mass_g', color ="species")
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('sex',('male','female'))
  bill_length_mm = st.slider('bill_length_mm', 32.1,59.6,43.9)

  data = {'island': island,
        'bill_length_mm': bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g,
        'sex': gender}

with st.expander('Sample'):
  st.write('**input_penguins**')
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X_raw], axis=0)
