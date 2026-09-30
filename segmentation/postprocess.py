from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from PIL import ImageChops



class MaskPostProcessor:


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
    # PROCESO COMPLETO
    # ==========================================================

    def process(
        self,
        mask
    ):


        result = self.clean(
            mask
        )


        result = self.smooth_edges(
            result
        )


        result = self.optimize(
            result
        )


        self._register(
            "process"
        )


        return result



    # ==========================================================
    # LIMPIEZA DE RUIDO
    # ==========================================================

    def clean(
        self,
        mask
    ):


        result = mask.filter(

            ImageFilter.MedianFilter(
                3
            )

        )


        self._register(
            "clean"
        )


        return result



    # ==========================================================
    # SUAVIZADO DE BORDES
    # ==========================================================

    def smooth_edges(
        self,
        mask,
        radius=2
    ):


        result = mask.filter(

            ImageFilter.GaussianBlur(
                radius
            )

        )


        self._register(
            "smooth_edges"
        )


        return result



    # ==========================================================
    # OPTIMIZAR MÁSCARA
    # ==========================================================

    def optimize(
        self,
        mask
    ):


        result = self.sharpen_edges(
            mask
        )


        self._register(
            "optimize"
        )


        return result



    # ==========================================================
    # AUMENTAR CALIDAD DE BORDE
    # ==========================================================

    def sharpen_edges(
        self,
        mask
    ):


        result = mask.filter(

            ImageFilter.SHARPEN

        )


        self._register(
            "sharpen_edges"
        )


        return result



    # ==========================================================
    # EXPANDIR MÁSCARA
    # ==========================================================

    def expand(
        self,
        mask,
        pixels=3
    ):


        result = mask.filter(

            ImageFilter.MaxFilter(

                pixels * 2 + 1

            )

        )


        self._register(
            "expand"
        )


        return result



    # ==========================================================
    # CONTRAER MÁSCARA
    # ==========================================================

    def shrink(
        self,
        mask,
        pixels=3
    ):


        result = mask.filter(

            ImageFilter.MinFilter(

                pixels * 2 + 1

            )

        )


        self._register(
            "shrink"
        )


        return result



    # ==========================================================
    # ELIMINAR BORDE EXTERNO
    # ==========================================================

    def remove_halo(
        self,
        mask
    ):


        expanded = self.expand(

            mask,

            2

        )


        result = ImageChops.darker(

            mask,

            expanded

        )


        self._register(
            "remove_halo"
        )


        return result



    # ==========================================================
    # BINARIZAR
    # ==========================================================

    def threshold(
        self,
        mask,
        value=128
    ):


        result = mask.point(

            lambda p:

            255
            if p > value
            else 0

        )


        self._register(
            "threshold"
        )


        return result



    # ==========================================================
    # INVERTIR
    # ==========================================================

    def invert(
        self,
        mask
    ):


        result = ImageOps.invert(

            mask

        )


        self._register(
            "invert"
        )


        return result



    # ==========================================================
    # APLICAR A IMAGEN
    # ==========================================================

    def apply_mask(
        self,
        image,
        mask
    ):


        result = image.copy()


        result.putalpha(

            mask

        )


        self._register(
            "apply_mask"
        )


        return result



    # ==========================================================
    # EXTRAER CAPA
    # ==========================================================

    def extract_layer(
        self,
        image,
        mask,
        name
    ):


        layer = image.copy()


        layer.putalpha(

            mask

        )


        result = {


            "name":

            name,


            "image":

            layer,


            "mask":

            mask



        }



        self._register(
            "extract_layer"
        )


        return result



    # ==========================================================
    # PREPARACIÓN PARA ANIMACIÓN
    # ==========================================================

    def prepare_animation_mask(
        self,
        mask
    ):


        result = self.process(

            mask

        )


        result = self.threshold(

            result,

            100

        )


        self._register(
            "prepare_animation_mask"
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

            self.last_operation



        }



    def get_last_operation(
        self
    ):

        return self.last_operation