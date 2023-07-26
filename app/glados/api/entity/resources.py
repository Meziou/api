from flask import request
from flask_restful import Resource
from glados.repositories.entities import *
from glados.repositories.rooms import *

from glados.api.entity.serializers import EntitiesRequestSerializer, EntityResponseSerializer
from glados.repositories.entities import get_entities


class EntitiesAPI(Resource):
    def get(self):
        request_serializer = EntitiesRequestSerializer()
        data = request_serializer.load(request.args)

        entities = get_entities(data)

        serializer = EntityResponseSerializer(many=True)
        return serializer.dump(entities), 200
    
    def post(self):
        data = request.get_json()
        create_entity(data)
        return {"message": "Entity created"}, 201

class EntityAPI(Resource):
    def get(self, entity_id):
        entity = get_entity(entity_id)
        if entity:
            serializer = EntityResponseSerializer()
            return serializer.dump(entity), 200
        else:
            return {"message": "Entity not found"}, 404

    def patch(self, entity_id):
        data = request.get_json()
        update_entity(entity_id, data)
        return {"message": "Entity updated"}, 200

    def delete(self, entity_id):
        delete_entity(entity_id)
        return {"message": "Entity deleted"}, 200

class RoomsAPI(Resource):
    def get(self):
        rooms = get_all_rooms()
        return [room.to_json() for room in rooms], 200