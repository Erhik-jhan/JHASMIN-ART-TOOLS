from pathlib import Path
import json



class TemplateManager:


    def __init__(self):

        self.templates = {}

        self.last_operation = None



    # ==========================================================
    # REGISTRAR PLANTILLA
    # ==========================================================

    def register_template(
        self,
        name,
        data
    ):

        self.templates[name] = data


        self.last_operation = (
            "register_template"
        )


        return data



    # ==========================================================
    # PLANTILLA PERSONAJE BASE
    # ==========================================================

    def create_character_template(
        self
    ):

        template = {


            "type":

            "character",


            "name":

            "JHASMIN Character",


            "layers":

            [

                "body",

                "head",

                "hair",

                "eyes",

                "wings",

                "clothes",

                "accessories"

            ],


            "animation":

            {

                "rig":

                True,


                "physics":

                True,


                "skeleton":

                True

            }


        }



        self.register_template(

            "character",

            template

        )


        return template



    # ==========================================================
    # PLANTILLA ESCENA
    # ==========================================================

    def create_scene_template(
        self
    ):

        template = {


            "type":

            "scene",


            "name":

            "JHASMIN Scene",


            "objects":

            [],


            "camera":

            {

                "position":

                [

                    0,

                    0,

                    0

                ],

                "zoom":

                1.0

            },


            "lighting":

            {

                "enabled":

                True

            }

        }



        self.register_template(

            "scene",

            template

        )


        return template



    # ==========================================================
    # CREAR PROYECTO COMPLETO
    # ==========================================================

    def create_project_template(
        self
    ):

        project = {


            "project":

            "JHASMIN Art Tools",


            "version":

            "1.0",


            "character":

            self.create_character_template(),


            "scene":

            self.create_scene_template()

        }


        self.register_template(

            "project",

            project

        )


        return project



    # ==========================================================
    # OBTENER PLANTILLA
    # ==========================================================

    def get_template(
        self,
        name
    ):

        return self.templates.get(
            name
        )



    # ==========================================================
    # GUARDAR PLANTILLA
    # ==========================================================

    def save_template(
        self,
        name,
        output_path
    ):

        if name not in self.templates:

            return False



        path = Path(
            output_path
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

                self.templates[name],

                file,

                indent=4

            )


        return str(
            path
        )



    # ==========================================================
    # CARGAR PLANTILLA
    # ==========================================================

    def load_template(
        self,
        file_path
    ):

        path = Path(
            file_path
        )


        if not path.exists():

            return False



        with open(

            path,

            "r",

            encoding="utf-8"

        ) as file:


            data = json.load(
                file
            )


        name = data.get(

            "name",

            path.stem

        )


        self.register_template(

            name,

            data

        )


        return data



    # ==========================================================
    # LISTAR
    # ==========================================================

    def list_templates(
        self
    ):

        return list(

            self.templates.keys()

        )



    def get_last_operation(
        self
    ):

        return self.last_operation