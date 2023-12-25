import streamlit as st
from streamlit import components
import os

st.write("testing Orange")

with st.spinner():
    try:
        os.system("./test.sh")
        st.write("done")

    except:
        st.write("error")