from src import Hotel
from src.controllers.controller import Controller
from src.controllers.payment_control import PaymentControl
from src.controllers.room_controller import RoomController
#from src.controllers.service_controller import ServiceController


class HotelController(Controller):
    def __init__(self):
        self.hotel = Hotel()
        self.room_controller = RoomController()
        self.payment_control = PaymentControl()

    def process(self):
        self.view_menu()
        print("Select section number: ")
        option = self.read_input()
        self.serve_section(option)

    def view_menu(self):
        print("------------------Customer----------------------")
        print("1. Check in")
        print("2. Check out")
        print("3. Clean")
        print("4. Out of service")
        print("5. Repair")
        print("6. Back to Main menu")
        print("------------------------------------------------")

    def read_input(self):
        return input()

    def serve_section(self, option):
        if option == "1":
            room_number = self.assign_room()
            print(room_number, " has assigned.")
            self.process()

        elif option == "2":
            print("Enter room number: ")
            room_number = self.read_input()
            self.check_out_room(room_number)
            self.process()

        elif option == "3":
            print("Enter room number: ")
            room_number = self.read_input()
            self.clean_room(room_number)
            self.process()

        elif option == "4":
            print("Enter room number: ")
            room_number = self.read_input()
            self.mark_room_out_of_service(room_number)
            self.process()

        elif option == "5":
            print("Enter room number: ")
            room_number = self.read_input()
            self.repair_room(room_number)
            self.process()

        elif option == "6":
            return

    def set_housekeeper(self, housekeeper):
        self.hotel.housekeeper = housekeeper

    def get_housekeeper(self):
        return self.hotel.housekeeper

    def get_all_rooms(self):
        return self.hotel.rooms

    def get_all_available_rooms(self):
        available_rooms = []
        for room in self.hotel.rooms:
            if room.status.name == "Available":
                available_rooms.append(room)
        return available_rooms

    def _get_first_nearest_available_room(self):
        available_room = None
        for room in self.hotel.rooms:
            #if room.status == Status.Available:
            if room.is_available():
                available_room = room
                break
        return available_room

    def _check_in_room(self):
        room = self._get_first_nearest_available_room()
        if not room:
            raise Exception("Sorry! Hotel is full")
        else:
            self.room_controller.check_in(room)
            self.payment_control.make_payment()
            return room.room_number

    def assign_room(self):
        """
        Assign nearest to entrance available room in hotel
        :return: room_number
        """
        try:
            room_number = self._check_in_room()
            return room_number
        except Exception as exp:
            return str(exp)

    '''def assign_room(self):
        available_rooms = self._get_first_nearest_available_room()
        if not available_rooms:
            return "Error! - No room is available"
        else:
            # !!!! Write Logic to find nearest entrance room
            room = available_rooms[0]
            room.check_in()
            return room.room_number'''

    def _find_room(self, room_number):
        rooms = self.get_all_rooms()
        result = None
        for room in rooms:
            if room.room_number == room_number:
                result = room
                break
        return result

    def _validate_room(self, room_number):
        room = self._find_room(room_number)
        if room is None:
            raise ValueError("Error!! Please input valid room number")
        else:
            return room

    def check_out_room(self, room_number):
        """
        Checking out of room
        :param room_number: room number of room in hotel
        :return: Success message
        """
        try:
            room = self._validate_room(room_number)
            self.room_controller.check_out(room)
            print(room.room_number, "is", room.status.name)
        except ValueError as err:
            print(err)
        except Exception as exp:
            print(exp)

    def clean_room(self, room_number):
        """
        Clean room
        :param room_number: room number of room in hotel
        :return: Success message
        """
        try:
            room = self._validate_room(room_number)
            self.room_controller.cleaned(room)
            print(room.room_number, "is", room.status.name)
        except ValueError as err:
            print(err)
        except Exception as exp:
            print(exp)

    def mark_room_out_of_service(self, room_number):
        """
        Mark room as out of service for repair
        :param room_number: room number of room in hotel
        :return: Success message
        """
        try:
            room = self._validate_room(room_number)
            self.room_controller.out_of_service(room)
            print(room.room_number, "is", room.status.name)
        except ValueError as err:
            print(err)
        except Exception as exp:
            print(exp)

    def repair_room(self, room_number):
        """
        Repair room
        :param room_number: room number of room in hotel
        :return: Success message
        """
        try:
            room = self._validate_room(room_number)
            self.room_controller.repaired(room)
            print(room.room_number, "is ", room.status.name)
        except ValueError as err:
            print(err)
        except Exception as exp:
            print(exp)




