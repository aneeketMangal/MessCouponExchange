from datetime import datetime
from typing import List
from pymongo import MongoClient
from src.MessCouponExchange.Coupons import Slots, Coupon

class DatabaseProvider:
    """
    class for database operations
    """
    def __init__(self, uri: str) -> None:
        self.client = MongoClient(uri)
        self.db = self.client.MessCouponExchange
        self.collection = self.db.coupons

    def addCoupon(self, data: Coupon) -> None:
        """function for inserting one coupon entry"""
        print(data.dict())
        self.collection.insert_one(data.dict())

    def findCoupons(self, date: datetime, slot: Slots) -> List[Coupon]:
        '''function for finding coupon entries'''
        print(date, slot.value)
        resp = self.collection.find({'date': date, 'slot': slot.value})
        return [Coupon(**i) for i in resp]
        
    def deleteCoupon(self, data: Coupon) -> None:
        '''function for deleting coupon entry'''
        self.collection.delete_one(data.dict())
