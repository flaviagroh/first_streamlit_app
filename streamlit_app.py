import streamlit as st
import pandas

st.title('My Parents Super New Healthy Dinner')
st.write('My first app')
st.write('Hello *world!*')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
