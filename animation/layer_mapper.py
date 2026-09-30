from dataclasses import dataclass, field



@dataclass
class LayerConnection:

    layer_name: str

    bone_name: str = None

    pivot_name: str = None

    category: str = "unknown"

    visible: bool = True

    properties: dict = field(
        default_factory=dict
    )



class LayerMapper:


    def __init__(self):

        self.layers = {}

        self.last_operation = None



    # ==========================================================
    # CREAR CONEXIÓN CAPA
    # ==========================================================

    def create_layer(
        self,
        layer_name,
        category="unknown"
    ):

        layer = LayerConnection(

            layer_name=layer_name,

            category=category

        )


        self.layers[layer_name] = layer


        self.last_operation = (
            "create_layer"
        )


        return layer



    # ==========================================================
    # MAPEO BÁSICO
    # ==========================================================

    def map_layer(
        self,
        layer_name,
        bone_name=None,
        pivot_name=None
    ):

        if layer_name not in self.layers:

            self.create_layer(
                layer_name
            )



        layer = self.layers[layer_name]


        layer.bone_name = bone_name

        layer.pivot_name = pivot_name



        self.last_operation = (
            "map_layer"
        )


        return layer



    # ==========================================================
    # MAPEO COMPLETO DE JHASMIN
    # ==========================================================

    def create_jhasmin_layers(
        self
    ):

        structure = {


            "body":

            {

                "category": "body",

                "bone": "body",

                "pivot": "body"

            },


            "head":

            {

                "category": "face",

                "bone": "head",

                "pivot": "head"

            },


            "hair":

            {

                "category": "hair",

                "bone": "hair",

                "pivot": "hair"

            },


            "left_wing":

            {

                "category": "wing",

                "bone": "left_wing",

                "pivot": "left_wing"

            },


            "right_wing":

            {

                "category": "wing",

                "bone": "right_wing",

                "pivot": "right_wing"

            },


            "eyes":

            {

                "category": "face_detail",

                "bone": "head",

                "pivot": "head"

            },


            "gem":

            {

                "category": "accessory",

                "bone": "gem",

                "pivot": "gem"

            },


            "dress":

            {

                "category": "clothes",

                "bone": "body",

                "pivot": "body"

            }

        }



        for name, data in structure.items():

            self.create_layer(

                name,

                data["category"]

            )


            self.map_layer(

                name,

                data["bone"],

                data["pivot"]

            )



        self.last_operation = (
            "create_jhasmin_layers"
        )


        return self.layers



    # ==========================================================
    # CAMBIAR CATEGORÍA
    # ==========================================================

    def set_category(
        self,
        layer_name,
        category
    ):

        if layer_name in self.layers:

            self.layers[layer_name].category = category



    # ==========================================================
    # VISIBILIDAD
    # ==========================================================

    def set_visibility(
        self,
        layer_name,
        visible
    ):

        if layer_name in self.layers:

            self.layers[layer_name].visible = visible



    # ==========================================================
    # PROPIEDADES
    # ==========================================================

    def add_property(
        self,
        layer_name,
        key,
        value
    ):

        if layer_name in self.layers:

            self.layers[layer_name].properties[key] = value



    # ==========================================================
    # ORDEN DE CAPAS
    # ==========================================================

    def get_render_order(
        self
    ):

        return list(
            self.layers.keys()
        )



    # ==========================================================
    # EXPORTAR
    # ==========================================================

    def export_data(
        self
    ):

        data = {}


        for name, layer in self.layers.items():

            data[name] = {

                "bone": layer.bone_name,

                "pivot": layer.pivot_name,

                "category": layer.category,

                "visible": layer.visible,

                "properties": layer.properties

            }



        return data



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_layer(
        self,
        name
    ):

        return self.layers.get(
            name
        )



    def get_all_layers(
        self
    ):

        return self.layers



    def get_last_operation(
        self
    ):

        return self.last_operation