import streamlit as st
import pandas as pd
import numpy as np
import os

def todo_list (archivo, c):
    with open(f"csv/{archivo}", "r") as ToDo:
        ToDo = ToDo.read().strip().split(';')
        for n in range(len(ToDo)):
            ToDo[n] = ToDo[n].split(',')

            if c.checkbox( f"--> {ToDo[n][1]}", value = int(ToDo[n][0]) ):
                ToDo[n][0] = '1'
            else:
                ToDo[n][0] = '0'

    if c.button("add"):
        # st.write(ToDo)
        text = c.text_input("Ingrese texto")
        # if text != '':
        #     ToDo.append([0, text])

    with open(f"csv/{archivo}", "w") as list:
        for n in range(len(ToDo)):
            ToDo[n] = ','.join(ToDo[n])
        ToDo = ';'.join(ToDo)

        list.write(ToDo)