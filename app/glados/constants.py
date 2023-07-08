import enum


class EntityType(enum.IntEnum):
    sensor = 1
    light = 2
    switch = 3
    multimedia = 4
    air_conditioner = 5


class EntityStatus(enum.IntEnum):
    on = 1
    off = 2
    unavailable = 3

class Room(enum.Enum):
    kitchen = "kitchen"
    living_room = "living_room"
    bedroom = "bedroom"
