import streamlit as st


st.set_page_config(page_title="clustering and explaining errors")

st.write("# clustering and explaining errors")

st.markdown(
    """
    a typical NLP classification task consists of fine-tuning a language model on a specific dataset. 
    
    these models rarely, if ever, achieve 100% accuracy. we developed a framework to help uncover the potential reasons behind the misclassification. 

    the framework consists of two stages: 1. clustering 2. generating a natural language explanation
    """
)

#TODO make it more visible 
st.page_link('pages/framework.py', label = 'click to get started')



