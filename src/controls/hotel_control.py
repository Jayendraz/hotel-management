from src import Hotel
from src.controls.control import Control
from src.controls.payment_control import PaymentControl
from src.controls.room_control import RoomControl


class HotelControl(Control):
    def __init__(self):
        self.hotel = Hotel()
        self.room_control = RoomControl()
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
            print(room_number, " has assigned.") if room_number != None else print("Checkin Failed")
            self.process()

        elif option == "2":
            print("Enter room number: ")
            room_number = self.read_input()
            result = self.check_out_room(room_number)
            print(result)
            self.process()

        elif option == "3":
            print("Enter room number: ")
            room_number = self.read_input()
            result = self.clean_room(room_number)
            print(result)
            self.process()

        elif option == "4":
            print("Enter room number: ")
            room_number = self.read_input()
            result = self.mark_room_out_of_service(room_number)
            print(result)
            self.process()

        elif option == "5":
            print("Enter room number: ")
            room_number = self.read_input()
            result = self.repair_room(room_number)
            print(result)
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
            self.room_control.check_in(room)
            status = self.payment_control.make_payment()
            if status != None:
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
            self.room_control.check_out(room)
            return f"{room.room_number} is {room.status.name}"
        except ValueError as err:
            return str(err)
        except Exception as exp:
            return str(exp)

    def clean_room(self, room_number):
        """
        Clean room
        :param room_number: room number of room in hotel
        :return: Success message
        """
        try:
            room = self._validate_room(room_number)
            self.room_control.cleaned(room)
            return f"{room.room_number} is {room.status.name}"
        except ValueError as err:
            return str(err)
        except Exception as exp:
            return str(exp)

    def mark_room_out_of_service(self, room_number):
        """
        Mark room as out of service for repair
        :param room_number: room number of room in hotel
        :return: Success message
        """
        try:
            room = self._validate_room(room_number)
            self.room_control.out_of_service(room)
            return f"{room.room_number} is {room.status.name}"
        except ValueError as err:
            return str(err)
        except Exception as exp:
            return str(exp)

    def repair_room(self, room_number):
        """
        Repair room
        :param room_number: room number of room in hotel
        :return: Success message
        """
        try:
            room = self._validate_room(room_number)
            self.room_control.repaired(room)
            return f"{room.room_number} is {room.status.name}"
        except ValueError as err:
            return str(err)
        except Exception as exp:
            return str(exp)




