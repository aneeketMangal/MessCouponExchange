from datetime import datetime
from typing import List
from src.MessCouponExchange.Coupons import Coupon
from src.MessCouponExchange.Services.Services import DB_INSTANCE
from src.MessCouponExchange.Coupons.Slots import Slots
from src.MessCouponExchange.Services import BOT_INSTANCE
from src.MessCouponExchange import Constants

@BOT_INSTANCE.message_handler(commands=[Constants.RETRACT])
def sell(message: object) -> None:
    '''Function to trigger on /show command'''
    try:
        messageJson = message.json
        user: str = f"@{messageJson['from']['username']}"
        messageComponents: List[str]  = messageJson['text'].split(" ")
        date: datetime = datetime.strptime(messageComponents[1], "%d/%m/%Y")
        slot: Slots = Slots(messageComponents[2])
        coupon: Coupon = Coupon(user = user, date = date, slot = slot)
        DB_INSTANCE.deleteCoupon(coupon)
        BOT_INSTANCE.reply_to(message, f"Your coupon has been retracted")
        print("dfsa")
        
    except Exception as e:
        print(e)
        BOT_INSTANCE.reply_to(message, f"Something went wrong. Try again!")
    