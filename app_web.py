import streamlit as st
import pandas as pd
import random
from collections import Counter

st.set_page_config(page_title="Lotto Intelligent", page_icon="🎰")

st.title("🎰 Generatore Intelligente")
st.write("Analisi basata su 5037 estrazioni")

# Caricamento dati (Streamlit legge i CSV molto bene)
@st.cache_data
def carica_dati():
    df = pd.read_csv('estrazioni_super.csv', sep=None, engine='python')
    # Supponendo che i numeri siano nelle colonne da 1 a 6
    numeri_tutti = df.iloc[:, 1:7].values.flatten().tolist()
    return numeri_tutti

try:
    dati = carica_dati()
    frequenze = Counter(dati)
    popolazione = list(range(1, 91))
    pesi = [frequenze.get(i, 1) for i in popolazione]

    if st.button('GENERA SESTINE FORTUNATE'):
        for i in range(2):
            sestina = set()
            while len(sestina) < 6:
                estratto = random.choices(popolazione, weights=pesi, k=1)[0]
                sestina.add(estratto)
            st.success(f"Schedina {i+1}: {sorted(list(sestina))}")

except Exception as e:
    st.error(f"Carica il file CSV per iniziare! Errore: {e}")
    
    # --- AGGIUNTA DISCLAIMER LEGALE IN FONDO ---
st.markdown("---") # Crea una linea di separazione
st.caption("⚠️ **DISCLAIMER LEGALE**")
st.caption("""
Questo software è rilasciato sotto licenza MIT. 
L'analisi è basata puramente su calcoli statistici delle frequenze storiche e non garantisce in alcun modo vincite. 
Il gioco è vietato ai minori di 18 anni e può causare dipendenza patologica. Gioca responsabilmente.
""")