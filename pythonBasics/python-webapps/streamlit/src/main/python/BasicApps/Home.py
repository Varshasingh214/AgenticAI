import streamlit as st
import pandas as pd

st.title("this is my first webapp using streamlit")

st.write('new line in my webapp')

lang_selected = st.radio("select language", ["python", "java"])


if lang_selected == "python":
    df = pd.read_csv("/Users/varshasingh/PycharmProjects/pythonBasics/twitter_data.csv/part-00000-55870fcf-0fa5-4c4e-8aad-28bec0b21135-c000.csv")

    df1 = df["created_at"]
    st.write(df1.head())
    st.write("count of records in file is : ", len(df))

else:
    st.write("code is not yet written for java")

# st.checkbox( ["python", "java"])
# st.selectbox("quarters : ", ["Q1", "Q2"])
# how to create containers?
# Hyperlink
# videos preview

# create a webapp for learning spark:
