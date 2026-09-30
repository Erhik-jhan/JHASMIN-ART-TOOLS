from dataclasses import dataclass, field



@dataclass
class PhysicsObject:

    name: str

    mass: float = 1.0

    stiffness: float = 0.5

    damping: float = 0.5

    gravity: float = 0.0

    enabled: bool = True

    properties: dict = field(
        default_factory=dict
    )



class PhysicsHelper:


    def __init__(self):

        self.objects = {}

        self.last_operation = None



    # ==========================================================
    # CREAR OBJETO FÍSICO
    # ==========================================================

    def create_object(
        self,
        name,
        mass=1.0,
        stiffness=0.5,
        damping=0.5
    ):

        obj = PhysicsObject(

            name=name,

            mass=mass,

            stiffness=stiffness,

            damping=damping

        )


        self.objects[name] = obj


        self.last_operation = (
            "create_object"
        )


        return obj



    # ==========================================================
    # CONFIGURACIÓN BASE JHASMIN
    # ==========================================================

    def create_jhasmin_physics(
        self
    ):


        self.create_object(

            "hair",

            mass=0.8,

            stiffness=0.3,

            damping=0.4

        )


        self.create_object(

            "left_wing",

            mass=2.0,

            stiffness=0.7,

            damping=0.6

        )


        self.create_object(

            "right_wing",

            mass=2.0,

            stiffness=0.7,

            damping=0.6

        )


        self.create_object(

            "dress",

            mass=1.5,

            stiffness=0.4,

            damping=0.5

        )


        self.create_object(

            "gem",

            mass=0.2,

            stiffness=0.9,

            damping=0.2

        )


        self.last_operation = (
            "create_jhasmin_physics"
        )


        return self.objects



    # ==========================================================
    # APLICAR GRAVEDAD
    # ==========================================================

    def set_gravity(
        self,
        name,
        gravity
    ):

        if name in self.objects:

            self.objects[name].gravity = gravity



    # ==========================================================
    # CAMBIAR RIGIDEZ
    # ==========================================================

    def set_stiffness(
        self,
        name,
        value
    ):

        if name in self.objects:

            self.objects[name].stiffness = value



    # ==========================================================
    # CAMBIAR AMORTIGUACIÓN
    # ==========================================================

    def set_damping(
        self,
        name,
        value
    ):

        if name in self.objects:

            self.objects[name].damping = value



    # ==========================================================
    # ACTIVAR / DESACTIVAR
    # ==========================================================

    def toggle(
        self,
        name,
        enabled
    ):

        if name in self.objects:

            self.objects[name].enabled = enabled



    # ==========================================================
    # SIMULACIÓN SIMPLE
    # ==========================================================

    def simulate(
        self,
        name,
        movement
    ):

        if name not in self.objects:

            return None


        obj = self.objects[name]


        response = {

            "object": name,

            "input": movement,

            "response": {

                "delay":

                obj.damping,

                "elasticity":

                obj.stiffness

            }

        }


        self.last_operation = (
            "simulate"
        )


        return response



    # ==========================================================
    # MOVIMIENTOS NATURALES
    # ==========================================================

    def breathing_effect(
        self,
        intensity=0.02
    ):

        return {

            "type": "breathing",

            "intensity": intensity

        }



    def hair_movement(
        self,
        wind=0.5
    ):

        return {

            "type": "hair",

            "wind": wind

        }



    def wing_flap(
        self,
        speed=1.0
    ):

        return {

            "type": "wing",

            "speed": speed

        }



    # ==========================================================
    # EXPORTAR
    # ==========================================================

    def export_data(
        self
    ):

        data = {}


        for name, obj in self.objects.items():

            data[name] = {

                "mass": obj.mass,

                "stiffness": obj.stiffness,

                "damping": obj.damping,

                "gravity": obj.gravity,

                "enabled": obj.enabled,

                "properties": obj.properties

            }


        return data



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_object(
        self,
        name
    ):

        return self.objects.get(
            name
        )



    def get_all_objects(
        self
    ):

        return self.objects



    def get_last_operation(
        self
    ):

        return self.last_operation