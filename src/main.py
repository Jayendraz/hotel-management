from hotel import Hotel


def main():
    print("Hello Customer")
    hotel = Hotel()
    app_running = True
    while app_running:
        print("------------------------------------------------")
        print("               Hotel Management                 ")
        print("------------------------------------------------")
        print("1. Checkin")
        print("2. Checkout ")
        print("3. Clean Room")
        print("4. Mark Out Of Service")
        print("5. Repair")
        print("6. Exit")
        print("------------------------------------------------")
        print("Enter option: ")
        user_input = int(input())

        if user_input == 1:
            room_number = hotel.assign_room()
            print(room_number, "has assign to you.")
        elif user_input == 2:
            print("Please enter room number: ")
            user_input = input()
            # case: non checked in room should throw error
            hotel.check_out_room(user_input)
        elif user_input == 3:
            print("Please enter room number: ")
            user_input = input()
            hotel.clean_room(user_input)
        elif user_input == 4:
            print("Please enter room number: ")
            user_input = input()
            hotel.mark_room_out_of_service(user_input)
        elif user_input == 5:
            print("Please enter room number: ")
            user_input = input()
            hotel.repair_room(user_input)
        elif user_input == 6:
            app_running = False

'''
    available_rooms = hotel.get_all_available_rooms()
    print("---", len(available_rooms), "---")
    for i in range(10):
        room_number = hotel.assign_room()
        print(room_number)
    available_rooms = hotel.get_all_available_rooms()
    print("---", len(available_rooms), "---")

    hotel.check_out_room("1B")
    hotel.check_out_room("1D")
    hotel.check_out_room("2B")

    all_rooms = hotel.get_all_rooms()

    for room in all_rooms:
        if room.get_status() == Status.Vacant:
            print(room.room_number)

    print("----Cleaning-----")

    hotel.clean_room("2B")
    hotel.clean_room("1D")

    print("----Cleaning Complete-----")

    room_number = hotel.assign_room()
    print(room_number)
'''

if __name__ == "__main__":
    main()
