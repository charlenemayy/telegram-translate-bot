from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - '
                    + '%(levelname)s - %(message)s', level=logging.INFO)

# updates stored on server until bot recieves them
updater = Updater(token='649269167:AAHkrWbTcMYRlbg9mqCwB6x--uavzL_S2TU')
dispatcher = updater.dispatcher


# write message on command 'translate'
def translate(bot, update, args):
    # change to send to google translate api
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_caps)


translate_handler = CommandHandler('caps', translate, pass_args=True)
dispatcher.add_handler(translate_handler)


# inline handler
def inline_translate(bot, update):
    query = update.inline_query.query #text of the query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(), #converts to uppercase; later pass variable
            title='Translate',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results) #shows the results above text entry


inline_translate_handler = InlineQueryHandler(inline_translate)
dispatcher.add_handler(inline_translate_handler)

# poll updates from Telegram
updater.start_polling()
