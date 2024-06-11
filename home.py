import streamlit as st
import base64

def home():
    # Paths to the images
    image_path = "fraud_1671214.png"
    icon_path = "money-laundering_11155632.png"

    # Function to encode image to base64
    def get_base64_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()

    # HTML content for styling and animation
    html_content = f"""
        <style>
            @keyframes fadeIn {{
                0% {{ opacity: 0; }}
                100% {{ opacity: 1; }}
            }}
            @keyframes bounce {{
                0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
                40% {{ transform: translateY(-30px); }}
                70% {{ transform: translateY(-15px); }}
            }}
            @keyframes slideIn {{
                0% {{ transform: translateX(-100%); }}
                100% {{ transform: translateX(0); }}
            }}
            @keyframes rotate {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
            @keyframes pulse {{
                0% {{ transform: scale(1); }}
                50% {{ transform: scale(1.05); }}
                100% {{ transform: scale(1); }}
            }}
            .container {{
                background-color: lightblue;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                animation: slideIn 2s;
            }}
            h1 {{
                color: green;
                animation: fadeIn 2s;
            }}
            h2 {{
                color: darkred;
                animation: pulse 2s infinite;
            }}
            .fade-in {{
                animation: fadeIn 2s;
            }}
            .bounce {{
                animation: bounce 2s infinite;
            }}
            .rotate {{
                animation: rotate 4s infinite;
            }}
            img {{
                width: 10%;
                max-width: 600px;
                border-radius: 10px;
            }}
        </style>
        <div class='container'>
            <h1>
                Detection de Fraude
                <img class='bounce' src='data:image/jpeg;base64,{get_base64_image(image_path)}' alt='Prévention de la Fraude'>
                dans le Transfert d'Argent au Sénégal
            </h1>
            <h2>
                Stop aux Fraudes liées au Gaming
                <img class='rotate' src='data:image/jpeg;base64,{get_base64_image(icon_path)}' alt='Prévention de la Fraude'>
            </h2>
        </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

