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
    KITCHEN = "Kitchen"
    LIVING_ROOM = "Living Room"
    BEDROOM = "Bedroom"
    BATHROOM = "Bathroom"