import unittest
from src import Hotel
from src import Status


class TestRoomFunctions(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel()

    def tearDown(self):
        self.hotel = None

    def test_should_get_list_of_all_available_rooms_in_hotel(self):
        # Arrange
        self.hotel.assign_room()
        self.hotel.repair_room("1D")
        self.hotel.mark_room_out_of_service("3E")
        expected_number_of_available_rooms = 17
        # Action
        available_room_list = self.hotel.get_all_available_rooms()
        # Assert
        self.assertEqual(type(available_room_list), list)
        self.assertEqual(len(available_room_list), expected_number_of_available_rooms)

    def test_should_return_empty_list_of_available_rooms_if_hotel_is_full(self):
        # Arrange
        for room in self.hotel.rooms:
            room.check_in()
        expected_number_of_available_rooms = 0
        expected_response = "Error! - No room is available"
        # Action
        available_room_list = self.hotel.get_all_available_rooms()
        # Assert
        self.assertEqual(len(available_room_list), expected_number_of_available_rooms)

    def test_should_assign_room_having_nearest_entrance_in_empty_hotel(self):
        # Arrange
        expected_room_number = "1A"
        # Action
        actual_room_number = self.hotel.assign_room()
        # Assert
        self.assertEqual(actual_room_number, expected_room_number)

    def test_should_assign_nearest_to_entrance_room_if_that_room_is_available(self):
        # Arrange
        # create MOCK hotel object with mixed room status
        guest1 = self.hotel.assign_room()  # 1A
        guest2 = self.hotel.assign_room()  # 1B
        guest3 = self.hotel.assign_room()  # 1C
        guest4 = self.hotel.assign_room()  # 1D
        self.hotel.clean_room("1B")
        expected_room_number = "1B"
        # Action
        actual_room_number = self.hotel.assign_room()
        # Assert
        self.assertEqual(actual_room_number, expected_room_number)

    def test_room_should_not_be_assigned_when_hotel_is_full(self):
        # Arrange
        for room in self.hotel.rooms:
            room.check_in()
        expected_response = "Error! - No room is available"
        # Action
        actual_response = self.hotel.assign_room()
        # Assert
        self.assertEqual(actual_response, expected_response)

    def test_rooms_with_status_available_should_not_be_repaired(self):
        # Arrange
        expected_response = "Error!! Available/Occupied room can not be marked as out of service"
        # Action
        actual_response = self.hotel.mark_room_out_of_service("1A")
        # Assert
        self.assertEqual(actual_response, expected_response)

    def test_rooms_with_status_occupied_should_not_be_repaired(self):
        # Arrange
        self.hotel.assign_room()  # 1A is occupied
        expected_response = "Error!! Available/Occupied room can not be marked as out of service"
        # Action
        actual_response = self.hotel.mark_room_out_of_service("1A")
        # Assert
        self.assertEqual(actual_response, expected_response)

