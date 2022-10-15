from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Today", callback_data="cb_today"),
        InlineKeyboardButton("Tomorrow", callback_data="cb_tomorrow"),
    )
    return markup
