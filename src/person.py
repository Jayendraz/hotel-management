class Person:
    def __init__(self, id, name, contact_no):
        self._id = id
        self._name = name
        self._contact_no = contact_no

    def update_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_contact_no(self, contact_no):
        if str(contact_no).isdigit():
            self._contact_no = contact_no

    def get_contact_no(self):
        return self._contact_no