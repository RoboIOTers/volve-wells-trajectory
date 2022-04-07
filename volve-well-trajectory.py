import streamlit as st
import welly
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup #for web scraping purposes to pull the data out of HTML and XML files
import pandas as pd
import plotly.express as ps

columns = ['md','tvd','azi','incl','dispNs','dispEw']
wells = [
    '9-F-1 C',
    '9-F-4',
    '9-F-5' ,
    '9-F-7',
    '9-F-9',
    '9-F-11',
    '9-F-12',
    '9-F-14',
    '9-F-15']


df_all_wells = pd.DataFrame()
for well in wells:
    filepath = "volve-wells-trajectory/" + well +".xml"
    with open(filepath) as f:
        data = f.read()
    data_xml = BeautifulSoup(data,'xml')
    df = pd.DataFrame()
    for col in columns:
        df[col] = [float(x.text) for x in data_xml.find_all(col)]
    df['well'] = well
    
    df_all_wells= pd.concat([df_all_wells, df], ignore_index = True)

fig =ps.line_3d(df_all_wells,'dispNs','dispEw','nmd','well')
fig.show()
st.pyplot(fig)
