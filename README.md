# JHASMIN Art Tools

## Información

JHASMIN Art Tools es una aplicación de edición y preparación de personajes
con asistencia de inteligencia artificial.

Proyecto desarrollado como parte del ecosistema JHENT TECH.


---

# Versión actual
---

*01*

# Objetivo

Crear una herramienta capaz de:

- Editar imágenes.
- Separar personajes por capas.
- Preparar personajes para animación.
- Generar estructuras de rig.
- Administrar modelos IA.
- Exportar proyectos compatibles.


---

# Estructura del proyecto
---

JHASMIN-ART-TOOLS/

│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── ui/
│
├── segmentation/
│
├── image/
│
├── animation/
│
├── exporter/
│
├── models/
│
├── assets/
│
├── output/
│
├── temp/
│
└── tests/

# Módulos


## UI

Sistema visual construido con:

- PySide6
- Ventanas
- Paneles
- Herramientas
- Vista de imagen


---

## Imagen

Funciones:

- Limpieza.
- Escalado.
- Corrección.
- Inpainting.
- Color.


---

## Segmentación IA

Preparado para:

- SAM.
- Detectores.
- Generación de máscaras.


---

## Animación

Sistema preparado para:

- Esqueleto.
- Pivotes.
- Rig.
- Capas.
- Física.


---

## Exportadores

Formatos:

- PNG.
- KRA.
- PSD.
- JSON.
- Sprite.


---

## Modelos IA

Gestión:

- Registro.
- Carga.
- Configuración.
- Descarga.


---

# Instalación


Crear entorno virtual:


```bash
python3 -m venv .venv
source .env/bin/activate
```
---

# Instalar Dependencias

```bash 
pip install-r requeriments.txt
```
---

# Ejecutar

```bash 
python3 app.py
```

---

# Desarrollo

Reglas del proyecto:

- Mantener módulos separados.
- No mezclar responsabilidades.
- Crear código escalable.
- Documentar cambios.
- Mantener compatibilidad futura con IA.

---

# Estado 

Actualmente:

UI              Preparado
Imagen          Preparado
Animación       Preparado
Exportación     Preparado
Modelos IA      Preparado

---

# Proximas Funciones 

- Integración SAM.
- Sistema de capas real.
- Editor visual avanzado.
- Animación de personajes.
- Motor IA JHASMIN.


Estado actual:

```text
JHASMIN-ART-TOOLS/

├── app.py             Proceso
├── config.py          Hecho
├── requirements.txt   Proceso
├── README.md          Hecho

```

# Siguiente Archivo

requirements.txt

Aqui definiremos todas las dependencias reales para que la aplicación puede ejecutarce.

