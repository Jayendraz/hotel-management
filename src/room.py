from src.status import Status


class Room:
    def __init__(self, room_number, status):
        self.room_number = room_number
        self.status = status

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def is_available(self):
        if self.status == Status.Available:
            return True

    def is_occupied(self):
        if self.status == Status.Occupied:
            return True

    def is_vacant(self):
        if self.status == Status.Vacant:
            return True

    def is_out_of_service(self):
        if self.status == Status.Repair:
            return True
