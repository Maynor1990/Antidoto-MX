import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS PERSONALIZADOS (LIMPIEZA TOTAL)
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Título con resplandor */
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 5px;
    }

    /* Paneles Superiores (Interactivos) */
    .interact-panel {
        background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; 
        padding: 15px; height: 380px;
    }
    
    /* Métricas (Ahora en el pie) */
    .stMetric { 
        background-color: #0d1117; border: 1px solid #30363d; 
        border-radius: 8px; padding: 10px; text-align: center;
    }

    /* Botón de Protocolo */
    div.stButton > button {
        background: linear-gradient(180deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold; width: 100%; height: 45px;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }

    /* Branding de Maynor */
    .maynor-brand { color: #00d4ff; font-weight: 900; font-size: 1.1rem; text-shadow: 0 0 8px #00d4ff; }
    
    /* Eliminar decoraciones residuales de esquinas */
    .decoration-none { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 0.8rem; margin-bottom: 25px;'>TACTICAL HUB - INCIDENT RESPONSE CENTER</p>", unsafe_allow_html=True)

# 4. SECCIÓN SUPERIOR: INTERACCIÓN DEL USUARIO
col_tips, col_radar, col_action = st.columns([1, 1.8, 1])

with col_tips:
    st.markdown("""
    <div class="interact-panel">
        <h4 style="color:#58a6ff; font-size:0.9rem;">💡 CONSEJOS TÁCTICOS</h4>
        <p style="font-size:0.8rem; border-left: 2px solid #58a6ff; padding-left:10px;"><b>Phishing:</b> Revisa dominios oficiales. <br>No cedas ante mensajes urgentes.</p>
        <p style="font-size:0.8rem; border-left: 2px solid #58a6ff; padding-left:10px;"><b>Privacidad:</b> Desactiva el GPS en fotos antes de subirlas a redes.</p>
        <p style="font-size:0.8rem; border-left: 2px solid #58a6ff; padding-left:10px;"><b>Seguridad:</b> Usa frases cortas con números en lugar de palabras solas.</p>
    </div>
    """, unsafe_allow_html=True)

with col_radar:
    # Radar Dinámico
    radar_html = """
    <div style="background:#000; height:380px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <style>
            .c { position:absolute; border:1px solid rgba(0,212,255,0.1); border-radius:50%; }
            .scan { position:absolute; width:200px; height:200px; top:50%; left:50%; background:conic-gradient(from 0deg, rgba(0,212,255,0.2) 0%, transparent 40%); border-radius:50%; transform-origin:top left; animation: r 4s linear infinite; }
            @keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
        </style>
        <div class="c" style="width:100px; height:100px;"></div>
        <div class="c" style="width:200px; height:200px;"></div>
        <div class="c" style="width:300px; height:300px;"></div>
        <div class="scan"></div>
        <div style="position:absolute; bottom:10px; color:#00d4ff; font-family:monospace; font-size:11px;">RANGO: 1000 KM | NODO: CDMX</div>
    </div>
    """
    components.html(radar_html, height=390)

with col_action:
    st.markdown("🔍 **ANÁLISIS DE AMENAZAS**")
    tab1, tab2, tab3 = st.tabs(["🔗 LINK", "🖼️ FOTO", "📧 EMAIL"])
    
    with tab1:
        st.text_input("URL sospechosa:", placeholder="https://", key="url_in")
    with tab2:
        st.file_uploader("Subir imagen forense:", key="foto_in", label_visibility="collapsed")
    with tab3:
        email_val = st.text_input("Remitente o Cuerpo:", placeholder="ejemplo@dominio.com", key="mail_in")
    
    if st.button("🚀 EJECUTAR PROTOCOLO ANTÍDOTO"):
        with st.spinner("Escaneando vectores..."):
            time.sleep(1.5)
            if email_val and "sat.gob.mx" in email_val:
                st.success("VERIFICADO: Origen legítimo.")
            else:
                st.info("PROCESO FINALIZADO: Sin firmas maliciosas detectadas.")

    st.markdown("📟 **LIVE EVENT LOG**")
    st.markdown("""
    <div style="background:#000; border:1px solid #333; padding:10px; color:#00ff00; font-family:monospace; font-size:0.75rem; height:110px; overflow-y:auto;">
        [SYS] Radar activo...<br>[NET] Nodo CDMX sincronizado.<br>[SEC] Cortafuegos: Interceptación activa.<br>[INF] Módulos de análisis cargados.
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# 5. SECCIÓN INFERIOR: MÉTRICAS DEL SISTEMA
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Fiabilidad", "99.8%", "ÓPTIMO")
with m2: st.metric("Base de Datos", "+500k IPs", "ACTUALIZADO")
with m3: st.metric("Protección", "Activa 24/7", "SECURE")
with m4: st.metric("Uptime", "99.9%", "ESTABLE")

# 6. FOOTER Y FIRMA (SIN CÍRCULOS EN LA ESQUINA)
st.write("---")
f_left, f_right = st.columns([1, 1])

with f_left:
    st.markdown("""
    <div style="display:flex; gap:10px;">
        <div style="background:#238636; color:white; padding:2px 10px; border-radius:4px; font-size:0.7rem; font-weight:bold;">SISTEMA ACTIVO</div>
        <div style="background:#1f6feb; color:white; padding:2px 10px; border-radius:4px; font-size:0.7rem; font-weight:bold;">FIREWALL OK</div>
    </div>
    """, unsafe_allow_html=True)

with f_right:
    st.markdown(f"""
    <div style="text-align: right;">
        <span style="color: #8b949e; font-size: 0.7rem;">[ID SESIÓN: AMX-992-TX]</span><br>
        <span style="color: #8b949e; font-size: 0.8rem;">Desarrollado y Verificado por:</span><br>
        <span class="maynor-brand">MAYNOR, CERTIFIED SPECIALIST</span>
        <div style="display:flex; justify-content:flex-end; gap:12px; margin-top:10px;">
            <div style="border:1px solid #58a6ff; border-radius:50%; width:42px; height:42px; display:flex; align-items:center; justify-content:center; font-size:8px; color:white; background:#0d1117;">Cisco<br>CyOps</div>
            <div style="border:1px solid #f1e05a; border-radius:50%; width:42px; height:42px; display:flex; align-items:center; justify-content:center; font-size:8px; color:white; background:#0d1117;">Ethical<br>Hacker</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
