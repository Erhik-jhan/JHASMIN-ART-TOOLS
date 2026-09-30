from pathlib import Path

import numpy as np

from PIL import Image

from segmentation.masks import MaskProcessor



class SAMModel:


    def __init__(self):

        self.model = None

        self.predictor = None

        self.model_path = None

        self.device = "cpu"

        self.loaded = False

        self.last_mask = None

        self.last_operation = None

        self.mask_processor = MaskProcessor()



    # ==========================================================
    # CONFIGURACIÓN DEL MODELO
    # ==========================================================

    def configure(
        self,
        model_path,
        device="cpu"
    ):

        self.model_path = Path(
            model_path
        )

        self.device = device


        self.last_operation = (
            "configure"
        )



    # ==========================================================
    # CARGAR MODELO
    # ==========================================================

    def load_model(
        self
    ):


        if self.model_path is None:

            return False



        if not self.model_path.exists():

            return False



        # Aquí se integrará:
        #
        # Segment Anything
        # SAM 1
        # SAM 2
        # PyTorch
        #
        # Ejemplo futuro:
        #
        # self.model = sam_model_registry(...)
        # self.predictor = SamPredictor(...)



        self.loaded = True


        self.last_operation = (
            "load_model"
        )


        return True



    # ==========================================================
    # ESTADO DEL MODELO
    # ==========================================================

    def is_loaded(
        self
    ):

        return self.loaded



    # ==========================================================
    # PREDICCIÓN PRINCIPAL
    # ==========================================================

    def predict(
        self,
        image,
        points=None,
        boxes=None
    ):


        if not isinstance(
            image,
            Image.Image
        ):

            return None



        if not self.loaded:

            return self._fallback_mask(
                image
            )



        # ======================================================
        # AQUÍ ENTRARÁ SAM REAL
        # ======================================================


        return self._fallback_mask(
            image
        )



    # ==========================================================
    # MÁSCARA TEMPORAL
    # ==========================================================

    def _fallback_mask(
        self,
        image
    ):


        mask = self.mask_processor.create_full(

            image.size

        )


        self.last_mask = mask


        self.last_operation = (
            "fallback_mask"
        )


        return mask



    # ==========================================================
    # SEGMENTACIÓN POR PUNTOS
    # ==========================================================

    def segment_point(
        self,
        image,
        x,
        y
    ):


        return self.predict(

            image,

            points=[

                (
                    x,

                    y

                )

            ]

        )



    # ==========================================================
    # SEGMENTACIÓN POR CAJA
    ==========================================================

    def segment_box(
        self,
        image,
        box
    ):


        return self.predict(

            image,

            boxes=[

                box

            ]

        )



    # ==========================================================
    # CONVERSIÓN NUMPY
    # ==========================================================

    def mask_to_numpy(
        self,
        mask
    ):


        return np.array(

            mask

        )



    # ==========================================================
    # CONVERSIÓN PIL
    # ==========================================================

    def numpy_to_mask(
        self,
        array
    ):


        return Image.fromarray(

            array.astype(

                np.uint8

            )

        )



    # ==========================================================
    # OBTENER ÚLTIMA MÁSCARA
    # ==========================================================

    def get_last_mask(
        self
    ):

        return self.last_mask



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_info(
        self
    ):

        return {


            "loaded":

            self.loaded,


            "model_path":

            str(
                self.model_path
            )
            if self.model_path
            else None,


            "device":

            self.device,


            "last_operation":

            self.last_operation


        }