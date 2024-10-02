import streamlit as st
import os
import pandas as pd



LANGUAGE_SELECTION  = st.session_state['language_selection']
EMBEDDING_SELECTION = st.session_state['embedding_selection']
OPERATION_SELECTION = st.session_state['operation_selection']


dataset_path = f'data/{OPERATION_SELECTION}/{LANGUAGE_SELECTION}_{EMBEDDING_SELECTION}_{OPERATION_SELECTION}.json'

if os.path.isfile(dataset_path):
    dataset = pd.read_json(dataset_path)
else:
    st.write(f'the file you picked does not exists.\nreading the labels generated for {LANGUAGE_SELECTION} and {EMBEDDING_SELECTION}')
    dataset = pd.read_json(f'data/labeling/{LANGUAGE_SELECTION}_{EMBEDDING_SELECTION}_labeling.json')