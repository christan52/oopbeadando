from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price


    @abstractmethod
    def get_room_type_extras(self):
        pass

