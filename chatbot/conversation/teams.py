from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext, ConversationHandler

from chatbot.clients.api import client as api
from chatbot.conversation import states
from chatbot.conversation.schemas import JSON


def team_choice(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    assert context.user_data is not None

    teams = api.teams.get_all()
    team_names = [team.name for team in teams]

    question = 'Какую команду из {teams}?'.format(teams=','.join(team_names))
    context.user_data['choice'] = 'team'
    update.message.reply_text(question, reply_markup=ReplyKeyboardRemove())

    return states.TEAM_STATS


def team_stats(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Ask the user for info about the selected predefined choice."""
    assert update.message is not None
    team = update.message.text
    answer = f'Вот тебе статистика за {team}'
    update.message.reply_text(answer)

    return ConversationHandler.END
