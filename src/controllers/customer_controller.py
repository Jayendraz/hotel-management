from src.controllers.controller import Controller
import uuid

from src.controllers.person_controller import PersonController
#from src.controllers.service_controller import ServiceController
from src.customer import Customer


class CustomerController(PersonController):

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
            self.register_new_housekeeper()
            self.process()

        elif option == "2":
            self.update_housekeeper()
            self.process()

        elif option == "3":
            self.delete_housekeeper()
            self.process()

        elif option == "4":
            self.display_all()
            self.process()

        '''elif option == 5:
            controllers = ServiceController()
            controllers.process()'''

    def _find_customer(self, ):
        pass

    def register_new_housekeeper(self):
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

    def update_housekeeper(self, name, contact_no):
        print("Customer has been updated")
        pass

    def delete_housekeeper(self, name):
        print("Customer has been deleted")
        pass

    def display_all(self):
        print("Display all customer ")
        pass
