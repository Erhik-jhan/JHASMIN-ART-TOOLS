from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageChops



class ImageInpainter:


    def __init__(self):

        self.last_operation = None

        self.history = []

        self.ai_model = None



    # ==========================================================
    # REGISTRO INTERNO
    # ==========================================================

    def _register(
        self,
        operation
    ):

        self.last_operation = operation

        self.history.append(
            operation
        )



    # ==========================================================
    # CONFIGURACIÓN IA
    # ==========================================================

    def set_ai_model(
        self,
        model
    ):

        self.ai_model = model


        self._register(
            "set_ai_model"
        )



    # ==========================================================
    # PROCESO PRINCIPAL
    # ==========================================================

    def process(
        self,
        image,
        mask
    ):


        result = self.inpaint(

            image,

            mask

        )


        self._register(
            "process"
        )


        return result



    # ==========================================================
    # INPAINTING BÁSICO
    # ==========================================================

    def inpaint(
        self,
        image,
        mask
    ):


        img = image.convert(

            "RGBA"

        ).copy()



        mask = mask.convert(

            "L"

        )



        blurred = img.filter(

            ImageFilter.GaussianBlur(

                8

            )

        )



        img.paste(

            blurred,

            (
                0,

                0

            ),

            mask

        )



        self._register(
            "inpaint"
        )


        return img



    # ==========================================================
    # RELLENO POR COLOR
    # ==========================================================

    def fill_color(
        self,
        image,
        mask,
        color
    ):


        result = image.convert(

            "RGBA"

        ).copy()



        fill = Image.new(

            "RGBA",

            result.size,

            color

        )



        result.paste(

            fill,

            (
                0,

                0

            ),

            mask

        )



        self._register(
            "fill_color"
        )


        return result



    # ==========================================================
    # RECONSTRUCCIÓN SUAVE
    # ==========================================================

    def smooth_repair(
        self,
        image,
        mask
    ):


        result = image.copy()



        repaired = image.filter(

            ImageFilter.MedianFilter(

                5

            )

        )



        result.paste(

            repaired,

            (
                0,

                0

            ),

            mask

        )



        self._register(
            "smooth_repair"
        )


        return result



    # ==========================================================
    # LIMPIAR IMPERFECCIONES
    # ==========================================================

    def remove_artifacts(
        self,
        image
    ):


        result = image.filter(

            ImageFilter.SMOOTH_MORE

        )



        self._register(
            "remove_artifacts"
        )


        return result



    # ==========================================================
    # CREAR MÁSCARA RECTANGULAR
    # ==========================================================

    def create_rectangle_mask(
        self,
        size,
        rectangle
    ):


        mask = Image.new(

            "L",

            size,

            0

        )


        draw = ImageDraw.Draw(

            mask

        )


        draw.rectangle(

            rectangle,

            fill=255

        )


        self._register(
            "create_rectangle_mask"
        )


        return mask



    # ==========================================================
    # CREAR MÁSCARA VACÍA
    # ==========================================================

    def create_empty_mask(
        self,
        size
    ):


        mask = Image.new(

            "L",

            size,

            0

        )


        self._register(
            "create_empty_mask"
        )


        return mask



    # ==========================================================
    # INVERTIR MÁSCARA
    # ==========================================================

    def invert_mask(
        self,
        mask
    ):


        result = ImageChops.invert(

            mask

        )


        self._register(
            "invert_mask"
        )


        return result



    # ==========================================================
    # INPAINTING CON IA
    # ==========================================================

    def ai_inpaint(
        self,
        image,
        mask
    ):


        """
        Preparado para:

        - Stable Diffusion Inpainting
        - LaMa
        - Diffusers
        - PyTorch
        """



        if self.ai_model is None:


            return self.inpaint(

                image,

                mask

            )



        result = self.ai_model(

            image,

            mask

        )



        self._register(
            "ai_inpaint"
        )


        return result



    # ==========================================================
    # HISTORIAL
    # ==========================================================

    def get_history(
        self
    ):

        return self.history



    def clear_history(
        self
    ):

        self.history.clear()



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_info(
        self
    ):

        return {


            "operations":

            len(

                self.history

            ),


            "last_operation":

            self.last_operation,


            "ai_connected":

            self.ai_model is not None



        }



    def get_last_operation(
        self
    ):

        return self.last_operation