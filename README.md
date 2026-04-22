# 🗳️ Pipeline ONPE - Resultados Electorales

Extrae y transforma los resultados electorales de la ONPE en tiempo real.

## 🚀 Correr con Docker

```bash
# 1. Construir la imagen
docker build -t onpe-pipeline .

# 2. Correr el container
docker run onpe-pipeline
```

## 📁 Estructura

```
onpe-pipeline/
├── Dockerfile        # Receta para crear la imagen
├── requirements.txt  # Dependencias Python
├── main.py           # Pipeline completo (extracción + transformación)
└── README.md
```

## 🔧 Correr localmente (sin Docker)

```bash
pip install -r requirements.txt
python main.py
```
