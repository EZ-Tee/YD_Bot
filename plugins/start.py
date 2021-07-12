from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel❤️", url="https://t.me/ez_bots")],
        [InlineKeyboardButton(
            "Contact us😊", url="https://t.me/tikka_bro")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}\n I'm Powerful Youtube Downloader BoT♥️ /n Use buttons for Download Youtube Videos, get help and Feedback.</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
