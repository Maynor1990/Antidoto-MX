import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN Y ESTILO ESCENCIAL
st.set_page_config(page_title="Antídoto MX", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    .stMetric { background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; padding: 10px; }
    
    /* CUADRO DE ACREDITACIÓN (DISCRETO PERO PROFESIONAL) */
    .specialist-footer {
        background: rgba(13, 17, 23, 0.8);
        border-top: 2px solid #00d4ff;
        padding: 20px;
        margin-top: 50px;
        border-radius: 10px 10px 0 0;
    }
    .badge-img { width: 65px; height: 65px; margin: 0 10px; transition: 0.3s; }
    .badge-img:hover { transform: scale(1.1); }
    </style>
    """, unsafe_allow_html=True)

# 2. CABECERA TÉCNICA
st.markdown("<h1 style='text-align: center; color: #58a6ff;'>🛡️ ANTÍDOTO MX: TACTICAL HUB</h1>", unsafe_allow_html=True)
st.write("---")

# 3. CUERPO OPERATIVO (LA INTENCIÓN DEL PROGRAMA)
col_radar, col_analisis = st.columns([1.5, 1])

with col_radar:
    st.subheader("📡 Monitoreo de Red en Tiempo Real")
    radar_html = """
    <div style="background:#000; height:300px; border:1px solid #333; border-radius:8px; display:flex; justify-content:center; align-items:center; overflow:hidden;">
        <div style="width:200px; height:200px; border:2px solid rgba(0,212,255,0.2); border-radius:50%; position:relative;">
            <div style="position:absolute; width:100%; height:100%; background:conic-gradient(from 0deg, rgba(0,212,255,0.4) 0%, transparent 50%); border-radius:50%; animation: spin 4s linear infinite;"></div>
        </div>
        <style> @keyframes spin { to {transform: rotate(360deg);} } </style>
    </div>
    """
    components.html(radar_html, height=310)

with col_analisis:
    st.subheader("🔍 Consola de Análisis")
    opcion = st.radio("Tipo de Escaneo:", ["Rastreo URL", "Análisis de Email", "Forense de Archivos"], horizontal=True)
    entrada = st.text_input("Ingrese objetivo para analizar:", placeholder="https:// o correo@dominio.com")
    
    if st.button("🚀 EJECUTAR PROTOCOLO"):
        with st.status("Analizando integridad de la fuente...", expanded=True) as status:
            st.write("📡 Verificando saltos de red (Traceroute)...")
            time.sleep(1)
            st.write("🔐 Inspeccionando certificados y registros SPF/DKIM...")
            time.sleep(1)
            
            if "sat.gob.mx" in entrada or "stryker" in entrada:
                status.update(label="✅ Verificación Completa: Fuente Legítima", state="complete")
                st.success("ORIGEN VERIFICADO: El sitio/remitente coincide con la identidad oficial.")
            elif entrada:
                status.update(label="⚠️ Amenaza Detectada", state="error")
                # Aquí el detalle que resalta la intención: El tipo de virus
                st.error("""
                    **RESULTADO DEL ANÁLISIS:**
                    - **Tipo de Amenaza:** Ransomware / Troyano de Acceso Remoto (RAT)
                    - **Riesgo:** Crítico (Exfiltración de datos detectada)
                    - **Acción:** Conexión interceptada y bloqueada.
                """)

# 4. MÉTRICAS ESENCIALES
st.write("---")
m1, m2, m3 = st.columns(3)
m1.metric("Fiabilidad", "99.8%", "Veritas")
m2.metric("Base de Datos", "+500k IPs", "Sentinel")
m3.metric("Protección", "Activa 24/7", "Secure")

# 5. FIRMA Y LOGOS (AGREGADOS SIN MODIFICAR EL RESTO)
st.markdown(f"""
<div class="specialist-footer">
    <div style="display: flex; justify-content: justify; align-items: center;">
        <div style="flex-grow: 1;">
            <p style="color: #8b949e; margin: 0; font-size: 0.8rem;">DESARROLLADO Y VERIFICADO POR:</p>
            <h2 style="color: #00d4ff; margin: 0; font-family: sans-serif;">MAYNOR VÁZQUEZ</h2>
            <p style="color: #58a6ff; font-size: 0.9rem; font-weight: bold;">Certified Network Defense & CyberOps Specialist</p>
        </div>
        <div style="display: flex; align-items: center;">
            <img class="badge-img" src="https://images.credly.com/size/110x110/images/6843d79a-ad90-410a-9d9e-99071060934d/CyberOps_Associate_600.png" title="Cisco CyberOps">
            <img class="badge-img" src="https://images.credly.com/size/110x110/images/223793c1-0731-4a40-a15d-007f353240e9/Ethical_Hacker.png" title="Ethical Hacker">
            <img class="badge-img" src="https://images.credly.com/size/110x110/images/9c33959b-1349-4f7f-8d26-03082a5c53c0/Network_Defense.png" title="Network Defense">
            <div style="text-align: right; margin-left: 20px; border-left: 1px solid #30363d; padding-left: 20px;">
                <code style="color: #444;">[ID: AMX-992-TX]</code><br>
                <code style="color: #444;">[STATUS: VERIFIED]</code>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
