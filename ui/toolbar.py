from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize



class MainToolbar(QToolBar):


    def __init__(
        self,
        parent=None
    ):

        super().__init__(
            "Herramientas",
            parent
        )


        self.setMovable(
            False
        )


        self.setIconSize(
            QSize(
                24,
                24
            )
        )


        self._create_actions()



    # ==========================================================
    # CREACIÓN DE ACCIONES
    # ==========================================================

    def _create_actions(
        self
    ):



        # ======================================================
        # ARCHIVO
        # ======================================================


        self.open_action = QAction(
            "Abrir",
            self
        )


        self.open_action.setToolTip(
            "Abrir una imagen"
        )


        self.addAction(
            self.open_action
        )



        self.save_action = QAction(
            "Guardar",
            self
        )


        self.save_action.setToolTip(
            "Guardar imagen actual"
        )


        self.addAction(
            self.save_action
        )



        self.addSeparator()



        # ======================================================
        # LIMPIEZA Y MEJORA
        # ======================================================


        self.clean_action = QAction(
            "Limpiar",
            self
        )


        self.clean_action.setToolTip(
            "Eliminar ruido y mejorar imagen"
        )


        self.addAction(
            self.clean_action
        )



        self.enhance_action = QAction(
            "Mejorar",
            self
        )


        self.enhance_action.setToolTip(
            "Aplicar mejora automática"
        )


        self.addAction(
            self.enhance_action
        )



        self.addSeparator()



        # ======================================================
        # ESCALADO
        # ======================================================


        self.upscale_action = QAction(
            "Escalar",
            self
        )


        self.upscale_action.setToolTip(
            "Aumentar resolución de imagen"
        )


        self.addAction(
            self.upscale_action
        )



        self.addSeparator()



        # ======================================================
        # COLOR
        # ======================================================


        self.color_action = QAction(
            "Color",
            self
        )


        self.color_action.setToolTip(
            "Corrección y procesamiento de color"
        )


        self.addAction(
            self.color_action
        )



        self.addSeparator()



        # ======================================================
        # SEGMENTACIÓN IA
        # ======================================================


        self.segment_action = QAction(
            "Segmentar",
            self
        )


        self.segment_action.setToolTip(
            "Separar elementos mediante IA"
        )


        self.addAction(
            self.segment_action
        )



        self.remove_background_action = QAction(
            "Fondo",
            self
        )


        self.remove_background_action.setToolTip(
            "Eliminar fondo de imagen"
        )


        self.addAction(
            self.remove_background_action
        )



        self.mask_action = QAction(
            "Máscara",
            self
        )


        self.mask_action.setToolTip(
            "Crear y editar máscaras"
        )


        self.addAction(
            self.mask_action
        )



        self.addSeparator()



        # ======================================================
        # RECONSTRUCCIÓN
        # ======================================================


        self.inpaint_action = QAction(
            "Rellenar",
            self
        )


        self.inpaint_action.setToolTip(
            "Reconstrucción inteligente de zonas"
        )


        self.addAction(
            self.inpaint_action
        )



        self.addSeparator()



        # ======================================================
        # IA
        # ======================================================


        self.ai_action = QAction(
            "IA",
            self
        )


        self.ai_action.setToolTip(
            "Herramientas de inteligencia artificial"
        )


        self.addAction(
            self.ai_action
        )



        self.addSeparator()



        # ======================================================
        # EXPORTACIÓN
        # ======================================================


        self.export_action = QAction(
            "Exportar",
            self
        )


        self.export_action.setToolTip(
            "Exportar resultado final"
        )


        self.addAction(
            self.export_action
        )



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_actions(
        self
    ):

        return {


            "open":

            self.open_action,


            "save":

            self.save_action,


            "clean":

            self.clean_action,


            "enhance":

            self.enhance_action,


            "upscale":

            self.upscale_action,


            "color":

            self.color_action,


            "segment":

            self.segment_action,


            "background":

            self.remove_background_action,


            "mask":

            self.mask_action,


            "inpaint":

            self.inpaint_action,


            "ai":

            self.ai_action,


            "export":

            self.export_action

        }