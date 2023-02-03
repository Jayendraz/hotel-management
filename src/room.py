from src.status import Status


class Room:
    def __init__(self, room_number, status):
        self.room_number = room_number
        # status == Status.Available or status == Status.Occupied or status == Status.Vacant
        self.status = status

    def get_status(self):
        return self.status

    def _set_status(self, status):
        self.status = status

    def check_in(self):
        if self.is_available():
            self._set_status(Status.Occupied)
        else:
            raise Exception("Error!! room in not available")

    def check_out(self):
        if self.is_occupied():
            self._set_status(Status.Vacant)
        else:
            raise Exception("Error!! room is not Occupied")

    def cleaned(self):
        if self.is_vacant():
            self._set_status(Status.Available)
        else:
            raise Exception("Error!! room is not Vacant")

    def repaired(self):
        if self.is_out_of_service():
            self._set_status(Status.Vacant)
        else:
            raise Exception("Error!! room can not be repair")

    def out_of_service(self):
        if self.is_available() or self.is_occupied():
            raise Exception("Error!! room can not be out of service")
        else:
            self._set_status(Status.Repair)

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
