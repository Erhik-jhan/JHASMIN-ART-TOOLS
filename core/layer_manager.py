from copy import deepcopy
from uuid import uuid4



class LayerManager:


    def __init__(self):

        self.layers = []

        self.selected_layer = None

        self.active_layer = None

        self.last_operation = None



    # ==========================================================
    # CREAR CAPA
    # ==========================================================

    def create_layer(
        self,
        name,
        image=None,
        mask=None,
        layer_type="image"
    ):

        layer = {

            "id": str(
                uuid4()
            ),

            "name": name,

            "type": layer_type,

            "image": image,

            "mask": mask,

            "visible": True,

            "locked": False,

            "opacity": 1.0,

            "blend_mode": "normal",

            "selected": False,

            "metadata": {},

            "children": []

        }


        self.layers.append(
            layer
        )


        if self.selected_layer is None:

            self.select_layer(
                layer["id"]
            )


        self.last_operation = (
            "create_layer"
        )


        return layer



    # ==========================================================
    # DUPLICAR CAPA
    # ==========================================================

    def duplicate_layer(
        self,
        layer_id
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer is None:

            return None


        copy_layer = deepcopy(
            layer
        )

        copy_layer["id"] = str(
            uuid4()
        )

        copy_layer["name"] += " Copy"

        copy_layer["selected"] = False


        self.layers.append(
            copy_layer
        )


        self.last_operation = (
            "duplicate_layer"
        )


        return copy_layer



    # ==========================================================
    # ELIMINAR CAPA
    # ==========================================================

    def remove_layer(
        self,
        layer_id
    ):

        for index, layer in enumerate(
            self.layers
        ):

            if layer["id"] == layer_id:

                self.layers.pop(
                    index
                )

                if self.selected_layer == layer_id:

                    self.selected_layer = None

                    self.active_layer = None

                self.last_operation = (
                    "remove_layer"
                )

                return True

        return False



    # ==========================================================
    # RENOMBRAR
    # ==========================================================

    def rename_layer(
        self,
        layer_id,
        new_name
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer is None:

            return False


        layer["name"] = new_name

        self.last_operation = (
            "rename_layer"
        )

        return True



    # ==========================================================
    # SELECCIONAR
    # ==========================================================

    def select_layer(
        self,
        layer_id
    ):

        found = None

        for layer in self.layers:

            layer["selected"] = False

            if layer["id"] == layer_id:

                found = layer


        if found is None:

            return False


        found["selected"] = True

        self.selected_layer = layer_id

        self.active_layer = found

        self.last_operation = (
            "select_layer"
        )

        return True



    # ==========================================================
    # VISIBILIDAD
    # ==========================================================

    def show_layer(
        self,
        layer_id
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["visible"] = True

            self.last_operation = (
                "show_layer"
            )



    def hide_layer(
        self,
        layer_id
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["visible"] = False

            self.last_operation = (
                "hide_layer"
            )



    def toggle_visibility(
        self,
        layer_id
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["visible"] = not layer["visible"]

            self.last_operation = (
                "toggle_visibility"
            )



    # ==========================================================
    # BLOQUEO
    # ==========================================================

    def lock_layer(
        self,
        layer_id
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["locked"] = True

            self.last_operation = (
                "lock_layer"
            )



    def unlock_layer(
        self,
        layer_id
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["locked"] = False

            self.last_operation = (
                "unlock_layer"
            )



    # ==========================================================
    # OPACIDAD
    # ==========================================================

    def set_opacity(
        self,
        layer_id,
        opacity
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer is None:

            return


        opacity = max(
            0.0,
            min(
                1.0,
                opacity
            )
        )

        layer["opacity"] = opacity

        self.last_operation = (
            "set_opacity"
        )



    # ==========================================================
    # MODO DE MEZCLA
    # ==========================================================

    def set_blend_mode(
        self,
        layer_id,
        mode
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["blend_mode"] = mode

            self.last_operation = (
                "set_blend_mode"
            )



    # ==========================================================
    # MÁSCARA
    # ==========================================================

    def set_mask(
        self,
        layer_id,
        mask
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["mask"] = mask

            self.last_operation = (
                "set_mask"
            )



    # ==========================================================
    # IMAGEN
    # ==========================================================

    def set_image(
        self,
        layer_id,
        image
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["image"] = image

            self.last_operation = (
                "set_image"
            )



    # ==========================================================
    # METADATA
    # ==========================================================

    def set_metadata(
        self,
        layer_id,
        key,
        value
    ):

        layer = self.get_layer(
            layer_id
        )

        if layer:

            layer["metadata"][key] = value

            self.last_operation = (
                "set_metadata"
            )



    # ==========================================================
    # ORDEN
    # ==========================================================

    def move_up(
        self,
        layer_id
    ):

        index = self.get_layer_index(
            layer_id
        )

        if index is None:

            return

        if index >= len(
            self.layers
        ) - 1:

            return

        self.layers[index], self.layers[index + 1] = (

            self.layers[index + 1],

            self.layers[index]

        )

        self.last_operation = (
            "move_up"
        )



    def move_down(
        self,
        layer_id
    ):

        index = self.get_layer_index(
            layer_id
        )

        if index is None:

            return

        if index == 0:

            return

        self.layers[index], self.layers[index - 1] = (

            self.layers[index - 1],

            self.layers[index]

        )

        self.last_operation = (
            "move_down"
        )



    # ==========================================================
    # BÚSQUEDA
    # ==========================================================

    def get_layer(
        self,
        layer_id
    ):

        for layer in self.layers:

            if layer["id"] == layer_id:

                return layer

        return None



    def get_layer_index(
        self,
        layer_id
    ):

        for index, layer in enumerate(
            self.layers
        ):

            if layer["id"] == layer_id:

                return index

        return None



    def get_layer_by_name(
        self,
        name
    ):

        for layer in self.layers:

            if layer["name"] == name:

                return layer

        return None



    # ==========================================================
    # LISTADOS
    # ==========================================================

    def get_layers(self):

        return self.layers



    def get_visible_layers(self):

        return [

            layer

            for layer in self.layers

            if layer["visible"]

        ]



    def get_selected_layer(self):

        return self.active_layer



    # ==========================================================
    # LIMPIEZA
    # ==========================================================

    def clear(self):

        self.layers.clear()

        self.selected_layer = None

        self.active_layer = None

        self.last_operation = "clear"



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_info(self):

        return {

            "layers": len(
                self.layers
            ),

            "selected": self.selected_layer,

            "last_operation": self.last_operation

        }