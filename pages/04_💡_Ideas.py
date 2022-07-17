import streamlit as st
import pandas as pd
import numpy as np
import os
from todo import todo_list

st.set_page_config(
     page_title="Hack the kit",
     layout="wide",
     initial_sidebar_state="expanded",
 )


st.title("Ideas")
todo_list("04_💡_Ideas.csv", st)


