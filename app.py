import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pointage Chantier", layout="wide")

st.title("🏗️ Suivi des Présences - Showroom")

# --- À MODIFIER : Mettez l'ID de votre feuille Google Sheets ---
# Exemple d'ID : "1A2B3C4D5E6F7G8H9I0J..." (c'est la longue suite de lettres et chiffres dans l'URL de votre Google Sheet)
sheet_id = "1p9vGuH9RH04PuOLGwvB7VjpCy-ozvg79upehhw9rUHE" 
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

def load_data():
    # On force Pandas à lire toutes les colonnes comme du texte pour éviter les erreurs
    df = pd.read_csv(url, dtype=str) 
    return df

try:
    data = load_data()
    
    st.subheader("Registre des entrées et sorties")
    st.dataframe(
        data, 
        use_container_width=True, 
        height=600,
        hide_index=True # Cache la numérotation automatique de la première colonne
    )
    
    st.info(f"Dernière mise à jour à l'ouverture de la page.")

except Exception as e:
    st.error("En attente de données ou erreur de connexion au registre. Vérifiez que votre Google Sheet est bien partagé en 'Tous les utilisateurs disposant du lien'.")

if st.button('Actualiser les données'):
    st.rerun()
