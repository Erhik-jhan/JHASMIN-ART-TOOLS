from pathlib import Path

from models.model_config import ModelConfig



class ModelManager:


    def __init__(self):

        self.models = {}

        self.loaded_models = {}

        self.last_operation = None



    # ==========================================================
    # REGISTRAR MODELO
    # ==========================================================

    def register_model(
        self,
        config
    ):

        if not isinstance(
            config,
            ModelConfig
        ):

            return False



        self.models[config.name] = config


        self.last_operation = (
            "register_model"
        )


        return True



    # ==========================================================
    # CREAR MODELO DESDE DATOS
    # ==========================================================

    def create_model(
        self,
        name,
        model_type,
        path=""
    ):

        config = ModelConfig(

            name=name,

            model_type=model_type,

            path=path

        )


        self.register_model(
            config
        )


        return config



    # ==========================================================
    # CARGAR MODELO
    # ==========================================================

    def load_model(
        self,
        name
    ):

        if name not in self.models:

            return None



        config = self.models[name]


        model = {

            "name": config.name,

            "type": config.model_type,

            "path": config.path,

            "status": "loaded"

        }



        self.loaded_models[name] = model


        self.last_operation = (
            "load_model"
        )


        return model



    # ==========================================================
    # DESCARGAR MODELO
    # ==========================================================

    def unload_model(
        self,
        name
    ):

        if name in self.loaded_models:

            del self.loaded_models[name]


            self.last_operation = (
                "unload_model"
            )


            return True



        return False



    # ==========================================================
    # CARGAR MODELOS BASE JHASMIN
    # ==========================================================

    def load_default_models(
        self
    ):

        defaults = [

            (
                "SAM",
                "segmentation"
            ),

            (
                "Vision",
                "image_analysis"
            ),

            (
                "Inpainting",
                "image_repair"
            )

        ]


        for name, model_type in defaults:


            self.create_model(

                name,

                model_type

            )



        return self.models



    # ==========================================================
    # BUSCAR MODELO
    # ==========================================================

    def get_model(
        self,
        name
    ):

        return self.models.get(
            name
        )



    # ==========================================================
    # MODELOS CARGADOS
    # ==========================================================

    def get_loaded(
        self
    ):

        return self.loaded_models



    # ==========================================================
    # VERIFICAR ARCHIVO
    # ==========================================================

    def validate_path(
        self,
        name
    ):

        if name not in self.models:

            return False



        path = Path(

            self.models[name].path

        )


        return path.exists()



    # ==========================================================
    # EXPORTAR DATOS
    # ==========================================================

    def export_data(
        self
    ):

        data = {}


        for name, model in self.models.items():

            data[name] = {

                "type": model.model_type,

                "path": model.path,

                "version": model.version,

                "device": model.device,

                "enabled": model.enabled

            }


        return data



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_last_operation(
        self
    ):

        return self.last_operation