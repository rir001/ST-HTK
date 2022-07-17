import streamlit as st
import pandas as pd
import numpy as np
import os
from todo import todo_list


st.set_page_config(
     page_title="Matatabot",
     layout="wide",
     initial_sidebar_state="collapsed",
)


st.title('Matatabot')

c1, c2 = st.columns([3, 1])

c1.subheader("Descripcion:")


c1.subheader("Pendientes:")
todo_list("01_🤖_Matatabot.csv", c1)



c2.image('https://fast.matatalab.com/cdn/ff/nev7sH9-ncolshyca7fwuwPlDgDpX6NewLrv5aiW-H0/1598513311/public/2020-08/matatabot.jpg')

st.markdown("---")

st.header("Resultados:")
st.subheader("Nº1 - aaaaa")
st.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
st.subheader("")
st.subheader("Nº2 - aaaaa")
st.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
st.subheader("")
st.subheader("Nº3 - aaaaa")
st.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


