import streamlit as st
import  pandas as pd 
from sklearn.ensemble import RandomForestClassifier
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
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))

  data = {'island': island,
        'bill_length_mm': bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g,
        'sex': gender}


  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X], axis=0)

encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
input_row = df_penguins[:1]

target_mapper = {'Adelie': 0,
                 'Chinstrap': 1,
                 'Gentoo': 2}
target = lambda p:target_mapper[p]


Y = Y.apply(target)  

with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguins data**')
  input_penguins


with st.expander('Data Preparation'):
  st.write('**encoded input row**')
  X = df_penguins[1:]
  X
  st.write('**encoded y **')
  Y
  
clf = RandomForestClassifier()
clf.fit(X,Y)


prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)
with st.expander('Prediction'):
  prediction
df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']
df_prediction_proba.rename(columns={0: 'Adelie',
                                 1: 'Chinstrap',
                                 2: 'Gentoo'})
with st.expander('Prediction'):
  
  df_prediction_proba
