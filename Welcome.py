import streamlit as st
import pandas as pd
import altair as alt

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
# def create_session_states(language, embedding_type, operation):

#     if 'language_selection' not in st.session_state:
#         if language == "arabic":
#             st.session_state['language_selection'] = 'ar'
#         else:
#             st.session_state['language_selection'] = 'en'

#     if 'embedding_selection' not in st.session_state:
#         if embedding_type == "last hidden state":
#             st.session_state['embedding_selection'] = "lhs"
#         elif embedding_type == "sentence-bert":
#             st.session_state['embedding_selection'] = "sb"
#         elif embedding_type == "linguistic features":
#             st.session_state['embedding_selection'] = "lf"
#         elif embedding_type == "concatenated":
#             st.session_state['embedding_selection'] = "concat"

#     if 'operation_selection' not in st.session_state:
#         st.session_state['operation_selection'] = operation

st.set_page_config(page_title="clustering and explaining errors")

st.write("# clustering and explaining errors")

st.markdown(
    """
    a typical NLP classification task consists of fine-tuning a language model on a specific dataset. 
    
    these models rarely, if ever, achieve 100% accuracy. We developed a framework to help uncover the potential reasons behind the misclassification. 

    the framework consists of two stages: 1. clustering 2. generating a natural language explanation

    select the language and embedding type:
    """
)


language = st.selectbox(label = "language", 
                        options = ('ar', 'en'),
                        format_func=lambda x: language_options.get(x),
                        key = "language_selection")

embedding_type = st.selectbox(label = "embedding type",
                              options = ('lhs', 'sb', 'lf', 'concat'),
                              format_func=lambda x: embedding_options.get(x),
                              key = "embedding_selection")

operation = st.selectbox("Operation", 
                    ("labeling", "summary"),
                    key = "operation_selection")

