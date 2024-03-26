import pandas as pd
import numpy as np
import streamlit as st


#setando a configuração da pagina
st.set_page_config(layout='wide', page_title="Saude")

st.title("Dados sobre o SIH")
st.divider()

st.markdown('<iframe src="https://app.powerbi.com/view?r=eyJrIjoiMzgyNTA0MjQtNDBmZi00ZTRiLWIzY2UtZTU0ZWJmMWNkMWEyIiwidCI6ImFkYWMzNzYyLWYzMWQtNDliNS1iYWI1LWY3NjcxNzZmZjQyNSJ9" width="100%" height="3000"></iframe>', unsafe_allow_html=True)
