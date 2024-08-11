import streamlit as st

def generarMenu():
    with st.sidebar:
        st.page_link('Makers_tech.py',label="Inicio", icon="🏚️")
        st.page_link('dash.py',label="dash", icon="📄")
        st.page_link('Usuario.py',label="Usuario", icon="📄")