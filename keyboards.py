from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
def main_key():
    main_inline = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('🖨ساخت رسید جعلی📃',callback_data='1')
    main_inline.row(b1)
    b2 = InlineKeyboardButton('⏰رسید با تایم دلخواه⏰',callback_data='1')
    b3 = InlineKeyboardButton('🧾رسید پایا (شبا)🧾',callback_data='1')
    main_inline.row(b2,b3)
    b4 = InlineKeyboardButton('📩پیامک بانکی📩',callback_data='1')
    main_inline.row(b4)
    b5 = InlineKeyboardButton('💳رسید موجودی',callback_data='1')
    b6 = InlineKeyboardButton('📱رسید انتقال شارژ',callback_data='1')
    b7 = InlineKeyboardButton('📆رسید تراکنش اخیر',callback_data='1')
    main_inline.row(b5,b6,b7)
    b8 = InlineKeyboardButton('👤حساب کاربری👤',callback_data='1')
    main_inline.row(b8)
    b9 = InlineKeyboardButton('🪙جمع آوری سکه🪙',callback_data='1')
    b10 = InlineKeyboardButton('💸انتقال سکه💸',callback_data='1')
    main_inline.row(b9,b10)
    b11 = InlineKeyboardButton('🥇نفرات برتر زیر مجموعه گیری🥇',callback_data='1')
    main_inline.row(b11)
    b12 = InlineKeyboardButton('👨‍💻پشتیبانی ربات👨‍💻',callback_data='1')
    b13 = InlineKeyboardButton('⁉️راهنمای ربات⁉️',callback_data='1')
    main_inline.row(b12,b13)
    return main_inline

def none_replay_keyboard():
    k=ReplyKeyboardRemove()
    return k