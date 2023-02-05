from src.hotel import Hotel
from src.person import Person


class HouseKeeper(Person):

    def __init__(self, h_id, name, contact_no):
        super().__init__(h_id, name, contact_no)
        self._salary = None

    def set_salary(self, salary):
        if str(salary).isdigit() and self._salary > 0:
            self._salary = salary

    def get_salary(self):
        return self._salary
