import pandas as pd
import numpy as np
import streamlit as st


#setando a configuração da pagina
st.set_page_config(layout='wide', page_title="Saude")

st.title("Dados sobre saude")
st.divider()

tab1, tab2 = st.tabs(["Vacinas", "SisReg"])

with tab1:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiYWNjOWY1NzYtZmZjMi00MjliLTk5MDMtNDU4Yzk1ZDE5ZTIxIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)

with tab2:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiYzgzZDRjYTUtZjNhZS00NmE3LThlMGQtMDc5N2I1OWY2MGE1IiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
