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
        self.assertEqual(expected_status, actual_status)

    def test_set_room_status(self):
        # Arrange
        room = Room("1A", Status.Available)
        expected_status = Status.Occupied
        # Action
        room._set_status(Status.Occupied)
        # Assert
        self.assertEqual(expected_status, room.status)

    def test_room_with_status_available_can_be_checkin(self):
        # Arrange
        room = Room("1A", Status.Available)
        expected_status = Status.Occupied
        # Action
        room.check_in()
        # Assert
        self.assertEqual(expected_status, room.status)

    def test_room_with_status_can_be_marked_as_vacant_after_checkout(self):
        # Arrange
        room = Room("1A", Status.Occupied)
        expected_status = Status.Vacant
        # Action
        room.check_out()
        # Assert
        self.assertEqual(expected_status, room.status)

    def test_room_with_status_vacant_can_be_marked_as_available_after_clean(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        expected_status = Status.Available
        # Action
        room.cleaned()
        # Assert
        self.assertEqual(expected_status, room.status)

    def test_room_with_status_vacant_can_be_marked_as_repair_after_called_as_out_of_service(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        expected_status = Status.Repair
        # Action
        room.out_of_service()
        # Assert
        self.assertEqual(expected_status, room.status)

    def test_room_with_status_repair_can_be_marked_as_vacant_after_repair(self):
        # Arrange
        room = Room("1A", Status.Repair)
        expected_status = Status.Vacant
        # Action
        room.repaired()
        # Assert
        self.assertEqual(expected_status, room.status)

    def test_room_is_available_should_be_true_for_available_room(self):
        # Arrange
        room = Room("1A", Status.Available)
        expected_response = True
        # Action
        actual_response = room.is_available()
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_room_is_vacant_should_be_true_for_vacant_room(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        expected_response = True
        # Action
        actual_response = room.is_vacant()
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_room_is_occupied_should_be_true_for_occupied_room(self):
        # Arrange
        room = Room("1A", Status.Occupied)
        expected_response = True
        # Action
        actual_response = room.is_occupied()
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_room_is_out_of_service_should_be_true_for_out_of_service_room(self):
        # Arrange
        room = Room("1A", Status.Repair)
        expected_response = True
        # Action
        actual_response = room.is_out_of_service()
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_checking_out_should_not_allow_from_available_room(self):
        # Arrange
        room = Room("1A", Status.Available)
        # Action & Assert
        self.assertRaises(Exception, lambda: room.check_out())

    def test_room_with_status_vacant_can_not_be_occupied(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.check_out())

    def test_room_with_status_repair_can_not_be_checked_in(self):
        # Arrange
        room = Room("1A", Status.Repair)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.check_in())

    def test_rooms_with_status_occupied_can_not_be_checked_in(self):
        # Arrange
        room = Room("1A", Status.Occupied)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.check_in())

    def test_rooms_with_status_occupied_can_not_be_repaired(self):
        # Arrange
        room = Room("1A", Status.Occupied)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.repaired())

    def test_rooms_with_status_occupied_can_not_be_marked_as_out_of_service(self):
        # Arrange
        room = Room("1A", Status.Occupied)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.out_of_service())

    def test_rooms_with_status_occupied_can_not_be_cleaned(self):
        # Arrange
        room = Room("1A", Status.Occupied)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.cleaned())

    def test_rooms_with_status_occupied_can_be_checked_out(self):
        # Arrange
        room = Room("1A", Status.Occupied)
        expected_status = Status.Vacant
        # Action
        room.check_out()
        # Assert
        self.assertEqual(expected_status, room.status)

    def test_rooms_with_status_repair_can_not_be_cleaned(self):
        # Arrange
        room = Room("1A", Status.Repair)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.cleaned())

    def test_rooms_with_status_repair_can_not_be_checkin(self):
        # Arrange
        room = Room("1A", Status.Repair)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.check_in())

    def test_rooms_with_status_repair_can_not_be_checkout(self):
        # Arrange
        room = Room("1A", Status.Repair)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.check_out())

    def test_rooms_with_status_repair_can_be_repaired(self):
        # Arrange
        room = Room("1A", Status.Repair)
        expected_response = Status.Vacant
        # Action
        room.repaired()
        # Assert
        self.assertEqual(expected_response, room.status)

    def test_rooms_with_status_available_can_not_be_cleaned(self):
        # Arrange
        room = Room("1A", Status.Available)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.cleaned())

    def test_rooms_with_status_available_can_not_be_checkout(self):
        # Arrange
        room = Room("1A", Status.Available)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.check_out())

    def test_rooms_with_status_available_can_not_be_marked_as_out_of_service(self):
        # Arrange
        room = Room("1A", Status.Available)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.out_of_service())

    def test_rooms_with_status_available_can_be_checkin(self):
        # Arrange
        room = Room("1A", Status.Available)
        expected_response = Status.Occupied
        # Action
        room.check_in()
        # Assert
        self.assertEqual(expected_response, room.status)

    def test_rooms_with_status_available_can_not_be_repaired(self):
        # Arrange
        room = Room("1A", Status.Available)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.repaired())

    def test_rooms_with_status_vacant_can_not_be_checkin(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.check_in())

    def test_rooms_with_status_vacant_can_not_be_checkout(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.check_out())

    def test_rooms_with_status_vacant_can_not_be_repaired(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.repaired())

    def test_rooms_with_status_vacant_can_be_cleaned(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.cleaned())

    def test_rooms_with_status_vacant_can_be_marked_as_out_of_service(self):
        # Arrange
        room = Room("1A", Status.Vacant)
        # Action & # Assert
        self.assertRaises(Exception, lambda: room.out_of_service())




