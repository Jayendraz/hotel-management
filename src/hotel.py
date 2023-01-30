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
