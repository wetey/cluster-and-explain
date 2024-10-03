from utils.welcome import Session
from utils.clustering import clustering
from utils.explanation import explanation
import streamlit as st

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

session = Session()

with st.sidebar:
    st.write('use the sidebar to select the language, embedding type, and operation.')
    with st.form("options_form", border = False):

        #select boxes
        language = st.selectbox(label = "language", 
                                options = ('ar', 'en'),
                                format_func=lambda x: language_options.get(x),
                                placeholder="select a language...",
                                index = None)
                                # key = "language_selection")

        embedding_type = st.selectbox(label = "embedding type",
                                    options = ('lhs', 'sb', 'lf', 'concat'),
                                    format_func=lambda x: embedding_options.get(x),
                                    placeholder="select an embedding type...",
                                    index = None)
                                    #   key = "embedding_selection")

        operation = st.selectbox("Operation", 
                            ("labeling", "summaries"),
                            format_func=lambda x: operation_options.get(x),
                            placeholder="select an operation...",
                            index = None)
                            # key = "operation_selection")

        submit = st.form_submit_button("submit")

        if submit:
            cluster_path = f'data/clustering/{language}_{embedding_type}_clustering.json'
            explain_path = f'data/{operation}/{language}_{embedding_type}_{operation}.json'
            session.set_params( language, 
                                embedding_type, 
                                operation, 
                                explain_path, 
                                cluster_path)
            
if session.cluster_path is not None:
    st.markdown('## clustering')
    clustering(cluster_path, session)

if session.explain_path is not None:
    if session.operation == 'labeling':
        st.markdown(f'## labels')
    else:
        st.markdown(f'## {session.operation}')
