from PIL import Image
from PIL import ImageFilter



class BackgroundRemover:


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
        image
    ):


        img = self.remove_simple_background(

            image

        )


        self._register(
            "process"
        )


        return img



    # ==========================================================
    # REMOCIÓN SIMPLE POR COLOR
    # ==========================================================

    def remove_simple_background(
        self,
        image,
        tolerance=30
    ):


        img = image.convert(

            "RGBA"

        )


        pixels = img.load()


        width, height = img.size


        background = pixels[0, 0]



        for y in range(height):

            for x in range(width):


                current = pixels[x, y]


                difference = (

                    abs(current[0] - background[0]) +

                    abs(current[1] - background[1]) +

                    abs(current[2] - background[2])

                )



                if difference < tolerance:


                    pixels[x, y] = (

                        current[0],

                        current[1],

                        current[2],

                        0

                    )



        self._register(
            "remove_simple_background"
        )


        return img



    # ==========================================================
    # DETECTAR COLOR DE FONDO
    # ==========================================================

    def detect_background_color(
        self,
        image
    ):


        img = image.convert(

            "RGBA"

        )


        corners = [

            img.getpixel((0,0)),

            img.getpixel(
                (
                    img.width-1,
                    0
                )
            ),

            img.getpixel(
                (
                    0,
                    img.height-1
                )
            ),

            img.getpixel(
                (
                    img.width-1,
                    img.height-1
                )
            )

        ]



        r = sum(
            p[0]
            for p in corners
        ) // 4


        g = sum(
            p[1]
            for p in corners
        ) // 4


        b = sum(
            p[2]
            for p in corners
        ) // 4



        return (

            r,

            g,

            b,

            255

        )



    # ==========================================================
    # REMOVER COLOR ESPECÍFICO
    # ==========================================================

    def remove_color(
        self,
        image,
        color,
        tolerance=40
    ):


        img = image.convert(

            "RGBA"

        )


        pixels = img.load()



        for y in range(img.height):

            for x in range(img.width):


                pixel = pixels[x, y]


                difference = (

                    abs(pixel[0]-color[0]) +

                    abs(pixel[1]-color[1]) +

                    abs(pixel[2]-color[2])

                )



                if difference < tolerance:


                    pixels[x,y] = (

                        pixel[0],

                        pixel[1],

                        pixel[2],

                        0

                    )



        self._register(
            "remove_color"
        )


        return img



    # ==========================================================
    # SUAVIZAR BORDES
    # ==========================================================

    def smooth_edges(
        self,
        image,
        radius=1
    ):


        alpha = image.getchannel(

            "A"

        )


        alpha = alpha.filter(

            ImageFilter.GaussianBlur(
                radius
            )

        )


        image.putalpha(

            alpha

        )


        self._register(
            "smooth_edges"
        )


        return image



    # ==========================================================
    # CREAR MÁSCARA
    # ==========================================================

    def create_mask(
        self,
        image
    ):


        mask = image.getchannel(

            "A"

        )


        self._register(
            "create_mask"
        )


        return mask



    # ==========================================================
    # REMOCIÓN CON IA
    # ==========================================================

    def remove_with_ai(
        self,
        image,
        mask
    ):


        result = image.copy()


        result.putalpha(

            mask

        )


        self._register(
            "remove_with_ai"
        )


        return result



    # ==========================================================
    # FUTURA INTEGRACIÓN SAM
    # ==========================================================

    def remove_using_segmentation(
        self,
        image,
        segmentation_model
    ):


        mask = segmentation_model.predict(

            image

        )


        result = image.copy()


        result.putalpha(

            mask

        )


        self._register(
            "remove_using_segmentation"
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

            "last_operation":

            self.last_operation,


            "operations":

            len(
                self.history
            ),


            "ai_connected":

            self.ai_model is not None

        }



    def get_last_operation(
        self
    ):

        return self.last_operation