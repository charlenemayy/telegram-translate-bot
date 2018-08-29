'''
 Charlene May
 translates typed messages in Telegram text box
 (languages recommended by friends) and sends
 the resulted translated text as a message
'''
from telegram.ext import Updater
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googletrans import Translator
import logging
import uuid

logging.basicConfig(format='%(asctime)s - %(name)s - '
                    + '%(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='649269167:AAHkrWbTcMYRlbg9mqCwB6x--uavzL_S2TU')
dispatcher = updater.dispatcher

# intialize google translate api
translator = Translator()

# don't want to import all available languages yet
languages = {'en': 'English', 'ru': 'Russian', 'es': 'Spanish',
             'ar': 'Arabic', 'fil': 'Tagalog', 'ja': 'Japanese'}


# to-do: slow loading time for bot; improve efficiency
# inline handler; loads available languages as buttons; change
# to horizontal format
def inline_translate(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    for k, v in languages.items():
        trans_text = translator.translate(query, dest=k).text
        results.append(
            InlineQueryResultArticle(
                id=uuid.uuid4(),
                title=v,
                input_message_content=InputTextMessageContent(trans_text)
            )
        )

    # shows the results above text entry
    bot.answer_inline_query(update.inline_query.id, results)


# add handler to telegram bot
inline_translate_handler = InlineQueryHandler(inline_translate)
dispatcher.add_handler(inline_translate_handler)

updater.start_polling()
