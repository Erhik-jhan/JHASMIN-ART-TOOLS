"""
==========================================================
JHASMIN Art Tools
Core Package
==========================================================

El módulo core coordina todo el funcionamiento interno
de la aplicación.

No contiene procesamiento de imagen directamente.

Su responsabilidad es conectar:

- UI
- Image
- Segmentation
- Animation
- Exporter

mediante administradores especializados.

"""


__version__ = "0.1.0"

__author__ = "JHENT TECH"



# ==========================================================
# IMPORTACIONES PRINCIPALES
# ==========================================================

from .image_manager import ImageManager
from .layer_manager import LayerManager
from .history import HistoryManager
from .project import ProjectManager
from .pipeline import ProcessingPipeline



# ==========================================================
# EXPORTACIONES
# ==========================================================

__all__ = [

    "ImageManager",

    "LayerManager",

    "HistoryManager",

    "ProjectManager",

    "ProcessingPipeline"

]