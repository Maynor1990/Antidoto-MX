import streamlit as st
import pandas as pd
import requests
import socket
import re
from datetime import datetime
from difflib import SequenceMatcher
from annotated_text import annotated_text
from PIL import Image
from PIL.ExifTags import TAGS

# =========================================================
# 0. CONFIGURACIÓN Y ESTILOS PROFESIONALES
# =========================================================
st.set_page_config(page_title="Antídoto MX | Inteligencia Digital", page_icon="🛡️", layout="wide")

if 'historial' not in st.session_state:
    st.session_state['historial'] = []

# Estilo Dark Mode y Radar Animado
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    h1 { color: #58a6ff; text-align: center; letter-spacing: 3px; text-shadow: 0 0 10px #58a6ff; }
    h3, h4 { color: #a5d6ff; }
    
    .stButton>button { 
        background: linear-gradient(45deg, #1f6feb, #388bfd); 
        color: white; border: none; border-radius: 4px; font-weight: bold; width: 100%;
    }

    @keyframes rotateRadar { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    @keyframes pulse { 0% { opacity: 0.4; } 50% { opacity: 1; } 100% { opacity: 0.4; } }

    .radar-container {
        position: relative; width: 280px; height: 280px;
        background-color: #000d00; border: 2px solid #00ff00;
        border-radius: 50%; margin: 20px auto; overflow: hidden;
    }
    .radar-sweep {
        position: absolute; width: 50%; height: 2px;
        background: linear-gradient(to left, #00ff00, transparent);
        top: 50%; left: 50%; transform-origin: 0% 50%;
        animation: rotateRadar 2s linear infinite;
    }
    .radar-threat {
        position: absolute; width: 8px; height: 8px;
        background-color: #ff0000; border-radius: 50%;
        animation: pulse 1.5s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ANTÍDOTO MX")
st.write("### Consola de Ciberinteligencia y Análisis Forense")
st.write("---")

# =========================================================
# 1. MOTOR DE ANÁLISIS
# =========================================================

def obtener_datos_forenses(url):
    try:
        dominio = url.split('//')[-1].split('/')[0]
        ip = socket.gethostbyname(dominio)
        geo = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()
        
        protocolo = url.split(':')[0]
        ssl_warning = ""
        if protocolo == "https" and (".xyz" in url or ".top" in url):
             ssl_warning = "⚠️ Certificado SSL sospechoso detectedo (dominio de bajo costo). HTTPS no garantiza legitimidad."

        return {
            "ip": ip, "pais": geo.get('country', 'Desconocido'),
            "isp": geo.get('isp', 'Desconocido'), "dominio": dominio,
            "ssl_warning": ssl_warning
        }
    except:
        return None

def analizar_archivo(nombre):
    riesgos = {".exe": "Ejecutable", ".scr": "Script de sistema", ".bat": "Archivo de comandos", ".vbs": "Script de Visual Basic"}
    ext = "." + nombre.split('.')[-1].lower() if '.' in nombre else ""
    return riesgos.get(ext, "Extensión estándar o desconocida")

def escanear_imagen(imagen_file):
    """Analiza metadatos EXIF de una imagen para detectar sospechas"""
    try:
        img = Image.open(imagen_file)
        exif_data = img._getexif()
        sospecha = "Baja"
        detalles = []
        
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == 'GPSInfo':
                    detalles.append("📍 Coordenadas GPS detectadas en los metadatos.")
                    sospecha = "Media"
                elif tag == 'DateTimeOriginal':
                    detalles.append(f"📅 Fecha de captura original: {value}")
                elif tag == 'Make' or tag == 'Model':
                    detalles.append(f"📷 Dispositivo: {value}")
        else:
            detalles.append("✅ No se detectaron metadatos EXIF críticos.")
            
        return sospecha, detalles
    except Exception as e:
        return "N/A", [f"Error al analizar la imagen: {e}"]

# =========================================================
# 2. INTERFAZ PRINCIPAL
# =========================================================
col_radar, col_analisis = st.columns([1, 2])

with col_radar:
    st.markdown("#### 🛰️ Radar de Nodos Activo")
    st.markdown("""
    <div class="radar-container">
        <div class="radar-sweep"></div>
        <div class="radar-threat" style="top: 25%; left: 75%;"></div>
        <div class="radar-threat" style="top: 65%; left: 25%;"></div>
        <div class="radar-threat" style="top: 80%; left: 60%; animation-delay: 1s;"></div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("🔴 Nodos externos bajo vigilancia en tiempo real.")

with col_analisis:
    st.markdown("#### 🔍 Consola de Rastre Forensic")
    
    with st.container():
        c1, c2 = st.columns(2)
        url_in = c1.text_input("🔗 Enlace a investigar:", placeholder="URL sospechosa...")
        file_in = c2.text_input("📁 Archivo a verificar:", placeholder="archivo.exe...")
        
    # NUEVA SECCIÓN: SUBIDA DE IMAGEN
    st.markdown("#### 🖼️ Escáner de Imágenes Forenses")
    img_in = st.file_uploader("Sube una foto sospechosa para analizar metadatos:", type=['jpg', 'jpeg', 'png'])

    # BOTÓN ÚNICO DE EJECUCIÓN
    st.write("")
    if st.button("🚀 EJECUTAR ESCANEO Y ANÁLISIS"):
        st.write("---")
        res_col1, res_col2, res_col3 = st.columns(3)
        
        # 1. ANÁLISIS DE URL
        with res_col1:
            if url_in:
                datos = obtener_datos_forenses(url_in)
                if datos:
                    st.success(f"Resultados para: {datos['dominio']}")
                    st.metric("País de Origen", datos['pais'])
                    st.metric("Dirección IP", datos['ip'])
                    if datos['ssl_warning']: st.warning(datos['ssl_warning'])
                    
                    if "Mexico" not in datos['pais']:
                        st.error(f"🚨 Alerta: Servidor fuera de México ({datos['pais']}). Riesgo alto.")

                    st.session_state['historial'].append({
                        "Fecha": datetime.now().strftime("%H:%M:%S"),
                        "Tipo": "URL", "Objetivo": datos['dominio'], "Origen": datos['pais']
                    })

        # 2. ANÁLISIS DE ARCHIVO
        with res_col2:
            if file_in:
                res_file = analizar_archivo(file_in)
                st.info(f"Análisis de archivo: {file_in}")
                if "Ejecutable" in res_file or "Script" in res_file:
                    st.error(f"🚨 Tipo: {res_file}. Riesgo Crítico.")
                else:
                    st.success(f"✅ Tipo: {res_file}.")
                
                st.session_state['historial'].append({
                    "Fecha": datetime.now().strftime("%H:%M:%S"),
                    "Tipo": "Archivo", "Objetivo": file_in, "Origen": "Local"
                })

        # 3. ANÁLISIS DE IMAGEN
        with res_col3:
            if img_in:
                sospecha_img, detalles_img = escanear_imagen(img_in)
                st.info(f"Análisis de imagen: {img_in.name}")
                st.metric("Nivel de Sospecha", sospecha_img)
                
                if sospecha_img == "Media":
                    st.warning("🚨 Alerta de Metadatos: Se encontraron datos de ubicación.")
                else:
                    st.success("✅ Metadatos limpios.")
                
                for detalle in detalles_img:
                    st.caption(detalle)
                
                st.session_state['historial'].append({
                    "Fecha": datetime.now().strftime("%H:%M:%S"),
                    "Tipo": "Imagen", "Objetivo": img_in.name, "Origen": sospecha_img
                })

# =========================================================
# 3. HISTORIAL Y PIE DE PÁGINA
# =========================================================
st.write("---")
if st.session_state['historial']:
    st.markdown("#### 📊 Actividad de Sesión Reciente")
    st.table(pd.DataFrame(st.session_state['historial']).iloc[::-1])

st.write("---")
f1, f2 = st.columns(2)
with f1:
    st.write("🛠️ **Estado:**")
    annotated_text(("Sistemas", "ONLINE", "#2ea043"), ("Radar", "ACTIVO", "#2ea043"))
with f2:
    st.write("👨‍💻 **Desarrollador:**")
    st.caption("Maynor | Especialista Independiente en Seguridad Digital")
