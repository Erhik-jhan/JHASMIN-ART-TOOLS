from pathlib import Path



# ==========================================================
# INFORMACIÓN DE APLICACIÓN
# ==========================================================

APP_NAME = "JHASMIN Art Tools"

APP_VERSION = "0.1"

APP_AUTHOR = "JHENT TECH"

APP_DESCRIPTION = (
    "Editor visual de imágenes preparado "
    "para herramientas de inteligencia artificial."
)



# ==========================================================
# DIRECTORIO BASE
# ==========================================================

BASE_DIR = Path(
    __file__
).resolve().parent



# ==========================================================
# ESTRUCTURA DEL PROYECTO
# ==========================================================

UI_DIR = BASE_DIR / "ui"

IMAGE_DIR = BASE_DIR / "image"

SEGMENTATION_DIR = BASE_DIR / "segmentation"

ANIMATION_DIR = BASE_DIR / "animation"

EXPORTER_DIR = BASE_DIR / "exporter"

MODELS_DIR = BASE_DIR / "models"

ASSETS_DIR = BASE_DIR / "assets"

CACHE_DIR = BASE_DIR / "cache"

LOG_DIR = BASE_DIR / "logs"


OUTPUT_DIR = BASE_DIR / "output"

TEMP_DIR = BASE_DIR / "temp"



# ==========================================================
# CREACIÓN DE CARPETAS
# ==========================================================

DIRECTORIES = [

    OUTPUT_DIR,

    TEMP_DIR,

    MODELS_DIR,

    ASSETS_DIR,

    CACHE_DIR,

    LOG_DIR

]



def create_directories():

    for directory in DIRECTORIES:

        directory.mkdir(

            parents=True,

            exist_ok=True

        )



# ==========================================================
# IMÁGENES
# ==========================================================

IMAGE_SUPPORTED_FORMATS = [

    ".png",

    ".jpg",

    ".jpeg",

    ".webp",

    ".bmp",

    ".tiff"

]


DEFAULT_IMAGE_SIZE = (

    1920,

    1080

)


MAX_IMAGE_SIZE = (

    8192,

    8192

)



IMAGE_CONFIG = {


    "default_mode":

    "RGBA",


    "keep_metadata":

    True,


    "smooth_resize":

    True


}



# ==========================================================
# CONFIGURACIÓN IA
# ==========================================================

AI_CONFIG = {


    "device":

    "cpu",


    "precision":

    "float32",


    "auto_load_models":

    False,


    "models_directory":

    str(MODELS_DIR),


    "enable_cache":

    True


}



# ==========================================================
# MODELOS IA DISPONIBLES
# ==========================================================

MODEL_CONFIG = {


    "segmentation":

    {

        "enabled":

        True,

        "model":

        "SAM"

    },


    "inpainting":

    {

        "enabled":

        True,

        "model":

        "future"

    },


    "upscale":

    {

        "enabled":

        True,

        "model":

        "future"

    }


}



# ==========================================================
# PROCESAMIENTO
# ==========================================================

PROCESSING_CONFIG = {


    "default_upscale":

    2,


    "default_blur":

    2,


    "default_mask_blur":

    2,


    "enable_history":

    True,


    "history_limit":

    50


}



# ==========================================================
# ANIMACIÓN
# ==========================================================

ANIMATION_CONFIG = {


    "fps":

    24,


    "enable_physics":

    True,


    "enable_rig":

    True,


    "enable_layers":

    True


}



# ==========================================================
# EXPORTACIÓN
# ==========================================================

EXPORT_CONFIG = {


    "default_format":

    "png",


    "include_metadata":

    True,


    "include_layers":

    True,


    "quality":

    100


}



# ==========================================================
# INTERFAZ
# ==========================================================

WINDOW_WIDTH = 1400

WINDOW_HEIGHT = 900



THEME_CONFIG = {


    "default":

    "jhasmin_dark",


    "accent":

    "#7b61ff"


}



# ==========================================================
# DEPURACIÓN
# ==========================================================

DEBUG_CONFIG = {


    "enabled":

    True,


    "save_temp_files":

    False


}



# ==========================================================
# INFORMACIÓN GLOBAL
# ==========================================================

def get_app_info():


    return {


        "name":

        APP_NAME,


        "version":

        APP_VERSION,


        "author":

        APP_AUTHOR,


        "description":

        APP_DESCRIPTION


    }



def get_paths():


    return {


        "base":

        str(BASE_DIR),


        "output":

        str(OUTPUT_DIR),


        "temp":

        str(TEMP_DIR),


        "models":

        str(MODELS_DIR),


        "cache":

        str(CACHE_DIR)


    }



# ==========================================================
# INICIALIZACIÓN
# ==========================================================

create_directories()