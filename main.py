from Room import Room
from Reservation import Reservation
from Hotel import Hotel
from SingleRoom import SingleRoom
from DoubleRoom import DoubleRoom
from abc import ABC, abstractmethod


def print_rooms(room_list):
    for room in room_list:
        if isinstance(room, SingleRoom):
            room_type = "Single Room"
        elif isinstance(room, DoubleRoom):
            room_type = "Double Room"
        else:
            room_type = "Other Room"

        print(f"Room number: {room.room_number}, Price: {room.price} Ft, Type: {room_type}")

        if isinstance(room, SingleRoom):
            print((f"Bathroom is in room: {room.bathroom}. \n"
                   f"Kitchen is in room: {room.kitchen}. \n"
                   f"Balcony is in room: {room.balcony}. \n"))
        elif isinstance(room, DoubleRoom):
            print((f"Bathroom is in room: {room.bathroom}.\n"
                   f"Kitchen is in room: {room.kitchen}.\n"
                   f"Balcony is in room: {room.balcony}.\n"))
        else:
            print("\tNo information.")

        print()


def list_all_reservations(hotel):
    if hotel.reservations:
        print(f"Reservations:")
        for reservation in hotel.reservations:
            room = reservation.room
            print(f"Room number: {room.room_number}, Price: {room.price} Ft, Date: {reservation.date}")
    else:
        print("There are no reservations at the moment.")


rooms = [
    SingleRoom(4000,10),
    SingleRoom(4500,11),
    SingleRoom(5000,12),

    DoubleRoom(8000,20),
    DoubleRoom(8500,21),
    DoubleRoom(9000,22)

]
hotel1 = Hotel("Grand Budapest Hotel", rooms)

reservations = [
    Reservation(rooms[0], "2024-05-10"),
    Reservation(rooms[1], "2024-05-15"),
    Reservation(rooms[2], "2024-05-20"),
    Reservation(rooms[3], "2024-05-25"),
    Reservation(rooms[4], "2024-05-30")
]

for reservation in reservations:
    hotel1.reservations.append(reservation)

user_interface = {
        "1": "Book a room.",
        "2": "Delete a booking",
        "3": "Check the rooms.",
        "4": "Check the reservations.",
        "5": "Room equipment",
        "0": "Exit"

    }

while True:
    for number, option in user_interface.items():
        print(f"{number} - {option}")

    number = input("Please choose from the list, type the number and press enter!\n")

    if number == "0":
        break
    elif number == "1":
        room_number = input("Let us know the number you want to reserve: ")
        date = input("Let us know the date: (Use this format : 'YYYY-MM-DD'): ")
        hotel1.reserve_room(int(room_number), date)

    elif number == "2":
        room_number = input("Let us know the reserved room number you want to cancel: ")
        date = input("Let us know the date (Use this format : 'YYYY-MM-DD'): ")
        hotel1.cancel_reservation(int(room_number), date)

    elif number == "3":
        print(" ")
        print_rooms(rooms)
        print(" ")

    elif number == "4":
        list_all_reservations(hotel1)

    elif number == "5":
        print("Room equipment:")
        for room in rooms:
            if isinstance(room, SingleRoom):
                print(f"Room: {room.room_number},",room.get_room_type_extras())
            elif isinstance(room, DoubleRoom):
                print(f"Room: {room.room_number},",room.get_room_type_extras())

    else:
        print("Wrong number! Choose a correct number.")
