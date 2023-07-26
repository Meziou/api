from glados.models import Entity, Room
from glados import db
from flask import request
from sqlalchemy.exc import SQLAlchemyError

def get_entities(filters):
    query = Entity.query

    type = filters.get("type")
    if type:
        query = query.filter(Entity.type == type)

    room = filters.get("room")
    if room:
        query = query.filter(Entity.room.has(name=room))

    status = filters.get("status")
    if status:
        query = query.filter(Entity.status == status)

    return query.all()

def create_entity(data):
    try:
        room_name = data.pop("room")
        room = Room.query.filter_by(name=room_name).first()
        if room:
            entity = Entity(**data)
            entity.room = room
            db.session.add(entity)
            db.session.commit()
            print("Entity created:", entity)
        else:
            print("Room not found for name:", room_name)
    except SQLAlchemyError as e:
        db.session.rollback()  # Annule toute transaction en cas d'erreur
        print("Error creating entity:", str(e))

def get_entity(entity_id):
    return Entity.query.get(entity_id)  

def update_entity(entity_id, data):
    entity = Entity.query.get(entity_id)  
    if entity:
        for key, value in data.items():
            setattr(entity, key, value)  
        db.session.commit()  

def delete_entity(entity_id):
    entity = Entity.query.get(entity_id)  
    if entity:
        db.session.delete(entity)
        db.session.commit()  