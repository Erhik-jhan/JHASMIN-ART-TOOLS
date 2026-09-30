import sys


from PySide6.QtWidgets import QApplication


from config import (
    create_directories,
    APP_NAME,
    APP_VERSION
)


from ui.main_window import MainWindow



# ==========================================================
# INICIALIZACIÓN
# ==========================================================

def initialize():

    create_directories()



# ==========================================================
# APLICACIÓN PRINCIPAL
# ==========================================================

def main():


    initialize()


    app = QApplication(
        sys.argv
    )


    app.setApplicationName(
        APP_NAME
    )


    app.setApplicationVersion(
        APP_VERSION
    )


    window = MainWindow()


    window.show()



    sys.exit(

        app.exec()

    )



# ==========================================================
# EJECUCIÓN
# ==========================================================

if __name__ == "__main__":

    main()