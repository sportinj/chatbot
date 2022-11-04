from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext, ConversationHandler

from chatbot.clients.api import client
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
    player_name = update.message.text
    if not player_name:
        update.message.reply_text('Введите имя игрока')
        return states.PLAYER_STATS

    players = client.players.find_by_name(player_name)
    if not players:
        update.message.reply_text('Сожалеем, но данных по этому игроку нет')
        return ConversationHandler.END

    if len(players) > 1:
        player_names = '\n'.join([player.name for player in players])
        update.message.reply_text(f'Выберите одного игрока из:\n\n{player_names}')
        return states.PLAYER_STATS

    player = players[0]

    injuries = client.players.get_injuries(player.uid)
    if not injuries:
        update.message.reply_text('По данному игроку нет информации о травмах')
        return ConversationHandler.END

    injuries_info = '\n\n'.join([injury.display() for injury in injuries])

    answer = f'Список травм по игроку {player.name}:\n\n{injuries_info}'
    update.message.reply_text(answer)

    return ConversationHandler.END
