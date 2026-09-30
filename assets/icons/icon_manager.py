from pathlib import Path



class IconManager:


    def __init__(self):

        self.icons = {}

        self.icon_folder = None

        self.last_operation = None



    # ==========================================================
    # CONFIGURAR CARPETA DE ICONOS
    # ==========================================================

    def set_folder(
        self,
        folder
    ):

        self.icon_folder = Path(
            folder
        )


        self.last_operation = (
            "set_folder"
        )


        return self.icon_folder



    # ==========================================================
    # REGISTRAR ICONO
    # ==========================================================

    def register_icon(
        self,
        name,
        path
    ):

        self.icons[name] = str(
            path
        )


        self.last_operation = (
            "register_icon"
        )


        return self.icons[name]



    # ==========================================================
    # ICONOS BASE JHASMIN
    # ==========================================================

    def create_default_icons(
        self
    ):

        icons = {


            "open":

            "open.png",


            "save":

            "save.png",


            "export":

            "export.png",


            "undo":

            "undo.png",


            "redo":

            "redo.png",


            "ai":

            "ai.png",


            "layers":

            "layers.png",


            "settings":

            "settings.png"

        }



        for name, file in icons.items():

            self.register_icon(

                name,

                file

            )



        return self.icons



    # ==========================================================
    # OBTENER ICONO
    # ==========================================================

    def get_icon(
        self,
        name
    ):

        return self.icons.get(
            name
        )



    # ==========================================================
    # VERIFICAR EXISTENCIA
    # ==========================================================

    def exists(
        self,
        name
    ):

        if name not in self.icons:

            return False



        return Path(

            self.icons[name]

        ).exists()



    # ==========================================================
    # LISTAR ICONOS
    # ==========================================================

    def list_icons(
        self
    ):

        return list(

            self.icons.keys()

        )



    # ==========================================================
    # EXPORTAR INFORMACIÓN
    # ==========================================================

    def export_data(
        self
    ):

        return {


            "folder":

            str(self.icon_folder)
            if self.icon_folder
            else "",


            "icons":

            self.icons

        }



    def get_last_operation(
        self
    ):

        return self.last_operation