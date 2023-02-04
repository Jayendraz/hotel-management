from src.controllers.controller import Controller
import uuid

from src.controllers.person_controller import PersonController
#from src.controllers.service_controller import ServiceController
from src.housekeeper import HouseKeeper


class HouseKeeperController(PersonController):

    def process(self):
        print("----------------Housekeeper--------------------")
        super().process()
        option = super().read_input()
        self.serve_section(option)

    def serve_section(self, option):
        if option == 1:
            self.register_new_housekeeper()

        elif option == 2:
            self.update_housekeeper()

        elif option == 3:
            self.delete_housekeeper()

        elif option == 4:
            self.display_all()

        elif option == 5:
            pass
            #controllers = ServiceController()
            #controllers.process()

    def _find_housekeeper(self, ):
        pass

    def register_new_housekeeper(self):
        print("Enter Hosuekeeper name: ")
        name = input()
        print("Enter Hosuekeeper contact No: ")
        contact_no = input()
        h_id = str(uuid.uuid4())[:8]
        new_housekeeper = HouseKeeper(h_id, name, contact_no)
        if new_housekeeper != None:
            print("Success")
        else:
            print("Error")

    def update_housekeeper(self):
        print("Customer has been updated")
        pass

    def delete_housekeeper(self, name):
        print("Housekeeper has been deleted")
        pass

    def display_all(self):
        print("Displaying all housekeepers")
        pass
