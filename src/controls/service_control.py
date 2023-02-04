from src.controls.customer_control import CustomerControl
from src.controls.control import Control
from src.controls.hotel_control import HotelControl
from src.controls.housekeeper_control import HouseKeeperControl


class ServiceControl(Control):
    def process(self):
        self.view_menu()
        option = self.read_input()
        self.serve_section(option)

    def view_menu(self):
        print("------------------------------------------------")
        print("1. Customer management")
        print("2. Housekeeper management ")
        print("3. Room management")
        print("4. Exit")
        print("------------------------------------------------")

    def read_input(self):
        print("Select section number: ")
        return input()

    def serve_section(self, option):
        if option == "1":
            print("selected ontion 1")
            controller = CustomerControl(self)
            controller.process()
            self.process()

        elif option == "2":
            controller = HouseKeeperControl()
            controller.process()
            self.process()

        elif option == "3":
            controller = HotelControl()
            controller.process()
            self.process()

        elif option == "4":
            exit()
