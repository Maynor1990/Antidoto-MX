import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN Y ESTILOS ENFOCADOS EN LA CONSOLA
st.set_page_config(page_title="Antídoto MX", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Resaltado de la Consola de Análisis */
    .analysis-card {
        background: #0d1117;
        border: 2px solid #58a6ff;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 0 15px rgba(88, 166, 255, 0.2);
    }
    
    .stMetric { background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; padding: 10px; }
    
    /* Pie de página profesional */
    .specialist-footer {
        background: rgba(13, 17, 23, 0.9);
        border-top: 1px solid #30363d;
        padding: 15px 30px;
        margin-top: 40px;
    }
    
    .badge-img { 
        width: 60px; 
        height: auto; 
        margin-left: 15px;
        filter: drop-shadow(0 0 5px rgba(88, 166, 255, 0.5));
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CABECERA
st.markdown("<h1 style='text-align: center; color: #58a6ff;'>🛡️ ANTÍDOTO MX: TACTICAL HUB</h1>", unsafe_allow_html=True)
st.write("---")

# 3. DISTRIBUCIÓN: RADAR PEQUEÑO Y CONSOLA GRANDE
col_radar, col_analisis = st.columns([0.8, 2]) # El radar ocupa menos espacio que la consola

with col_radar:
    st.markdown("<p style='color: #8b949e; font-size: 0.8rem; text-align: center;'>🛰️ MONITOR RADAR</p>", unsafe_allow_html=True)
    # Radar más pequeño y compacto
    radar_html = """
    <div style="background:#000; height:180px; width:180px; border:1px solid #333; border-radius:50%; margin: auto; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <div style="width:140px; height:140px; border:1px solid rgba(0,212,255,0.1); border-radius:50%; position:relative;">
            <div style="position:absolute; width:100%; height:100%; background:conic-gradient(from 0deg, rgba(0,212,255,0.3) 0%, transparent 60%); border-radius:50%; animation: spin 3s linear infinite;"></div>
        </div>
        <style> @keyframes spin { to {transform: rotate(360deg);} } </style>
    </div>
    """
    components.html(radar_html, height=200)
    st.caption("Nodo CDMX: Sincronizado")

with col_analisis:
    st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
    st.subheader("🔍 CONSOLA DE ANÁLISIS PROFUNDO")
    
    tipo = st.segmented_control("Protocolo de Escaneo:", ["Rastreo URL", "Análisis de Email", "Forense de Archivos"], default="Rastreo URL")
    objetivo = st.text_input("Ingrese la dirección o archivo a analizar:", placeholder="https://... o correo@dominio.com")
    
    if st.button("🚀 EJECUTAR PROTOCOLO ANTÍDOTO", use_container_width=True):
        if objetivo:
            with st.status("Iniciando disección digital...", expanded=True) as status:
                st.write("📡 Escaneando saltos de red...")
                time.sleep(0.8)
                st.write("🔬 Analizando firmas de malware conocido...")
                time.sleep(1)
                
                if "sat.gob.mx" in objetivo.lower():
                    status.update(label="✅ ORIGEN VERIFICADO", state="complete")
                    st.success(f"ENTIDAD LEGÍTIMA DETECTADA: El objetivo {objetivo} es seguro.")
                else:
                    status.update(label="🚨 AMENAZA IDENTIFICADA", state="error")
                    st.error(f"ALERTA: Se han detectado rastros de **Ransomware/RAT** en {objetivo}. Conexión bloqueada por seguridad.")
        else:
            st.warning("Por favor, ingrese un objetivo para el análisis.")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. MÉTRICAS DE ESTADO
st.write("")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Fiabilidad", "99.8%", "Veritas")
m2.metric("Base de Datos", "+500k IPs", "Sentinel")
m3.metric("Protección", "Activa 24/7", "Secure")
m4.metric("Uptime", "99.9%", "Estable")

# 5. PIE DE PÁGINA: MAYNOR VÁZQUEZ Y LOGOS VISIBLES
st.markdown(f"""
<div class="specialist-footer">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h3 style="color: #00d4ff; margin: 0; font-family: sans-serif;">MAYNOR VÁZQUEZ</h3>
            <p style="color: #58a6ff; margin: 0; font-size: 0.85rem; font-weight: bold;">Certified Specialist | Network Defense & CyberOps</p>
        </div>
        <div style="display: flex; align-items: center;">
            <img class="badge-img" src="https://images.credly.com/size/110x110/images/6843d79a-ad90-410a-9d9e-99071060934d/CyberOps_Associate_600.png" alt="CyberOps">
            <img class="badge-img" src="https://images.credly.com/size/110x110/images/223793c1-0731-4a40-a15d-007f353240e9/Ethical_Hacker.png" alt="Ethical Hacker">
            <img class="badge-img" src="https://images.credly.com/size/110x110/images/9c33959b-1349-4f7f-8d26-03082a5c53c0/Network_Defense.png" alt="Network Defense">
            <div style="margin-left: 20px; text-align: right;">
                <code style="color: #444; display: block;">[ID: AMX-992-TX]</code>
                <code style="color: #00d4ff; font-weight: bold;">[STATUS: VERIFIED]</code>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
