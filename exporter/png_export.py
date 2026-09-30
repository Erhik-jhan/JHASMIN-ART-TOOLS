from pathlib import Path

from PIL import Image



class PNGExporter:


    def __init__(self):

        self.last_export = None



    # ==========================================================
    # EXPORTACIÓN PRINCIPAL
    # ==========================================================

    def export(
        self,
        image,
        output_path
    ):

        path = Path(
            output_path
        )


        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        image.save(
            path,
            "PNG"
        )


        self.last_export = str(
            path
        )


        return str(
            path
        )



    # ==========================================================
    # EXPORTAR CAPA INDIVIDUAL
    # ==========================================================

    def export_layer(
        self,
        layer,
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


        file_path = folder / (
            f"{name}.png"
        )


        layer.save(
            file_path,
            "PNG"
        )


        self.last_export = str(
            file_path
        )


        return str(
            file_path
        )



    # ==========================================================
    # EXPORTAR MÚLTIPLES CAPAS
    # ==========================================================

    def export_layers(
        self,
        layers,
        output_folder
    ):

        results = []


        for name, image in layers.items():

            result = self.export_layer(

                image,

                name,

                output_folder

            )


            results.append(
                result
            )


        self.last_export = results


        return results



    # ==========================================================
    # EXPORTAR CON TRANSPARENCIA
    # ==========================================================

    def export_transparent(
        self,
        image,
        output_path
    ):

        if image.mode != "RGBA":

            image = image.convert(
                "RGBA"
            )


        return self.export(
            image,
            output_path
        )



    # ==========================================================
    # EXPORTAR SPRITE SIMPLE
    # ==========================================================

    def export_sprite(
        self,
        frames,
        output_path
    ):

        if not frames:

            return None



        width = max(
            frame.width
            for frame in frames
        )


        height = max(
            frame.height
            for frame in frames
        )


        sprite = Image.new(

            "RGBA",

            (
                width * len(frames),

                height

            ),

            (
                0,
                0,
                0,
                0
            )

        )


        for index, frame in enumerate(frames):

            sprite.paste(

                frame,

                (
                    index * width,

                    0

                ),

                frame

            )



        return self.export(
            sprite,
            output_path
        )



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_last_export(
        self
    ):

        return self.last_export