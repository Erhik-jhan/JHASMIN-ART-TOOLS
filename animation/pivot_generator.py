from dataclasses import dataclass

from PIL import Image



@dataclass
class PivotPoint:

    name: str

    x: float

    y: float

    rotation: float = 0.0

    scale: float = 1.0



class PivotGenerator:


    def __init__(self):

        self.pivots = {}

        self.last_operation = None



    # ==========================================================
    # CREAR PUNTO PIVOTE
    # ==========================================================

    def create_pivot(
        self,
        name,
        x,
        y
    ):

        pivot = PivotPoint(

            name=name,

            x=x,

            y=y

        )


        self.pivots[name] = pivot


        self.last_operation = (
            "create_pivot"
        )


        return pivot



    # ==========================================================
    # GENERAR PIVOTES BÁSICOS
    # ==========================================================

    def generate_basic(
        self,
        image
    ):

        width, height = image.size


        self.create_pivot(

            "center",

            width / 2,

            height / 2

        )


        self.create_pivot(

            "head",

            width / 2,

            height * 0.20

        )


        self.create_pivot(

            "body",

            width / 2,

            height * 0.50

        )


        self.create_pivot(

            "feet",

            width / 2,

            height * 0.90

        )


        self.last_operation = (
            "generate_basic"
        )


        return self.pivots



    # ==========================================================
    # PIVOTES JHASMIN
    # ==========================================================

    def generate_jhasmin(
        self,
        image
    ):

        width, height = image.size



        points = {

            "body":

            (
                width * 0.50,

                height * 0.55

            ),


            "head":

            (
                width * 0.50,

                height * 0.18

            ),


            "hair":

            (
                width * 0.50,

                height * 0.12

            ),


            "left_wing":

            (
                width * 0.20,

                height * 0.40

            ),


            "right_wing":

            (
                width * 0.80,

                height * 0.40

            ),


            "gem":

            (
                width * 0.50,

                height * 0.45

            ),


            "hands":

            (
                width * 0.50,

                height * 0.55

            )

        }



        for name, position in points.items():

            self.create_pivot(

                name,

                position[0],

                position[1]

            )



        self.last_operation = (
            "generate_jhasmin"
        )


        return self.pivots



    # ==========================================================
    # DETECTAR CENTRO DE CAPA
    # ==========================================================

    def detect_center(
        self,
        image
    ):

        bbox = image.getbbox()


        if bbox is None:

            return (
                0,
                0
            )


        x1, y1, x2, y2 = bbox


        center = (

            (x1 + x2) / 2,

            (y1 + y2) / 2

        )


        return center



    # ==========================================================
    # CREAR PIVOTE DESDE CAPA
    # ==========================================================

    def create_from_layer(
        self,
        name,
        layer
    ):

        x, y = self.detect_center(
            layer
        )


        return self.create_pivot(

            name,

            x,

            y

        )



    # ==========================================================
    # TRANSFORMACIONES
    # ==========================================================

    def set_rotation(
        self,
        name,
        rotation
    ):

        if name in self.pivots:

            self.pivots[name].rotation = rotation



    def set_scale(
        self,
        name,
        scale
    ):

        if name in self.pivots:

            self.pivots[name].scale = scale



    # ==========================================================
    # EXPORTAR
    # ==========================================================

    def export_data(
        self
    ):

        data = {}


        for name, pivot in self.pivots.items():

            data[name] = {

                "x": pivot.x,

                "y": pivot.y,

                "rotation": pivot.rotation,

                "scale": pivot.scale

            }


        return data



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_pivot(
        self,
        name
    ):

        return self.pivots.get(
            name
        )



    def get_all(
        self
    ):

        return self.pivots



    def get_last_operation(
        self
    ):

        return self.last_operation