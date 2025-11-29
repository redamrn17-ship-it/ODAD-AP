import streamlit as st
import numpy as np

# ================================
# 1. CONFIGURATION DE LA PAGE
# ================================
st.set_page_config(
    page_title="Prédiction Titre P2O5",
    page_icon="🧪",
    layout="centered"
)

# ================================
# 2. STYLE (CSS)
# ================================
st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
        color: #e5e7eb;
    }

    .stMetric {
        background: #020617;
        padding: 1rem;
        border-radius: 1rem;
        box-shadow: 0 0 25px rgba(15,23,42,0.7);
    }

    [data-testid="stMetricValue"] {
        color: #f9fafb !important;
    }

    [data-testid="stMetricLabel"] {
        color: #e5e7eb !important;
    }

    .title-card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        padding: 1.5rem;
        border-radius: 1.2rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.7);
        margin-bottom: 1.5rem;
        border: 1px solid rgba(148,163,184,0.4);
    }

    .eq-card {
        background: #020617;
        padding: 1rem 1.2rem;
        border-radius: 0.8rem;
        font-size: 0.9rem;
        border: 1px dashed rgba(75,85,99,0.9);
        color: #e5e7eb;
    }

    .footer {
        color: #9ca3af;
        font-size: 0.8rem;
        text-align: center;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================================
# 3. TITRE & DESCRIPTION
# ================================
st.markdown(
    """
    <div class="title-card">
        <h1 style="margin-bottom:0.3rem; color:white; font-weight:900;">
            🧪 Outils d'aide à la décision /JFC4: Prédiction du titre - P<sub>2</sub>O<sub>5</sub>
        </h1>
        <p style="color:#9ca3af; margin-top:0.5rem;">
            Interface interactive pour estimer le %P<sub>2</sub>O<sub>5</sub> à partir de la
            <b>densité</b> et du <b>%TS</b> avec une précision de 94,4%, pour deux qualités d'acide : <b>29%</b> et <b>54%</b>.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ================================
# 4. FONCTIONS DE CALCUL
# ================================
def predict_titre_54(densite: float, ts: float) -> float:
    return (
        88.015120
        + (-0.102618) * densite
        + 9.746723 * ts
        + 0.000049 * (densite ** 2)
        - 0.006485 * densite * ts
        + 0.017463 * (ts ** 2)
    )


def predict_titre_29(densite: float, ts: float) -> float:
    return (
        -386.871156
        + 0.555471 * densite
        + 3.959929 * ts
        - 0.000182 * (densite ** 2)
        - 0.004088 * densite * ts
        + 0.201024 * (ts ** 2)
    )

# ================================
# 5. ZONE DE SAISIE
# ================================
col1, col2 = st.columns(2)

with col1:
    densite = st.number_input(
        "🔢 Densité",
        min_value=1220.0,
        max_value=1700.0,
        value=1290.0,
        step=1.0,
        help="Entrer la densité mesurée (kg/m³)"
    )

with col2:
    ts = st.number_input(
        "💧 TS (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.9,
        step=0.01,
        help="Entrer le pourcentage de TS"
    )

st.markdown("---")

# 👉 On ne laisse que deux choix
mode = st.radio(
    "Que souhaites-tu afficher ?",
    ["Titre 29% uniquement", "Titre 54% uniquement"],
    horizontal=True
)

# ================================
# 6. CALCULS
# ================================
titre_29 = predict_titre_29(densite, ts)
titre_54 = predict_titre_54(densite, ts)

# ================================
# 7. AFFICHAGE DES RÉSULTATS
# ================================
st.write("")
st.subheader("📊 Résultats de la prédiction")

if mode == "Titre 29% uniquement":
    st.metric(label="Titre 29%", value=f"{titre_29:.2f} %")
else:  # "Titre 54% uniquement"
    st.metric(label="Titre 54%", value=f"{titre_54:.2f} %")

# ================================
# 8. ÉQUATIONS
# ================================
with st.expander("📐 Voir les équations utilisées"):
    st.markdown(
        """
        <div class="eq-card">
        <b>Titre 54%</b><br>
        Demander de l'admin
        <br><br>
        <b>Titre 29%</b><br>
        Demander de l'admin
        </div>
        """,
        unsafe_allow_html=True
    )

# ================================
# 9. FOOTER
# ================================
st.markdown(
    """
    <div class="footer">
        🧬 Outil interne de prédiction – basé sur modèles polynomiaux.
        <br>Vérifiez toujours avec les analyses labo si la valeur est critique.
    </div>
    """,
    unsafe_allow_html=True
)



