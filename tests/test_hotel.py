import unittest
from src import Hotel
from src import Status


class TestRoomFunctions(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel()

    def tearDown(self):
        self.hotel = None

    def test_hotel_should_have_four_floors(self):
        # Arrange
        expected_floors = 4
        # Action
        actual_floors = self.hotel.Floors
        # Assert
        self.assertEqual(expected_floors, actual_floors)

    def test_hotel_should_have_twenty_rooms(self):
        # Arrange
        expected_rooms = 20
        # Action
        actual_rooms = len(self.hotel.get_all_rooms())
        # Assert
        self.assertEqual(expected_rooms, actual_rooms)

    def test_should_get_list_of_all_available_rooms_in_hotel(self):
        # Arrange
        self.hotel.assign_room()
        self.hotel.repair_room("1D")
        expected_number_of_available_rooms = 18
        # Action
        available_room_list = self.hotel.get_all_available_rooms()
        # Assert
        self.assertEqual(type(available_room_list), list)
        self.assertEqual(expected_number_of_available_rooms, len(available_room_list))

    def test_should_return_empty_list_of_available_rooms_if_hotel_is_full(self):
        # Arrange
        for room in self.hotel.rooms:
            room.check_in()
        expected_number_of_available_rooms = 0
        expected_response = "Error! - No room is available"
        # Action
        available_room_list = self.hotel.get_all_available_rooms()
        # Assert
        self.assertEqual(expected_number_of_available_rooms, len(available_room_list))

    def test_should_assign_room_having_nearest_entrance_in_empty_hotel(self):
        # Arrange
        expected_room_number = "1A"
        # Action
        actual_room_number = self.hotel.assign_room()
        # Assert
        self.assertEqual(expected_room_number, actual_room_number)

    def test_should_assign_nearest_to_entrance_room_if_that_room_is_available(self):
        # Arrange
        # create MOCK hotel object with mixed room status
        self.hotel.assign_room()  # 1A
        self.hotel.assign_room()  # 1B
        self.hotel.assign_room()  # 1C
        self.hotel.assign_room()  # 1D
        self.hotel.clean_room("1B")
        expected_room_number = "1B"
        # Action
        actual_room_number = self.hotel.assign_room()
        # Assert
        self.assertEqual(expected_room_number, actual_room_number)

    def test_room_should_not_be_assigned_when_hotel_is_full(self):
        # Arrange
        for room in self.hotel.rooms:
            room.check_in()
        expected_response = "Sorry! Hotel is full"
        # Action
        actual_response = self.hotel.assign_room()
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_rooms_with_status_available_should_not_be_repaired(self):
        # Arrange
        expected_response = "Error! Available/Occupied room can not be marked as out of service"
        # Action
        actual_response = self.hotel.mark_room_out_of_service("1A")
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_rooms_with_status_occupied_should_not_be_repaired(self):
        # Arrange
        self.hotel.assign_room()  # 1A is occupied
        expected_response = "Error! Available/Occupied room can not be marked as out of service"
        # Action
        actual_response = self.hotel.mark_room_out_of_service("1A")
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_invalid_room_number_input_should_return_error(self):
        # Arrange
        self.hotel.assign_room()
        expected_response = "Error!! Please input valid room number"
        # Action
        actual_response = self.hotel.check_out_room("5M")
        # Assert
        self.assertEqual(expected_response, actual_response)



