import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS (ESTRUCTURA TÁCTICA)
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Contenedores de Métricas (Ahora abajo) */
    .stMetric { 
        background-color: #0d1117; border: 1px solid #30363d; 
        border-radius: 8px; padding: 10px; text-align: center;
    }

    /* Título con resplandor */
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 5px;
    }

    /* Panel de Consejos */
    .security-tips {
        background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; 
        padding: 15px; height: 350px;
    }
    .tips-list li { margin-bottom: 12px; font-size: 0.85rem; border-left: 2px solid #58a6ff; padding-left: 8px; list-style: none; }
    .tips-list b { color: #f1e05a; }

    /* Botón de Acción */
    div.stButton > button {
        background: linear-gradient(180deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold; width: 100%; height: 40px;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }

    /* Footer y Texto de Maynor */
    .maynor-brand { color: #00d4ff; font-weight: 900; font-size: 1.2rem; text-shadow: 0 0 8px #00d4ff; }
    .session-id { font-size: 0.7rem; color: #8b949e; font-family: monospace; }
    
    /* Eliminar cualquier decoración extra en las esquinas */
    .decoration-none { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO PRINCIPAL
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 0.8rem; margin-bottom: 20px;'>CENTRO DE RESPUESTA A INCIDENTES</p>", unsafe_allow_html=True)

# 4. FILA SUPERIOR: LO QUE EL USUARIO USA (CONSOLA Y RADAR)
col_tips, col_radar, col_action = st.columns([1, 1.8, 1])

with col_tips:
    st.markdown("""
    <div class="security-tips">
        <h4 style="color:#58a6ff; font-size:1rem;">💡 CONSEJOS TÁCTICOS</h4>
        <ul class="tips-list">
            <li><b>Phishing:</b> Revisa dominios oficiales. No cedas ante la urgencia.</li>
            <li><b>Privacidad:</b> Limpia metadatos EXIF antes de compartir imágenes.</li>
            <li><b>Passphrase:</b> Usa frases largas como "Ciber*Seguridad*2026".</li>
            <li><b>Redes:</b> Evita transacciones en Wi-Fi públicas sin VPN.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_radar:
    # Radar Central Dinámico
    radar_html = """
    <div style="background:#000; height:350px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <style>
            .c { position:absolute; border:1px solid rgba(0,212,255,0.15); border-radius:50%; }
            .scan { position:absolute; width:180px; height:180px; top:50%; left:50%; background:conic-gradient(from 0deg, rgba(0,212,255,0.3) 0%, transparent 40%); border-radius:50%; transform-origin:top left; animation: r 4s linear infinite; }
            .dot { position:absolute; width:6px; height:6px; background:#ff4b4b; border-radius:50%; box-shadow:0 0 8px #ff4b4b; animation: p 2s infinite; }
            @keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
            @keyframes p { 0%,100% {opacity:1;} 50% {opacity:0.3;} }
        </style>
        <div class="c" style="width:80px; height:80px;"></div>
        <div class="c" style="width:160px; height:160px;"></div>
        <div class="c" style="width:240px; height:240px;"></div>
        <div class="scan"></div>
        <div class="dot" style="top:25%; left:65%;"></div>
        <div class="dot" style="top:70%; left:35%;"></div>
        <div style="position:absolute; bottom:8px; color:#00d4ff; font-family:monospace; font-size:10px;">SCANNING... | NODO: CDMX</div>
    </div>
    """
    components.html(radar_html, height=360)

with col_action:
    st.markdown("🔍 **ANÁLISIS DE AMENAZAS**")
    tab1, tab2 = st.tabs(["🔗 LINK", "🖼️ FORENSE"])
    with tab1: st.text_input("URL sospechosa:", placeholder="https://", label_visibility="collapsed")
    with tab2: st.file_uploader("Subir archivo:", label_visibility="collapsed")
    
    if st.button("🚀 EJECUTAR PROTOCOLO"):
        with st.spinner("Analizando..."):
            time.sleep(1.5)
            st.success("SISTEMA PROTEGIDO")

    st.markdown("📟 **LIVE LOG**")
    st.markdown("""
    <div style="background:#000; border:1px solid #333; padding:8px; color:#00ff00; font-family:monospace; font-size:0.7rem; height:100px; overflow-y:auto;">
        [SYS] Radar activo.<br>[NET] Nodo CDMX sincronizado.<br>[SEC] Cortafuegos: Interceptando...<br>[INF] Análisis listo.
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# 5. FILA INFERIOR: MÉTRICAS (LO QUE BAJAMOS)
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Fiabilidad", "99.8%", "+ ÓPTIMO")
with m2: st.metric("Base de Datos", "+500k IPs", "SENTINEL")
with m3: st.metric("Protección Global", "Activa 24/7", "SECURE")
with m4: st.metric("Uptime Sistema", "99.9%", "ESTABLE")

# 6. FOOTER FINAL: INSIGNIAS Y FIRMA (SIN CÍRCULOS EN LA ESQUINA)
st.write("---")
foot_left, foot_right = st.columns([1, 1])

with foot_left:
    st.markdown("""
    <div style="display:flex; gap:10px; align-items:center;">
        <div style="background:#238636; color:white; padding:2px 8px; border-radius:4px; font-size:0.7rem;">SENTINEL ACTIVE</div>
        <div style="background:#1f6feb; color:white; padding:2px 8px; border-radius:4px; font-size:0.7rem;">FIREWALL OK</div>
    </div>
    """, unsafe_allow_html=True)

with foot_right:
    st.markdown(f"""
    <div style="text-align: right;">
        <span class="session-id">[ID SESIÓN: AMX-982-TX]</span><br>
        <span style="color:#8b949e; font-size:0.8rem;">Desarrollado por:</span> 
        <span class="maynor-brand">MAYNOR, VERIFIED SPECIALIST</span>
        <div style="display:flex; justify-content:flex-end; gap:10px; margin-top:8px;">
            <div style="border:1px solid #58a6ff; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center; font-size:8px; color:#fff; text-align:center; background:#0d1117;">Cisco<br>CyOps</div>
            <div style="border:1px solid #f1e05a; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center; font-size:8px; color:#fff; text-align:center; background:#0d1117;">Ethical<br>Hacker</div>
            <div style="border:1px solid #3fb950; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center; font-size:8px; color:#fff; text-align:center; background:#0d1117;">Network<br>Def.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
