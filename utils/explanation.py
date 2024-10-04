import streamlit as st
import os
import pandas as pd

def multiselect():
    pass

def explanation(explain_path, session):

    explain = pd.read_json(explain_path)

    clusters = explain.cluster.tolist()

    if session.operation == 'labeling':
        operation = 'label'
    else:
        operation = 'summary'

    options = st.multiselect(" ",
                                clusters,
                                default = None)

    if st.button('view information about cluster(s)'):
        for option in options:
            st.markdown(f'### cluster {option}')
            st.markdown(f'{explain[operation][option]}')
