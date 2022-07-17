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
todo_list("03_🪞_Osmo_coding.csv", c1)



c2.image('https://images.playosmo.com/shopping/product-renders-square/osmo_coding_sk.jpg')

