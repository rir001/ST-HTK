import streamlit as st
import pandas as pd
import numpy as np
import os
from todo import todo_list


st.set_page_config(
     page_title="Botley",
     layout="wide",
     initial_sidebar_state="collapsed",
)


st.title('Botley')

c1, c2 = st.columns([3, 1])

c1.subheader("Descripcion:")


c1.subheader("Pendientes:")
todo_list("02_🕹️_Botley.csv", c1)



c2.image('https://www.toysrus.ca/dw/image/v2/BDFX_PRD/on/demandware.static/-/Sites-toys-master-catalog/default/dw0a4f7f20/images/F4EEF8E1_1.jpg?sw=767&sh=767&sm=fit')

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
