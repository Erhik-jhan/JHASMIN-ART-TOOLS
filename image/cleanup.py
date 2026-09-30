from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageOps



class ImageCleaner:


    def __init__(self):

        self.last_operation = None

        self.history = []



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
    # PROCESO GENERAL
    # ==========================================================

    def process(
        self,
        image
    ):


        img = image.copy()


        img = self.remove_noise(
            img
        )


        img = self.auto_contrast(
            img
        )


        img = self.sharpen(
            img
        )


        self._register(
            "process"
        )


        return img



    # ==========================================================
    # REDUCCIÓN DE RUIDO
    # ==========================================================

    def remove_noise(
        self,
        image,
        radius=1
    ):


        img = image.filter(

            ImageFilter.MedianFilter(
                radius
            )

        )


        self._register(
            "remove_noise"
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

            ImageFilter.SMOOTH

        )


        self._register(
            "smooth"
        )


        return img



    # ==========================================================
    # DESENFOQUE
    # ==========================================================

    def blur(
        self,
        image,
        radius=2
    ):


        img = image.filter(

            ImageFilter.GaussianBlur(
                radius
            )

        )


        self._register(
            "blur"
        )


        return img



    # ==========================================================
    # ENFOQUE
    # ==========================================================

    def sharpen(
        self,
        image
    ):


        img = image.filter(

            ImageFilter.SHARPEN

        )


        self._register(
            "sharpen"
        )


        return img



    # ==========================================================
    # CONTRASTE AUTOMÁTICO
    # ==========================================================

    def auto_contrast(
        self,
        image
    ):


        img = ImageOps.autocontrast(

            image

        )


        self._register(
            "auto_contrast"
        )


        return img



    # ==========================================================
    # CONTRASTE
    # ==========================================================

    def contrast(
        self,
        image,
        factor=1.2
    ):


        enhancer = ImageEnhance.Contrast(

            image

        )


        img = enhancer.enhance(

            factor

        )


        self._register(
            "contrast"
        )


        return img



    # ==========================================================
    # BRILLO
    # ==========================================================

    def brightness(
        self,
        image,
        factor=1.1
    ):


        enhancer = ImageEnhance.Brightness(

            image

        )


        img = enhancer.enhance(

            factor

        )


        self._register(
            "brightness"
        )


        return img



    # ==========================================================
    # SATURACIÓN
    # ==========================================================

    def saturation(
        self,
        image,
        factor=1.2
    ):


        enhancer = ImageEnhance.Color(

            image

        )


        img = enhancer.enhance(

            factor

        )


        self._register(
            "saturation"
        )


        return img



    # ==========================================================
    # DETALLE
    # ==========================================================

    def detail(
        self,
        image
    ):


        img = image.filter(

            ImageFilter.DETAIL

        )


        self._register(
            "detail"
        )


        return img



    # ==========================================================
    # DETALLE AVANZADO
    # ==========================================================

    def detail_plus(
        self,
        image
    ):


        img = image.filter(

            ImageFilter.EDGE_ENHANCE_MORE

        )


        self._register(
            "detail_plus"
        )


        return img



    # ==========================================================
    # ESCALA DE GRISES
    # ==========================================================

    def grayscale(
        self,
        image
    ):


        img = ImageOps.grayscale(

            image

        )


        self._register(
            "grayscale"
        )


        return img



    # ==========================================================
    # NEGATIVO
    # ==========================================================

    def invert(
        self,
        image
    ):


        if image.mode == "RGBA":


            rgb = image.convert(

                "RGB"

            )


            rgb = ImageOps.invert(

                rgb

            )


            img = rgb.convert(

                "RGBA"

            )


        else:


            img = ImageOps.invert(

                image

            )



        self._register(
            "invert"
        )


        return img



    # ==========================================================
    # BINARIZACIÓN
    # ==========================================================

    def threshold(
        self,
        image,
        threshold=128
    ):


        gray = image.convert(

            "L"

        )


        img = gray.point(

            lambda p:

            255
            if p > threshold
            else 0

        )


        self._register(
            "threshold"
        )


        return img.convert(

            "RGBA"

        )



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

            self.last_operation



        }



    def get_last_operation(
        self
    ):

        return self.last_operation