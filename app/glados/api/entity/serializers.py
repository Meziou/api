from marshmallow import fields, validate, Schema

from glados import ma, constants
from glados.models import Entity


class EntitiesRequestSerializer(ma.Schema):
    type = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityType]))
    status = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityStatus]))
    room = fields.String(required=False, validate=validate.OneOf([room.value for room in constants.Room]))


class EntitySerializer(ma.Schema):
    created_at = fields.DateTime("%Y-%m-%dT%H:%M:%S")

    class Meta:
        model = Entity
        ordered = True
        fields = [
            "id",
            "name",
            "type",
            "status",
            "value",
            "created_at"
        ]

class RoomSerializer(Schema):
    id = fields.UUID()
    name = fields.String()
    created_at = fields.DateTime(format="%Y-%m-%dT%H:%M:%S")

class EntityResponseSerializer(EntitySerializer):
    room = fields.String(attribute="room.name")

    class Meta:
        model = Entity
        ordered = True
        fields = [
            "id",
            "name",
            "type",
            "status",
            "value",
            "created_at",
            "room"  # Add the room field to the serializer
        ]
    pass