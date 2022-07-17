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



col1.checkbox('--> deshechar')



col2.image('https://www.toysrus.ca/dw/image/v2/BDFX_PRD/on/demandware.static/-/Sites-toys-master-catalog/default/dw0a4f7f20/images/F4EEF8E1_1.jpg?sw=767&sh=767&sm=fit')