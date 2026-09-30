from dataclasses import dataclass, field



@dataclass
class RigPart:

    name: str

    layer: str = None

    bone: str = None

    parent: str = None

    enabled: bool = True

    properties: dict = field(
        default_factory=dict
    )



class RigHelper:


    def __init__(self):

        self.parts = {}

        self.constraints = []

        self.last_operation = None



    # ==========================================================
    # CREAR PARTE DEL RIG
    # ==========================================================

    def create_part(
        self,
        name,
        layer=None,
        bone=None,
        parent=None
    ):

        part = RigPart(

            name=name,

            layer=layer,

            bone=bone,

            parent=parent

        )


        self.parts[name] = part


        self.last_operation = (
            "create_part"
        )


        return part



    # ==========================================================
    # RIG BASE DE PERSONAJE
    # ==========================================================

    def create_character_rig(
        self
    ):

        self.create_part(
            "body",
            "body",
            "body"
        )


        self.create_part(
            "head",
            "head",
            "head",
            "body"
        )


        self.create_part(
            "hair",
            "hair",
            "hair",
            "head"
        )


        self.create_part(
            "left_wing",
            "left_wing",
            "left_wing",
            "body"
        )


        self.create_part(
            "right_wing",
            "right_wing",
            "right_wing",
            "body"
        )


        self.create_part(
            "left_hand",
            "left_hand",
            "left_hand",
            "body"
        )


        self.create_part(
            "right_hand",
            "right_hand",
            "right_hand",
            "body"
        )


        self.create_part(
            "gem",
            "gem",
            "gem",
            "body"
        )


        self.last_operation = (
            "create_character_rig"
        )


        return self.parts



    # ==========================================================
    # RIG JHASMIN
    # ==========================================================

    def create_jhasmin_rig(
        self
    ):

        parts = {

            "body": (
                "body",
                "body"
            ),

            "face": (
                "face",
                "head"
            ),

            "hair": (
                "hair",
                "hair"
            ),

            "eyes": (
                "eyes",
                "head"
            ),

            "left_wing": (
                "left_wing",
                "left_wing"
            ),

            "right_wing": (
                "right_wing",
                "right_wing"
            ),

            "dress": (
                "dress",
                "body"
            ),

            "gem": (
                "gem",
                "gem"
            )

        }



        for name, data in parts.items():

            self.create_part(

                name,

                data[0],

                data[1]

            )



        self.last_operation = (
            "create_jhasmin_rig"
        )


        return self.parts



    # ==========================================================
    # ASIGNAR CAPA
    # ==========================================================

    def assign_layer(
        self,
        part_name,
        layer_name
    ):

        if part_name in self.parts:

            self.parts[part_name].layer = layer_name



    # ==========================================================
    # ASIGNAR HUESO
    # ==========================================================

    def assign_bone(
        self,
        part_name,
        bone_name
    ):

        if part_name in self.parts:

            self.parts[part_name].bone = bone_name



    # ==========================================================
    # RESTRICCIONES
    # ==========================================================

    def add_constraint(
        self,
        source,
        target,
        constraint_type
    ):

        constraint = {

            "source": source,

            "target": target,

            "type": constraint_type

        }


        self.constraints.append(
            constraint
        )


        self.last_operation = (
            "add_constraint"
        )


        return constraint



    # ==========================================================
    # ACTIVAR / DESACTIVAR PARTE
    # ==========================================================

    def toggle_part(
        self,
        name,
        enabled
    ):

        if name in self.parts:

            self.parts[name].enabled = enabled



    # ==========================================================
    # EXPORTAR RIG
    # ==========================================================

    def export_data(
        self
    ):

        data = {

            "parts": {},

            "constraints": self.constraints

        }



        for name, part in self.parts.items():

            data["parts"][name] = {

                "layer": part.layer,

                "bone": part.bone,

                "parent": part.parent,

                "enabled": part.enabled,

                "properties": part.properties

            }



        return data



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_part(
        self,
        name
    ):

        return self.parts.get(
            name
        )



    def get_all_parts(
        self
    ):

        return self.parts



    def get_last_operation(
        self
    ):

        return self.last_operation