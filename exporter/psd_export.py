from pathlib import Path

from PIL import Image



class PSDExporter:


    def __init__(self):

        self.last_export = None



    # ==========================================================
    # EXPORTACIÓN PRINCIPAL PSD
    # ==========================================================

    def export(
        self,
        layers,
        output_path
    ):

        path = Path(
            output_path
        )


        if path.suffix != ".psd":

            path = path.with_suffix(
                ".psd"
            )


        images = []


        for name, image in layers.items():

            if image.mode != "RGBA":

                image = image.convert(
                    "RGBA"
                )


            images.append(
                image
            )



        if not images:

            return None



        base = images[0]


        if len(images) > 1:

            base = self.merge_layers(
                images
            )


        base.save(
            path
        )


        self.last_export = str(
            path
        )


        return str(
            path
        )



    # ==========================================================
    # COMBINAR CAPAS
    # ==========================================================

    def merge_layers(
        self,
        layers
    ):

        width = max(

            layer.width

            for layer in layers

        )


        height = max(

            layer.height

            for layer in layers

        )


        result = Image.new(

            "RGBA",

            (
                width,
                height
            ),

            (
                0,
                0,
                0,
                0
            )

        )


        for layer in layers:

            result.alpha_composite(
                layer
            )


        return result



    # ==========================================================
    # EXPORTAR CAPAS INDIVIDUALES
    # ==========================================================

    def export_layers(
        self,
        layers,
        folder
    ):

        output = Path(
            folder
        )


        output.mkdir(

            parents=True,

            exist_ok=True

        )


        exported = []



        for name, image in layers.items():


            file_path = output / (

                f"{name}.png"

            )


            image.save(

                file_path,

                "PNG"

            )


            exported.append(

                str(file_path)

            )



        self.last_export = exported


        return exported



    # ==========================================================
    # PREPARAR CAPAS PARA EDICIÓN
    # ==========================================================

    def prepare_layers(
        self,
        layers
    ):

        prepared = {}


        for name, image in layers.items():

            if image.mode != "RGBA":

                image = image.convert(
                    "RGBA"
                )


            prepared[name] = image



        return prepared



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_last_export(
        self
    ):

        return self.last_export
        