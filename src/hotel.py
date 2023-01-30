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

    def assign_room(self):
        available_rooms = self.get_all_available_rooms()
        if not available_rooms:
            return "Error! - No room is available"
        else:
            # !!!! Write algorithm to find nearest entrance room
            room = available_rooms[0]
            room.check_in()
            return room.room_number

    def find_room(self, room_number):
        rooms = self.get_all_rooms()
        for room in rooms:
            if room.room_number == room_number:
                return room

    def check_out_room(self, room_number):
        room = self.find_room(room_number)
        room.check_out()

    def clean_room(self, room_number):
        room = self.find_room(room_number)
        room.cleaned()

    def mark_room_out_of_service(self, room_number):
        room = self.find_room(room_number)
        if not (room.is_available() or room.is_occupied()):
            room.out_of_service()
        else:
            return "Error!! Available/Occupied room can not be marked as out of service"

    def repair_room(self, room_number):
        room = self.find_room(room_number)
        room.repaired()


"""
    room1A = Room("1A", Status.Available)
    room1B = Room("1B", Status.Available)
    room1C = Room("1C", Status.Available)
    room1D = Room("1D", Status.Available)
    room1E = Room("1E", Status.Available)
    #floor 2
    room2A = Room("2A", Status.Available)
    room2B = Room("2B", Status.Available)
    room2C = Room("2C", Status.Available)
    room2D = Room("2D", Status.Available)
    room2E = Room("2E", Status.Available)
    #Floor 3
    room3A = Room("1A", Status.Available)
    room3B = Room("1A", Status.Available)
    room3C = Room("1A", Status.Available)
    room3D = Room("1A", Status.Available)
    room3E = Room("1A", Status.Available)
    #Floor 4
    room4A = Room("1A", Status.Available)
    room4B = Room("1A", Status.Available)
    room4C = Room("1A", Status.Available)
    room4D = Room("1A", Status.Available)
    room4E = Room("1A", Status.Available)
    """
