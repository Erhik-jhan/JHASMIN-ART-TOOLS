from pathlib import Path
import json



class ThemeManager:


    def __init__(self):

        self.themes = {}

        self.current_theme = None

        self.last_operation = None



    # ==========================================================
    # REGISTRAR TEMA
    # ==========================================================

    def register_theme(
        self,
        name,
        data
    ):

        self.themes[name] = data


        self.last_operation = (
            "register_theme"
        )


        return data



    # ==========================================================
    # CREAR TEMA OSCURO JHASMIN
    # ==========================================================

    def create_jhasmin_theme(
        self
    ):

        theme = {


            "name":

            "JHASMIN Dark",


            "window":

            {

                "background":

                "#121212",


                "text":

                "#ffffff"

            },


            "panel":

            {

                "background":

                "#1e1e1e",


                "border":

                "#444444"

            },


            "accent":

            {

                "primary":

                "#8a5cff",


                "secondary":

                "#00d4ff"

            },


            "image":

            {

                "background":

                "#0f0f0f"

            }


        }



        self.register_theme(

            "jhasmin_dark",

            theme

        )


        return theme



    # ==========================================================
    # CAMBIAR TEMA
    # ==========================================================

    def set_theme(
        self,
        name
    ):

        if name not in self.themes:

            return False



        self.current_theme = name


        self.last_operation = (
            "set_theme"
        )


        return True



    # ==========================================================
    # OBTENER TEMA ACTUAL
    # ==========================================================

    def get_current(
        self
    ):

        if self.current_theme is None:

            return None



        return self.themes.get(

            self.current_theme

        )



    # ==========================================================
    # EXPORTAR TEMA
    # ==========================================================

    def export_theme(
        self,
        name,
        output_path
    ):

        if name not in self.themes:

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

                self.themes[name],

                file,

                indent=4

            )


        return str(
            path
        )



    # ==========================================================
    # CARGAR TEMA
    # ==========================================================

    def load_theme(
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


            theme = json.load(
                file
            )


        self.register_theme(

            theme["name"],

            theme

        )


        return theme



    # ==========================================================
    # LISTAR TEMAS
    # ==========================================================

    def list_themes(
        self
    ):

        return list(

            self.themes.keys()

        )



    def get_last_operation(
        self
    ):

        return self.last_operation