import uuid

from src.controls.person_control import PersonControl
from src.customer import Customer


class CustomerControl(PersonControl):

    def __init__(self, service_control):
        self.service_control = service_control

    def process(self):
        print("------------------Customer----------------------")
        super().view_menu()
        option = super().read_input()
        self.serve_section(option)

    def read_input(self):
        print("Select section number: ")
        return input()

    def serve_section(self, option):
        if option == "1":
            self.register_new_customer()
            self.process()

        elif option == "2":
            self.update_customer()
            self.process()

        elif option == "3":
            self.delete_customer()
            self.process()

        elif option == "4":
            self.display_all()
            self.process()

        elif option == 5:
            return

    def _find_customer(self, ):
        pass

    def register_new_customer(self):
        print("Enter Customer name: ")
        name = input()
        print("Enter Customer contact No: ")
        contact_no = input()
        c_id = str(uuid.uuid4())[:8]
        new_customer = Customer(c_id, name, contact_no)
        if new_customer != None:
            print("Success")
        else:
            print("Error")

    def update_customer(self):
        print("Customer has been updated")

    def delete_customer(self):
        print("Customer has been deleted")

    def display_all(self):
        print("Display all customer ")
