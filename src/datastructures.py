from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return {
            "message": f"Miembro '{member['first_name']}' añadido correctamente a la familia {self.last_name}.",
            "member": member
        }

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member) #SI NO PONGO "DONE" NO PASA EL TEST
                return {"done": True}
        return {
            "error": f"No se encontró ningún miembro con ID {id} para eliminar."
        }

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return {
            "error": f"No se encontró ningún miembro con ID {id}."
        }

    def get_all_members(self):
        return self._members
