from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext, ConversationHandler

from chatbot.conversation import states
from chatbot.conversation.schemas import JSON

reply_keyboard = [
    ['Team', 'Player'],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def start(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Start the conversation and ask user for input."""
    question = """Привет.
Команда или игрок?
    """
    assert update.message is not None
    update.message.reply_text(text=question, reply_markup=markup)

    return states.CHOOSING


def cancel(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    question = 'Всего хорошего'
    update.message.reply_text(question)

    return ConversationHandler.END
