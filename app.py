import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN DE PÁGINA TÁCTICA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS (RESTAURACIÓN DE ESTÉTICA ORIGINAL)
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 20px;
    }

    /* CONTENEDOR INTEGRADO MAYNOR VÁZQUEZ */
    .maynor-footer {
        margin-top: 40px; padding: 25px; border-top: 1px solid #30363d;
        background: rgba(13, 17, 23, 0.8); border-radius: 12px;
        display: flex; justify-content: space-between; align-items: center;
    }

    .badge-container { display: flex; gap: 15px; flex-wrap: nowrap; }

    .badge-card {
        background-color: #0d1117; border: 2px solid #30363d; border-radius: 10px;
        padding: 15px; text-align: center; width: 140px;
        transition: transform 0.2s, border-color 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.5);
    }

    .badge-card:hover { 
        transform: scale(1.05); border-color: #58a6ff; 
        box-shadow: 0 0 15px rgba(88, 166, 255, 0.3);
    }

    .badge-icon { 
        width: 60px; height: 60px; margin-bottom: 10px;
        filter: drop-shadow(0 0 8px rgba(88, 166, 255, 0.8));
    }

    .badge-title { font-size: 0.85rem; font-weight: bold; color: #ffffff; margin: 0; }
    .badge-date { font-size: 0.7rem; color: #58a6ff; font-family: monospace; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)

# 4. PANEL OPERATIVO (RADAR Y CONSOLA)
col_l, col_r = st.columns([1, 1.2])
with col_l:
    radar_html = """
    <div style="background:#000; height:300px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <div style="position:absolute; width:220px; height:220px; background:conic-gradient(from 0deg, rgba(0,212,255,0.2) 0%, transparent 50%); border-radius:50%; animation: r 3s linear infinite;"></div>
        <style>@keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }</style>
        <div style="color:#00d4ff; font-family:monospace; font-size:11px; position:absolute; bottom:10px;">DB STATUS: SYNCHRONIZED</div>
    </div>
    """
    components.html(radar_html, height=310)

with col_r:
    st.markdown("### 🔍 CONSOLA DE ANÁLISIS")
    target = st.text_input("Ingrese URL o Email:", placeholder="Ej: sospechoso.top")
    if st.button("🚀 INICIAR ESCANEO TÁCTICO", use_container_width=True):
        with st.status("Analizando firmas...", expanded=True):
            time.sleep(1)
            st.success("Análisis completo.")

st.write("---")

# 5. PIE DE PÁGINA (ESTILO ORIGINAL RECUPERADO)
st.markdown(f"""
    <div class="maynor-footer">
        <div>
            <h2 style="color: #00d4ff; margin:0; text-shadow: 0 0 10px #00d4ff;">MAYNOR VÁZQUEZ</h2>
            <p style="color: #ffffff; font-size: 0.95rem; font-weight: bold;">Network Defense & CyberOps Specialist</p>
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
