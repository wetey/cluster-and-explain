import pandas as pd
import altair as alt
import streamlit as st

def clustering(cluster_path, session):

    cluster = pd.read_json(cluster_path)
    selection = alt.selection_point("point_selection",fields=['cluster'], bind = 'legend')
    color = alt.condition(
        selection,
        alt.Color('cluster:N',
                    scale=alt.Scale(scheme='category20b')
                    ).legend(direction = 'vertical', 
                            symbolSize = 200, 
                            labelFontSize=20, 
                            titleFontSize=24,
                            titleColor='#888da7',
                            labelColor='#888da7'),
        alt.value('lightgray')
        )
    scatter = alt.Chart(cluster).mark_point(size=300, filled=True).encode(
        x = alt.X('x:Q', axis=None),
        y = alt.Y('y:Q', axis=None),
        color = color,
        tooltip = ['cluster:N',"string_pred:N", "string_label:N"],
        shape = alt.Shape('string_pred:N', 
                          scale=alt.Scale(
                              range = ['circle', 'diamond', 'square']
                          )).legend(direction = 'vertical', 
                                    symbolSize = 200, 
                                    labelFontSize=20, 
                                    titleFontSize=24,
                                    titleColor='#888da7',
                                    labelColor='#888da7',
                                    title = 'predicted'), 
        ).properties(
            width = 1000,
            height = 600
        ).add_params(selection).interactive()
    
    st.altair_chart(scatter)

    


