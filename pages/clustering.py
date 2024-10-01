import streamlit as st
import pandas as pd
import altair as alt

LANGUAGE_SELECTION  = st.session_state['language_selection']
EMBEDDING_SELECTION = st.session_state['embedding_selection']

dataset = pd.read_json(f'data/clustering/{LANGUAGE_SELECTION}_{EMBEDDING_SELECTION}_clustering.json')

scatter = alt.Chart(dataset).mark_point(size=200, filled=True).encode(
    x = alt.X('x:Q', axis=None),
    y = alt.Y('y:Q', axis=None),
    color = alt.Color('cluster:N',
                      scale=alt.Scale(scheme='category20b')
                      ).legend(direction = 'vertical', 
                               symbolSize = 200, 
                               labelFontSize=14, 
                               titleFontSize=20,
                               titleColor='black',
                               labelColor='black'),
    #TODO change the predicated and label to strings
    tooltip = ['cluster:N',"string_pred:N", "string_label:N"],
    ).properties(
        width = 1000,
        height = 600
    ).interactive()

st.altair_chart(scatter)

