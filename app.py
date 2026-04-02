import streamlit as st
import streamlit.components.v1 as components
import time
import random

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS (DISEÑO TÁCTICO Y FIRMA EXPANDIDA)
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Título con resplandor */
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 5px;
    }

    /* Paneles de Interacción */
    .interact-panel {
        background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; 
        padding: 15px; height: 350px;
    }

    /* Métricas del Sistema */
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

    /* CUADRO DE ESPECIALISTA (PIE DE PÁGINA) */
    .specialist-card {
        background: rgba(13, 17, 23, 0.9);
        border: 2px solid #00d4ff;
        border-radius: 15px;
        padding: 25px;
        margin-top: 30px;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
    }
    
    .name-brand {
        color: #ffffff; font-size: 2.2rem; font-weight: 900;
        text-shadow: 0 0 10px #58a6ff; margin-bottom: 20px;
        font-family: 'Segoe UI', sans-serif;
    }

    .badge-container { display: flex; justify-content: flex-start; gap: 25px; flex-wrap: wrap; }
    
    .badge-circle {
        width: 85px; height: 85px; border-radius: 50%; border: 2px solid #30363d;
        display: flex; align-items: center; justify-content: center; background: #010409;
        margin-bottom: 10px; padding: 5px;
    }

    .badge-label { font-size: 0.7rem; font-weight: bold; color: #58a6ff; text-align: center; max-width: 90px; }

    /* Estilo del Log */
    .log-text { color: #00ff00; font-family: monospace; font-size: 0.75rem; }
    .log-err { color: #ff4b4b; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 0.8rem;'>TACTICAL HUB - CENTRO DE RESPUESTA A INCIDENTES</p>", unsafe_allow_html=True)

# 4. FILA SUPERIOR: PANEL OPERATIVO
col_tips, col_radar, col_action = st.columns([1, 1.8, 1])

with col_tips:
    st.markdown("""
    <div class="interact-panel">
        <h4 style="color:#58a6ff;">💡 CONSEJOS TÁCTICOS</h4>
        <p style="font-size:0.85rem; border-left: 2px solid #58a6ff; padding-left:10px;"><b>Phishing:</b> Verifica dominios. No cedas a la urgencia.</p>
        <p style="font-size:0.85rem; border-left: 2px solid #58a6ff; padding-left:10px;"><b>Privacidad:</b> Limpia metadatos EXIF de tus archivos.</p>
        <p style="font-size:0.85rem; border-left: 2px solid #58a6ff; padding-left:10px;"><b>Redes:</b> Usa VPN en puntos de acceso públicos.</p>
    </div>
    """, unsafe_allow_html=True)

with col_radar:
    radar_code = """
    <div style="background:#000; height:350px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <style>
            .scan { position:absolute; width:180px; height:180px; background:conic-gradient(from 0deg, rgba(0,212,255,0.3) 0%, transparent 40%); border-radius:50%; animation: r 4s linear infinite; }
            @keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
        </style>
        <div class="scan"></div>
        <div style="position:absolute; bottom:8px; color:#00d4ff; font-family:monospace; font-size:10px;">SCANNING NODO CDMX...</div>
    </div>
    """
    components.html(radar_code, height=360)

with col_action:
    st.markdown("🔍 **ANÁLISIS DE AMENAZAS**")
    tab1, tab2, tab3 = st.tabs(["🔗 LINK", "🖼️ FOTO", "📧 EMAIL"])
    with tab1: url_in = st.text_input("URL:", placeholder="https://", key="u1")
    with tab2: st.file_uploader("Imagen:", key="f1", label_visibility="collapsed")
    with tab3: mail_in = st.text_input("Remitente:", placeholder="ejemplo@dominio.com", key="m1")
    
    if st.button("🚀 INICIAR PROTOCOLO"):
        log_placeholder = st.empty()
        logs = ["[SYS] Iniciando Protocolo Antídoto MX..."]
        
        for msg in ["Analizando cabeceras...", "Verificando reputación IP...", "Escaneando firmas de malware..."]:
            logs.append(f"[INF] {msg}")
            log_placeholder.markdown(f"<div style='background:#000; padding:10px; height:80px; border:1px solid #333;'>{'<br>'.join(logs)}</div>", unsafe_allow_html=True)
            time.sleep(0.5)
            
        if url_in and ".top" in url_in:
            st.error("🚨 AMENAZA DETECTADA: Ransomware (LockBit V3)")
        elif mail_in and ("premio" in mail_in.lower() or "ganaste" in mail_in.lower()):
            st.error("🚨 AMENAZA DETECTADA: Phishing/Scam (Ingeniería Social)")
        else:
            st.success("✅ SISTEMA LIMPIO: Sin anomalías detectadas.")

st.write("---")

# 5. MÉTRICAS
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Fiabilidad", "99.8%", "ÓPTIMO")
with m2: st.metric("Base de Datos", "+500k IPs", "ACTUALIZADO")
with m3: st.metric("Protección", "Activa 24/7", "SECURE")
with m4: st.metric("Uptime", "99.9%", "ESTABLE")

# 6. CUADRO DE ESPECIALISTA (MAYNOR VÁZQUEZ)
st.markdown(f"""
<div class="specialist-card">
    <div style="float:right; font-family:monospace; color:#444; font-size:0.75rem;">[ID SESIÓN: AMX-992-TX]</div>
    <div style="color:#8b949e; font-size:0.9rem; letter-spacing:2px;">DESARROLLADO Y VERIFICADO POR:</div>
    <div class="name-brand">MAYNOR VÁZQUEZ, CERTIFIED SPECIALIST</div>
    
    <div class="badge-container">
        <div class="badge-item">
            <div class="badge-circle" style="border-color:#58a6ff;"><img src="https://images.credly.com/size/110x110/images/6843d79a-ad90-410a-9d9e-99071060934d/CyberOps_Associate_600.png" width="70"></div>
            <div class="badge-label">Cisco CyberOps Associate</div>
        </div>
        <div class="badge-item">
            <div class="badge-circle" style="border-color:#f1e05a;"><img src="https://images.credly.com/size/110x110/images/223793c1-0731-4a40-a15d-007f353240e9/Ethical_Hacker.png" width="70"></div>
            <div class="badge-label">Ethical Hacker</div>
        </div>
        <div class="badge-item">
            <div class="badge-circle" style="border-color:#3fb950;"><img src="https://images.credly.com/size/110x110/images/9c33959b-1349-4f7f-8d26-03082a5c53c0/Network_Defense.png" width="70"></div>
            <div class="badge-label">Network Defense</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
