from glados.models import Entity
from glados import db
from flask import request


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
    entity = Entity(**data) 
    db.session.add(entity)  
    db.session.commit()  

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