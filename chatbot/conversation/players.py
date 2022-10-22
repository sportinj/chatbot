from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext, ConversationHandler

from chatbot.conversation import states
from chatbot.conversation.schemas import JSON


def player_choice(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    assert context.user_data is not None
    question = 'Какой игрок?'
    context.user_data['choice'] = 'player'
    update.message.reply_text(question, reply_markup=ReplyKeyboardRemove())

    return states.PLAYER_STATS


def player_stats(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    player = update.message.text
    answer = f'Вот тебе статистика за {player}'
    update.message.reply_text(answer)

    return ConversationHandler.END
