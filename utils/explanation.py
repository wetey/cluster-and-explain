import streamlit as st
import os
import pandas as pd


def explanation(explain_path, session):
    explain = pd.read_json(explain_path)

    clusters = explain.cluster.tolist()

    if session.operation == 'labeling':
        operation = 'label'
    else:
        operation = 'summary'
    
    for cluster in clusters:
        st.markdown(f'''### cluster: {cluster}
#### {operation}: 
{explain[operation][cluster]}''')