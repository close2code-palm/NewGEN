import datetime
import os
import random
from threading import Timer

import telegram
from telegram import Update, ForceReply, Bot
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters

from users import Contract

TOKEN = "<paste your token>"

def help_command(update: Update) -> None:
    """Prints  list of available commands"""
    #update.message.reply_text('Help!')

def start(update: Update) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Доброго дня {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def not_processable(update: Update) -> None:
    """unrecognised input"""
    update.message.reply_text("Не знаю")


def contact(update: Update) -> None:
    """Redirect to manager chat"""
    update.message.text("@New GEN")

def authorization():
    """Making users trusted, give them access
    by  auth on 'gosuslugi' or..."""
    pass


def  main() -> None:
    """Initialize bot"""

    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("contact", contact))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, not_processable))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


class FileDialog():
    """Realization of file signing by user"""

#documents = [for file in files os..filename]

    def __init__(self):

    def send_chosen_file(self, update: Update, documents):
        update.message.text(f'Доступные документы: {documents}')


    def update_file(self, update: Update, signed):
        #download
        update.message.text('Файлы обновлены')
        pass



if __name__ == '__main__':
    main()

    def dtnow():
        return datetime.date.today()

    shedule = dtnow.replace(day = dtnow.day +1,
                           hour = 9)
    delta_shed = shedule - dtnow

    def dateup(contract: Contract):
        #need to overwrite datetime __sub__
        contract_daystl = dtnow() - contract.expires
        if (contract_daystl < 7):
            if contract_daystl < 2:
               return f"{contract.id} почти расторгнут!!!"
            return f"Срок действия {contract.id} скоро истечёт."
        return


    def all_dateup():
        [dateup(x) for x in Contract.CONTRACTS]

    def all_users_ads(database):
        updater = Updater(TOKEN)
        users_id = database.do("SELECT id FROM users"
                            "WHERE role = 'User'")
        insurance_companies_names = database.do("SELECT name FROM users"
                                          "where role = 'IsnuranceCompany'")

        for tg_id in users_id:
            ad_ins = random.choice(insurance_companies_names)
            telegram.Bot.send_message(tg_id, ad_ins)


    task_sheded = Timer(delta_shed.seconds,[all_dateup(), all_users_ads()] )

    task_sheded.start()

