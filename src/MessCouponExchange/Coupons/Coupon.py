from typing import Optional
from src.MessCouponExchange.Coupons.Slots import Slots
import datetime
from pydantic import BaseModel


class Coupon(BaseModel):
    """model for coupon"""

    id: int
    username: str
    date: Optional[datetime.datetime]
    slot: Slots
    count: int = 1

    class Config:
        use_enum_values = True
