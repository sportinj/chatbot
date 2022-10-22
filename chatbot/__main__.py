import logging
import os
from typing import Any

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    ConversationHandler,
    Filters,
    MessageHandler,
    Updater,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
CHOOSING = 1
TEAM_STATS = 2
PLAYER_STATS = 3

reply_keyboard = [
    ['Team', 'Player'],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

JSON = dict[str, Any]


def start(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Start the conversation and ask user for input."""
    question = """Привет.
Команда или игрок?
    """
    assert update.message is not None
    update.message.reply_text(text=question, reply_markup=markup)

    return CHOOSING


def team_choice(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    assert context.user_data is not None
    question = 'Какую команду?'
    context.user_data['choice'] = 'team'
    update.message.reply_text(question, reply_markup=ReplyKeyboardRemove())

    return TEAM_STATS


def player_choice(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    assert context.user_data is not None
    question = 'Какой игрок?'
    context.user_data['choice'] = 'player'
    update.message.reply_text(question, reply_markup=ReplyKeyboardRemove())

    return PLAYER_STATS


def cancel(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    question = 'Всего хорошего'
    update.message.reply_text(question)

    return ConversationHandler.END


def team_stats(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    team = update.message.text
    answer = f'Вот тебе статистика за {team}'
    update.message.reply_text(answer)

    return ConversationHandler.END


def player_stats(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    player = update.message.text
    answer = f'Вот тебе статистика за {player}'
    update.message.reply_text(answer)

    return ConversationHandler.END


def main():
    logger.info('hello, world')
    updater = Updater(os.environ['BOT_TOKEN'])

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(Team|команда)$'), team_choice,
                ),

                MessageHandler(
                    Filters.regex('^(Player|игрок)$'), player_choice,
                ),
            ],
            TEAM_STATS: [
                MessageHandler(
                    Filters.text, team_stats,
                ),
            ],
            PLAYER_STATS: [
                MessageHandler(
                    Filters.text, player_stats,
                ),
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
