from src.status import Status


class Room:
    def __init__(self, room_number, status):
        self.room_number = room_number
        # status == Status.Available or status == Status.Occupied or status == Status.Vacant
        self.status = status

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def check_in(self):
        self.set_status(Status.Occupied)

    def check_out(self):
        self.set_status(Status.Vacant)

    def cleaned(self):
        self.set_status(Status.Available)

    def repaired(self):
        self.set_status(Status.Vacant)

    def out_of_service(self):
        self.set_status(Status.Repair)

    def is_available(self):
        if self.status == Status.Available:
            return True

    def is_occupied(self):
        if self.status == Status.Occupied:
            return True
