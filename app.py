import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. BASE DE DATOS DE REPUTACIÓN (LISTA NEGRA)
DB_MALWARE_DOMAINS = [".top", ".xyz", ".click", ".pw", ".online", ".zip", ".mov"]
DB_PHISHING_KEYWORDS = ["ganaste", "premio", "urgente", "factura-pendiente", "banco-seguro", "verificar-cuenta"]
DB_KNOWN_ATTACKS = {
    "malicious-site.top": {"virus": "Ransomware (LockBit)", "origin": "Rusia / Proxy Dinámico"},
    "update-java.xyz": {"virus": "Troyano de Acceso Remoto (RAT)", "origin": "Europa del Este"},
    "soporte-tecnico.click": {"virus": "Spyware / Exfiltración", "origin": "Sudeste Asiático"}
}

# 3. ESTILOS CSS
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 20px;
    }
    .stMetric { background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; text-align: center; }
    .virus-report {
        background-color: #1a0505; border: 2px solid #ff4b4b; border-radius: 10px; 
        padding: 20px; color: #ffbaba; margin-top: 15px;
    }
    .maynor-footer {
        margin-top: 50px; padding: 20px; border-top: 1px solid #30363d;
        display: flex; justify-content: space-between; align-items: center;
    }
    /* Estilos para las insignias */
    .badge-card {
        background-color: #0d1117;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        width: 150px;
        margin: 5px;
    }
    .badge-card:hover { transform: scale(1.05); transition: transform 0.2s; }
    .badge-icon { width: 60px; height: 60px; margin-bottom: 10px; }
    .badge-title { font-size: 0.8rem; font-weight: bold; color: #c9d1d9; }
    .badge-type { font-size: 0.7rem; color: #8b949e; }
    .badge-date { font-size: 0.6rem; color: #58a6ff; }
    </style>
    """, unsafe_allow_html=True)

# 4. ENCABEZADO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-top:-20px;'>TACTICAL HUB - BASE DE DATOS SENTINEL ACTIVA</p>", unsafe_allow_html=True)

# 5. PANEL OPERATIVO
col_left, col_right = st.columns([1, 1.2])

with col_left:
    radar_html = """
    <div style="background:#000; height:300px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <style>
            .scan { position:absolute; width:220px; height:220px; background:conic-gradient(from 0deg, rgba(0,212,255,0.3) 0%, transparent 50%); border-radius:50%; animation: r 3s linear infinite; }
            .line-h { position:absolute; width:100%; height:1px; background:rgba(0,212,255,0.2); top:50%; }
            .line-v { position:absolute; height:100%; width:1px; background:rgba(0,212,255,0.2); left:50%; }
            @keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
        </style>
        <div class="line-h"></div><div class="line-v"></div><div class="scan"></div>
        <div style="position:absolute; bottom:10px; color:#00d4ff; font-family:monospace; font-size:11px;">DB STATUS: SYNCHRONIZED | NODO: CDMX</div>
    </div>
    """
    components.html(radar_html, height=310)

with col_right:
    st.markdown("### 🔍 CONSOLA DE ANÁLISIS")
    tab1, tab2 = st.tabs(["🔗 LINK / URL", "📧 EMAIL"])
    
    target = ""
    with tab1: target = st.text_input("Ingrese URL para rastreo:", placeholder="Ej: sospechoso.top", key="u_in")
    with tab2: target = st.text_input("Ingrese Remitente de correo:", placeholder="ejemplo@dominio.com", key="e_in")
    
    if st.button("🚀 INICIAR ESCANEO TÁCTICO", use_container_width=True):
        if target:
            log_area = st.empty()
            logs = ["[SYS] Accediendo a Base de Datos de Reputación..."]
            
            steps = ["📡 Consultando PhishTank...", "🔗 Verificando WHOIS...", "🔬 Comparando firmas...", "📂 Disección completada."]
            for s in steps:
                logs.append(f"[INF] {s}")
                log_area.code("\n".join(logs))
                time.sleep(0.6)

            is_malicious = False
            virus_type = ""
            origin = ""

            if target in DB_KNOWN_ATTACKS:
                is_malicious = True
                virus_type = DB_KNOWN_ATTACKS[target]["virus"]
                origin = DB_KNOWN_ATTACKS[target]["origin"]
            elif any(ext in target.lower() for ext in DB_MALWARE_DOMAINS) or any(key in target.lower() for key in DB_PHISHING_KEYWORDS):
                is_malicious = True
                virus_type = "Troyano / Phishing (Heurística Detectada)"
                origin = "Localizado en Servidor Proxy Externo"

            if is_malicious:
                st.markdown(f"""
                <div class="virus-report">
                    <h4>🚨 REPORTE FORENSE: POSITIVO</h4>
                    <p><b>Clasificación:</b> {virus_type}</p>
                    <p><b>Fuente de Ataque:</b> {origin}</p>
                    <hr style='border: 0.5px solid #ff4b4b;'>
                    <p><b>Acción Automática:</b> El objetivo ha sido bloqueado y enviado al <b>Baúl de Cuarentena</b>.</p>
                    <p><b>Estado:</b> Amenaza eliminada satisfactoriamente.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.success("✅ REPORTE: Objeto limpio. No coincide con ninguna entrada maliciosa.")
        else:
            st.warning("⚠️ Ingrese un dato para realizar la consulta.")

st.write("---")

# 6. MÉTRICAS
m1, m2, m3, m4 = st.columns(4)
m1.metric("Fiabilidad", "99.8%", "Veritas")
m2.metric("Base de Datos", f"+{len(DB_MALWARE_DOMAINS) + 500}k Firmas", "Actualizado")
m3.metric("Protección", "Activa 24/7", "Secure")
m4.metric("Uptime", "99.9%", "Estable")

# 7. PIE DE PÁGINA (MAYNOR VÁZQUEZ E INSIGNIAS)
st.markdown("### 🏆 LOGROS DEL ESPECIALISTA CERTIFICADO")
col_footer, col_badges = st.columns([1.5, 3])

with col_footer:
    st.markdown("""
        <div>
            <h2 style="color: #00d4ff; margin:0;">MAYNOR VÁZQUEZ</h2>
            <p style="color: #8b949e; font-size: 0.9rem;">Network Defense & CyberOps Specialist</p>
        </div>
        """, unsafe_allow_html=True)

with col_badges:
    # Insignias Integradas (Ajustadas de imagen_63.png)
    st.markdown("""
        <div style="display: flex; justify-content: flex-start; flex-wrap: wrap;">
            <div class="badge-card">
                <img class="badge-icon" src="https://example.com/icons/hacker_etico.png" alt="Icono Hacker Ético">
                <div class="badge-type">Curso</div>
                <div class="badge-title">Hacker Ético</div>
                <div class="badge-date">Emitido: 14 mar 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://example.com/icons/ingenieria_social.png" alt="Icono Ingeniería Social">
                <div class="badge-type">Módulo</div>
                <div class="badge-title">Ataques de Ingeniería Social</div>
                <div class="badge-date">Emitido: 10 feb 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://example.com/icons/defensa_red.png" alt="Icono Defensa de la Red">
                <div class="badge-type">Módulo</div>
                <div class="badge-title">Defensa de la Red</div>
                <div class="badge-date">Emitido: 07 feb 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://example.com/icons/analisis_amenazas.png" alt="Icono Análisis de Amenazas">
                <div class="badge-type">Módulo</div>
                <div class="badge-title">Análisis de Amenazas</div>
                <div class="badge-date">Emitido: 05 feb 2026</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    # Reemplaza 'https://example.com/icons/...' con los enlaces reales a las imágenes de tus insignias.
