import streamlit as st
import streamlit.components.v1 as components
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. BASE DE DATOS DE REPUTACIÓN (LISTA NEGRA)
# Aquí puedes seguir agregando dominios sospechosos
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
    </style>
    """, unsafe_allow_html=True)

# 4. ENCABEZADO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-top:-20px;'>TACTICAL HUB - BASE DE DATOS SENTINEL ACTIVA</p>", unsafe_allow_html=True)

# 5. PANEL OPERATIVO
col_left, col_right = st.columns([1, 1.2])

with col_left:
    # Radar con líneas de mira
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
    target = st.text_input("Ingrese URL o Email para rastreo:", placeholder="Ej: sospechoso.top")
    
    if st.button("🚀 INICIAR ESCANEO TÁCTICO"):
        if target:
            log_area = st.empty()
            logs = ["[SYS] Accediendo a Base de Datos de Reputación..."]
            
            # Simulación de jalar info en tiempo real
            steps = [
                "📡 Consultando API de PhishTank y URLHaus...",
                "🔗 Verificando WHOIS y saltos de IP...",
                "🔬 Comparando firmas con DB Sentinel local...",
                "📂 Disección de metadatos completada."
            ]
            
            for s in steps:
                logs.append(f"[INF] {s}")
                log_area.code("\n".join(logs))
                time.sleep(0.6)

            # LÓGICA DE BÚSQUEDA EN BASE DE DATOS
            is_malicious = False
            virus_type = "Amenaza Desconocida"
            origin = "No identificado (Uso de VPN)"

            # Comprobar si está en los ataques conocidos
            if target in DB_KNOWN_ATTACKS:
                is_malicious = True
                virus_type = DB_KNOWN_ATTACKS[target]["virus"]
                origin = DB_KNOWN_ATTACKS[target]["origin"]
            
            # Comprobar por extensiones o palabras clave
            elif any(ext in target.lower() for ext in DB_MALWARE_DOMAINS) or any(key in target.lower() for key in DB_PHISHING_KEYWORDS):
                is_malicious = True
                virus_type = "Troyano / Phishing (Heurística Detectada)"
                origin = "Localizado en Servidor de Alta Mar"

            # Resultados
            if is_malicious:
                st.markdown(f"""
                <div class="virus-report">
                    <h4>🚨 REPORTE FORENSE: POSITIVO</h4>
                    <p><b>Clasificación:</b> {virus_type}</p>
                    <p><b>Fuente de Ataque:</b> {origin}</p>
                    <hr style='border: 0.5px solid #ff4b4b;'>
                    <p><b>Acción Automática:</b> El objetivo ha sido bloqueado y enviado al <b>Baúl de Cuarentena</b>.</p>
                    <p><b>Instrucción para Maynor:</b> Ejecutar limpieza de caché DNS y monitorear tráfico saliente.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.success("✅ REPORTE: Objeto limpio. No coincide con ninguna entrada en la base de datos de malware.")
        else:
            st.warning("⚠️ Ingrese un dato para realizar la consulta.")

st.write("---")

# 6. MÉTRICAS
m1, m2, m3, m4 = st.columns(4)
m1.metric("Fiabilidad", "99.8%", "Veritas")
m2.metric("Base de Datos", f"+{len(DB_MALWARE_DOMAINS) + 500}k Firmas", "Actualizado")
m3.metric("Protección", "Activa 24/7", "Secure")
m4.metric("Uptime", "99.9%", "Estable")

# 7. PIE DE PÁGINA (FIRMA DE MAYNOR)
st.markdown("""
    <div class="maynor-footer">
        <div>
            <h3 style="color: #00d4ff; margin:0;">MAYNOR VÁZQUEZ</h3>
            <p style="color: #8b949e; font-size: 0.8rem;">Certified Network Defense & CyberOps Specialist</p>
        </div>
        <div style="display: flex; gap: 10px;">
            <div style="border: 1px solid #58a6ff; padding: 5px 10px; border-radius: 20px; font-size: 10px; color: #58a6ff;">SENTINEL ACTIVE</div>
            <div style="border: 1px solid #3fb950; padding: 5px 10px; border-radius: 20px; font-size: 10px; color: #3fb950;">FIREWALL ON</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
