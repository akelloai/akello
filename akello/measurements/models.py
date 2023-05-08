from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class MeasurementConfig(BaseModel):
    account_id: str
    user_id: str
    measure: str
    min: float = None
    max: float = None
    callback: str = None
    base_timestamp: int = None
