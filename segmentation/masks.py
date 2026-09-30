from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageOps



class MaskProcessor:


    def __init__(self):

        self.last_operation = None

        self.masks = {}



    # ==========================================================
    # CREAR MÁSCARA VACÍA
    # ==========================================================

    def create_empty(
        self,
        size,
        name=None
    ):

        mask = Image.new(
            "L",
            size,
            0
        )


        self._register_mask(
            name,
            mask
        )


        self.last_operation = "create_empty"


        return mask



    # ==========================================================
    # CREAR MÁSCARA COMPLETA
    # ==========================================================

    def create_full(
        self,
        size,
        name=None
    ):

        mask = Image.new(
            "L",
            size,
            255
        )


        self._register_mask(
            name,
            mask
        )


        self.last_operation = "create_full"


        return mask



    # ==========================================================
    # CREAR DESDE PUNTOS
    # ==========================================================

    def create_polygon(
        self,
        size,
        points,
        name=None
    ):

        mask = Image.new(
            "L",
            size,
            0
        )


        draw = ImageDraw.Draw(
            mask
        )


        draw.polygon(
            points,
            fill=255
        )


        self._register_mask(
            name,
            mask
        )


        self.last_operation = (
            "create_polygon"
        )


        return mask



    # ==========================================================
    # CREAR DESDE RECTÁNGULO
    # ==========================================================

    def create_rectangle(
        self,
        size,
        box,
        name=None
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
            box,
            fill=255
        )


        self._register_mask(
            name,
            mask
        )


        self.last_operation = (
            "create_rectangle"
        )


        return mask



    # ==========================================================
    # REGISTRO DE MÁSCARAS
    # ==========================================================

    def _register_mask(
        self,
        name,
        mask
    ):

        if name:

            self.masks[name] = mask



    # ==========================================================
    # OBTENER MÁSCARA
    # ==========================================================

    def get_mask(
        self,
        name
    ):

        return self.masks.get(
            name
        )



    # ==========================================================
    # LISTAR MÁSCARAS
    # ==========================================================

    def get_all_masks(
        self
    ):

        return self.masks



    # ==========================================================
    # SUAVIZAR BORDES
    # ==========================================================

    def blur(
        self,
        mask,
        radius=3
    ):

        result = mask.filter(
            ImageFilter.GaussianBlur(
                radius
            )
        )


        self.last_operation = "blur"


        return result



    # ==========================================================
    # LIMPIAR RUIDO
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


        self.last_operation = "clean"


        return result



    # ==========================================================
    # DILATAR MÁSCARA
    # ==========================================================

    def expand(
        self,
        mask,
        pixels=2
    ):

        result = mask.filter(
            ImageFilter.MaxFilter(
                pixels * 2 + 1
            )
        )


        self.last_operation = "expand"


        return result



    # ==========================================================
    # CONTRAER MÁSCARA
    ==========================================================

    def shrink(
        self,
        mask,
        pixels=2
    ):

        result = mask.filter(
            ImageFilter.MinFilter(
                pixels * 2 + 1
            )
        )


        self.last_operation = "shrink"


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


        self.last_operation = "invert"


        return result



    # ==========================================================
    # COMBINAR MÁSCARAS
    # ==========================================================

    def merge(
        self,
        mask_a,
        mask_b
    ):

        result = ImageOps.lighter(
            mask_a,
            mask_b
        )


        self.last_operation = "merge"


        return result



    # ==========================================================
    # APLICAR MÁSCARA
    # ==========================================================

    def apply(
        self,
        image,
        mask
    ):

        result = image.copy()

        result.putalpha(
            mask
        )


        self.last_operation = "apply"


        return result



    # ==========================================================
    # EXTRAER CONTORNO
    # ==========================================================

    def outline(
        self,
        mask
    ):

        expanded = self.expand(
            mask,
            3
        )


        outline = ImageOps.subtract(
            expanded,
            mask
        )


        self.last_operation = "outline"


        return outline



    # ==========================================================
    # EXPORTAR INFORMACIÓN
    # ==========================================================

    def export_data(
        self
    ):

        data = {}


        for name, mask in self.masks.items():

            data[name] = {

                "size": mask.size,

                "mode": mask.mode

            }


        return data



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_last_operation(
        self
    ):

        return self.last_operation