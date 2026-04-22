import pandas as pd
from curl_cffi import requests

BASE = "https://resultadoelectoral.onpe.gob.pe/presentacion-backend"
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.8",
    "referer": "https://resultadoelectoral.onpe.gob.pe/main/resumen",
}

def get(ruta):
    r = requests.get(BASE + ruta, headers=HEADERS, impersonate="chrome", timeout=10)
    return r.json()["data"]

# ── PASO 1: Extracción ──────────────────────────────────────────────
print("📡 Extrayendo datos de la ONPE...")
raw = get("/resumen-general/participantes?idEleccion=10&tipoFiltro=eleccion")
print(f"✅ {len(raw)} registros obtenidos\n")

# ── PASO 2: Transformación ──────────────────────────────────────────
print("🔄 Transformando datos...")
df = pd.DataFrame(raw)

df = df.rename(columns={
    "nombreCandidato": "candidato",
    "nombreAgrupacionPolitica": "partido",
    "totalVotosValidos": "votos",
    "porcentajeVotosValidos": "pct_validos",
})

df = df.sort_values("votos", ascending=False).reset_index(drop=True)
df.index = df.index + 1

# ── PASO 3: Resultado ───────────────────────────────────────────────
print("📊 Resultados electorales ONPE:\n")
print(df[["candidato", "partido", "votos", "pct_validos"]].to_string())
