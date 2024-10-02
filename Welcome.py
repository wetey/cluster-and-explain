import streamlit as st
import pandas as pd
import altair as alt
import os

#TODO put these all in the same object
language = None
embedding_type = None
operation = None
explain_path = None
explain = None
cluster = None
cluster_path = None

language_options = {
    'ar': 'arabic',
    'en': 'english',
}

embedding_options = {
    'lhs':'last hidden state',
    'sb':'sentence-bert',
    'lf':'linguistic features',
    'concat':'concatenated'
}

operation_options = {
    'labeling':'labeling',
    'summaries': 'summaries'
}


st.set_page_config(page_title="clustering and explaining errors")

st.write("# clustering and explaining errors")

st.markdown(
    """
    a typical NLP classification task consists of fine-tuning a language model on a specific dataset. 
    
    these models rarely, if ever, achieve 100% accuracy. we developed a framework to help uncover the potential reasons behind the misclassification. 

    the framework consists of two stages: 1. clustering 2. generating a natural language explanation

    select the language and embedding type:
    """
)

with st.form("options_form", border = False):

    #select boxes
    language = st.selectbox(label = "language", 
                            options = ('ar', 'en'),
                            format_func=lambda x: language_options.get(x))
                            # key = "language_selection")

    embedding_type = st.selectbox(label = "embedding type",
                                options = ('lhs', 'sb', 'lf', 'concat'),
                                format_func=lambda x: embedding_options.get(x))
                                #   key = "embedding_selection")

    operation = st.selectbox("Operation", 
                        ("labeling", "summaries"),
                        format_func=lambda x: operation_options.get(x))
                        # key = "operation_selection")

    submit = st.form_submit_button("submit")

    if submit:
        st.write('generating clustering...')

        cluster_path = f'data/clustering/{language}_{embedding_type}_clustering.json'

#TODO keep after submitting the other form
if cluster_path:

    cluster = pd.read_json(cluster_path)
    scatter = alt.Chart(cluster).mark_point(size=300, filled=True).encode(
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


explain_path = f'data/{operation}/{language}_{embedding_type}_{operation}.json'

if os.path.isfile(explain_path):
    explain = pd.read_json(explain_path)
else:
    st.write(f'''
            the file you picked does not exists.
            
            reading the labels generated for {language_options[language]} and {embedding_options[embedding_type]}

            ''')
    explain = pd.read_json(f'data/labeling/{language}_{embedding_type}_labeling.json')

with st.form("cluster", border = False):

    num_clusters = tuple(explain.cluster.unique())
    clusters = st.selectbox(label = "cluster",
                            options = num_clusters)

    submit = st.form_submit_button("submit")

    #TODO fix formatting
    if submit:    
        st.write(explain['summary'].tolist()[clusters])

