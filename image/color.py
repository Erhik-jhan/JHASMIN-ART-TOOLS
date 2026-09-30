from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageStat
from PIL import ImageFilter



class ColorProcessor:


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
    # CONFIGURACIÓN IA COLOR
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
    # PROCESO COMPLETO
    # ==========================================================

    def process(
        self,
        image
    ):


        img = image.copy()


        img = self.auto_contrast(
            img
        )


        img = self.auto_color(
            img
        )


        img = self.vibrance(
            img,
            1.15
        )


        img = self.sharpness(
            img,
            1.10
        )


        self._register(
            "process"
        )


        return img



    # ==========================================================
    # BRILLO
    # ==========================================================

    def brightness(
        self,
        image,
        factor=1.0
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
    # CONTRASTE
    # ==========================================================

    def contrast(
        self,
        image,
        factor=1.0
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
    # SATURACIÓN
    # ==========================================================

    def saturation(
        self,
        image,
        factor=1.0
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
    # NITIDEZ
    # ==========================================================

    def sharpness(
        self,
        image,
        factor=1.0
    ):


        enhancer = ImageEnhance.Sharpness(

            image

        )


        img = enhancer.enhance(

            factor

        )


        self._register(
            "sharpness"
        )


        return img



    # ==========================================================
    # COLOR AUTOMÁTICO
    # ==========================================================

    def auto_color(
        self,
        image
    ):


        img = ImageOps.equalize(

            image.convert(
                "RGB"
            )

        )


        self._register(
            "auto_color"
        )


        return img.convert(
            "RGBA"
        )



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
    # TONO CÁLIDO
    # ==========================================================

    def warm(
        self,
        image
    ):


        r, g, b, a = image.split()


        r = r.point(
            lambda i:
            min(
                255,
                int(i * 1.08)
            )
        )


        b = b.point(
            lambda i:
            int(i * 0.95)
        )


        img = Image.merge(

            "RGBA",

            (
                r,
                g,
                b,
                a
            )

        )


        self._register(
            "warm"
        )


        return img



    # ==========================================================
    # TONO FRÍO
    # ==========================================================

    def cool(
        self,
        image
    ):


        r, g, b, a = image.split()


        r = r.point(
            lambda i:
            int(i * 0.95)
        )


        b = b.point(
            lambda i:
            min(
                255,
                int(i * 1.08)
            )
        )


        img = Image.merge(

            "RGBA",

            (
                r,
                g,
                b,
                a
            )

        )


        self._register(
            "cool"
        )


        return img



    # ==========================================================
    # SEPIA
    # ==========================================================

    def sepia(
        self,
        image
    ):


        img = image.convert(
            "RGB"
        )


        pixels = img.load()


        for y in range(img.height):

            for x in range(img.width):

                r, g, b = pixels[x,y]


                tr = int(
                    0.393*r +
                    0.769*g +
                    0.189*b
                )


                tg = int(
                    0.349*r +
                    0.686*g +
                    0.168*b
                )


                tb = int(
                    0.272*r +
                    0.534*g +
                    0.131*b
                )


                pixels[x,y] = (

                    min(255,tr),

                    min(255,tg),

                    min(255,tb)

                )


        self._register(
            "sepia"
        )


        return img.convert(
            "RGBA"
        )



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


        return img.convert(
            "RGBA"
        )



    # ==========================================================
    # NEGATIVO
    # ==========================================================

    def invert(
        self,
        image
    ):


        rgb = image.convert(
            "RGB"
        )


        rgb = ImageOps.invert(
            rgb
        )


        self._register(
            "invert"
        )


        return rgb.convert(
            "RGBA"
        )



    # ==========================================================
    # VIBRANCE
    # ==========================================================

    def vibrance(
        self,
        image,
        factor=1.2
    ):


        img = ImageEnhance.Color(

            image

        ).enhance(

            factor

        )


        self._register(
            "vibrance"
        )


        return img



    # ==========================================================
    # DESATURAR
    # ==========================================================

    def desaturate(
        self,
        image
    ):


        img = ImageEnhance.Color(

            image

        ).enhance(

            0

        )


        self._register(
            "desaturate"
        )


        return img



    # ==========================================================
    # REALCE COMPLETO
    # ==========================================================

    def enhance(
        self,
        image
    ):


        img = image.filter(

            ImageFilter.DETAIL

        )


        img = ImageEnhance.Contrast(

            img

        ).enhance(
            1.15
        )


        img = ImageEnhance.Color(

            img

        ).enhance(
            1.10
        )


        img = ImageEnhance.Sharpness(

            img

        ).enhance(
            1.20
        )


        self._register(
            "enhance"
        )


        return img



    # ==========================================================
    # COLORIZACIÓN IA
    # ==========================================================

    def colorize_ai(
        self,
        image
    ):


        if self.ai_model is None:

            return image



        result = self.ai_model(
            image
        )


        self._register(
            "colorize_ai"
        )


        return result



    # ==========================================================
    # ESTADÍSTICAS
    # ==========================================================

    def average_color(
        self,
        image
    ):


        rgb = image.convert(
            "RGB"
        )


        stat = ImageStat.Stat(
            rgb
        )


        return tuple(

            int(v)

            for v in stat.mean

        )



    def average_brightness(
        self,
        image
    ):


        gray = image.convert(
            "L"
        )


        stat = ImageStat.Stat(
            gray
        )


        return stat.mean[0]



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



    def get_history(
        self
    ):

        return self.history



    def clear_history(
        self
    ):

        self.history.clear()



    def get_last_operation(
        self
    ):

        return self.last_operation