import streamlit as st
import pandas as pd
import numpy as np
import os


st.set_page_config(
     page_title="Matatabot",
     layout="wide",
     initial_sidebar_state="collapsed",
)


st.title('Matatabot')

col1, col2 = st.columns([3, 1])



col1.checkbox('--> investigar linealidad procesamiento codigo')
col1.checkbox('--> investigar modelo placa')
col1.checkbox('--> investigar aplicacion y conexion bluetooht')



col2.image('https://fast.matatalab.com/cdn/ff/nev7sH9-ncolshyca7fwuwPlDgDpX6NewLrv5aiW-H0/1598513311/public/2020-08/matatabot.jpg')


