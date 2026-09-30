from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

from image.image_manager import ImageManager


class ImageView(QLabel):

    def __init__(self, image_manager: ImageManager):

        super().__init__()

        self.image_manager = image_manager

        self.zoom = 1.0

        self.setAlignment(Qt.AlignCenter)

        self.setMinimumSize(400, 400)

        self.setMouseTracking(True)

        self.setText("No hay imagen cargada")

        self.setStyleSheet("""
            QLabel {
                background-color: #1e1e1e;
                color: #aaaaaa;
                border: 2px dashed #444444;
                font-size:16px;
            }
        """)

    # ==========================================================
    # CARGAR IMAGEN
    # ==========================================================

    def load_image(self, file_path):

        loaded = self.image_manager.load_image(file_path)

        if not loaded:
            return False

        self.zoom = 1.0

        self.update_image()

        return True

    # ==========================================================
    # ACTUALIZAR VISTA
    # ==========================================================

    def update_image(self):

        if not self.image_manager.has_image():

            self.clear()

            self.setText("No hay imagen cargada")

            return

        pixmap = self.image_manager.to_qpixmap()

        if pixmap is None:
            return

        width = int(self.width() * self.zoom)
        height = int(self.height() * self.zoom)

        scaled = pixmap.scaled(
            width,
            height,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(scaled)

    # ==========================================================
    # ZOOM
    # ==========================================================

    def zoom_in(self):

        self.zoom += 0.10

        if self.zoom > 8.0:
            self.zoom = 8.0

        self.update_image()

    def zoom_out(self):

        self.zoom -= 0.10

        if self.zoom < 0.10:
            self.zoom = 0.10

        self.update_image()

    def reset_zoom(self):

        self.zoom = 1.0

        self.update_image()

    def get_zoom(self):

        return self.zoom

    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_image_info(self):

        return self.image_manager.get_info()

    # ==========================================================
    # LIMPIAR
    # ==========================================================

    def clear_image(self):

        self.image_manager.clear()

        self.zoom = 1.0

        self.clear()

        self.setText("No hay imagen cargada")

    # ==========================================================
    # REFRESCAR
    # ==========================================================

    def refresh(self):

        self.update_image()

    # ==========================================================
    # FUTURAS CAPAS
    # ==========================================================

    def show_mask(self, mask):

        """
        Aquí se dibujarán las máscaras generadas
        por Segment Anything.
        """
        pass

    def show_layers(self, layers):

        """
        Aquí se mostrarán las capas separadas
        del personaje.
        """
        pass

    def show_selection(self, polygon):

        """
        Dibujará la selección del usuario.
        """
        pass

    # ==========================================================
    # EVENTOS
    # ==========================================================

    def resizeEvent(self, event):

        self.update_image()

        super().resizeEvent(event)

    def wheelEvent(self, event):

        if event.angleDelta().y() > 0:

            self.zoom_in()

        else:

            self.zoom_out()