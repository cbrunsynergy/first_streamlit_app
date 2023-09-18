
import streamlit as st
import pandas as pd

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

# Afficher le dataframe
st.dataframe(my_fruit_list)

# Créer une liste déroulante pour sélectionner des fruits
selected_fruits = st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# (Optionnel) Afficher les fruits sélectionnés
if selected_fruits:
    st.write(f"You selected: {', '.join(selected_fruits)}")
