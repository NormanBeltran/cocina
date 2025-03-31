import streamlit as st
import google.generativeai as genai

# Gemini API key
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# Sidebar options
sidebar_options = ["Acerca de mi", "Descripción del Proyecto", "Recetas del Mundo"]
selected_sidebar_option = st.sidebar.selectbox("Opciones", sidebar_options)

# Lista de países
paises = ["Argentina", "Italia", "Japón", "México", "Francia", "India"]

# Diccionario de banderas
banderas = {
    "Argentina": "https://flagcdn.com/w320/ar.png",
    "Italia": "https://flagcdn.com/w320/it.png",
    "Japón": "https://flagcdn.com/w320/jp.png",
    "México": "https://flagcdn.com/w320/mx.png",
    "Francia": "https://flagcdn.com/w320/fr.png",
    "India": "https://flagcdn.com/w320/in.png",
}

if selected_sidebar_option == "Acerca de mi":
    st.title("Acerca de mi")
    st.write("Soy un apasionado de la cocina y la inteligencia artificial.")
elif selected_sidebar_option == "Descripción del Proyecto":
    st.title("Descripción del Proyecto")
    st.write("Este proyecto utiliza Streamlit y Gemini 2.0 Flash para generar recetas típicas de diferentes países.")
else:
    st.title("Recetas del Mundo")

    # Selección de país
    pais_seleccionado = st.selectbox("Selecciona un país", paises)

    # Mostrar bandera
    st.image(banderas[pais_seleccionado], width=100)

    # Botón "A Cocinar"
    if st.button("A Cocinar"):
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = f"Dame una receta tipica de {pais_seleccionado}"
        response = model.generate_content(prompt)
        st.write(response.text)
