import streamlit as st
import pandas as pd
import requests
import os

# Disable proxy settings
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

# Set the title of the Streamlit app
st.title('Hello World!')

# File uploader for CSV files
fichier = st.file_uploader("Télécharger un fichier", type=["csv"])

# Display uploaded data if a file is uploaded
if fichier is not None:
    try:
        data = pd.read_csv(fichier)
        st.write(data)
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier: {e}")

# URL of the FastAPI endpoint
API_URL = "http://localhost:8000"  # Modify with the address of your API

def get_item_from_api(item_id):
    try:
        # Make the GET request while bypassing the proxy
        response = requests.get(f"{API_URL}/fraudeAndNonFraude", proxies={"http": None, "https": None})
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Erreur lors de la récupération de l'élément. Code d'erreur: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de connexion à l'API: {e}")
        return None

def main():
    st.title("Communication entre Streamlit et FastAPI")

    # Input field for item ID
    item_id = st.text_input("Entrez l'ID de l'élément:")

    # Button to trigger API request
    if st.button("Obtenir l'élément"):
        if item_id:
            result = get_item_from_api(item_id)
            if result is not None:
                st.write("Résultat de l'API:")
                st.json(result)
        else:
            st.error("Veuillez entrer un ID d'élément.")
