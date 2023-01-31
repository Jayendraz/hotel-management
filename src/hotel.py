from src.room import Room
from src.status import Status


class Hotel:
    Floors = 4

    def __init__(self):
        rooms = []
        for floor in range(1, Hotel.Floors + 1):
            if floor % 2 != 0:
                for letter in "ABCDE":
                    room_number = f"{floor}{letter}"
                    rooms.append(Room(room_number, Status.Available))
            else:
                for letter in "EDCBA":
                    room_number = f"{floor}{letter}"
                    rooms.append(Room(room_number, Status.Available))
        self.rooms = rooms

    def get_all_rooms(self):
        return self.rooms

    def get_all_available_rooms(self):
        available_rooms = []
        for room in self.rooms:
            if room.status.name == "Available":
                available_rooms.append(room)
        return available_rooms

    def _get_first_nearest_available_room(self):
        available_room = None
        for room in self.rooms:
            if room.status == Status.Available:
                available_room = room
                break
        return available_room

    def _check_into_room(self):
        room = self._get_first_nearest_available_room()
        if not room:
            raise Exception("Sorry! Hotel is full")
        else:
            room.check_in()
            return room.room_number

    def assign_room(self):
        try:
            room_number = self._check_into_room()
            return room_number
        except Exception as exp:
            return str(exp)

    '''def assign_room(self):
        available_rooms = self.get_first_nearest_available_room()
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
        try:
            room = self._validate_room(room_number)
            room.check_out()
        except ValueError as err:
            return str(err)

    def clean_room(self, room_number):
        try:
            room = self._validate_room(room_number)
            room.cleaned()
        except ValueError as err:
            return str(err)

    def mark_room_out_of_service(self, room_number):
        room = self._validate_room(room_number)
        if not (room.is_available() or room.is_occupied()):
            room.out_of_service()
            print(room.status)
        else:
            return "Error! Available/Occupied room can not be marked as out of service"

    def repair_room(self, room_number):
        try:
            room = self._validate_room(room_number)
            room.repaired()
        except ValueError as err:
            return str(err)
