from datetime import datetime

from pydantic import BaseModel, ValidationError


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]


d = Delivery(timestamp="2025-02-12T11:45:34Z", dimensions=["10", "20"])
print(d.model_dump())

try:
    o = {"timestamp": "test", "dimensions": [10, 20]}
    Delivery(**o)
except ValidationError as e:
    print(e)
