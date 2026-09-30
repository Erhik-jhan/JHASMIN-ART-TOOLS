from copy import deepcopy
from datetime import datetime
from uuid import uuid4



class HistoryManager:


    def __init__(
        self,
        max_history=500
    ):

        self.max_history = max_history

        self.undo_stack = []

        self.redo_stack = []

        self.current_state = None

        self.enabled = True

        self.last_operation = None

        self.group_mode = False

        self.current_group = None



    # ==========================================================
    # HABILITAR / DESHABILITAR
    # ==========================================================

    def enable(self):

        self.enabled = True

        self.last_operation = "enable"



    def disable(self):

        self.enabled = False

        self.last_operation = "disable"



    # ==========================================================
    # CREAR SNAPSHOT
    # ==========================================================

    def create_snapshot(

        self,

        project,

        action="",

        description=""

    ):

        if not self.enabled:

            return


        snapshot = {

            "id": str(

                uuid4()

            ),

            "time": datetime.now(),

            "action": action,

            "description": description,

            "state": deepcopy(

                project

            )

        }


        self.undo_stack.append(

            snapshot

        )


        if len(

            self.undo_stack

        ) > self.max_history:

            self.undo_stack.pop(

                0

            )


        self.redo_stack.clear()


        self.current_state = snapshot


        self.last_operation = (

            "create_snapshot"

        )


        return snapshot



    # ==========================================================
    # GUARDAR ACCIÓN SIMPLE
    # ==========================================================

    def push(

        self,

        action,

        state,

        description=""

    ):

        return self.create_snapshot(

            state,

            action,

            description

        )



    # ==========================================================
    # DESHACER
    # ==========================================================

    def undo(self):

        if len(

            self.undo_stack

        ) <= 1:

            return None


        current = self.undo_stack.pop()

        self.redo_stack.append(

            current

        )


        self.current_state = (

            self.undo_stack[-1]

        )


        self.last_operation = (

            "undo"

        )


        return deepcopy(

            self.current_state["state"]

        )



    # ==========================================================
    # REHACER
    # ==========================================================

    def redo(self):

        if not self.redo_stack:

            return None


        state = self.redo_stack.pop()

        self.undo_stack.append(

            state

        )


        self.current_state = state


        self.last_operation = (

            "redo"

        )


        return deepcopy(

            state["state"]

        )



    # ==========================================================
    # LIMPIAR REDO
    # ==========================================================

    def clear_redo(self):

        self.redo_stack.clear()

        self.last_operation = (

            "clear_redo"

        )



    # ==========================================================
    # LIMPIAR HISTORIAL
    # ==========================================================

    def clear(self):

        self.undo_stack.clear()

        self.redo_stack.clear()

        self.current_state = None

        self.last_operation = "clear"



    # ==========================================================
    # AGRUPACIÓN
    # ==========================================================

    def begin_group(

        self,

        name

    ):

        if self.group_mode:

            return


        self.group_mode = True

        self.current_group = {

            "name": name,

            "operations": []

        }


        self.last_operation = (

            "begin_group"

        )



    def add_group_operation(

        self,

        operation

    ):

        if not self.group_mode:

            return


        self.current_group[

            "operations"

        ].append(

            operation

        )


        self.last_operation = (

            "add_group_operation"

        )



    def end_group(self):

        if not self.group_mode:

            return None


        result = deepcopy(

            self.current_group

        )


        self.group_mode = False

        self.current_group = None


        self.last_operation = (

            "end_group"

        )


        return result



    # ==========================================================
    # CONSULTAS
    # ==========================================================

    def can_undo(self):

        return len(

            self.undo_stack

        ) > 1



    def can_redo(self):

        return len(

            self.redo_stack

        ) > 0



    def get_last_snapshot(self):

        return self.current_state



    def get_history(self):

        return deepcopy(

            self.undo_stack

        )



    def get_redo_history(self):

        return deepcopy(

            self.redo_stack

        )



    # ==========================================================
    # ELIMINAR SNAPSHOT
    # ==========================================================

    def remove_snapshot(

        self,

        snapshot_id

    ):

        for index, snapshot in enumerate(

            self.undo_stack

        ):

            if snapshot["id"] == snapshot_id:

                self.undo_stack.pop(

                    index

                )

                self.last_operation = (

                    "remove_snapshot"

                )

                return True


        return False



    # ==========================================================
    # BUSCAR
    # ==========================================================

    def find_snapshot(

        self,

        snapshot_id

    ):

        for snapshot in self.undo_stack:

            if snapshot["id"] == snapshot_id:

                return snapshot


        return None



    # ==========================================================
    # EXPORTAR HISTORIAL
    # ==========================================================

    def export(self):

        result = []


        for snapshot in self.undo_stack:

            result.append(

                {

                    "id":

                    snapshot["id"],

                    "time":

                    str(

                        snapshot["time"]

                    ),

                    "action":

                    snapshot["action"],

                    "description":

                    snapshot["description"]

                }

            )


        return result



    # ==========================================================
    # ESTADÍSTICAS
    # ==========================================================

    def get_statistics(self):

        return {

            "undo":

            len(

                self.undo_stack

            ),

            "redo":

            len(

                self.redo_stack

            ),

            "enabled":

            self.enabled,

            "group_mode":

            self.group_mode

        }



    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def get_info(self):

        return {

            "last_operation":

            self.last_operation,

            "current_snapshot":

            self.current_state["id"]

            if self.current_state

            else None,

            "max_history":

            self.max_history

        }