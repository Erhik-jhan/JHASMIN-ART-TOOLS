from pathlib import Path
import zipfile
import json

from PIL import Image



class KRAExporter:


    def __init__(self):

        self.last_export = None



    # ==========================================================
    # EXPORTACIÓN PRINCIPAL KRA
    # ==========================================================

    def export(
        self,
        layers,
        output_path,
        document_name="JHASMIN"
    ):

        path = Path(
            output_path
        )


        if path.suffix != ".kra":

            path = path.with_suffix(
                ".kra"
            )


        temp_folder = path.parent / (
            f"{path.stem}_temp"
        )


        temp_folder.mkdir(
            parents=True,
            exist_ok=True
        )


        self.create_structure(
            temp_folder
        )


        self.save_layers(
            layers,
            temp_folder
        )


        self.create_metadata(
            document_name,
            temp_folder
        )


        self.compress_kra(
            temp_folder,
            path
        )


        self.last_export = str(
            path
        )


        return str(
            path
        )



    # ==========================================================
    # CREAR ESTRUCTURA KRA
    # ==========================================================

    def create_structure(
        self,
        folder
    ):

        folders = [

            "mergedimage",

            "preview",

            "layers",

            "data"

        ]


        for name in folders:

            (
                folder / name
            ).mkdir(
                exist_ok=True
            )



    # ==========================================================
    # GUARDAR CAPAS
    # ==========================================================

    def save_layers(
        self,
        layers,
        folder
    ):

        layer_folder = folder / (
            "layers"
        )


        index = 0


        for name, image in layers.items():

            file_path = layer_folder / (

                f"layer_{index}.png"

            )


            image.save(
                file_path,
                "PNG"
            )


            index += 1



    # ==========================================================
    # CREAR INFORMACIÓN
    # ==========================================================

    def create_metadata(
        self,
        name,
        folder
    ):

        metadata = {

            "application":

            "JHASMIN Art Tools",


            "document":

            name,


            "layers":

            "generated"

        }


        file_path = folder / (
            "data/metadata.json"
        )


        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(

                metadata,

                file,

                indent=4

            )



    # ==========================================================
    # COMPRIMIR COMO KRA
    # ==========================================================

    def compress_kra(
        self,
        folder,
        output
    ):

        with zipfile.ZipFile(

            output,

            "w",

            zipfile.ZIP_DEFLATED

        ) as archive:


            for file in folder.rglob("*"):

                if file.is_file():

                    archive.write(

                        file,

                        file.relative_to(
                            folder
                        )

                    )



    # ==========================================================
    # EXPORTAR UNA CAPA
    # ==========================================================

    def export_single_layer(
        self,
        image,
        name,
        output_folder
    ):

        folder = Path(
            output_folder
        )


        folder.mkdir(
            parents=True,
            exist_ok=True
        )


        path = folder / (

            f"{name}.png"

        )


        image.save(
            path,
            "PNG"
        )


        return str(
            path
        )



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_last_export(
        self
    ):

        return self.last_export