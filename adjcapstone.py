import pandas as pd
import numpy as np
import streamlit as st
#import plotly
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from plotly.subplots import make_subplots
from datetime import date
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import openpyxl
import io
from random import randint

import calendar

# use wide layout
st.set_page_config(layout='wide')

# hide 'made with streamlit'
st.markdown("""<style>footer{visibility:hidden;}</style>""",unsafe_allow_html=True)



# create widget to upload files
uploaded_files = st.sidebar.file_uploader("Upload Files", type="csv", accept_multiple_files=True) 


   
    
@st.cache(allow_output_mutation=True, show_spinner=False)
def load_data(uploaded_files):
    
    data = pd.DataFrame()
    for i in uploaded_files: 
        df = pd.read_csv(i,encoding='latin-1') 
        data = data.append(df)
            
    # Drop columns
    cols_to_drop=['Item Code','Pack','Symb','Discount','V.A.T','Item Type Code','Supplier','Tel','Group Code'
                      ,'Sub-Group Code','Country Code','Brand Code','Unit-Measure Code','salespersoncode','Details',
                      'salespersondescription']
    data.drop(cols_to_drop, axis=1, inplace = True)
    return data   

        

if uploaded_files:
    df = load_data(uploaded_files)  
    x = df.head()  
    x  