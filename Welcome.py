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

select_file = st.selectbox('Select Location', file_name_list)

df = pd.read_csv(select_file)
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('Select Element X', el_list)
y_axis = st.selectbox('Select Element Y', el_list)

p = figure(title='simple line example', x_axis_label=x_axis, y_axis_label=y_axis)
p.x_range = Range1d([np.min(df[x_axis]/10000)], [np.max(df[x_axis]/10000)])
p.y_range = Range1d([np.min(df[y_axis]/10000)], [np.max(df[y_axis]/10000)])
#p.y_range = 

p.circle(df[x_axis]/10000, df[y_axis]/10000)
p.line([np.min(df[x_axis]/10000), np.max(df[y_axis]/10000)], [5, 5])
p.rect(x = 24, y = 4)
st.bokeh_chart(p, use_container_width=True)

#st.multiselect('select location', file_name_list, file_name_list[0])
