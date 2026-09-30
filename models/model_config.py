from dataclasses import dataclass



@dataclass
class ModelConfig:


    name: str

    path: str = ""

    model_type: str = ""

    version: str = "1.0"

    device: str = "cpu"

    enabled: bool = True

    description: str = ""



class ModelConfigurations:


    def __init__(self):

        self.models = {}



    # ==========================================================
    # REGISTRAR MODELO
    # ==========================================================

    def register(
        self,
        config
    ):

        self.models[config.name] = config


        return config



    # ==========================================================
    # MODELOS BASE JHASMIN
    # ==========================================================

    def create_default_models(
        self
    ):


        self.register(

            ModelConfig(

                name="SAM",

                model_type="segmentation",

                version="1",

                description=
                "Segmentación de imágenes por IA"

            )

        )


        self.register(

            ModelConfig(

                name="Vision",

                model_type="image_analysis",

                version="1",

                description=
                "Análisis visual del personaje"

            )

        )


        self.register(

            ModelConfig(

                name="Inpainting",

                model_type="image_repair",

                version="1",

                description=
                "Reconstrucción de partes dañadas"

            )

        )


        return self.models



    # ==========================================================
    # OBTENER MODELO
    # ==========================================================

    def get(
        self,
        name
    ):

        return self.models.get(
            name
        )



    # ==========================================================
    # ACTUALIZAR RUTA
    # ==========================================================

    def set_path(
        self,
        name,
        path
    ):

        if name in self.models:

            self.models[name].path = path



    # ==========================================================
    # ACTIVAR / DESACTIVAR
    # ==========================================================

    def enable(
        self,
        name,
        state=True
    ):

        if name in self.models:

            self.models[name].enabled = state



    # ==========================================================
    # EXPORTAR CONFIGURACIÓN
    # ==========================================================

    def export_data(
        self
    ):

        data = {}


        for name, model in self.models.items():

            data[name] = {

                "path": model.path,

                "type": model.model_type,

                "version": model.version,

                "device": model.device,

                "enabled": model.enabled,

                "description": model.description

            }


        return data 