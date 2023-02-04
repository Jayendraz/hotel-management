import uuid

from src.controls.person_control import PersonControl
from src.housekeeper import HouseKeeper


class HouseKeeperControl(PersonControl):

    def process(self):
        print("----------------Housekeeper--------------------")
        super().process()
        option = super().read_input()
        self.serve_section(option)

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

        elif option == "5":
            return

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
        print("Housekeeper has been updated")

    def delete_housekeeper(self):
        print("Housekeeper has been deleted")

    def display_all(self):
        print("Displaying all housekeepers")
