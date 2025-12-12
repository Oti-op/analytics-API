import os
from fastapi import APIRouter
from .schemas import EventSchema, EventlistSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()

@router.get("/")
def read_events() -> EventlistSchema:
    print(os.environ.get)
    return {
        "results": [
            {"id": 1}, {"id": 2}, {"id": 3}
            ],
            "count": 3
    }

@router.post("/")
def create_event(payload: EventCreateSchema):
    data = payload.model_dump() # payload -> dict -> pydantic
    return {"id": 123, **data}

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {
        "id": event_id
    }

@router.put("/{event_id}")
def get_event(event_id: int, payload:EventUpdateSchema) -> EventSchema:
    return {
        "id": event_id, **data
    }

#hdn