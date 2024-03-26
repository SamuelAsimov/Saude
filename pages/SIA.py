import pandas as pd
import numpy as np
import streamlit as st


#setando a configuração da pagina
st.set_page_config(layout='wide', page_title="Saude")

st.title("Dados sobre o SIA")
st.divider()

tab1, tab2, tab3, tab4= st.tabs(["Dialitico", "Medicamentos", "Radio", "Producão ambulatorial"])

with tab1:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiYjdlNGNhNTItOGJkMS00YTZkLTk5MjYtYTVmZmFlZDM5NmE0IiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)

with tab2:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiOTU1YWJmMmItMTRhMi00NzQ5LWIxMWYtZTJlM2JmZGUzZTNkIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)


with tab3:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiYzBhMGI4MTUtMmYyMi00ZGU0LWEwZjEtMzllMWI2NDY3ZjMyIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)

with tab4:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiZWY5YTMyMmYtMWQ3MC00ODdiLWI4YmItOWIwMTAyYTc4ZmI0IiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
