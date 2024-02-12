import streamlit as st
st.set_page_config(
    page_title="Mon Application Streamlit",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",
)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Création d'un graphique avec Matplotlib
x = np.linspace(- 2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

# Affichage du graphique avec st.pyplot
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
import pandas as pd

# Création d'un DataFrame de démonstration
data = {'Nom': ['Alice', 'Bob', 'Charlie'],
        'Âge': [25, 30, 35],
        'Ville': ['Paris', 'New York', 'Londres']}
df = pd.DataFrame(data)
# Affichage du DataFrame avec st.dataframe
st.dataframe(df)
if st.button("Cliquez-moi"):
    st.write("Vous venez de cliquer sur le boutton !")