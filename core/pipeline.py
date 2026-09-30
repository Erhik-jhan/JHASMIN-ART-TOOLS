from copy import deepcopy

from image.cleanup import ImageCleaner
from image.remove_background import BackgroundRemover
from image.upscale import ImageUpscaler
from image.color import ColorProcessor
from image.inpainting import ImageInpainter

from segmentation.detector import ObjectDetector
from segmentation.predictor import SegmentationPredictor
from segmentation.postprocess import MaskPostProcessor
from segmentation.sam_model import SAMModel

from core.image_manager import ImageManager
from core.layer_manager import LayerManager
from core.history import HistoryManager


class ProcessingPipeline:


    def __init__(self):

        # ==========================================
        # Núcleo
        # ==========================================

        self.image_manager = ImageManager()

        self.layer_manager = LayerManager()

        self.history = HistoryManager()


        # ==========================================
        # Imagen
        # ==========================================

        self.cleaner = ImageCleaner()

        self.background = BackgroundRemover()

        self.upscaler = ImageUpscaler()

        self.color = ColorProcessor()

        self.inpainter = ImageInpainter()


        # ==========================================
        # Segmentación
        # ==========================================

        self.detector = ObjectDetector()

        self.predictor = SegmentationPredictor()

        self.postprocessor = MaskPostProcessor()

        self.sam = SAMModel()


        # ==========================================
        # Estado
        # ==========================================

        self.last_result = None

        self.last_mask = None

        self.last_detection = None

        self.last_pipeline = []



    # ==========================================================
    # IMAGEN
    # ==========================================================

    def set_image(
        self,
        image,
        name="Imagen"
    ):

        self.image_manager.set_image(
            image,
            name
        )

        self.layer_manager.clear()

        self.layer_manager.add_layer(
            name,
            image
        )

        self.history.clear()

        self.save_state(
            "Imagen cargada"
        )



    def get_image(self):

        return self.image_manager.get_image()



    # ==========================================================
    # HISTORIAL
    # ==========================================================

    def save_state(
        self,
        operation
    ):

        image = self.image_manager.get_image()

        if image is None:

            return

        self.history.push(

            image,

            operation

        )



    def undo(self):

        image = self.history.undo()

        if image is None:

            return None

        self.image_manager.set_image(
            image
        )

        return image



    def redo(self):

        image = self.history.redo()

        if image is None:

            return None

        self.image_manager.set_image(
            image
        )

        return image



    # ==========================================================
    # APLICAR RESULTADO
    # ==========================================================

    def _update_image(
        self,
        image,
        operation
    ):

        self.image_manager.set_image(
            image
        )

        self.layer_manager.update_selected(
            image
        )

        self.save_state(
            operation
        )

        self.last_result = image

        self.last_pipeline.append(
            operation
        )

        return image



    # ==========================================================
    # LIMPIEZA
    # ==========================================================

    def clean(self):

        image = self.get_image()

        if image is None:

            return None

        result = self.cleaner.process(
            image
        )

        return self._update_image(

            result,

            "clean"

        )



    # ==========================================================
    # COLOR
    # ==========================================================

    def enhance_color(self):

        image = self.get_image()

        if image is None:

            return None

        result = self.color.process(
            image
        )

        return self._update_image(

            result,

            "color"

        )



    # ==========================================================
    # UPSCALE
    # ==========================================================

    def upscale(
        self,
        scale=2
    ):

        image = self.get_image()

        if image is None:

            return None

        result = self.upscaler.process(

            image,

            scale

        )

        return self._update_image(

            result,

            "upscale"

        )



    # ==========================================================
    # QUITAR FONDO
    # ==========================================================

    def remove_background(self):

        image = self.get_image()

        if image is None:

            return None

        result = self.background.process(
            image
        )

        return self._update_image(

            result,

            "background"

        )



    # ==========================================================
    # DETECTAR OBJETOS
    # ==========================================================

    def detect(self):

        image = self.get_image()

        if image is None:

            return None

        detection = self.detector.detect_subject(
            image
        )

        self.last_detection = detection

        return detection



    # ==========================================================
    # SEGMENTACIÓN
    # ==========================================================

    def segment(self):

        image = self.get_image()

        if image is None:

            return None

        detection = self.detect()

        prediction = self.predictor.predict(

            image,

            detection

        )

        mask = prediction["mask"]

        mask = self.postprocessor.process(
            mask
        )

        self.last_mask = mask

        return mask



    # ==========================================================
    # SEGMENTACIÓN SAM
    # ==========================================================

    def segment_sam(

        self,

        points=None,

        boxes=None

    ):

        image = self.get_image()

        if image is None:

            return None

        mask = self.sam.predict(

            image,

            points,

            boxes

        )

        mask = self.postprocessor.process(
            mask
        )

        self.last_mask = mask

        return mask



    # ==========================================================
    # EXTRAER PERSONAJE
    # ==========================================================

    def extract_character(self):

        image = self.get_image()

        if image is None:

            return None

        if self.last_mask is None:

            self.segment()

        result = image.copy()

        result.putalpha(
            self.last_mask
        )

        self.layer_manager.add_layer(

            "Personaje",

            result

        )

        return result



    # ==========================================================
    # INPAINT
    # ==========================================================

    def inpaint(self):

        image = self.get_image()

        if image is None:

            return None

        if self.last_mask is None:

            return None

        result = self.inpainter.process(

            image,

            self.last_mask

        )

        return self._update_image(

            result,

            "inpaint"

        )



    # ==========================================================
    # REINICIAR
    # ==========================================================

    def reset(self):

        self.history.clear()

        self.layer_manager.clear()

        self.image_manager.clear()

        self.last_result = None

        self.last_mask = None

        self.last_detection = None

        self.last_pipeline.clear()



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_info(self):

        return {

            "image": self.image_manager.get_info(),

            "layers": self.layer_manager.count(),

            "history": self.history.count(),

            "operations": deepcopy(
                self.last_pipeline
            ),

            "has_mask": self.last_mask is not None,

            "has_detection": self.last_detection is not None

        }