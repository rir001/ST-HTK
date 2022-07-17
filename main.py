import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(
     page_title="Hack the kit",
     layout="wide",
     initial_sidebar_state="expanded",
 )


st.title("IPre Hack the kit")
st.subheader("Hola! Si estás aquí, probablemente te llamas Jorge o Valeria, aunque también puede que seas un entusiasta que está buscando los resultados de nuestra investigación, cualquiera sea el caso, creamos este espacio para facilitar la difusión de nuestra investigación ---")


buttons = map(lambda x : x[3:-3]  , os.listdir('pages'))

for n in buttons:
    st.button(n)

