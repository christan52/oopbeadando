from Room import Room


class SingleRoom(Room):

    def __init__(self, price, room_number):
        super().__init__(price=price, room_number=room_number)
        self.bathroom = True
        self.kitchen = False
        self.balcony = False

    def get_room_type_extras(self):
        return "Single room has bathroom, but no kitchen and balcony."

