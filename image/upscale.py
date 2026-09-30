from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter



class ImageUpscaler:


    def __init__(self):

        self.last_scale = 1

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
        scale=2
    ):


        img = self.upscale(

            image,

            scale

        )


        img = self.enhance(

            img

        )


        self._register(
            "process"
        )


        return img



    # ==========================================================
    # ESCALADO PRINCIPAL
    # ==========================================================

    def upscale(
        self,
        image,
        scale=2
    ):


        if scale < 1:

            scale = 1



        width = image.width * scale

        height = image.height * scale



        img = image.resize(

            (
                width,

                height

            ),

            Image.Resampling.LANCZOS

        )



        self.last_scale = scale


        self._register(
            "upscale"
        )


        return img



    # ==========================================================
    # ESCALADO PERSONALIZADO
    # ==========================================================

    def resize(
        self,
        image,
        width,
        height
    ):


        img = image.resize(

            (
                width,

                height

            ),

            Image.Resampling.LANCZOS

        )


        self._register(
            "resize"
        )


        return img



    # ==========================================================
    # MEJORA DESPUÉS DEL ESCALADO
    # ==========================================================

    def enhance(
        self,
        image
    ):


        img = image.filter(

            ImageFilter.DETAIL

        )


        img = ImageEnhance.Sharpness(

            img

        ).enhance(

            1.25

        )


        img = ImageEnhance.Contrast(

            img

        ).enhance(

            1.10

        )


        self._register(
            "enhance"
        )


        return img



    # ==========================================================
    # SUPER RESOLUCIÓN IA
    # ==========================================================

    def upscale_ai(
        self,
        image,
        scale=4
    ):


        """
        Preparado para:

        - Real ESRGAN
        - SwinIR
        - modelos PyTorch
        - ONNX Runtime

        """

        if self.ai_model is None:

            return self.upscale(

                image,

                scale

            )



        result = self.ai_model(

            image

        )


        self._register(
            "upscale_ai"
        )


        return result



    # ==========================================================
    # NITIDEZ
    # ==========================================================

    def sharpen(
        self,
        image,
        amount=1.5
    ):


        enhancer = ImageEnhance.Sharpness(

            image

        )


        img = enhancer.enhance(

            amount

        )


        self._register(
            "sharpen"
        )


        return img



    # ==========================================================
    # SUAVIZADO
    # ==========================================================

    def smooth(
        self,
        image
    ):


        img = image.filter(

            ImageFilter.SMOOTH_MORE

        )


        self._register(
            "smooth"
        )


        return img



    # ==========================================================
    # ESCALADOS PREDEFINIDOS
    # ==========================================================

    def upscale_2x(
        self,
        image
    ):

        return self.upscale(

            image,

            2

        )



    def upscale_4x(
        self,
        image
    ):

        return self.upscale(

            image,

            4

        )



    def upscale_8x(
        self,
        image
    ):

        return self.upscale(

            image,

            8

        )



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_info(
        self
    ):

        return {


            "last_scale":

            self.last_scale,


            "last_operation":

            self.last_operation,


            "operations":

            len(

                self.history

            ),


            "ai_connected":

            self.ai_model is not None



        }



    def get_history(
        self
    ):

        return self.history



    def clear_history(
        self
    ):

        self.history.clear()



    def get_last_scale(
        self
    ):

        return self.last_scale



    def get_last_operation(
        self
    ):

        return self.last_operation