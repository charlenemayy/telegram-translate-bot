from telegram.ext import Updater
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googletrans import Translator
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - '
                    + '%(levelname)s - %(message)s', level=logging.INFO)

# updates stored on server until bot recieves them
updater = Updater(token='649269167:AAHkrWbTcMYRlbg9mqCwB6x--uavzL_S2TU')
dispatcher = updater.dispatcher

# initalize translate api
translator = Translator()


# inline handler
# eventually make dynamic instead
# of having to write new translate line per language
def inline_translate(bot, update):
    query = update.inline_query.query  # text of the query
    if not query:
        return
    results = list()
    # russian
    ru_text = translator.translate(query, dest='ru').text
    results.append(
        InlineQueryResultArticle(
            id=ru_text,
            title='Russian',
            input_message_content=InputTextMessageContent(ru_text)
        )
    )
    # english
    en_text = translator.translate(query, dest='en').text
    results.append(
        InlineQueryResultArticle(
            id=en_text,
            title='English',
            input_message_content=InputTextMessageContent(en_text)
        )
    )
    # shows the results above text entry
    bot.answer_inline_query(update.inline_query.id, results)


inline_translate_handler = InlineQueryHandler(inline_translate)
dispatcher.add_handler(inline_translate_handler)

# poll updates from Telegram
updater.start_polling()
