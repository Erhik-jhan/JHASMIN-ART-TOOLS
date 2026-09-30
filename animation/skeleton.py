from dataclasses import dataclass, field



@dataclass
class Bone:

    name: str

    parent: str = None

    position: tuple = (0, 0)

    rotation: float = 0.0

    length: float = 0.0

    children: list = field(
        default_factory=list
    )



class Skeleton:


    def __init__(self):

        self.bones = {}

        self.root = None

        self.last_operation = None



    # ==========================================================
    # CREAR HUESO
    # ==========================================================

    def create_bone(
        self,
        name,
        parent=None,
        position=(0, 0),
        length=0
    ):

        bone = Bone(

            name=name,

            parent=parent,

            position=position,

            length=length

        )


        self.bones[name] = bone



        if parent:

            if parent in self.bones:

                self.bones[parent].children.append(
                    name
                )

        else:

            self.root = name



        self.last_operation = (
            "create_bone"
        )


        return bone



    # ==========================================================
    # ELIMINAR HUESO
    # ==========================================================

    def remove_bone(
        self,
        name
    ):

        if name not in self.bones:

            return False



        del self.bones[name]


        self.last_operation = (
            "remove_bone"
        )


        return True



    # ==========================================================
    # CREAR ESQUELETO BASE PERSONAJE
    # ==========================================================

    def create_character_skeleton(
        self
    ):

        self.create_bone(
            "root",
            position=(0, 0)
        )


        self.create_bone(
            "spine",
            "root",
            (0, -100),
            100
        )


        self.create_bone(
            "neck",
            "spine",
            (0, -150),
            40
        )


        self.create_bone(
            "head",
            "neck",
            (0, -190),
            50
        )


        self.create_bone(
            "left_arm",
            "spine",
            (-60, -100),
            70
        )


        self.create_bone(
            "right_arm",
            "spine",
            (60, -100),
            70
        )


        self.create_bone(
            "left_leg",
            "root",
            (-40, 80),
            100
        )


        self.create_bone(
            "right_leg",
            "root",
            (40, 80),
            100
        )


        self.last_operation = (
            "create_character_skeleton"
        )


        return self.bones



    # ==========================================================
    # JHASMIN BASE
    # ==========================================================

    def create_jhasmin_skeleton(
        self
    ):

        self.create_bone(
            "body"
        )


        self.create_bone(
            "head",
            "body",
            (0, -120)
        )


        self.create_bone(
            "hair",
            "head"
        )


        self.create_bone(
            "left_wing",
            "body",
            (-80, -20)
        )


        self.create_bone(
            "right_wing",
            "body",
            (80, -20)
        )


        self.create_bone(
            "left_hand",
            "body"
        )


        self.create_bone(
            "right_hand",
            "body"
        )


        self.create_bone(
            "gem",
            "body"
        )


        self.create_bone(
            "dress",
            "body"
        )


        self.last_operation = (
            "create_jhasmin_skeleton"
        )


        return self.bones



    # ==========================================================
    # TRANSFORMACIONES
    # ==========================================================

    def set_position(
        self,
        bone_name,
        position
    ):

        if bone_name in self.bones:

            self.bones[bone_name].position = position



    def set_rotation(
        self,
        bone_name,
        rotation
    ):

        if bone_name in self.bones:

            self.bones[bone_name].rotation = rotation



    # ==========================================================
    # EXPORTAR
    # ==========================================================

    def export_data(
        self
    ):

        data = {}


        for name, bone in self.bones.items():

            data[name] = {

                "parent": bone.parent,

                "position": bone.position,

                "rotation": bone.rotation,

                "length": bone.length,

                "children": bone.children

            }


        return data



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_bone(
        self,
        name
    ):

        return self.bones.get(
            name
        )



    def get_all_bones(
        self
    ):

        return self.bones



    def get_last_operation(
        self
    ):

        return self.last_operation