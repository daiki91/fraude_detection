import streamlit as st
import pandas as pd
import requests
import os

# Disable proxy settings
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

API_URL = "http://localhost:8000"

def upload_and_predict(file):
    files = {'file': (file.name, file.getvalue())}
    response = requests.post(f"{API_URL}/predict", files=files)
    return response

def strempost():
    st.title("Télécharger un fichier et obtenir des résultats")

    uploaded_file = st.file_uploader("Choisissez un fichier", type=["csv", "txt"])

    if uploaded_file is not None:
        st.write("Fichier téléchargé:")
        try:
            df = pd.read_csv(uploaded_file)
            st.write(df)
        except Exception as e:
            st.error(f"Erreur lors de la lecture du fichier: {e}")
            return

        if st.button("Obtenir des prédictions"):
            response = upload_and_predict(uploaded_file)

            if response.status_code == 200:
                st.success("Fichier traité avec succès!")
                result = response.json()
                st.write("Résultat de l'API:")
                st.json(result)
            else:
                st.error(f"Erreur lors du traitement du fichier. Code d'erreur: {response.status_code}")
    else:
        st.info("Veuillez télécharger un fichier pour continuer.")


