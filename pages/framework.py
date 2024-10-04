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

st.set_page_config(page_title='cluster and explain',
                   layout='wide')

with st.sidebar:
    st.write('use the sidebar to select the language, embedding type, and operation')

    language = st.selectbox(label = "language", 
                            options = ('ar', 'en'),
                            format_func=lambda x: language_options.get(x),
                            placeholder="select a language...",
                            index = None)

    embedding_type = st.selectbox(label = "embedding type",
                                options = ('lhs', 'sb', 'lf', 'concat'),
                                format_func=lambda x: embedding_options.get(x),
                                placeholder="select an embedding type...",
                                index = None)

    operation = st.selectbox("Operation", 
                        ("labeling", "summaries"),
                        format_func=lambda x: operation_options.get(x),
                        placeholder="select an operation...",
                        index = None)

    if language and embedding_type and operation:
        cluster_path = f'data/clustering/{language}_{embedding_type}_clustering.json'
        explain_path = f'data/{operation}/{language}_{embedding_type}_{operation}.json'
        session.set_params( language, 
                            embedding_type, 
                            operation, 
                            explain_path, 
                            cluster_path)
            
    st.markdown('''## navigating the interface''')
    st.markdown('''### interactive clustering plot:''')
    st.markdown('if you hover over the data points you can see more information about the data point. if you want to see all the points that belong to a specfic cluster, select the cluster you\'re interested in by clicking the cluster number from the legend. you can select multiple cluster by holding down the shift button and selecting all clusters you\'re interested in.')
    st.markdown('''### selecting clusters''')
    st.markdown('''select the clusters you\'re interested in learning more about.''')

if session.cluster_path is not None:
    st.markdown('## clustering')
    clustering(cluster_path)
    
if session.explain_path is not None:
    if session.operation == 'labeling':
        st.markdown(f'## labels')
    else:
        st.markdown(f'## {session.operation}')
    
    explanation(explain_path,session)
