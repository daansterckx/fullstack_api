from pydantic import BaseModel
from datetime import datetime

class Delivery(BaseModel):
    delivery_id: int
    location_name: str
    location_address: str
    delivery_date: datetime
    product_name: str
    product_count: int
