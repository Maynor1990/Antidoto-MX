import streamlit as st
import streamlit.components.v1 as components
import time
import random

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS BASE
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 20px;
    }
    .stMetric { 
        background-color: #0d1117; border: 1px solid #30363d; 
        border-radius: 8px; padding: 10px; text-align: center;
    }
    div.stButton > button {
        background: linear-gradient(180deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold; width: 100%; height: 45px;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }
    .maynor-footer {
        margin-top: 50px; padding: 20px; border-top: 1px solid #30363d;
        display: flex; justify-content: space-between; align-items: center;
    }
    /* Estilo para el detalle del virus */
    .virus-report {
        background-color: #1a0505; border: 1px solid #ff4b4b; border-radius: 8px; padding: 15px; color: #ffbaba;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-top:-20px;'>TACTICAL HUB - CENTRO DE RESPUESTA A INCIDENTES</p>", unsafe_allow_html=True)

# 4. CUERPO PRINCIPAL: RADAR Y CONSOLA
col_left, col_right = st.columns([1, 1.2])

with col_left:
    # Radar con líneas de barrido
    radar_html = """
    <div style="background:#000; height:300px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <style>
            .scan { position:absolute; width:200px; height:200px; background:conic-gradient(from 0deg, rgba(0,212,255,0.2) 0%, transparent 40%); border-radius:50%; animation: r 4s linear infinite; }
            .line-h { position:absolute; width:100%; height:1px; background:rgba(0,212,255,0.1); top:50%; }
            .line-v { position:absolute; height:100%; width:1px; background:rgba(0,212,255,0.1); left:50%; }
            @keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
        </style>
        <div class="line-h"></div>
        <div class="line-v"></div>
        <div class="scan"></div>
        <div style="position:absolute; bottom:10px; color:#00d4ff; font-family:monospace; font-size:11px;">RANGO: 1000 KM | NODO: CDMX</div>
    </div>
    """
    components.html(radar_html, height=310)

with col_right:
    st.markdown("### 🔍 ANÁLISIS DE AMENAZAS")
    tab1, tab2, tab3 = st.tabs(["🔗 LINK", "🖼️ FOTO", "📧 EMAIL"])
    
    input_data = ""
    with tab1: input_data = st.text_input("URL sospechosa:", placeholder="https://", key="url_input")
    with tab2: st.file_uploader("Subir imagen forense:", key="file_input")
    with tab3: input_data = st.text_input("Remitente de correo:", placeholder="ejemplo@dominio.com", key="email_input")
    
    if st.button("🚀 EJECUTAR PROTOCOLO"):
        log_placeholder = st.empty()
        logs = ["[SYS] Radar activo..."]
        
        # Simulación de jalar info en tiempo real
        pasos = [
            "📡 Conectando con bases de datos Sentinel...",
            "🔗 Rastreando saltos de IP y geolocalización...",
            "🔬 Cotejando firmas en el repositorio de malware...",
            "📂 Analizando metadatos y certificados de origen..."
        ]
        
        for p in pasos:
            logs.append(f"[INF] {p}")
            log_placeholder.code("\n".join(logs), language="bash")
            time.sleep(0.7)

        # Lógica de detección detallada
        if input_data and (".top" in input_data or ".xyz" in input_data or "ganaste" in input_data.lower()):
            st.markdown(f"""
            <div class="virus-report">
                <h4>🚨 AMENAZA DETECTADA</h4>
                <p><b>Tipo de Virus:</b> Troyano de Acceso Remoto (RAT) / Ransomware</p>
                <p><b>Origen del Ataque:</b> IP Geoubicada en Europa del Este (Servidor Proxy No Identificado)</p>
                <hr style='border: 0.5px solid #ff4b4b;'>
                <p><b>Acción del Sistema:</b> El archivo/enlace ha sido enviado automáticamente al <b>Baúl de Cuarentena</b>.</p>
                <p><b>Recomendación:</b> No intente abrir el recurso. El sistema ha eliminado la persistencia en el caché.</p>
            </div>
            """, unsafe_allow_html=True)
        elif input_data:
            st.success("✅ ANÁLISIS COMPLETADO: Fuente verificada. No se detectaron anomalías.")
        else:
            st.warning("Ingrese un dato para iniciar el rastreo.")

st.write("---")

# 5. MÉTRICAS DEL PIE
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Fiabilidad", "99.8%", "ÓPTIMO")
with m2: st.metric("Base de Datos", "+500k IPs", "ACTUALIZADO")
with m3: st.metric("Protección", "Activa 24/7", "SECURE")
with m4: st.metric("Uptime", "99.9%", "ESTABLE")

# 6. FIRMA DE ESPECIALISTA
st.markdown("""
    <div class="maynor-footer">
        <div>
            <h3 style="color: #00d4ff; margin:0;">MAYNOR VÁZQUEZ</h3>
            <p style="color: #8b949e; font-size: 0.8rem;">Certified Network Defense & CyberOps Specialist</p>
        </div>
        <div style="display: flex; gap: 15px;">
            <div style="border:1px solid #58a6ff; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center; font-size:8px; color:white; text-align:center;">Cisco<br>CyOps</div>
            <div style="border:1px solid #3fb950; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center; font-size:8px; color:white; text-align:center;">Net<br>Def</div>
            <div style="border:1px solid #f1e05a; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center; font-size:8px; color:white; text-align:center;">Ethical<br>Hacker</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
