from hotel import Hotel
from housekeeper import HouseKeeper


def main():
    hotel = Hotel()
    hotel.set_housekeeper(HouseKeeper("John", hotel))
    app_running = True
    while app_running:
        banner()
        print("Enter option: ")
        user_input = int(input())

        if user_input == 1:
            room_number = hotel.assign_room()
            print(room_number, "has assign to you.")
        elif user_input == 2:
            rm_num = room_number_input()

            hotel.check_out_room(rm_num)
        elif user_input == 3:
            rm_num = room_number_input()
            hotel.housekeeper.clean_room(rm_num)
            #hotel.clean_room(rm_num)
        elif user_input == 4:
            rm_num = room_number_input()
            mark_room_out_of_service(rm_num)
        elif user_input == 5:
            rm_num = room_number_input()
            hotel.repair_room(rm_num)
        elif user_input == 6:
            app_running = False


def room_number_input():
    print("Please enter room number: ")
    return input()


def header():
    print("------------------------------------------------")
    print("               Hotel Management                 ")


def banner():
    print("------------------------------------------------")
    print("1. Checkin")
    print("2. Checkout ")
    print("3. Clean Room")
    print("4. Mark Out Of Service")
    print("5. Repair")
    print("6. Exit")
    print("------------------------------------------------")


if __name__ == "__main__":
    main()
