from nbformat import write
import streamlit as st
import pandas as pd
import numpy as np
import os


st.set_page_config(
     page_title="Botley",
     layout="wide",
     initial_sidebar_state="collapsed",
)


st.title('Botley')

col1, col2 = st.columns([3, 1])



col1.checkbox('--> aplicar ing inversa app')



col2.image('https://images.playosmo.com/shopping/product-renders-square/osmo_coding_sk.jpg')

