from PySide6.QtWidgets import (
    QMessageBox,
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QProgressBar
)

from PySide6.QtCore import Qt



class MessageDialog:


    @staticmethod
    def info(
        parent,
        title,
        message
    ):

        QMessageBox.information(
            parent,
            title,
            message
        )



    @staticmethod
    def warning(
        parent,
        title,
        message
    ):

        QMessageBox.warning(
            parent,
            title,
            message
        )



    @staticmethod
    def error(
        parent,
        title,
        message
    ):

        QMessageBox.critical(
            parent,
            title,
            message
        )



    @staticmethod
    def confirm(
        parent,
        title,
        message
    ):


        result = QMessageBox.question(
            parent,
            title,
            message,
            QMessageBox.Yes |
            QMessageBox.No
        )


        return result == QMessageBox.Yes





class ProcessingDialog(QDialog):


    def __init__(
        self,
        title="Procesando...",
        parent=None
    ):

        super().__init__(
            parent
        )


        self.setWindowTitle(
            title
        )


        self.setFixedSize(
            400,
            150
        )


        self._create_ui()



    def _create_ui(self):


        layout = QVBoxLayout(
            self
        )


        self.label = QLabel(
            "Trabajando..."
        )


        self.label.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            self.label
        )



        self.progress = QProgressBar()


        self.progress.setRange(
            0,
            0
        )


        layout.addWidget(
            self.progress
        )



        self.cancel_button = QPushButton(
            "Cancelar"
        )


        self.cancel_button.clicked.connect(
            self.close
        )


        layout.addWidget(
            self.cancel_button
        )



    def set_message(
        self,
        text
    ):

        self.label.setText(
            text
        )