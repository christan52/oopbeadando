from Room import Room


class DoubleRoom(Room):

    def __init__(self, price, room_number):
        super().__init__(price=price, room_number=room_number)
        self.bathroom = True
        self.kitchen = True
        self.balcony = True

    def get_room_type_extras(self):
        return "Double room has bathroom, kitchen and balcony as well."

