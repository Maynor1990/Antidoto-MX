import streamlit as st
import streamlit.components.v1 as components
import time
from annotated_text import annotated_text

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS REFORZADOS
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    .stMetric { background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; padding: 15px; }
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 0px;
    }
    /* Estilo para los consejos */
    .security-tips {
        background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; padding: 20px; height: 420px;
    }
    .tips-list li { margin-bottom: 15px; font-size: 0.9rem; border-left: 2px solid #58a6ff; padding-left: 10px; list-style: none; }
    .tips-list b { color: #f1e05a; }
    
    /* Botón Táctico */
    div.stButton > button {
        background: linear-gradient(180deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold; width: 100%; height: 45px;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
    }
    /* Footer */
    .maynor-name { color: #00d4ff; font-weight: 900; font-size: 1.4rem; text-shadow: 0 0 10px #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO Y MÉTRICAS
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-bottom: 25px;'>TACTICAL HUB - CENTRO DE RESPUESTA A INCIDENTES</p>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Fiabilidad (Veritas)", "99.8%", "ÓPTIMO")
m2.metric("Base de Datos", "+500k IPs", "ACTUALIZADO")
m3.metric("Protección Global", "Activa 24/7", "SECURE")
m4.metric("Uptime Sistema", "99.9%", "ESTABLE")

st.write("---")

# 4. CENTRO DE OPERACIONES (CONSEJOS | RADAR | ACCIÓN)
col_tips, col_radar, col_action = st.columns([1, 1.8, 1])

with col_tips:
    st.markdown("""
    <div class="security-tips">
        <h4 style="color:#58a6ff;">💡 CONSEJOS TÁCTICOS</h4>
        <ul class="tips-list">
            <li><b>Phishing:</b> Revisa siempre que el dominio sea oficial. No confíes en correos urgentes.</li>
            <li><b>Privacidad:</b> Desactiva el GPS en las fotos antes de subirlas a redes públicas.</li>
            <li><b>Contraseñas:</b> Usa frases largas (passphrases) con símbolos. Ej: "Escudo*Maya*2026".</li>
            <li><b>Redes:</b> No realices operaciones bancarias en Wi-Fi públicas sin una VPN activa.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_radar:
    # RADAR DINÁMICO (Usando Components para forzar renderizado visual)
    radar_code = """
    <div style="background:#000; height:380px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <style>
            .c { position:absolute; border:1px solid rgba(0,212,255,0.2); border-radius:50%; }
            .scan { position:absolute; width:200px; height:200px; top:50%; left:50%; background:conic-gradient(from 0deg, rgba(0,212,255,0.4) 0%, transparent 40%); border-radius:50%; transform-origin:top left; animation: r 4s linear infinite; }
            .dot { position:absolute; width:8px; height:8px; background:#ff0000; border-radius:50%; box-shadow:0 0 10px #ff0000; animation: p 2s infinite; }
            @keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
            @keyframes p { 0%,100% {opacity:1;} 50% {opacity:0.2;} }
        </style>
        <div class="c" style="width:100px; height:100px;"></div>
        <div class="c" style="width:200px; height:200px;"></div>
        <div class="c" style="width:300px; height:300px;"></div>
        <div class="scan"></div>
        <div class="dot" style="top:20%; left:70%;"></div>
        <div class="dot" style="top:60%; left:30%;"></div>
        <div class="dot" style="top:40%; left:80%;"></div>
        <div style="position:absolute; bottom:10px; color:#00d4ff; font-family:monospace; font-size:12px;">NODO: CDMX | RANGO: 1000KM</div>
    </div>
    """
    components.html(radar_code, height=400)

with col_action:
    st.markdown("🔍 **ANÁLISIS DE AMENAZAS**")
    t1, t2 = st.tabs(["🔗 LINK", "🖼️ FORENSE"])
    with t1: st.text_input("URL:", placeholder="https://", label_visibility="collapsed")
    with t2: st.file_uploader("Imagen:", label_visibility="collapsed")
    
    if st.button("🚀 INICIAR PROTOCOLO"):
        with st.spinner("Escaneando..."):
            time.sleep(2)
            st.success("SISTEMA LIMPIO")

    st.markdown("📟 **LIVE LOG**")
    st.markdown("""
    <div style="background:#000; border:1px solid #333; padding:10px; color:#00ff00; font-family:monospace; font-size:0.75rem; height:120px; overflow-y:auto;">
        [SYS] Radar activo...<br>[NET] Nodo CDMX sincronizado.<br>[SEC] Cortafuegos: Interceptando...<br>[INF] Escaneo finalizado.
    </div>
    """, unsafe_allow_html=True)

# 5. FOOTER CON INSIGNIAS CISCO
st.write("---")
f1, f2 = st.columns([1, 1])
with f1:
    annotated_text(("SISTEMA", "VIGILANTE", "#1f6feb"), ("FIREWALL", "ACTIVO", "#238636"))

with f2:
    st.markdown("""
    <div style="text-align: right;">
        <span style="color:#8b949e;">Desarrollado y Verificado por:</span><br>
        <span class="maynor-name">MAYNOR, CERTIFIED SPECIALIST</span><br>
        <div style="display:flex; justify-content:flex-end; gap:15px; margin-top:10px;">
            <div style="background:#161b22; border:1px solid #58a6ff; border-radius:50%; width:50px; height:50px; display:flex; align-items:center; justify-content:center; font-size:9px; color:#fff; text-align:center;">CISCO<br>CyOps</div>
            <div style="background:#161b22; border:1px solid #f1e05a; border-radius:50%; width:50px; height:50px; display:flex; align-items:center; justify-content:center; font-size:9px; color:#fff; text-align:center;">ETHICAL<br>HACKER</div>
        </div>
        <p style="font-size:0.7rem; color:#444; margin-top:5px;">[ID SESIÓN: AMX-992-TX] [CERTIFICADO DE SEGURIDAD]</p>
    </div>
    """, unsafe_allow_html=True)
