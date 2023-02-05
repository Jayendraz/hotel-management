import unittest
from src.controls.hotel_control import HotelControl


class TestRoomFunctions(unittest.TestCase):

    def setUp(self):
        self.hotel_control = HotelControl()

    def tearDown(self):
        self.hotel_control = None

    def test_hotel_should_have_four_floors(self):
        # Arrange
        expected_floors = 4
        # Action
        actual_floors = self.hotel_control.hotel.Floors
        # Assert
        self.assertEqual(expected_floors, actual_floors)

    def test_hotel_should_have_twenty_rooms(self):
        # Arrange
        expected_rooms = 20
        # Action
        actual_rooms = len(self.hotel_control.get_all_rooms())
        # Assert
        self.assertEqual(expected_rooms, actual_rooms)

    def test_invalid_room_number_input_should_return_error(self):
        # Arrange
        self.hotel_control.assign_room()
        expected_response = "Error!! Please input valid room number"
        # Action
        actual_response = self.hotel_control.check_out_room("5M")
        # Assert
        self.assertEqual(expected_response, actual_response)

    def test_should_get_list_of_all_available_rooms_in_hotel(self):
        # Arrange
        self.hotel_control.assign_room()
        self.hotel_control.assign_room()
        expected_number_of_available_rooms = 18
        # Action
        available_room_list = self.hotel_control.get_all_available_rooms()
        # Assert
        self.assertEqual(type(available_room_list), list)
        self.assertEqual(expected_number_of_available_rooms, len(available_room_list))

    def test_should_return_empty_list_of_available_rooms_if_hotel_is_full(self):
        # Arrange
        for room in self.hotel_control.hotel.rooms:
            self.hotel_control.room_control.check_in(room)
        expected_number_of_available_rooms = 0
        expected_response = "Error! - No room is available"
        # Action
        available_room_list = self.hotel_control.get_all_available_rooms()
        # Assert
        self.assertEqual(expected_number_of_available_rooms, len(available_room_list))

    def test_should_assign_room_having_nearest_entrance_in_empty_hotel(self):
        # Arrange
        expected_room_number = "1A"
        # Action
        actual_room_number = self.hotel_control.assign_room()
        # Assert
        self.assertEqual(expected_room_number, actual_room_number)

    def test_should_assign_nearest_to_entrance_room_if_that_room_is_available(self):
        # Arrange
        # create MOCK hotel object with mixed room status
        self.hotel_control.assign_room()  # 1A
        self.hotel_control.assign_room()  # 1B
        self.hotel_control.assign_room()  # 1C
        self.hotel_control.assign_room()  # 1D
        self.hotel_control.check_out_room("1B")
        self.hotel_control.clean_room("1B")
        expected_room_number = "1B"
        # Action
        actual_room_number = self.hotel_control.assign_room()
        # Assert
        self.assertEqual(expected_room_number, actual_room_number)

    def test_room_should_not_be_assigned_when_hotel_is_full(self):
        # Arrange
        for room in self.hotel_control.hotel.rooms:
            self.hotel_control.room_control.check_in(room)
        expected_response = "Sorry! Hotel is full"
        # Action
        actual_response = self.hotel_control.assign_room()
        # Assert
        self.assertEqual(expected_response, actual_response)
