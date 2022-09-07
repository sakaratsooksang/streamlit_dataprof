import streamlit as st
import pandas as pd 
import subprocess 
try : import seaborn
except: subprocess.call(["pip","install","seaborn"])
import seaborn as sns
import numpy as np

st.title('🎈 Dataframe Display 🎈')
st.sidebar.subheader("Input")
source = st.sidebar.text_input("Souce Data","")
# https://github.com/dataprofessor/data/blob/master/iris.csv

if source :
    st.subheader("Output")
    st.info(f"the github url of your data is : {source}")
    st.subheader("Dataframe Display")
    df = pd.read_csv(source)
    choice = df.columns.append(pd.Index(np.array(["All"])))
    option = st.selectbox(
     'Show only selected column',
     choice)
    st.write('You selected:', option)
    if option == "All":
        st.write(df)
    else:
        st.write(df[option])
    figure = sns.pairplot(df, hue=df.keys()[-1])
    st.subheader("Plotting dataset")
    st.pyplot(figure)
    
else : 
    st.subheader("Enter Your Input")
    st.warning('Awaiting your input')
