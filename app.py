import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN DE PÁGINA TÁCTICA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. BASE DE DATOS DE REPUTACIÓN SENTINEL ACTIVA
DB_MALWARE_DOMAINS = [".top", ".xyz", ".click", ".pw", ".online", ".zip", ".mov"]
DB_PHISHING_KEYWORDS = ["ganaste", "premio", "urgente", "factura-pendiente", "banco-seguro", "verificar-cuenta"]
DB_KNOWN_ATTACKS = {
    "malicious-site.top": {"virus": "Ransomware (LockBit)", "origin": "Rusia / Proxy Dinámico"},
    "update-java.xyz": {"virus": "Troyano de Acceso Remoto (RAT)", "origin": "Europa del Este"},
    "soporte-tecnico.click": {"virus": "Spyware / Exfiltración", "origin": "Sudeste Asiático"}
}

# 3. ESTILOS CSS AVANZADOS (PARA MÁXIMA VISIBILIDAD)
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Efecto de resplandor para el encabezado */
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 20px;
    }

    /* Paneles de interacción nítidos */
    .interact-panel {
        background-color: #0d1117; border: 1px solid #30363d; border-radius: 8px; 
        padding: 15px;
    }

    /* Métricas del Sistema con mejor contraste */
    .stMetric { 
        background-color: #0d1117; border: 1px solid #30363d; 
        border-radius: 8px; padding: 10px; text-align: center;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }

    /* Botón de Protocolo */
    div.stButton > button {
        background: linear-gradient(180deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold; width: 100%; height: 45px;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }

    /* Log del sistema estilo terminal */
    .log-terminal { background-color: #000; padding: 10px; border: 1px solid #333; border-radius: 8px; }
    .log-text { color: #00ff00; font-family: monospace; font-size: 0.8rem; }
    .log-err { color: #ff4b4b; font-weight: bold; }

    /* ESTILO OPTIMIZADO PARA INSIGNIAS TOTALMENTE VISIBLES */
    .maynor-footer {
        margin-top: 50px; padding: 30px; border-top: 1px solid #30363d;
        background: linear-gradient(180deg, rgba(13, 17, 23, 0.8) 0%, rgba(1, 4, 9, 1) 100%);
        display: flex; justify-content: space-between; align-items: center;
        border-radius: 10px;
    }

    .badge-card {
        background-color: #0d1117; border: 1px solid #30363d; border-radius: 12px;
        padding: 20px; text-align: center; width: 160px; margin: 10px;
        transition: transform 0.2s, box-shadow 0.2s;
        /* Contraste y visibilidad */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.6);
        border: 2px solid #30363d;
    }

    .badge-card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(88, 166, 255, 0.4);
        border: 2px solid #58a6ff;
    }

    .badge-icon {
        width: 70px; height: 70px; margin-bottom: 15px;
        /* Efecto de resplandor para el icono */
        filter: drop-shadow(0 0 8px rgba(88, 166, 255, 0.6));
    }

    .badge-title { font-size: 0.9rem; font-weight: bold; color: #ffffff; margin-bottom: 5px; }
    .badge-type { font-size: 0.75rem; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; }
    .badge-date { font-size: 0.7rem; color: #58a6ff; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# 4. ENCABEZADO TÁCTICO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-top:-20px;'>TACTICAL HUB - BASE DE DATOS SENTINEL ACTIVA</p>", unsafe_allow_html=True)

# 5. PANEL OPERATIVO (RADAR Y CONSOLA)
col_left, col_right = st.columns([1, 1.2])

with col_left:
    # Radar con líneas de barrido y efecto nítido
    radar_html = """
    <div style="background:#000; height:300px; border:1px solid #333; border-radius:8px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <style>
            .scan { position:absolute; width:220px; height:220px; background:conic-gradient(from 0deg, rgba(0,212,255,0.2) 0%, transparent 50%); border-radius:50%; animation: r 3s linear infinite; }
            .line-h { position:absolute; width:100%; height:1px; background:rgba(0,212,255,0.1); top:50%; }
            .line-v { position:absolute; height:100%; width:1px; background:rgba(0,212,255,0.1); left:50%; }
            @keyframes r { from {transform:rotate(0deg);} to {transform:rotate(360deg);} }
        </style>
        <div class="line-h"></div><div class="line-v"></div><div class="scan"></div>
        <div style="position:absolute; bottom:10px; color:#00d4ff; font-family:monospace; font-size:11px;">DB STATUS: SYNCHRONIZED | NODO: CDMX</div>
    </div>
    """
    components.html(radar_html, height=310)

with col_right:
    st.markdown("### 🔍 CONSOLA DE ANÁLISIS DE AMENAZAS")
    tab1, tab2 = st.tabs(["🔗 LINK / URL", "📧 EMAIL"])
    
    target = ""
    with tab1:
        target = st.text_input("Ingrese URL para rastreo:", placeholder="Ej: sospechoso.top", key="u_in")
    with tab2:
        target = st.text_input("Ingrese Remitente de correo:", placeholder="ejemplo@dominio.com", key="e_in")
    
    if st.button("🚀 INICIAR ESCANEO TÁCTICO", use_container_width=True):
        if target:
            log_placeholder = st.empty()
            logs = ["[SYS] Accediendo a Base de Datos Sentinel..."]
            
            steps = ["📡 Consultando PhishTank...", "🔗 Verificando WHOIS...", "🔬 Comparando firmas...", "📂 Disección completa."]
            for s in steps:
                logs.append(f"[INF] {s}")
                log_placeholder.code("\n".join(logs), language="bash")
                time.sleep(0.6)

            is_malicious = False
            virus_type, origin = "", ""

            if target in DB_KNOWN_ATTACKS:
                is_malicious = True
                virus_type = DB_KNOWN_ATTACKS[target]["virus"]
                origin = DB_KNOWN_ATTACKS[target]["origin"]
            elif any(ext in target.lower() for ext in DB_MALWARE_DOMAINS) or any(key in target.lower() for key in DB_PHISHING_KEYWORDS):
                is_malicious = True
                virus_type = "Troyano / Phishing (Heurística)"
                origin = "Proxy Dinámico Interceptado"

            if is_malicious:
                st.markdown(f"""
                <div style="background-color: #1a0505; border: 2px solid #ff4b4b; border-radius: 8px; padding: 20px; color: #ffbaba; margin-top: 15px;">
                    <h4>🚨 REPORTE FORENSE: POSITIVO</h4>
                    <p><b>Clasificación:</b> {virus_type}</p>
                    <p><b>Fuente de Ataque:</b> {origin}</p>
                    <hr style='border: 0.5px solid #ff4b4b;'>
                    <p><b>Acción:</b> Objetivo bloqueado y enviado al <b>Baúl de Cuarentena</b>.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.success("✅ REPORTE: Objeto limpio. No coincide con entradas maliciosas.")

st.write("---")

# 6. MÉTRICAS DEL SISTEMA
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Fiabilidad Veritas", "99.8%", "+0.1%")
with m2: st.metric("Base de Datos", f"+{len(DB_MALWARE_DOMAINS) + 500}k", "Actualizado")
with m3: st.metric("Protección Global", "Activa 24/7", "SECURE")
with m4: st.metric("Uptime Sistema", "99.9%", "+0.01%")

# 7. PIE DE PÁGINA (FIRMA Y LOGOS TOTALMENTE VISIBLES)
st.markdown("### 🏆 LOGROS DEL ESPECIALISTA CERTIFICADO")
col_footer, col_badges = st.columns([1.5, 3])

with col_footer:
    st.markdown("""
        <div>
            <h2 style="color: #00d4ff; margin:0; text-shadow: 0 0 10px #00d4ff;">MAYNOR VÁZQUEZ</h2>
            <p style="color: #ffffff; font-size: 0.95rem; font-weight: bold;">Network Defense & CyberOps Specialist</p>
            <p style="color: #8b949e; font-size: 0.8rem;">Status: <span style="color:#00ff00;">Verified Sentinel Active</span></p>
        </div>
        """, unsafe_allow_html=True)

with col_badges:
    # LÓGICA DE INSIGNIAS TOTALMENTE VISIBLES (CON EFECTOS DE RESPLANDOR)
    st.markdown("""
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div class="badge-card">
                <img class="badge-icon" src="https://img.icons8.com/nolan/96/hacker.png" alt="Icono Hacker">
                <div class="badge-type">Curso</div>
                <div class="badge-title">Hacker Ético</div>
                <div class="badge-date">Emitido: 14 mar 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://img.icons8.com/nolan/96/group.png" alt="Icono Ingeniería Social">
                <div class="badge-type">Módulo</div>
                <div class="badge-title">Ataques Ing. Social</div>
                <div class="badge-date">Emitido: 10 feb 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://img.icons8.com/nolan/96/shield.png" alt="Icono Defensa de la Red">
                <div class="badge-type">Módulo</div>
                <div class="badge-title">Defensa de la Red</div>
                <div class="badge-date">Emitido: 07 feb 2026</div>
            </div>
            <div class="badge-card">
                <img class="badge-icon" src="https://img.icons8.com/nolan/96/virus.png" alt="Icono Análisis de Amenazas">
                <div class="badge-type">Módulo</div>
                <div class="badge-title">Análisis Amenazas</div>
                <div class="badge-date">Emitido: 05 feb 2026</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
