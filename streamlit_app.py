import streamlit as st
import  pandas as pd 
st.title('ML app 😒')

st.info('This is a ML app')

with st.expander('Data'):
  st.write(**Raw data**)
  
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
