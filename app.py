import streamlit as st

from default_docs import DEFAULT_DOCS
from search_docs import search_docs


st.set_page_config(page_title='Information retrieval')

searched_txt = st.text_input('Search term')
st.write('Press enter after entering your query')

results, frequency_mat, weights_mat = search_docs(searched_txt, DEFAULT_DOCS)


if frequency_mat is not None:
    st.header('Results')
    st.table(results)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Frequency matrix')
        st.table(frequency_mat)
    with col2:
        st.subheader('Weights matrix')
        st.table(weights_mat)
else:
    st.header('All documents')
    st.table(results)
