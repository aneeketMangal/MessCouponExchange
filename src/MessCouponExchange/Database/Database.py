from datetime import datetime
from typing import Any, List
from pymongo import MongoClient
from src.MessCouponExchange import Constants
from src.MessCouponExchange.Coupons import Slots, Coupon


class DatabaseProvider:
    """
    class for database operations
    """

    def __init__(self, uri: str) -> None:
        self.client = MongoClient(uri)
        self.db = self.client.MessCouponExchange
        self.collection = self.db.coupons

    def addCoupons(self, data: Coupon) -> None:
        """function for inserting one coupon entry"""
        finalCouponCount: int = data.count
        print(data.slot)
        resp: Any = self.collection.find_one(
            {
                Constants.USER: data.user,
                Constants.DATE: data.date,
                Constants.SLOT: data.slot,
            }
        )

        if resp:
            finalCouponCount += resp[Constants.COUNT]

        self.collection.update_one(
            {
                Constants.USER: data.user,
                Constants.DATE: data.date,
                Constants.SLOT: data.slot,
            },
            {"$set": {Constants.COUNT: finalCouponCount}},
            upsert=True,
        )

    def findCoupons(self, date: datetime, slot: Slots) -> List[Coupon]:
        """function for finding coupon entries"""
        resp = self.collection.find({"date": date, "slot": slot.value})
        return [Coupon(**i) for i in resp]

    def deleteCoupon(self, data: Coupon) -> bool:
        """function for deleting coupon entry"""
        resp: Any = self.collection.find_one(
            {
                Constants.USER: data.user,
                Constants.DATE: data.date,
                Constants.SLOT: data.slot,
            }
        )
        finalCouponCount: int = 0
        isCouponInDatabase: bool = False

        if resp:
            finalCouponCount = resp[Constants.COUNT] - data.count
            isCouponInDatabase = True

        if finalCouponCount < 0 or isCouponInDatabase is False:
            return False

        if finalCouponCount == 0:
            self.collection.delete_one(
                {
                    Constants.USER: data.user,
                    Constants.DATE: data.date,
                    Constants.SLOT: data.slot,
                }
            )

            return True

        self.collection.update_one(
            {
                Constants.USER: data.user,
                Constants.DATE: data.date,
                Constants.SLOT: data.slot,
            },
            {"$set": {Constants.COUNT: finalCouponCount}},
            upsert=True,
        )

        return True
