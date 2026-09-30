from PIL import Image

from segmentation.masks import MaskProcessor



class SegmentationPredictor:


    def __init__(self):

        self.mask_processor = MaskProcessor()

        self.last_prediction = None

        self.predictions = []

        self.sam_model = None

        self.last_operation = None



    # ==========================================================
    # CONFIGURACIÓN SAM
    # ==========================================================

    def set_sam_model(
        self,
        model
    ):

        self.sam_model = model


        self.last_operation = (
            "set_sam_model"
        )



    # ==========================================================
    # PREDICCIÓN PRINCIPAL
    # ==========================================================

    def predict(
        self,
        image,
        detection=None
    ):


        if detection is None:

            detection = {


                "bbox":

                (

                    0,

                    0,

                    image.width,

                    image.height

                )


            }



        mask = self.create_mask_from_detection(

            image,

            detection

        )



        result = {


            "mask":

            mask,


            "confidence":

            0.5,


            "type":

            "segmentation"



        }



        self._save_prediction(
            result
        )


        return result



    # ==========================================================
    # CREAR MÁSCARA DESDE DETECCIÓN
    # ==========================================================

    def create_mask_from_detection(
        self,
        image,
        detection
    ):


        size = image.size


        bbox = detection.get(
            "bbox"
        )


        if bbox is None:

            return self.mask_processor.create_empty(

                size

            )



        mask = self.mask_processor.create_rectangle(

            size,

            bbox

        )


        mask = self.refine_mask(

            mask

        )


        self.last_operation = (
            "create_mask"
        )


        return mask



    # ==========================================================
    # PREDICCIÓN POR PUNTOS
    # ==========================================================

    def predict_points(
        self,
        image,
        points
    ):


        mask = self.mask_processor.create_polygon(

            image.size,

            points

        )


        mask = self.refine_mask(

            mask

        )


        self._save_prediction(

            mask

        )


        return mask



    # ==========================================================
    # PREDICCIÓN POR CAJA
    # ==========================================================

    def predict_box(
        self,
        image,
        box
    ):


        detection = {


            "bbox":

            box


        }


        result = self.predict(

            image,

            detection

        )


        return result



    # ==========================================================
    # REFINAR MÁSCARA
    # ==========================================================

    def refine_mask(
        self,
        mask
    ):


        result = self.mask_processor.clean(

            mask

        )


        result = self.mask_processor.blur(

            result,

            1

        )


        self.last_operation = (
            "refine_mask"
        )


        return result



    # ==========================================================
    # SEPARAR COMPONENTES
    # ==========================================================

    def separate_parts(
        self,
        image,
        parts
    ):


        layers = {}



        for name, mask in parts.items():


            if mask is None:

                continue



            layer = image.copy()


            layer.putalpha(

                mask

            )


            layers[name] = layer



        self._save_prediction(

            layers

        )


        return layers



    # ==========================================================
    # PREDICCIÓN CON SAM
    # ==========================================================

    def predict_with_sam(
        self,
        image,
        points=None,
        boxes=None
    ):


        if self.sam_model:


            return self.sam_model.predict(

                image,

                points,

                boxes

            )



        return self.predict(

            image

        )



    # ==========================================================
    # GUARDAR PREDICCIÓN
    # ==========================================================

    def _save_prediction(
        self,
        data
    ):


        self.last_prediction = data


        self.predictions.append(

            data

        )


        self.last_operation = (
            "prediction"
        )



    # ==========================================================
    # HISTORIAL
    # ==========================================================

    def get_predictions(
        self
    ):

        return self.predictions



    def clear_history(
        self
    ):

        self.predictions.clear()



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_info(
        self
    ):


        return {


            "predictions":

            len(

                self.predictions

            ),


            "sam_connected":

            self.sam_model is not None,


            "last_operation":

            self.last_operation



        }



    # ==========================================================
    # ÚLTIMA PREDICCIÓN
    # ==========================================================

    def get_last_prediction(
        self
    ):

        return self.last_prediction