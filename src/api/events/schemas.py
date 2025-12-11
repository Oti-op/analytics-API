from pydantic import BaseModel, Field
from typing import List, Optional

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
    page: Optional[str] = ""
    description: Optional[str] = Field(default="my description")

class EventlistSchema(BaseModel):
    results: List[EventSchema]
    count: int