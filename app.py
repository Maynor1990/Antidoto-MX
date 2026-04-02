import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN TÁCTICA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS (LIMPIEZA TOTAL Y FOCO EN INSIGNIAS)
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* ENCABEZADO */
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 20px;
    }

    /* CONTENEDOR INTEGRADO (SIN TÍTULO DE LOGROS) */
    .maynor-footer {
        margin-top: 50px; padding: 30px; border-top: 1px solid #30363d;
        background: rgba(13, 17, 23, 0.9); border-radius: 12px;
        display: flex; justify-content: space-between; align-items: center;
    }

    .badge-container { display: flex; gap: 15px; }

    .badge-card {
        background-color: #0d1117; border: 1px solid #30363d; border-radius: 10px;
        padding: 15px; text-align: center; width: 140px;
        transition: transform 0.3s;
    }

    .badge-card:hover { 
        transform: translateY(-5px); border-color: #00d4ff; 
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
    }

    .badge-icon { 
        width: 65px; height: 65px; margin-bottom: 10px;
        filter: drop-shadow(0 0 10px rgba(88, 166, 255, 0.8));
    }

    .badge-title { font-size: 0.85rem; font-weight: bold; color: #ffffff; margin: 0; }
    .badge-date { font-size: 0.7rem; color: #00d4ff; font-family: monospace; margin-top: 5px; }

    div.stButton > button {
        background: linear-gradient(180deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFAZ SUPERIOR
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)

col_radar, col_console = st.columns([1, 1.2])

with col_radar:
    radar_html = """
    <div style="background:#000; height:300px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <div style="position:absolute; width:220px; height:220px; background:conic-gradient(from 0deg, rgba(0,212,255,0.1) 0%, transparent 50%); border-radius:50%; animation: r 3s linear infinite;"></div>
        <style>@keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }</style>
        <div style="color:#00d4ff; font-family:monospace; font-size:11px; position:absolute; bottom:10px;">DB STATUS: SYNCHRONIZED</div>
    </div>
    """
    components.html(radar_html, height=310)

with col_console:
    st.markdown("### 🔍 CONSOLA DE ANÁLISIS")
    target = st.text_input("Ingrese URL o Email:", placeholder="ejemplo.com")
    if st.button("🚀 INICIAR ESCANEO TÁCTICO", use_container_width=True):
        with st.status("Rastreando amenazas..."):
            time.sleep(1)
            st.success("Análisis Sentinel completado.")

st.write("---")

# 4. PIE DE PÁGINA (MAYNOR VÁZQUEZ + INSIGNIAS ORIGINALES)
# Se eliminó por completo el texto de "Logros"
st.markdown(f"""
    <div class="maynor-footer">
        <div>
            <h2 style="color: #00d4ff; margin:0; text-shadow: 0 0 10px #00d4ff;">MAYNOR VÁZQUEZ</h2>
            <p style="color: #ffffff; font-size: 0.95rem; font-weight: bold; margin:0;">Network Defense & CyberOps Specialist</p>
        </div>
        <div class="badge-container">
            <div class="badge-card">
                <img class="badge-icon" src="https://img.icons8.com/nolan/96/hacker.png">
                <div class="badge-title">Hacker Ético</div>
                <div class="badge-date">14 mar 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://img.icons8.com/nolan/96/group.png">
                <div class="badge-title">Ing. Social</div>
                <div class="badge-date">10 feb 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://img.icons8.com/nolan/96/shield.png">
                <div class="badge-title">Defensa Red</div>
                <div class="badge-date">07 feb 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://img.icons8.com/nolan/96/virus.png">
                <div class="badge-title">Amenazas</div>
                <div class="badge-date">05 feb 2026</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
