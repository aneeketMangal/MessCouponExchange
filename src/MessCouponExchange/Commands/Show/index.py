from datetime import datetime
from typing import List
from src.MessCouponExchange.Coupons import Coupon
from src.MessCouponExchange.Services.Services import DB_INSTANCE
from src.MessCouponExchange.Coupons.Slots import Slots
from src.MessCouponExchange.Services import BOT_INSTANCE
from src.MessCouponExchange import Constants


@BOT_INSTANCE.message_handler(commands=[Constants.SHOW])
def sell(message: object) -> None:
    """Function to trigger on /show command"""
    try:
        messageJson = message.json
        messageComponents: List[str] = messageJson["text"].split(" ")
        date: datetime = datetime.strptime(messageComponents[1], "%d/%m/%Y")
        slot: Slots = Slots(messageComponents[2])
        couponList: List[Coupon] = DB_INSTANCE.findCoupons(date, slot)

        if len(couponList) == 0:
            BOT_INSTANCE.reply_to(message, "No coupons found for this date and slot")
            return

        respList: List[str] = []

        for coupon in couponList:
            respList.append(
                f"'['+{coupon.name}+'](tg://user?id='+str({coupon.id})+')' {coupon.date.strftime('%d/%m/%Y')} {coupon.slot} {coupon.count}"
            )
        BOT_INSTANCE.reply_to(message, ("\n").join(respList))

    except Exception as e:
        BOT_INSTANCE.reply_to(message, f"Something went wrong! Try again!")
