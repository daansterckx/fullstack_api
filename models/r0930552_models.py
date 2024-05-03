from pydantic import BaseModel
from datetime import datetime

class Tour(BaseModel):
    tour_id: int
    tour_name: str
    description: str
    tour_date: datetime
    max_attendees: int

tour_data = {
    "tour_id": 1,
    "tour_name": "Tour 1",
    "description": "This is a tour",
    "tour_date": datetime.now(),
    "max_attendees": 10
}

tour = Tour(**tour_data)