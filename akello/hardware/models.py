from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):

    first_name: str
    last_name: str
    phone_number: str  # must be in +1xxxxxxxxxx format
    birthday: int

    address_1: str
    address_2: str = None
    city: str
    state: str
    zip: str
    country: str # must be US

    gender: str
    preflang: str # en_US
    measures: str
    unit_pref: str
    timezone: str
    shortname: str

class Device(BaseModel):
    ean: str

class WithingsOrder(BaseModel):
    user: User
    device: Device