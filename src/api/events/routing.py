from fastapi import APIRouter
from .schemas import EventSchema, EventlistSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()

@router.get("/")
def read_events() -> EventlistSchema:
    return {
        "results": [
            {"id": 1}, {"id": 2}, {"id": 3}
            ],
            "count": 3
    }

@router.post("/")
def create_event(payload: EventCreateSchema):
    print(payload)
    return {"id": 123}

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {
        "id": event_id
    }

@router.put("/{event_id}")
def get_event(event_id: int, payload:EventUpdateSchema) -> EventSchema:
    print(payload)
    return {
        "id": event_id
    }
