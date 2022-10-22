from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler

from chatbot.conversation import states
from chatbot.conversation.core import cancel, start
from chatbot.conversation.players import player_choice, player_stats
from chatbot.conversation.teams import team_choice, team_stats

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        states.CHOOSING: [
            MessageHandler(
                Filters.regex('^(Team|команда)$'), team_choice,
            ),

            MessageHandler(
                Filters.regex('^(Player|игрок)$'), player_choice,
            ),
        ],
        states.TEAM_STATS: [
            MessageHandler(
                Filters.text, team_stats,
            ),
        ],
        states.PLAYER_STATS: [
            MessageHandler(
                Filters.text, player_stats,
            ),
        ],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
