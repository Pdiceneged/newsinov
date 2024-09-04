import streamlit as st
from GoogleNews import GoogleNews
import base64

st.set_page_config(
    page_title="News Innovation",
    page_icon="📰"
)

@st.cache_data()
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("pdipaper5.png")
img2 = get_img_as_base64("pdiside.png")

page_bg_img = f"""
<style>
header, footer {{
    visibility: hidden !important;
}}

#MainMenu {{
    visibility: visible !important;
    color: #F44D00;
}}

[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:fundoesg4k/png;base64,{img}");
    background-size: cover; 
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:esgfundo1/png;base64,{img2}");
    background-position: center; 
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

.stTextInput>div>div>input[type="text"] {{
    background-color: #C5D6ED; 
    color: #000; 
    border-radius: 7px; 
    border: 2px solid #000010; 
    padding: 5px; 
    width: 500;
}}

@media (max-width: 360px) {{
    [data-testid="stAppViewContainer"] > .main, [data-testid="stSidebar"] > div:first-child {{
        background-size: auto;
    }}
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.image("Logopdi.png", width=250)

def main():
    st.title('Buscador de Notícias')
    st.subheader('Selecione os tópicos de interesse e encontre as últimas notícias')

    # Lista de tópicos predefinidos
    topic_options = [
        "Fomento", "Tecnologia", "Inovação", "Energia",
        "Financiamento", "Edital", "Investimento", "Renováveis",
        "Pesquisa", "Ciência"
    ]

    #  Criação das caixas de seleção para os tópicos
    selected_topics = []
    for topic in topic_options:
        if st.checkbox(topic, key=topic):
            selected_topics.append(topic)

    # Botão para iniciar a busca
    if st.button('Buscar Notícias'):
        if not selected_topics:
            st.warning("Por favor, selecione pelo menos um tópico para buscar.")
        else:
            # Inicializar o objeto GoogleNews para cada tópico selecionado e buscar notícias
            googlenews = GoogleNews(lang='pt-BR', period='7d')
            all_results = []
            for topic in selected_topics:
                googlenews.search(topic)
                # Extrair e acumular os resultados
                all_results.extend(googlenews.results())
                # Limpar os resultados do objeto para a próxima iteração
                googlenews.clear()

            # Verificar se há resultados acumulados
            if not all_results:
                st.write("Nenhuma notícia encontrada para os tópicos fornecidos.")
            else:
                for result in all_results:
                    # Mostrar títulos, datas e links das notícias
                    st.write(f"Título: {result['title']}")
                    st.write(f"Data: {result['date']}")
                    st.write(f"Link: [Leia mais]({result['link']})")
                    st.markdown("---")
                    st.write("")  # Espaço entre notícias

if __name__ == "__main__":
    main()

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por [PedroFS](https://linktr.ee/Pedrofsf)")
