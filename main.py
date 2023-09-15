import streamlit  as st
import pandas as pd

st.header("CYBER HOSTELER CONTACT DETAILS")
dataset = pd.read_csv("CSCH CONTACT DETAILS.csv")

st.dataframe(dataset)