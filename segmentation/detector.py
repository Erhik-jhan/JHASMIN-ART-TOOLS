from PIL import Image
from PIL import ImageStat
from PIL import ImageFilter
from PIL import ImageOps



class ObjectDetector:


    def __init__(self):

        self.last_detection = None

        self.detections = []

        self.model = None

        self.loaded = False

        self.last_operation = None



    # ==========================================================
    # CONFIGURACIÓN DEL DETECTOR
    # ==========================================================

    def configure(
        self,
        model=None
    ):

        self.model = model


        self.last_operation = (
            "configure"
        )



    # ==========================================================
    # PROCESO PRINCIPAL
    # ==========================================================

    def detect(
        self,
        image
    ):


        result = {


            "image_size":

            image.size,


            "objects":

            [],


            "confidence":

            0



        }


        self._save_detection(
            result
        )


        return result



    # ==========================================================
    # DETECCIÓN DE SILUETA
    # ==========================================================

    def detect_subject(
        self,
        image
    ):


        img = image.convert(
            "RGBA"
        )


        bbox = img.getbbox()


        if bbox is None:

            return None



        detection = {


            "type":

            "subject",


            "bbox":

            bbox,


            "confidence":

            0.5



        }



        self._save_detection(
            detection
        )


        return detection



    # ==========================================================
    # DETECCIÓN DE ZONAS POR COLOR
    # ==========================================================

    def detect_color_region(
        self,
        image,
        color,
        tolerance=40
    ):


        img = image.convert(
            "RGBA"
        )


        pixels = img.load()


        points = []



        for y in range(img.height):

            for x in range(img.width):


                pixel = pixels[x, y]



                distance = (

                    abs(pixel[0] - color[0]) +

                    abs(pixel[1] - color[1]) +

                    abs(pixel[2] - color[2])

                )



                if distance < tolerance:

                    points.append(

                        (
                            x,

                            y

                        )

                    )



        if not points:

            return None



        xs = [

            p[0]

            for p in points

        ]


        ys = [

            p[1]

            for p in points

        ]



        bbox = (

            min(xs),

            min(ys),

            max(xs),

            max(ys)

        )



        result = {


            "type":

            "color_region",


            "bbox":

            bbox,


            "pixels":

            len(points)


        }



        self._save_detection(
            result
        )


        return result



    # ==========================================================
    # DETECCIÓN DE BORDES
    # ==========================================================

    def detect_edges(
        self,
        image
    ):


        gray = ImageOps.grayscale(

            image

        )


        edges = gray.filter(

            ImageFilter.FIND_EDGES

        )


        self.last_operation = (
            "edges"
        )


        return edges



    # ==========================================================
    # ANÁLISIS DE IMAGEN
    # ==========================================================

    def analyze(
        self,
        image
    ):


        stat = ImageStat.Stat(

            image.convert(
                "RGB"
            )

        )


        analysis = {


            "mean_color":

            stat.mean,


            "extrema":

            stat.extrema,


            "size":

            image.size



        }



        self._save_detection(
            analysis
        )


        return analysis



    # ==========================================================
    # PARTES DEL PERSONAJE
    # ==========================================================

    def detect_character_parts(
        self,
        image
    ):


        parts = {


            "hair":

            None,


            "face":

            None,


            "eyes":

            None,


            "wings":

            None,


            "clothes":

            None,


            "accessories":

            None,


            "gem":

            None



        }



        self._save_detection(
            parts
        )


        return parts



    # ==========================================================
    # REGISTRO INTERNO
    # ==========================================================

    def _save_detection(
        self,
        data
    ):

        self.last_detection = data

        self.detections.append(
            data
        )


        self.last_operation = (
            "detect"
        )



    # ==========================================================
    # HISTORIAL
    # ==========================================================

    def get_detections(
        self
    ):

        return self.detections



    # ==========================================================
    # LIMPIAR HISTORIAL
    # ==========================================================

    def clear_history(
        self
    ):

        self.detections.clear()



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_info(
        self
    ):

        return {


            "loaded":

            self.loaded,


            "detections":

            len(
                self.detections
            ),


            "last_operation":

            self.last_operation



        }



    # ==========================================================
    # ÚLTIMA DETECCIÓN
    # ==========================================================

    def get_last_detection(
        self
    ):

        return self.last_detection