from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,  RegexHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from search import search_title
from goo_search import google_search
from uuid import uuid4
import logging
import settings
import telegram
import re


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(update, context):
    text = f'Привет! Это поисковой бот канала\
            <a href="http://t.me/podrec">*Рекомендации подкастов*</a>.\
            Для поиска подкаста используйте кобанду /search' 
    my_keyboard = ReplyKeyboardMarkup([["Старт", "Поиск"]])
    update.message.reply_text(text, reply_markup=my_keyboard, 
                                parse_mode=telegram.ParseMode.HTML,
                                disable_web_page_preview=True)


def show_inline(update, user_data):
    inlinekeyboard = [[InlineKeyboardButton("Apple Podcasts", callback_data='1'),
                    InlineKeyboardButton("Google Podcasts", callback_data='0')]]
    reply_markup = InlineKeyboardMarkup(inlinekeyboard)
    update.message.reply_text('Где будем искать?', reply_markup=reply_markup)


def search_pod(update, context):
    user_text = update.message.text
    pattern = r'[a-zA-z]'  
    check_lang = re.findall(pattern, user_text)
    if check_lang:
        update.message.reply_text('Только кириллица, только хардкор!')
    else:    
        try:
            
            for key in context.user_data:
                value = context.user_data[key]
            
            if value:
                result = search_title(user_text)
                for url in result:
                    text = f'<a href="{url}">Открыть</a>'
                    context.bot.send_message(chat_id=update.message.chat_id, text=text, 
                    parse_mode=telegram.ParseMode.HTML)
            else:
                goo_result = google_search(user_text)
                for url in goo_result:
                    text_goo = f'<a href="{url}">Открыть</a>'
                    context.bot.send_message(chat_id=update.message.chat_id, text=text_goo,
                    parse_mode=telegram.ParseMode.HTML)

        except KeyError:
            update.message.reply_text('Not found')
   
    
def inline_button_pressed(update, context):
    query = update.callback_query
    text = "Введите ключевое слово для поиска"
    try:
        data = int(query.data)
        key = str(uuid4())
        context.user_data[key] = data
    except TypeError:
        text = "Что-то пошло не так :-("
    context.bot.edit_message_text(text=text, chat_id=query.message.chat.id,
            message_id=query.message.message_id)
    

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)

    logging.info('Bot start')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("search", show_inline, pass_user_data=True))
    dp.add_handler(RegexHandler("^(Старт)$", greet_user))
    dp.add_handler(RegexHandler("^(Поиск)$", show_inline, pass_user_data=True))
    dp.add_handler(CallbackQueryHandler(inline_button_pressed))
    dp.add_handler(MessageHandler(Filters.text, search_pod))

    mybot.start_polling()
    mybot.idle()

main()
         