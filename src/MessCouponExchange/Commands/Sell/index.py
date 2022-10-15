from socket import CAN_BCM_RX_TIMEOUT
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
from typing import List
from src.MessCouponExchange.Coupons import Coupon
from src.MessCouponExchange.InlineInput.CouponDataInput import gen_markup
from src.MessCouponExchange.Services.Services import DB_INSTANCE
from src.MessCouponExchange.Coupons.Slots import Slots
from src.MessCouponExchange.Services import BOT_INSTANCE
from src.MessCouponExchange import Constants


@BOT_INSTANCE.callback_query_handler(
    lambda query: query.data in ["cb_today", "cb_tomorrow"]
)
@BOT_INSTANCE.message_handler(commands=[Constants.SELL])
def sell(message: object) -> None:

    date: str = "Today"
    slot: Slots = Slots()

    def process_callback_1(query):
        if query.data == "cb_today":
            date = "Today"
        elif query.data == "cb_tomorrow":
            date = "Tomorrow"

    BOT_INSTANCE.send_message(
        message.chat.id, "When do you want to sell?", reply_markup=gen_markup()
    )
    BOT_INSTANCE.register_next_step_handler(message, process_callback_1)

    BOT_INSTANCE.send_message(message.chat.id, "What slot do you want to sell?")

    # """Function to trigger on /show command"""
    # try:

    #     messageJson = message.json
    #     id: int = messageJson["from"]["id"] if messageJson["from"]["id"] else -1
    #     username: str = (
    #         messageJson["from"]["first_name"]
    #         if messageJson["from"]["first_name"]
    #         else "Unknown"
    #     )
    #     messageComponents: List[str] = messageJson["text"].split(" ")
    #     date: datetime = datetime.strptime(messageComponents[1], "%d/%m/%Y")
    #     currentDate: datetime = datetime.now()

    #     if date.date() < currentDate.date():
    #         BOT_INSTANCE.reply_to(message, "Date cannot be in the past")
    #         return

    #     if (date - currentDate).days > 2:
    #         BOT_INSTANCE.reply_to(
    #             message, "Date cannot be more than 2 days in the future"
    #         )
    #         return

    #     slot: Slots = Slots(messageComponents[2])
    #     count = 1
    #     if len(messageComponents) > 3:
    #         count = int(messageComponents[3])
    #     coupon: Coupon = Coupon(
    #         id=id, username=username, date=date, slot=slot, count=count
    #     )
    #     print(coupon)
    #     DB_INSTANCE.addCoupons(coupon)
    #     BOT_INSTANCE.reply_to(
    #         message, "Your coupon details have been added to database!"
    #     )
    #     print("dfsa")

    # except Exception as e:
    #     print("errorShow", e)
    #     BOT_INSTANCE.reply_to(message, "Some error encoutered try again!")
