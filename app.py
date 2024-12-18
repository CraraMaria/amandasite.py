import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Amanda Ferreira Dahm",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto"
)

# Tabulação
tab1, tab2 = st.tabs(["Currículo", "Outros Conteúdos"])

with tab1:
    # Colunas dentro da aba 1
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.title("Amanda Ferreira Dahm")
        st.write("Estudante de Ciência da Computação. Interesse em Ciência de Dados e Desenvolvimento Fullstack.")
        st.write("Experiência em projetos acadêmicos e voluntários e em busca de estágio para aplicar conhecimentos.")

        st.divider()
        st.subheader(":blue[PROJETOS]")
        st.write("**Projeto de Jogos de Probabilidade**")
        st.caption("Criação de jogos envolvendo probabilidade e estatística")
        
        st.divider()
        st.subheader(":blue[CERTIFICAÇÃO]")
        st.write("Curso Pleno de Língua Estrangeira Moderna Inglês — **Concluído em 2021**")
        st.caption("Thomas jefferson")

        st.divider()
        st.subheader(":blue[FORMAÇÃO]")
        st.write("Instituto de Educação Superior de Brasília (IESB), Asa Sul, DF")
        st.caption("Bacharelado em Ciência da Computação - Quarto semestre, com previsão de formatura em 2026.")
        st.write("Centro de Ensino Médio Setor Leste, Asa Sul, DF")
        st.caption("Ensino Médio - Concluído em 2018")

       # st.divider()
       # st.subheader(":blue[EXPERIÊNCIA PROFISSIONAL]")
       # st.write("Gerente de Operações de Airbnb")
       # st.caption("""
# Responsável pelo gerenciamento de imóveis no Airbnb, incluindo:
#""")
        ## st.caption("por algum tempo")

        st.divider()

        st.subheader(":blue[REDES]")

        button_col1, button_col2 = st.columns([1, 1])

        with button_col1:
            st.link_button("🐱 Github", "https://github.com/mandsd") 

        with button_col2:
            st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/amanda-dahm-138105250/")
          


    with col2:
        st.caption("Asa Norte, DF")
        st.caption("**☎️ +55 61 98197-1043**")
        st.caption("**amandafd@outlook.com**")
        st.caption("**a.dahm@iesb.edu.br**")
        
        st.divider()
        st.write(":blue[COMPETÊNCIAS]")
        st.caption("Programação: C, Java, Python.")
        st.caption("Análise de Dados: Excel, Python (Pandas, NumPy), SQL.")
        st.caption("Desenvolvimento Web: HTML, CSS, Streamlit.")
        st.caption("Ferramentas: Eclipse, Visual Studio Code, Spring Boot.")
        st.caption("Gestão de Projetos: Scrum, Kanban, Microsoft Project, Trello, Jira.")
        st.caption("Pacote Office: Word, Excel, PowerPoint.")
        st.caption("Sistemas Operacionais: Linux, Windows.")

        st.divider()
        #st.write(":blue[PROJETOS VOLUNTÁRIOS]")
       #st.caption("Apoio na organização e aplicação de provas para o EAD.")
        
        st.divider()
        st.write(":blue[IDIOMAS]")
        st.caption("Língua Moderna Inglês avançado.")


st.divider()

# URL do arquivo PDF no GitHub
pdf_url = "https://raw.githubusercontent.com/CraraMaria/amandasite.py/main/Currículo final.pdf"  # Atualize com o link correto

# Cria o botão de download
st.markdown(f'<a href="{pdf_url}" download="Currículo final.pdf">Baixar em PDF</a>', unsafe_allow_html=True)

with tab2:
    # Conteúdo para a aba 2
    # tentar colocar foto interativa
    st.write("Mais sobre mim")
    # st.image("fotodeperfil.png", caption="Clara Fontenele", width=200)

    st.write("EM CONSTRUÇÃO 🛠👩‍🚒")
