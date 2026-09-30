from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QHBoxLayout,
    QListWidgetItem
)

from PySide6.QtCore import Qt



class LayerPanel(QWidget):


    def __init__(
        self,
        parent=None
    ):

        super().__init__(
            parent
        )


        self.layers = []

        self.layer_data = []

        self.active_layer = None


        self._create_ui()



    # ==========================================================
    # INTERFAZ
    # ==========================================================

    def _create_ui(
        self
    ):


        layout = QVBoxLayout(
            self
        )



        title = QLabel(
            "Capas"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            title
        )



        self.layer_list = QListWidget()


        self.layer_list.setSelectionMode(
            QListWidget.SingleSelection
        )


        self.layer_list.currentRowChanged.connect(
            self.change_active_layer
        )


        layout.addWidget(
            self.layer_list
        )



        buttons_layout = QHBoxLayout()



        self.add_button = QPushButton(
            "+"
        )


        self.remove_button = QPushButton(
            "-"
        )


        self.up_button = QPushButton(
            "↑"
        )


        self.down_button = QPushButton(
            "↓"
        )



        buttons_layout.addWidget(
            self.add_button
        )


        buttons_layout.addWidget(
            self.remove_button
        )


        buttons_layout.addWidget(
            self.up_button
        )


        buttons_layout.addWidget(
            self.down_button
        )



        layout.addLayout(
            buttons_layout
        )



        self.add_button.clicked.connect(
            self.create_empty_layer
        )


        self.remove_button.clicked.connect(
            self.remove_selected_layer
        )


        self.up_button.clicked.connect(
            self.move_layer_up
        )


        self.down_button.clicked.connect(
            self.move_layer_down
        )



    # ==========================================================
    # AGREGAR CAPA
    # ==========================================================

    def add_layer(
        self,
        name,
        data=None
    ):


        if name in self.layers:

            return



        self.layers.append(
            name
        )


        self.layer_data.append(

            {

                "name": name,

                "visible": True,

                "locked": False,

                "data": data

            }

        )


        item = QListWidgetItem(
            name
        )


        self.layer_list.addItem(
            item
        )



    # ==========================================================
    # CREAR CAPA VACÍA
    # ==========================================================

    def create_empty_layer(
        self
    ):


        number = len(
            self.layers
        ) + 1



        self.add_layer(

            f"Capa {number}"

        )



    # ==========================================================
    # ELIMINAR CAPA
    # ==========================================================

    def remove_selected_layer(
        self
    ):


        current = self.layer_list.currentRow()


        if current < 0:

            return



        self.layer_list.takeItem(
            current
        )


        self.layers.pop(
            current
        )


        self.layer_data.pop(
            current
        )


        self.active_layer = None



    # ==========================================================
    # CAMBIAR CAPA ACTIVA
    # ==========================================================

    def change_active_layer(
        self,
        index
    ):


        if index < 0:

            self.active_layer = None

            return



        self.active_layer = (

            self.layers[index]

        )



    # ==========================================================
    # MOVER CAPA ARRIBA
    # ==========================================================

    def move_layer_up(
        self
    ):


        row = self.layer_list.currentRow()


        if row <= 0:

            return



        self.layers[row], self.layers[row-1] = (

            self.layers[row-1],

            self.layers[row]

        )


        self.layer_data[row], self.layer_data[row-1] = (

            self.layer_data[row-1],

            self.layer_data[row]

        )


        item = self.layer_list.takeItem(
            row
        )


        self.layer_list.insertItem(
            row-1,
            item
        )


        self.layer_list.setCurrentRow(
            row-1
        )



    # ==========================================================
    # MOVER CAPA ABAJO
    # ==========================================================

    def move_layer_down(
        self
    ):


        row = self.layer_list.currentRow()


        if row < 0 or row >= len(self.layers)-1:

            return



        self.layers[row], self.layers[row+1] = (

            self.layers[row+1],

            self.layers[row]

        )


        self.layer_data[row], self.layer_data[row+1] = (

            self.layer_data[row+1],

            self.layer_data[row]

        )


        item = self.layer_list.takeItem(
            row
        )


        self.layer_list.insertItem(
            row+1,
            item
        )


        self.layer_list.setCurrentRow(
            row+1
        )



    # ==========================================================
    # LIMPIAR
    # ==========================================================

    def clear_layers(
        self
    ):


        self.layers.clear()

        self.layer_data.clear()

        self.active_layer = None


        self.layer_list.clear()



    # ==========================================================
    # OBTENER CAPA ACTIVA
    ==========================================================

    def get_selected_layer(
        self
    ):


        item = self.layer_list.currentItem()


        if item is None:

            return None



        return item.text()



    # ==========================================================
    # OBTENER DATOS
    ==========================================================

    def get_layers(
        self
    ):

        return self.layer_data