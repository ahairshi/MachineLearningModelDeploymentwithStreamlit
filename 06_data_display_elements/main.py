import streamlit as st
import pandas as pd

df = pd.read_csv("data/sample.csv", dtype="int")

st.dataframe(df)
st.write(df)

st.table(df)

st.metric(label="Expenses", value=900, delta=20, delta_color="normal")
st.metric(label="Expenses", value=900, delta=-20, delta_color="inverse")

st.metric(label="Population", value=10000, delta=20, delta_color="normal")
st.metric(label="Population", value=9900, delta=-100, delta_color="normal")