from pathlib import Path
import json



class JSONExporter:


    def __init__(self):

        self.last_export = None



    # ==========================================================
    # EXPORTACIÓN PRINCIPAL
    # ==========================================================

    def export(
        self,
        data,
        output_path
    ):

        path = Path(
            output_path
        )


        if path.suffix != ".json":

            path = path.with_suffix(
                ".json"
            )


        path.parent.mkdir(

            parents=True,

            exist_ok=True

        )


        with open(

            path,

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                data,

                file,

                indent=4,

                ensure_ascii=False

            )



        self.last_export = str(
            path
        )


        return str(
            path
        )



    # ==========================================================
    # EXPORTAR PROYECTO JHASMIN
    # ==========================================================

    def export_project(
        self,
        project_name,
        layers=None,
        skeleton=None,
        pivots=None,
        rig=None,
        physics=None,
        output_path="output/project.json"
    ):


        project = {


            "project":

            {

                "name": project_name,

                "version": "1.0"

            },


            "layers":

            layers or {},


            "skeleton":

            skeleton or {},


            "pivots":

            pivots or {},


            "rig":

            rig or {},


            "physics":

            physics or {}

        }



        return self.export(

            project,

            output_path

        )



    # ==========================================================
    # CARGAR PROYECTO
    # ==========================================================

    def load(
        self,
        file_path
    ):

        path = Path(
            file_path
        )


        if not path.exists():

            return None



        with open(

            path,

            "r",

            encoding="utf-8"

        ) as file:


            data = json.load(
                file
            )


        return data



    # ==========================================================
    # EXPORTAR CONFIGURACIÓN
    # ==========================================================

    def export_config(
        self,
        config,
        output_path
    ):

        return self.export(

            {

                "config": config

            },

            output_path

        )



    # ==========================================================
    # CONVERTIR DATOS
    # ==========================================================

    def serialize(
        self,
        object_data
    ):

        try:

            return json.dumps(

                object_data,

                indent=4

            )


        except Exception:

            return None



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_last_export(
        self
    ):

        return self.last_export