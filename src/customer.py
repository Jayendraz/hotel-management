from src.person import Person


class Customer(Person):
    def __init__(self, c_id, name, contact_no):
        super().__init__(c_id, name, contact_no)

    def update_id(self, c_id):
        super().update_id(c_id)

    def get_id(self):
        super().get_id()

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_contact_no(self, contact_no):
        if str(contact_no).isdigit():
            self._contact_no = contact_no

    def get_contact_no(self):
        return self._contact_no
