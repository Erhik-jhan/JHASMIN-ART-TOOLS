from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFormLayout,
    QFrame,
    QScrollArea
)

from PySide6.QtCore import Qt



class PropertiesPanel(QWidget):


    def __init__(
        self,
        parent=None
    ):

        super().__init__(
            parent
        )


        self.properties = {}


        self.sections = {}


        self.setFixedWidth(
            280
        )


        self._create_ui()



    # ==========================================================
    # CREAR INTERFAZ
    # ==========================================================

    def _create_ui(
        self
    ):


        main_layout = QVBoxLayout(
            self
        )



        title = QLabel(
            "Propiedades"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        main_layout.addWidget(
            title
        )



        separator = QFrame()


        separator.setFrameShape(
            QFrame.HLine
        )


        main_layout.addWidget(
            separator
        )



        self.form_layout = QFormLayout()


        scroll = QScrollArea()


        container = QWidget()


        container.setLayout(
            self.form_layout
        )


        scroll.setWidget(
            container
        )


        scroll.setWidgetResizable(
            True
        )


        main_layout.addWidget(
            scroll
        )


        main_layout.addStretch()



    # ==========================================================
    # ACTUALIZAR PROPIEDADES
    # ==========================================================

    def update_properties(
        self,
        data
    ):


        self.properties = data.copy()


        self.clear_properties()



        for key, value in data.items():


            self._add_property(
                key,
                value
            )



    # ==========================================================
    # AGREGAR PROPIEDAD
    # ==========================================================

    def _add_property(
        self,
        key,
        value
    ):


        label_key = QLabel(

            str(key).capitalize()

        )


        label_value = QLabel(

            str(value)

        )


        label_value.setWordWrap(
            True
        )


        self.form_layout.addRow(

            label_key,

            label_value

        )



    # ==========================================================
    # ACTUALIZAR UNA SOLA PROPIEDAD
    # ==========================================================

    def set_property(
        self,
        name,
        value
    ):


        self.properties[name] = value


        self.update_properties(
            self.properties
        )



    # ==========================================================
    # INFORMACIÓN DE IMAGEN
    # ==========================================================

    def update_image_info(
        self,
        image
    ):


        if image is None:

            return



        data = {


            "width":

            image.width,


            "height":

            image.height,


            "mode":

            image.mode



        }


        self.update_properties(
            data
        )



    # ==========================================================
    # INFORMACIÓN DE CAPA
    # ==========================================================

    def update_layer_info(
        self,
        layer
    ):


        if layer is None:

            return



        self.update_properties(
            layer
        )



    # ==========================================================
    # INFORMACIÓN IA
    # ==========================================================

    def update_ai_status(
        self,
        status
    ):


        self.set_property(

            "IA",

            status

        )



    # ==========================================================
    # LIMPIAR
    # ==========================================================

    def clear_properties(
        self
    ):


        while self.form_layout.rowCount():

            self.form_layout.removeRow(
                0
            )



    # ==========================================================
    # OBTENER PROPIEDAD
    # ==========================================================

    def get_property(
        self,
        name
    ):


        return self.properties.get(

            name,

            None

        )



    # ==========================================================
    # OBTENER TODO
    # ==========================================================

    def get_all_properties(
        self
    ):


        return self.properties