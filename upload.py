import streamlit as st
import pandas as pd
import numpy as np
import cv2

def upload():
    # Function to load and display the CSV file
    def load_and_display_csv(file_path):
        if file_path is not None:
            try:
                df = pd.read_csv(file_path)
                # HTML content for styling
                html_content = """
                    <div style='background-color: lightblue; padding: 10px; border-radius: 5px;'>
                        <h2>Fichier de présentation des données fournies</h2>     
                    </div>
                """
                st.markdown(html_content, unsafe_allow_html=True)
                st.write(df)
                return df
            except FileNotFoundError:
                st.error("Le fichier CSV n'a pas été trouvé. Assurez-vous que le chemin est correct.")
                return None
        else:
            return None
    
    # Charger l'image depuis l'upload
    uploaded_file = st.file_uploader("Téléchargez un fichier csv...", type=['csv'])

    # Load and display the CSV file
    df = load_and_display_csv(uploaded_file)
