import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure
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
x_axis = st.selectbox('select element X', el_list)
y_axis = st.selectbox('select element Y', el_list)

p = figure(title='simple line example', x_axis_label='x', y_axis_label='y')

st.bokeh_chart(p, use_container_width=True)
p.circle(df['Si']/10000, df['Mg']/10000)
#p.line([np.min(df[x_axis]/10000), np.max(df[y_axis]/10000)], [5, 5])
show(p)

#st.multiselect('select location', file_name_list, file_name_list[0])
