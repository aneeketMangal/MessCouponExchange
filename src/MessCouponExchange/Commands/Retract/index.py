from datetime import datetime
from typing import List
from src.MessCouponExchange.Coupons import Coupon
from src.MessCouponExchange.Services.Services import DB_INSTANCE
from src.MessCouponExchange.Coupons.Slots import Slots
from src.MessCouponExchange.Services import BOT_INSTANCE
from src.MessCouponExchange import Constants


@BOT_INSTANCE.message_handler(commands=[Constants.RETRACT])
def sell(message: object) -> None:
    """Function to trigger on /show command"""
    try:
        messageJson = message.json
        user: str = f"@{messageJson['from']['username']}"
        messageComponents: List[str] = messageJson["text"].split(" ")
        date: datetime = datetime.strptime(messageComponents[1], "%d/%m/%Y")
        slot: Slots = Slots(messageComponents[2])
        count = 1

        if len(messageComponents) > 3:
            count = int(messageComponents[3])

        count = int(messageComponents[3])
        coupon: Coupon = Coupon(user=user, date=date, slot=slot, count=count)

        resp: bool = DB_INSTANCE.deleteCoupon(coupon)
        if not resp:
            BOT_INSTANCE.send_message(message.chat.id, "Not enough coupons to delete")
            return

        BOT_INSTANCE.reply_to(message, f"Your coupon has been retracted")
        print("dfsa")

    except Exception as e:
        print(e)
        BOT_INSTANCE.reply_to(message, f"Something went wrong. Try again!")
