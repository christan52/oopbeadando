from datetime import datetime
from Reservation import Reservation
class Hotel:

    def __init__(self, name, rooms):
        self._name = name
        self.rooms = rooms
        self.reservations = []


    def reserve_room(self, room_number, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Wrong format. Please use 'YYYY-MM-DD' format")
            return False

        room = next((r for r in self.rooms if r.room_number == room_number), None)
        if room is None:
            print("Invalid room number")
            return False

        for reservation in self.reservations:
            if reservation.date == date and reservation.room.room_number == room_number:
                print("This room is already booked on this day.")
                return False

        reservation = Reservation(room, date)
        self.reservations.append(reservation)
        print(f"Room {room_number} has been booked on {date}.")
        return True

    def cancel_reservation(self, room_number, date):

        for reservation in self.reservations:
            if reservation.room.room_number == room_number and reservation.date == date:
                self.reservations.remove(reservation)
                print(f"The reservation for room {room_number} on {date} is cancelled.")
                return True

        print(f"There is no reservation for room {room_number} on {date}.")
        return False