from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStatusBar,
    QFileDialog,
    QMessageBox,
    QFrame
)

from PySide6.QtGui import QAction

from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    APP_NAME,
    APP_VERSION
)


from ui.image_view import ImageView
from ui.toolbar import MainToolbar
from ui.layer_panel import LayerPanel
from ui.properties_panel import PropertiesPanel


from image.remove_background import BackgroundRemover
from image.cleanup import ImageCleaner
from image.upscale import ImageUpscaler
from image.inpainting import ImageInpainter
from image.color import ColorProcessor



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            f"{APP_NAME} v{APP_VERSION}"
        )


        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )


        self.image_path = None

        self.current_image = None



        # ======================================================
        # MOTORES
        # ======================================================


        self.background_remover = BackgroundRemover()

        self.image_cleaner = ImageCleaner()

        self.image_upscaler = ImageUpscaler()

        self.image_inpainter = ImageInpainter()

        self.color_processor = ColorProcessor()



        # ======================================================
        # INTERFAZ
        # ======================================================


        self._create_menu()

        self._create_toolbar()

        self._create_statusbar()

        self._create_layout()



    # ==========================================================
    # MENU
    # ==========================================================

    def _create_menu(self):


        menubar = self.menuBar()



        file_menu = menubar.addMenu(
            "Archivo"
        )


        open_action = QAction(
            "Abrir imagen",
            self
        )


        open_action.triggered.connect(
            self.open_image
        )


        file_menu.addAction(
            open_action
        )



        save_action = QAction(
            "Guardar",
            self
        )


        save_action.triggered.connect(
            self.save_image
        )


        file_menu.addAction(
            save_action
        )



        exit_action = QAction(
            "Salir",
            self
        )


        exit_action.triggered.connect(
            self.close
        )


        file_menu.addAction(
            exit_action
        )



        ia_menu = menubar.addMenu(
            "IA"
        )


        segment_action = QAction(
            "Segmentar",
            self
        )


        ia_menu.addAction(
            segment_action
        )



        export_menu = menubar.addMenu(
            "Exportar"
        )


        export_action = QAction(
            "Exportar imagen",
            self
        )


        export_action.triggered.connect(
            self.export_image
        )


        export_menu.addAction(
            export_action
        )



        help_menu = menubar.addMenu(
            "Ayuda"
        )


        about_action = QAction(
            "Acerca de",
            self
        )


        about_action.triggered.connect(
            self.show_about
        )


        help_menu.addAction(
            about_action
        )



    # ==========================================================
    # TOOLBAR
    # ==========================================================

    def _create_toolbar(self):


        self.toolbar = MainToolbar(
            self
        )


        self.addToolBar(
            self.toolbar
        )



        self.toolbar.open_action.triggered.connect(
            self.open_image
        )


        self.toolbar.save_action.triggered.connect(
            self.save_image
        )


        self.toolbar.clean_action.triggered.connect(
            self.clean_image
        )


        self.toolbar.enhance_action.triggered.connect(
            self.enhance_image
        )


        self.toolbar.upscale_action.triggered.connect(
            self.upscale_image
        )


        self.toolbar.color_action.triggered.connect(
            self.process_color
        )


        self.toolbar.remove_background_action.triggered.connect(
            self.remove_background
        )



    # ==========================================================
    # STATUS
    # ==========================================================

    def _create_statusbar(self):


        status = QStatusBar()


        status.showMessage(
            "Esperando imagen..."
        )


        self.setStatusBar(
            status
        )



    # ==========================================================
    # LAYOUT
    # ==========================================================

    def _create_layout(self):


        central = QWidget()


        self.setCentralWidget(
            central
        )


        layout = QHBoxLayout(
            central
        )



        left = QFrame()


        left.setFixedWidth(
            220
        )


        left_layout = QVBoxLayout(
            left
        )


        self.layer_panel = LayerPanel()


        left_layout.addWidget(
            self.layer_panel
        )



        center = QFrame()


        center_layout = QVBoxLayout(
            center
        )


        self.image_view = ImageView()


        center_layout.addWidget(
            self.image_view
        )



        self.properties_panel = PropertiesPanel()



        layout.addWidget(
            left
        )


        layout.addWidget(
            center,
            1
        )


        layout.addWidget(
            self.properties_panel
        )



    # ==========================================================
    # ABRIR
    # ==========================================================

    def open_image(self):


        path, _ = QFileDialog.getOpenFileName(

            self,

            "Abrir imagen",

            "",

            "Imagen (*.png *.jpg *.jpeg *.webp)"

        )


        if not path:

            return



        if not self.image_view.load_image(path):

            QMessageBox.warning(
                self,
                "Error",
                "No se pudo cargar la imagen"
            )

            return



        self.image_path = path


        self.current_image = (
            self.image_view.original_pixmap
        )



        self.layer_panel.clear_layers()


        self.layer_panel.add_layer(
            "Imagen original"
        )



        info = self.image_view.get_image_info()


        info["name"] = path.split("/")[-1]


        self.properties_panel.update_properties(
            info
        )


        self.statusBar().showMessage(
            "Imagen cargada"
        )



    # ==========================================================
    # PROCESOS
    # ==========================================================

    def clean_image(self):


        self.statusBar().showMessage(
            "Limpiando imagen..."
        )



    def enhance_image(self):


        self.statusBar().showMessage(
            "Mejorando imagen..."
        )



    def upscale_image(self):


        self.statusBar().showMessage(
            "Escalando imagen..."
        )



    def process_color(self):


        self.statusBar().showMessage(
            "Procesando color..."
        )



    def remove_background(self):


        self.statusBar().showMessage(
            "Eliminando fondo..."
        )



    # ==========================================================
    # GUARDAR / EXPORTAR
    # ==========================================================

    def save_image(self):

        self.export_image()



    def export_image(self):


        path, _ = QFileDialog.getSaveFileName(

            self,

            "Guardar imagen",

            "",

            "PNG (*.png)"

        )


        if not path:

            return



        QMessageBox.information(

            self,

            "Exportar",

            "Exportación preparada"

        )



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def show_about(self):


        QMessageBox.information(

            self,

            "JHASMIN Art Tools",

            f"{APP_NAME} v{APP_VERSION}\n\n"
            "Editor visual preparado para IA."

        )