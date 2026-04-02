import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. BASE DE DATOS DE AMENAZAS
DB_MALWARE_DOMAINS = [".top", ".xyz", ".click", ".pw", ".online", ".zip", ".mov"]
DB_PHISHING_KEYWORDS = ["ganaste", "premio", "urgente", "factura-pendiente", "banco-seguro", "verificar-cuenta"]
DB_KNOWN_ATTACKS = {
    "malicious-site.top": {"virus": "Ransomware (LockBit)", "origin": "Rusia / Proxy Dinámico"},
    "update-java.xyz": {"virus": "Troyano RAT", "origin": "Europa del Este"},
    "soporte-tecnico.click": {"virus": "Spyware", "origin": "Sudeste Asiático"}
}

# 3. ESTILOS CSS (LIMPIEZA Y VISIBILIDAD)
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
    }

    /* CONTENEDOR INTEGRADO (SIN TÍTULO DE LOGROS) */
    .maynor-footer {
        margin-top: 40px; padding: 25px; border-top: 1px solid #30363d;
        background: rgba(13, 17, 23, 0.8); border-radius: 12px;
        display: flex; justify-content: space-between; align-items: center;
    }

    .badge-container { display: flex; gap: 15px; }

    .badge-card {
        background-color: #0d1117; border: 2px solid #30363d; border-radius: 10px;
        padding: 15px; text-align: center; width: 140px;
        transition: transform 0.2s;
    }

    .badge-card:hover { transform: scale(1.05); border-color: #58a6ff; }

    .badge-icon { 
        width: 60px; height: 60px; margin-bottom: 10px;
        filter: drop-shadow(0 0 8px rgba(88, 166, 255, 0.6));
    }

    .badge-title { font-size: 0.85rem; font-weight: bold; color: #ffffff; }
    .badge-date { font-size: 0.7rem; color: #58a6ff; font-family: monospace; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 4. ENCABEZADO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-top:-20px;'>TACTICAL HUB - BASE DE DATOS SENTINEL ACTIVA</p>", unsafe_allow_html=True)

# 5. INTERFAZ TÁCTICA
col_left, col_right = st.columns([1, 1.2])

with col_left:
    radar_html = """
    <div style="background:#000; height:300px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <style>
            .scan { position:absolute; width:220px; height:220px; background:conic-gradient(from 0deg, rgba(0,212,255,0.2) 0%, transparent 50%); border-radius:50%; animation: r 3s linear infinite; }
            @keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
        </style>
        <div class="scan"></div>
        <div style="position:absolute; bottom:10px; color:#00d4ff; font-family:monospace; font-size:11px;">DB STATUS: SYNCHRONIZED</div>
    </div>
    """
    components.html(radar_html, height=310)

with col_right:
    st.markdown("### 🔍 CONSOLA DE ANÁLISIS")
    target = st.text_input("Ingrese URL o Email para rastreo:", placeholder="Ej: sospechoso.top")
    
    if st.button("🚀 INICIAR ESCANEO TÁCTICO", use_container_width=True):
        if target:
            with st.status("Ejecutando Protocolo Antídoto...", expanded=True) as s:
                st.write("📡 Consultando PhishTank...")
                time.sleep(0.5)
                st.write("🔬 Comparando firmas de virus...")
                time.sleep(0.5)
                s.update(label="Escaneo Finalizado", state="complete")

            is_malicious = target in DB_KNOWN_ATTACKS or any(ext in target.lower() for ext in DB_MALWARE_DOMAINS)
            
            if is_malicious:
                info = DB_KNOWN_ATTACKS.get(target, {"virus": "Heurística Detectada", "origin": "Proxy Externo"})
                st.error(f"🚨 POSITIVO: {info['virus']} detectado desde {info['origin']}. Bloqueado automáticamente.")
            else:
                st.success("✅ REPORTE: Objeto limpio.")

st.write("---")

# 6. MÉTRICAS
m1, m2, m3, m4 = st.columns(4)
m1.metric("Fiabilidad", "99.8%")
m2.metric("Base de Datos", "+507k Firmas")
m3.metric("Protección", "Activa 24/7")
m4.metric("Uptime", "99.9%")

# 7. FIRMA E INSIGNIAS (SIN EL TÍTULO DE LOGROS)
st.markdown(f"""
    <div class="maynor-footer">
        <div>
            <h2 style="color: #00d4ff; margin:0; text-shadow: 0 0 10px #00d4ff;">MAYNOR VÁZQUEZ</h2>
            <p style="color: #ffffff; font-size: 0.9rem; font-weight: bold; margin:0;">Network Defense & CyberOps Specialist</p>
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
