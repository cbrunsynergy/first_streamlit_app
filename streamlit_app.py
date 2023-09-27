import streamlit as st
import pandas as pd
st.caching.clear_cache()

st.title('My parents New Healthy Diner')

st.header('Breakfast Menu')
st.text('🥣Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🐔Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Lecture du fichier CSV
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Définir 'Fruit' comme index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Ajout d'une barre de recherche pour filtrer les fruits
search_term = st.text_input("Search for fruits:")

if search_term:
    my_fruit_list = my_fruit_list[my_fruit_list.index.str.contains(search_term, case=False)]

# Afficher le dataframe filtré
st.dataframe(my_fruit_list)


# Créer une liste déroulante pour sélectionner des fruits
selected_fruits = st.multiselect("Pick some fruits:", list(my_fruit_list.index), default=['Avocado', 'Strawberries'])

# (Optionnel) Afficher les fruits sélectionnés
if selected_fruits:
    st.write(f"You selected: {', '.join(selected_fruits)}")

fruits_to_show = my_fruit_list.loc[selected_fruits]  # Corrigez ici

st.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
