## Copyright Ilham mansiz


from Data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from .Nande import nande

ERROR_MESSAGE = "Oops! \n\n**Error kack🥺** : {} " \
            "\n\nTolong Laporan ke @Klyuserbot jika eror "

# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )

    elif query in ["nande", "dev"]:
        await callback_query.answer()
        try:
            if query == "nande":
                await nande(bot, callback_query.message, dev=True)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))

