from src.controllers.customer_controller import CustomerController
from src.controllers.controller import Controller
from .hotel_controller import HotelController
from .housekeeper_controller import HouseKeeperController


class ServiceController(Controller):
    def process(self):
        self.view_menu()
        option = self.read_input()
        print("OPtion is ", option)
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
            controller = CustomerController()
            controller.process()

        elif option == "2":
            controller = HouseKeeperController()
            controller.process()

        elif option == "3":
            controller = HotelController()
            controller.process()

        elif option == "4":
            exit()
