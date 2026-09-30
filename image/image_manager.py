from pathlib import Path

from PIL import Image

import numpy as np

from PySide6.QtGui import (
    QImage,
    QPixmap
)



class ImageManager:


    def __init__(self):

        self.original_image = None

        self.current_image = None

        self.image_path = None

        self.image_name = None



    # -----------------------------
    # CARGA
    # -----------------------------

    def load_image(self, file_path):

        file_path = Path(file_path)

        image = Image.open(file_path).convert("RGBA")

        self.original_image = image.copy()

        self.current_image = image.copy()

        self.image_path = file_path

        self.image_name = file_path.name

        return True



    # -----------------------------
    # INFORMACIÓN
    # -----------------------------

    def get_info(self):

        if self.current_image is None:

            return {}


        width, height = self.current_image.size


        return {

            "name": self.image_name,

            "path": str(self.image_path),

            "width": width,

            "height": height,

            "size": f"{width} x {height}",

            "mode": self.current_image.mode

        }



    # -----------------------------
    # IMAGEN ACTUAL
    # -----------------------------

    def get_current_image(self):

        return self.current_image



    def set_current_image(self, image):

        self.current_image = image.copy()



    # -----------------------------
    # ORIGINAL
    # -----------------------------

    def get_original_image(self):

        return self.original_image



    def restore_original(self):

        if self.original_image is None:

            return


        self.current_image = self.original_image.copy()



    # -----------------------------
    # CONVERSIONES
    # -----------------------------

    def to_numpy(self):

        if self.current_image is None:

            return None


        return np.array(self.current_image)



    def from_numpy(self, array):

        self.current_image = Image.fromarray(array)



    def to_qimage(self):

        if self.current_image is None:

            return None


        image = self.current_image.convert("RGBA")


        data = image.tobytes("raw", "RGBA")


        qimage = QImage(

            data,

            image.width,

            image.height,

            QImage.Format_RGBA8888

        )


        return qimage.copy()



    def to_qpixmap(self):

        qimage = self.to_qimage()

        if qimage is None:

            return None

        return QPixmap.fromImage(qimage)



    # -----------------------------
    # GUARDAR
    # -----------------------------

    def save(self, file_path):

        if self.current_image is None:

            return False


        self.current_image.save(file_path)

        return True



    # -----------------------------
    # ESTADO
    # -----------------------------

    def has_image(self):

        return self.current_image is not None



    def clear(self):

        self.original_image = None

        self.current_image = None

        self.image_path = None

        self.image_name = None