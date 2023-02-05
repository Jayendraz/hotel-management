from src.person import Person


class Customer(Person):
    def __init__(self, c_id, name, contact_no):
        super().__init__(c_id, name, contact_no)
