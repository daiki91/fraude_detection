import streamlit as st
import pandas as pd
import numpy as np
import cv2
from upload import upload

def graphe():
    # Charger l'image depuis l'upload
    uploaded_file = st.file_uploader("Téléchargez un fichier csv...", type=['csv'])
    # Vérifier si le dataframe n'est pas vide
    if df is not None:
        # Obtenir toutes les colonnes pour le tracé
        all_columns = df.columns.tolist()

        if all_columns:
            # Message pour indiquer que les graphiques vont être affichés
            st.write("Graphiques des données fournies")

            # Sélectionner les colonnes pour les axes X et Y
            x_axis = st.selectbox("Choisissez la colonne pour l'axe X", options=all_columns)
            y_axis = st.multiselect("Choisissez les colonnes pour l'axe Y", options=all_columns)

            # Sélectionner le type de graphique
            plot_type = st.selectbox("Choisissez le type de graphique", ["Ligne", "Barres", "Nuage de points"])

            if x_axis and y_axis:
                try:
                    # Convertir les données catégoriques en numériques pour l'axe X si nécessaire
                    if df[x_axis].dtype == 'object':
                        df[x_axis] = pd.factorize(df[x_axis])[0]
                    
                    st.write(f"Graphique(s) de {', '.join(y_axis)} en fonction de {x_axis}")
                    
                    # Set the index once outside the chart plotting
                    df.set_index(x_axis, inplace=True)

                    if plot_type == "Ligne":
                        st.line_chart(df[y_axis])
                    elif plot_type == "Barres":
                        st.bar_chart(df[y_axis])
                    elif plot_type == "Nuage de points":
                        for col in y_axis:
                            st.write(f"Nuage de points de {col} en fonction de {x_axis}")
                            st.scatter_chart(df[[col]])
                except KeyError as e:
                    st.error(f"Erreur: {e}. Vérifiez que les colonnes sélectionnées existent dans le fichier CSV.")
        else:
            st.warning("Le fichier CSV ne contient pas de colonnes à afficher.")
    else:
        st.warning("Aucun graphique à afficher car le fichier CSV n'a pas été chargé correctement.")


