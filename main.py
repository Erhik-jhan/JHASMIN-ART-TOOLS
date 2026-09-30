import sys


from PySide6.QtWidgets import QApplication


from config import (
    APP_NAME,
    create_directories
)


from ui.main_window import MainWindow



# ==========================================================
# INICIO DE APLICACIÓN
# ==========================================================

def main():


    create_directories()



    app = QApplication(
        sys.argv
    )


    app.setApplicationName(
        APP_NAME
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