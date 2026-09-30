from pathlib import Path

from PIL import Image



class SpriteExporter:


    def __init__(self):

        self.last_export = None



    # ==========================================================
    # EXPORTACIÓN PRINCIPAL SPRITE
    # ==========================================================

    def export(
        self,
        frames,
        output_path,
        columns=1
    ):

        path = Path(
            output_path
        )


        if path.suffix != ".png":

            path = path.with_suffix(
                ".png"
            )


        if not frames:

            return None



        sprite = self.create_sheet(

            frames,

            columns

        )


        path.parent.mkdir(

            parents=True,

            exist_ok=True

        )


        sprite.save(

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
    # CREAR SPRITE SHEET
    # ==========================================================

    def create_sheet(
        self,
        frames,
        columns=1
    ):


        frame_width = max(

            frame.width

            for frame in frames

        )


        frame_height = max(

            frame.height

            for frame in frames

        )


        rows = (

            len(frames)

            + columns

            - 1

        ) // columns



        sheet = Image.new(

            "RGBA",

            (

                frame_width * columns,

                frame_height * rows

            ),

            (

                0,

                0,

                0,

                0

            )

        )



        for index, frame in enumerate(frames):


            x = (

                index % columns

            ) * frame_width



            y = (

                index // columns

            ) * frame_height



            sheet.alpha_composite(

                frame,

                (

                    x,

                    y

                )

            )



        return sheet



    # ==========================================================
    # EXPORTAR FRAMES INDIVIDUALES
    # ==========================================================

    def export_frames(
        self,
        frames,
        folder
    ):

        directory = Path(
            folder
        )


        directory.mkdir(

            parents=True,

            exist_ok=True

        )


        files = []


        for index, frame in enumerate(frames):


            file_path = directory / (

                f"frame_{index:04d}.png"

            )


            frame.save(

                file_path,

                "PNG"

            )


            files.append(

                str(file_path)

            )



        self.last_export = files


        return files



    # ==========================================================
    # CREAR ANIMACIÓN SIMPLE
    # ==========================================================

    def create_animation_data(
        self,
        frames,
        fps=24
    ):

        animation = {


            "frames":

            len(frames),


            "fps":

            fps,


            "duration":

            len(frames) / fps

        }


        return animation



    # ==========================================================
    # EXPORTAR DATOS ANIMACIÓN
    # ==========================================================

    def export_animation(
        self,
        frames,
        output_folder,
        fps=24
    ):


        data = {


            "frames":

            self.export_frames(

                frames,

                output_folder

            ),


            "animation":

            self.create_animation_data(

                frames,

                fps

            )

        }


        return data



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_last_export(
        self
    ):

        return self.last_export