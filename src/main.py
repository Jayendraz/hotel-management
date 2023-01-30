from hotel import Hotel


def main():
    print("Hello Customer")
    hotel = Hotel()

    for rm in hotel.rooms:
        print(rm.room_number, rm.status.name)


if __name__ == "__main__":
    main()
