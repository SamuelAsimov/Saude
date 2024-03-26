import pandas as pd
import numpy as np
import streamlit as st


#setando a configuração da pagina
st.set_page_config(layout='wide', page_title="Saude")

st.title("Dados sobre o SINAN")
st.divider()

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Acidentes de Trabalho", "Botulismo", "Cancer", "Desease", "Difteria", "Intoxicação", "Kombate", "Lepstopirose", "Meningite", "Tuberculose"])

with tab1:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiYmNlNDA4NDMtZDJhNC00N2U2LTgzNzAtNmJlNWQ2YWQ2ZjMyIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)

with tab2:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiNjdmZWE2NzctZGQ5Ny00NmIyLWJkYzEtYTM5YTQ4YTcxZjJmIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)


with tab3:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiZjZhNGJmZTQtM2U5ZS00MDViLWI0ZGQtZGYzMjY4ZjkzZTBkIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
    
with tab4:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiODdjNTMyY2UtNzljMy00NDE0LTg3MzQtMGJlMjg0NDZjNjc4IiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
    
with tab5:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiYmM0MWQ1YzItMjUzMy00NDQ2LWFhZjMtYmVlZTcwY2E3MDQ2IiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
    
with tab6:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiMjMzYjk0YmUtM2FiOC00MjM2LWE5MTgtMjRhNzY5NWIyYWQwIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
    
with tab7:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiODZjNDdiY2ItNTk1Mi00NzAzLTk3ZjItNWM3OWVlODE1M2U5IiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
    
with tab8:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiYzQ5ZTQ5N2EtOGE2Ni00MWNiLTg2OGItNmRlMmUwNjA0MjRiIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
    
with tab9:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiMTU5ZWM0NDktN2NhMi00YzNmLTllYTItMzczNjVmZWVlN2RiIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
    
with tab10:
    st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiMTJmNTkzZmItMGY2OC00ZjUwLWIxNTItMzc0MTczZDI1YjQ5IiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="600"></iframe>', unsafe_allow_html=True)
