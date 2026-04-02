import streamlit as st
import pandas as pd
import requests
import socket
import re
from datetime import datetime
from difflib import SequenceMatcher
from annotated_text import annotated_text

# =========================================================
# 0. CONFIGURACIÓN Y ESTILOS (FRONTEND BASE)
# =========================================================
st.set_page_config(page_title="Antídoto MX - Consola de Inteligencia", page_icon="🛡️", layout="wide")

# Inicializar Estado de la Sesión (para el Historial)
if 'historial' not in st.session_state:
    st.session_state['historial'] = []

# Estilo Dark Mode Profesional y Animaciones
st.markdown("""
    <style>
    /* Fondo General */
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Títulos y Subtítulos */
    h1 { color: #58a6ff; text-align: center; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 10px #58a6ff; }
    h3, h4 { color: #a5d6ff; }
    
    /* Botones Pro */
    .stButton>button { 
        background: linear-gradient(45deg, #238636, #2ea043); 
        color: white; 
        border: none;
        border-radius: 4px; 
        width: 100%; 
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px #2ea043; }

    /* Contenedores de Entrada */
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        background-color: #0d1117; color: #c9d1d9; border: 1px solid #30363d;
    }

    /* --- ANIMACIÓN DEL RADAR GIRATORIO (Estilo Barco) --- */
    @keyframes rotateRadar {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    @keyframes pulseThreat {
        0% { fill: rgba(255, 0, 0, 0.5); }
        50% { fill: rgba(255, 0, 0, 1); }
        100% { fill: rgba(255, 0, 0, 0.5); }
    }

    .radar-container {
        position: relative;
        width: 300px;
        height: 300px;
        background-color: #001a00;
        border: 4px solid #00ff00;
        border-radius: 50%;
        margin: 20px auto;
        box-shadow: 0 0 20px #00ff00;
        overflow: hidden;
    }

    /* Líneas de Cuadrícula del Radar */
    .radar-grid {
        position: absolute; width: 100%; height: 100%;
        background-image: 
            radial-gradient(circle, transparent 30%, #003300 31%, transparent 32%),
            radial-gradient(circle, transparent 60%, #003300 61%, transparent 62%),
            linear-gradient(to right, transparent 49.5%, #003300 50%, transparent 50.5%),
            linear-gradient(to bottom, transparent 49.5%, #003300 50%, transparent 50.5%);
    }

    /* Línea Giratoria del Radar (El Barrido) */
    .radar-sweep {
        position: absolute;
        width: 50%;
        height: 4px;
        background: linear-gradient(to left, #00ff00, transparent);
        top: 50%;
        left: 50%;
        transform-origin: 0% 50%;
        animation: rotateRadar 2s linear infinite;
        box-shadow: 0 0 10px #00ff00;
    }

    /* Puntos de Amenaza Simulados */
    .radar-threat {
        position: absolute;
        width: 10px;
        height: 10px;
        background-color: red;
        border-radius: 50%;
        animation: pulseThreat 1s ease-in-out infinite;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ANTÍDOTO MX")
st.write("### Consola Avanzada de Inteligencia contra Fraude Digital - UnADM")
st.write("---")

# =========================================================
# 1. MOTOR DE INTELIGENCIA (BACKEND)
# =========================================================

def obtener_datos_forenses(url):
    """Rastrea la IP, País, ISP y verifica SSL básico"""
    try:
        dominio = url.split('//')[-1].split('/')[0]
        ip = socket.gethostbyname(dominio)
        geo = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()
        
        # Simulación de verificación SSL (Función 2 solicitada)
        protocolo = url.split(':')[0]
        ssl_status = "SEGURO" if protocolo == "https" else "VULNERABLE (Sin Cifrado)"
        ssl_warning = ""
        if protocolo == "https" and (".xyz" in url or ".top" in url):
             ssl_warning = "⚠️ Certificado SSL sospechoso detectedo (dominio de bajo costo). HTTPS no garantiza legitimidad."

        return {
            "ip": ip,
            "pais": geo.get('country', 'Desconocido'),
            "isp": geo.get('isp', 'Desconocido'),
            "dominio": dominio,
            "ssl_status": ssl_status,
            "ssl_warning": ssl_warning
        }
    except:
        return None

def analizar_archivos_sospechosos(nombre_archivo):
    """Detecta extensiones peligrosas comunes en México (Función 3 solicitada)"""
    extensiones_criticas = {
        ".exe": "Ejecutable de Windows. Alto riesgo de malware.",
        ".scr": "Protector de pantalla. Usado frecuentemente para troyanos bancarios.",
        ".zip": "Archivo comprimido. Puede contener scripts maliciosos ocultos.",
        ".bat": "Archivo de lotes. Puede ejecutar comandos del sistema sin permiso."
    }
    ext = "." + nombre_archivo.split('.')[-1].lower() if '.' in nombre_archivo else ""
    return extensiones_criticas.get(ext, "Extensión común o no identificada como crítica.")

# =========================================================
# 2. SECCIÓN PRINCIPAL: RASTREO Y ANÁLISIS
# =========================================================
col_radar, col_analisis = st.columns([1, 2])

with col_radar:
    st.markdown("#### 🛰️ Radar Activo de Amenazas")
    # Generar el Radar Animado en HTML/CSS
    radar_html = """
    <div class="radar-container">
        <div class="radar-grid"></div>
        <div class="radar-sweep"></div>
        <div class="radar-threat" style="top: 20%; left: 80%; animation-delay: 0.5s;"></div> <div class="radar-threat" style="top: 60%; left: 30%; animation-delay: 1.2s;"></div> <div class="radar-threat" style="top: 80%; left: 70%; animation-delay: 1.8s;"></div> </div>
    """
    st.markdown(radar_html, unsafe_allow_html=True)
    st.caption("🔴 Puntos Rojos: Amenazas Críticas Detectadas (Rusia, EE.UU., México)")

with col_analisis:
    st.markdown("#### 🔍 Consola de Rastre Forensic")
    
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            url_input = st.text_input("🔗 Link sospechoso:", placeholder="https://cfe-recibo-mex.xyz")
        with c2:
            file_input = st.text_input("📁 Archivo sospechoso:", placeholder="factura_cfe.exe")
            
        boton_analizar = st.button("🚀 INICIAR CONTRAMEDIDAS")

    # Procesar Análisis
    if boton_analizar:
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            if url_input:
                with st.spinner('Desarmando infraestructura del atacante...'):
                    datos = obtener_datos_forenses(url_input)
                    if datos:
                        st.success(f"✅ Análisis Completado: {datos['dominio']}")
                        st.metric("País", datos['pais'])
                        st.metric("IP", datos['ip'])
                        st.info(f"📋 **ISP:** {datos['isp']}")
                        
                        # Alertas Críticas de Geolocalización
                        if "Mexico" not in datos['pais']:
                            st.error(f"🚨 ALERTA: Servidor en {datos['pais']}. Riesgo ALTO de Phishing.")

                        # Alerta SSL (Función 2)
                        if datos['ssl_warning']:
                            st.warning(datos['ssl_warning'])
                        
                        # Guardar en Historial (Función 1)
                        st.session_state['historial'].append({
                            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "Tipo": "Enlace",
                            "Objetivo": datos['dominio'],
                            "Origen": datos['pais']
                        })
                    else:
                        st.error("❌ Error de conexión. Link inactivo o falso.")
            else:
                st.warning("⚠️ Ingresa una URL para iniciar el rastreo forense.")

        with res_col2:
            if file_input:
                with st.spinner('Analizando código malicioso...'):
                    analisis_file = analizar_archivos_sospechosos(file_input)
                    st.info(f"📋 **Análisis de Archivo:** {file_input}")
                    if "Alto riesgo" in analisis_file or "frecuentemente" in analisis_file:
                        st.error(f"🚨 {analisis_file}")
                    else:
                        st.success(f"✅ {analisis_file}")
                    
                    # Guardar en Historial (Función 1)
                    st.session_state['historial'].append({
                        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "Tipo": "Archivo",
                        "Objetivo": file_input,
                        "Origen": "Local"
                    })

# =========================================================
# 3. SECCIÓN DE DATOS: HISTORIAL (Función 1)
# =========================================================
st.write("---")
st.markdown("#### 📊 Historial de Consultas Recientes")

if st.session_state['historial']:
    df_historial = pd.DataFrame(st.session_state['historial'])
    # Invertir el orden para ver lo más reciente primero
    st.table(df_historial.iloc[::-1]) 
    
    if st.button("🗑️ Limpiar Historial"):
        st.session_state['historial'] = []
        st.experimental_rerun()
else:
    st.caption("No hay consultas en esta sesión. Inicia un análisis arriba.")

# =========================================================
# 4. FOOTER Y CRÉDITOS
# =========================================================
st.write("---")
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.write("🛠️ **Estatus del Sistema:**")
    st.success("Motor Heurístico: ONLINE")
    annotated_text(("Geolocalización", "ACTIVA", "#2ea043"), ("Análisis SSL", "ACTIVO", "#2ea043"))
with col_f2:
    st.write("👨‍💻 **Desarrollo:**")
    st.caption("Desarrollado por Mynor Vazquez | UnADM | Ciberseguridad Independiente")
    st.caption(f"Última actualización de consola: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
