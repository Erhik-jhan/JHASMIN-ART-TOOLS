from pathlib import Path
import urllib.request
import json



class ModelDownloader:


    def __init__(self):

        self.downloads = {}

        self.last_operation = None



    # ==========================================================
    # REGISTRAR DESCARGA
    # ==========================================================

    def register(
        self,
        name,
        url,
        destination
    ):

        self.downloads[name] = {

            "url": url,

            "destination": destination,

            "status": "pending",

            "progress": 0

        }


        self.last_operation = (
            "register"
        )


        return self.downloads[name]



    # ==========================================================
    # DESCARGAR MODELO
    # ==========================================================

    def download(
        self,
        name
    ):

        if name not in self.downloads:

            return False



        data = self.downloads[name]


        url = data["url"]

        destination = Path(

            data["destination"]

        )


        destination.parent.mkdir(

            parents=True,

            exist_ok=True

        )


        try:

            urllib.request.urlretrieve(

                url,

                destination

            )


            data["status"] = (
                "completed"
            )


            data["progress"] = 100



            self.last_operation = (
                "download"
            )


            return True



        except Exception as error:


            data["status"] = (
                "error"
            )


            data["error"] = str(
                error
            )


            return False



    # ==========================================================
    # PREPARAR MODELO LOCAL
    # ==========================================================

    def prepare_local_model(
        self,
        name,
        path
    ):

        self.downloads[name] = {

            "url": "",

            "destination": path,

            "status": "local",

            "progress": 100

        }


        return self.downloads[name]



    # ==========================================================
    # VERIFICAR MODELO
    # ==========================================================

    def exists(
        self,
        name
    ):

        if name not in self.downloads:

            return False



        path = Path(

            self.downloads[name]["destination"]

        )


        return path.exists()



    # ==========================================================
    # EXPORTAR INFORMACIÓN
    # ==========================================================

    def export_data(
        self
    ):

        return self.downloads



    # ==========================================================
    # GUARDAR CONFIGURACIÓN
    # ==========================================================

    def save_config(
        self,
        file_path
    ):

        path = Path(
            file_path
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

                self.downloads,

                file,

                indent=4

            )


        return str(
            path
        )



    # ==========================================================
    # CARGAR CONFIGURACIÓN
    # ==========================================================

    def load_config(
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


            self.downloads = json.load(
                file
            )



        return True



    # ==========================================================
    # ESTADO
    # ==========================================================

    def get_status(
        self,
        name
    ):

        return self.downloads.get(
            name
        )



    def get_last_operation(
        self
    ):

        return self.last_operation