import pandas as pd
import numpy as np
import streamlit as st
import webbrowser

#setando a configuração da pagina
st.set_page_config(layout='wide', page_title="Saude")

st.title("Sistema Saude")
st.divider()
st.text('''Explorando os Dados do Sistema de Saúde com Data Mining e Power BI

Nos bastidores da complexa teia de informações do sistema de saúde, reside um vasto mar de dados que espera ser explorado e compreendido. 
Através de meticulosos esforços e uma combinação de tecnologias avançadas, mergulhamos nesse oceano de informações para trazer à luz insights valiosos
e relevantes.
Com a ajuda de scripts de análise personalizados, meticulosamente criados por nossos especialistas em dados, embarcamos em uma jornada pelo vasto 
repositório do DATASUS, uma fonte rica e diversificada de dados de saúde. Esses scripts foram projetados para navegar através dos intricados 
detalhes dos conjuntos de dados, identificar padrões ocultos e extrair informações significativas.
        
Utilizando técnicas de Data Mining, mergulhamos profundamente nos dados, explorando padrões, correlações e tendências. Cada linha de código executada
representava uma oportunidade de descoberta, revelando insights que poderiam moldar políticas de saúde, melhorar os cuidados ao paciente e impulsionar
a eficiência dos serviços médicos.
No entanto, a verdadeira transformação aconteceu quando esses insights foram traduzidos em visualizações dinâmicas e intuitivas. Com a ajuda do Power BI,
uma poderosa ferramenta de Business Intelligence, demos vida aos dados, criando dashboards interativos que fornecem uma visão abrangente e acessível das 
informações.

Os dashboards criados oferecem uma panorâmica detalhada de uma variedade de métricas e indicadores de saúde, desde taxas de mortalidade até padrões 
de doenças específicas, passando por análises geográficas e demográficas. Cada gráfico e cada tabela conta uma história, permitindo que os usuários 
explorem os dados de maneira personalizada e obtenham insights relevantes de forma rápida e eficaz.

Essas ferramentas não apenas capacitam os profissionais de saúde e os formuladores de políticas a tomar decisões informadas e baseadas em evidências, 
mas também abrem portas para a inovação e o avanço contínuo no campo da saúde pública.

À medida que continuamos a nossa jornada de exploração e análise de dados, estamos conscientes do poder transformador dessas informações.
Cada descoberta, cada insight,é uma peça crucial no quebra-cabeça da saúde pública, moldando um futuro mais saudável e mais resiliente para todos.''')
st.divider()

st.subheader("Para facilitar a navegação o sistema foi divido em paginas que podem ser encontradas no menu lateral!")

st.divider()

st.text(''' Ainda esta disponibilizado abaixo um link para acesso do drive com todos os arquivos utilizados para essa analize de dados''')
url = 'https://drive.google.com/drive/folders/1nPPD9PivSLVOm4tQ4o4kwbnA2NGeuRan?usp=sharing'
if st.button('Acessar Drive'):
    webbrowser.open(url)
