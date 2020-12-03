import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

btc_csv = pd.read_csv('btc.csv')
btc_year_2017 = pd.read_csv('btc_year_2017.csv')

#week_list = list(range(0,52,1))

week1, week2 = st.sidebar.slider('Select the range of weeks:', 0, 51, (0, 25))

def my_random_variable ():
    return np.random.rand( week1 ).sum()

import matplotlib.pyplot as plt
sample = [ my_random_variable() for i in range(week2)]

btc_year_2017 = btc_year_2017.iloc[week1*7:week2*7]
plt.plot(btc_year_2017['date'], btc_year_2017['CapMrktCurUSD'] )
plt.ylabel('Market Cap (Hundred Billion USD)')
plt.xlabel('Date')
plt.title('Bitcoin Market Cap 2017')
locs, texts = plt.xticks()
which_ones = list(range(0,len(btc_year_2017),50))
locs = [ locs[i] for i in which_ones ]
texts = btc_year_2017['date'].iloc[which_ones].to_list()
plt.xticks( locs, texts, rotation=90 )
st.pyplot(plt.gcf())
