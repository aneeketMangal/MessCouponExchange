import src.MessCouponExchange.Commands
from src.MessCouponExchange.Services import BOT_INSTANCE
import time

while True:
    try:
        BOT_INSTANCE.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)
