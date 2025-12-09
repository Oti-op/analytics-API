from pydantic import BaseModel
from typing import List

'''
id
path
description
'''


class EventCreateSchema(BaseModel):
    path: str

class EventUpdateSchema(BaseModel):
    description: str

class EventSchema(BaseModel):
    id: int

class EventlistSchema(BaseModel):
    results: List[EventSchema]
    count: int