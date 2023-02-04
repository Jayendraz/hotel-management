from src import Status
from src.controllers.controller import Controller


class RoomController(Controller):

    def process(self):
        pass

    def check_in(self, room):
        if room.is_available():
            room.set_status(Status.Occupied)
        else:
            raise Exception("Error!! room in not available")

    def check_out(self, room):
        if room.is_occupied():
            room.set_status(Status.Vacant)
        else:
            raise Exception("Error!! room is not Occupied")

    def cleaned(self, room):
        if room.is_vacant():
            room.set_status(Status.Available)
        else:
            raise Exception("Error!! room is not Vacant")

    def repaired(self, room):
        if room.is_out_of_service():
            room.set_status(Status.Vacant)
        else:
            raise Exception("Error!!", room.status.name, "room can not be repair")

    def out_of_service(self, room):
        if room.is_available() or room.is_occupied():
            raise Exception("Error!!", room.status.name, "room can not be out of service")
        else:
            room.set_status(Status.Repair)
