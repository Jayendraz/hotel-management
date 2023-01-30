import unittest
from src import Room
from src import Status


class TestRoomFunctions(unittest.TestCase):

    def test_get_room_status(self):
        # Arrange
        room = Room("1A", Status.Available)
        expected_status = Status.Available
        # Action
        actual_status = room.get_status()
        # Assert
        self.assertEqual(actual_status, expected_status)

    def test_set_room_status(self):
        # Arrange
        room = Room("1A", Status.Available)
        expected_status = Status.Occupied
        # Action
        room.set_status(Status.Occupied)
        # Assert
        self.assertEqual(room.status, expected_status)

    def test_checkin(self):
        # Arrange
        room = Room("1A", Status.Available)
        expected_status = Status.Occupied
        # Action
        room.check_in()
        # Assert
        self.assertEqual(room.status, expected_status)

    def test_room_should_be_marked_as_vacant_after_checkout(self):
        # Arrange
        room = Room("1A", Status.Occupied)
        expected_status = Status.Vacant
        # Action
        room.check_out()
        # Assert
        self.assertEqual(room.status, expected_status)

    def test_room_should_be_marked_as_available_after_clean(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        expected_status = Status.Available
        # Action
        room.cleaned()
        # Assert
        self.assertEqual(room.status, expected_status)

    def test_room_should_be_marked_as_repair_after_callled_as_out_of_service(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        expected_status = Status.Repair
        # Action
        room.out_of_service()
        # Assert
        self.assertEqual(room.status, expected_status)

    def test_room_should_be_marked_as_vacant_after_repair(self):
        # Arrange
        room = Room("1A", Status.Repair)
        expected_status = Status.Vacant
        # Action
        room.repaired()
        # Assert
        self.assertEqual(room.status, expected_status)
