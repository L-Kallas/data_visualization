import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import os

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)

st.write('Hello World')

select_file = st.selectbox('select location', file_name_list)

df = pd.read_csv (select_file)
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)
#y_axis = st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list, file_name_list[0])
