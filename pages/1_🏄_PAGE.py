import streamlit as st
import streamlit as st
with st.sidebar : 
    # Utilisation de st.sidebar pour ajouter des éléments dans la barre latérale
    st.header("Options")
    texte_sidebar = st.text_input("Entrez du texte","Abraham")
    nombre_sidebar = st.number_input("Entrez un nombre", min_value=0, max_value=100, value=27)
import streamlit as st
import streamlit as st
with st.sidebar : 
    # Utilisation de st.sidebar pour ajouter des éléments dans la barre latérale
    st.header("Options")
    texte_sidebar = st.text_input("Entrez du texte","Abraham")
    nombre_sidebar = st.number_input("Entrez un nombre", min_value=0, max_value=100, value=27)

# Affichage des valeurs saisies dans le contenu principal
st.write(f"Vous avez saisi en barre latérale : Texte - **:blue[{texte_sidebar}]**, Nombre - **:blue[{nombre_sidebar}]**")

st.title("Tutoriel :red[Streamlit]")
st.header(':blue[Introduction aux bases de données]')
st.subheader("👨🏾‍💻 Applications web")
st.text("Ma première application web avec Streamlit ! ")
