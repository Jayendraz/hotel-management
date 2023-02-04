from src.hotel import Hotel
from src.person import Person


class HouseKeeper(Person):

    def __init__(self, h_id, name, contact_no, id):
        super().__init__(id, name, contact_no)
        self._salary = None

    def update_id(self, h_id):
        super().update_id(h_id)

    def get_id(self):
        return self._h_id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_salary(self, salary):
        if str(salary).isdigit() and self._salary > 0:
            self._salary = salary

    def get_salary(self):
        return self._salary

    def set_contact_no(self, contact_no):
        if str(contact_no).isdigit():
            self._contact_no = contact_no

    def get_contact_no(self):
        return self._contact_no




