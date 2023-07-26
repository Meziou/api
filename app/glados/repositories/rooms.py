from glados.models import Room, Entity
from glados import db

def get_all_rooms(entity_id=None):
    query = Room.query

    if entity_id:
        query = query.join(Entity, Room.entities).filter(Entity.id == entity_id)

    return query.all()

def get_rooms_with_entities():
    try:
        rooms = Room.query.all()

        # Format the response to include the associated entities for each room
        response = []
        for room in rooms:
            room_data = {
                "id": room.id,
                "name": room.name,
                "created_at": room.created_at,
                "entities": [entity.to_json() for entity in room.entities]
            }
            response.append(room_data)

        return response
    except Exception as e:
        print("Error fetching rooms:", str(e))
        return []
