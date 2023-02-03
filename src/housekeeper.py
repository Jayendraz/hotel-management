from src.hotel import Hotel


class HouseKeeper:

    def __init__(self, name, hotel: Hotel):
        self.name = name
        self.hotel = hotel

    def _find_room(self, room_number):
        rooms = self.hotel.rooms
        result = None
        for room in rooms:
            if room.room_number == room_number:
                result = room
                break
        return result

    def validate_room_number(self, room_number):
        room = self._find_room(room_number)
        if room is None:
            raise ValueError("Error!! Please input valid room number")
        else:
            return room

    def clean_room(self, room_number):
        print("cleaning room")
        try:
            room = self.validate_room_number(room_number)
            room.cleaned()
            print("after room clean up")
            print(room.status)
            return "success"
        except ValueError as err:
            print("error 1")
            return str(err)
        except Exception as exp:
            print("error 2")
            return str(exp)

    def mark_room_out_of_service(self, room_number):
        try:
            room = self.validate_room_number(room_number)
            room.out_of_service()
            return "success"
        except ValueError as err:
            return str(err)
        except Exception as exp:
            return str(exp)

    def repair_room(self, room_number):
        try:
            room = self.validate_room_number(room_number)
            room.repaired()
            return "success"
        except ValueError as err:
            return str(err)
        except Exception as exp:
            return exp
