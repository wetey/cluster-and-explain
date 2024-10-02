import streamlit as st
import pandas as pd
import altair as alt

LANGUAGE_SELECTION  = st.session_state['language_selection']
EMBEDDING_SELECTION = st.session_state['embedding_selection']

dataset = pd.read_json(f'data/clustering/{LANGUAGE_SELECTION}_{EMBEDDING_SELECTION}_clustering.json')

scatter = alt.Chart(dataset).mark_point(size=300, filled=True).encode(
    x = alt.X('x:Q', axis=None),
    y = alt.Y('y:Q', axis=None),
    color = alt.Color('cluster:N',
                      scale=alt.Scale(scheme='category20b')
                      ).legend(direction = 'vertical', 
                               symbolSize = 200, 
                               labelFontSize=20, 
                               titleFontSize=24,
                               titleColor='#888da7',
                               labelColor='#888da7'),
    tooltip = ['cluster:N',"string_pred:N", "string_label:N"],
    ).properties(
        width = 1000,
        height = 600
    ).interactive()

st.altair_chart(scatter)

