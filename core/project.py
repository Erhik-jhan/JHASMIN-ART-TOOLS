from copy import deepcopy
from datetime import datetime
from pathlib import Path
from uuid import uuid4



class ProjectManager:


    def __init__(self):

        self.reset()



    # ==========================================================
    # CREAR PROYECTO
    # ==========================================================

    def create(
        self,
        name="Nuevo Proyecto"
    ):

        self.reset()

        self.project_id = str(
            uuid4()
        )

        self.project_name = name

        self.created_at = datetime.now()

        self.modified_at = self.created_at

        self.is_open = True

        self.is_modified = False

        self.last_operation = "create"

        return self.get_project()



    # ==========================================================
    # REINICIAR
    # ==========================================================

    def reset(self):

        self.project_id = None

        self.project_name = "Sin nombre"

        self.project_path = None

        self.project_directory = None

        self.project_version = "1.0"

        self.created_at = None

        self.modified_at = None

        self.is_open = False

        self.is_modified = False

        self.last_operation = None

        self.original_image = None

        self.current_image = None

        self.preview_image = None

        self.layers = []

        self.masks = {}

        self.objects = {}

        self.segmentations = {}

        self.animations = {}

        self.rig = {}

        self.physics = {}

        self.pipeline = None

        self.history = None

        self.image_manager = None

        self.layer_manager = None

        self.metadata = {}

        self.settings = {}

        self.tags = []

        self.notes = ""

        self.exports = []

        self.statistics = {}



    # ==========================================================
    # ABRIR PROYECTO
    # ==========================================================

    def open_project(
        self,
        path
    ):

        path = Path(
            path
        )

        self.project_path = path

        self.project_directory = path.parent

        self.is_open = True

        self.modified_at = datetime.now()

        self.last_operation = "open_project"



    # ==========================================================
    # GUARDAR
    # ==========================================================

    def save_project(self):

        self.is_modified = False

        self.modified_at = datetime.now()

        self.last_operation = "save_project"



    # ==========================================================
    # CERRAR
    # ==========================================================

    def close_project(self):

        self.reset()

        self.last_operation = "close_project"



    # ==========================================================
    # IMÁGENES
    # ==========================================================

    def set_original_image(
        self,
        image
    ):

        self.original_image = image

        self.last_operation = "set_original_image"



    def set_current_image(
        self,
        image
    ):

        self.current_image = image

        self.modified()

        self.last_operation = "set_current_image"



    def set_preview_image(
        self,
        image
    ):

        self.preview_image = image

        self.last_operation = "set_preview_image"



    # ==========================================================
    # CAPAS
    # ==========================================================

    def add_layer(
        self,
        layer
    ):

        self.layers.append(
            layer
        )

        self.modified()

        self.last_operation = "add_layer"



    def remove_layer(
        self,
        layer
    ):

        if layer in self.layers:

            self.layers.remove(
                layer
            )

            self.modified()

            self.last_operation = (
                "remove_layer"
            )



    def clear_layers(self):

        self.layers.clear()

        self.modified()

        self.last_operation = (
            "clear_layers"
        )



    # ==========================================================
    # MÁSCARAS
    # ==========================================================

    def set_mask(
        self,
        name,
        mask
    ):

        self.masks[name] = mask

        self.modified()

        self.last_operation = "set_mask"



    def get_mask(
        self,
        name
    ):

        return self.masks.get(
            name
        )



    # ==========================================================
    # SEGMENTACIONES
    # ==========================================================

    def add_segmentation(
        self,
        name,
        data
    ):

        self.segmentations[name] = data

        self.modified()

        self.last_operation = (
            "add_segmentation"
        )



    # ==========================================================
    # OBJETOS
    # ==========================================================

    def add_object(
        self,
        name,
        data
    ):

        self.objects[name] = data

        self.modified()

        self.last_operation = (
            "add_object"
        )



    # ==========================================================
    # EXPORTACIONES
    # ==========================================================

    def register_export(
        self,
        export_data
    ):

        self.exports.append(
            export_data
        )

        self.last_operation = (
            "register_export"
        )



    # ==========================================================
    # METADATA
    # ==========================================================

    def set_metadata(
        self,
        key,
        value
    ):

        self.metadata[key] = value

        self.last_operation = (
            "set_metadata"
        )



    def get_metadata(
        self,
        key,
        default=None
    ):

        return self.metadata.get(
            key,
            default
        )



    # ==========================================================
    # CONFIGURACIÓN
    # ==========================================================

    def set_setting(
        self,
        key,
        value
    ):

        self.settings[key] = value

        self.last_operation = (
            "set_setting"
        )



    def get_setting(
        self,
        key,
        default=None
    ):

        return self.settings.get(
            key,
            default
        )



    # ==========================================================
    # CONEXIONES
    # ==========================================================

    def connect_pipeline(
        self,
        pipeline
    ):

        self.pipeline = pipeline

        self.last_operation = (
            "connect_pipeline"
        )



    def connect_history(
        self,
        history
    ):

        self.history = history

        self.last_operation = (
            "connect_history"
        )



    def connect_image_manager(
        self,
        manager
    ):

        self.image_manager = manager

        self.last_operation = (
            "connect_image_manager"
        )



    def connect_layer_manager(
        self,
        manager
    ):

        self.layer_manager = manager

        self.last_operation = (
            "connect_layer_manager"
        )



    # ==========================================================
    # ESTADO
    # ==========================================================

    def modified(self):

        self.is_modified = True

        self.modified_at = datetime.now()



    # ==========================================================
    # SERIALIZACIÓN
    # ==========================================================

    def to_dict(self):

        return {

            "project_id": self.project_id,

            "project_name": self.project_name,

            "project_version": self.project_version,

            "project_path": str(
                self.project_path
            )
            if self.project_path
            else None,

            "created_at": str(
                self.created_at
            )
            if self.created_at
            else None,

            "modified_at": str(
                self.modified_at
            )
            if self.modified_at
            else None,

            "metadata": deepcopy(
                self.metadata
            ),

            "settings": deepcopy(
                self.settings
            ),

            "tags": deepcopy(
                self.tags
            ),

            "notes": self.notes,

            "exports": deepcopy(
                self.exports
            )

        }



    def load_dict(
        self,
        data
    ):

        self.project_id = data.get(
            "project_id"
        )

        self.project_name = data.get(
            "project_name",
            "Proyecto"
        )

        self.project_version = data.get(
            "project_version",
            "1.0"
        )

        self.metadata = deepcopy(
            data.get(
                "metadata",
                {}
            )
        )

        self.settings = deepcopy(
            data.get(
                "settings",
                {}
            )
        )

        self.tags = deepcopy(
            data.get(
                "tags",
                []
            )
        )

        self.notes = data.get(
            "notes",
            ""
        )

        self.exports = deepcopy(
            data.get(
                "exports",
                []
            )
        )

        self.last_operation = "load_dict"



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_project(self):

        return {

            "id": self.project_id,

            "name": self.project_name,

            "version": self.project_version,

            "opened": self.is_open,

            "modified": self.is_modified,

            "layers": len(
                self.layers
            ),

            "masks": len(
                self.masks
            ),

            "objects": len(
                self.objects
            ),

            "segmentations": len(
                self.segmentations
            ),

            "exports": len(
                self.exports
            ),

            "last_operation": self.last_operation

        }