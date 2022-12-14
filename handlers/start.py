import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("https://telegra.ph//file/eb71290c9beba9dcda6c1.jpg")
    await message.reply_photo("
        photo=f"{START_IMG}",
        caption=f""" ** ๐๐ฒ๐น๐น๐ผ ๐๐ถ๐ฟ {message.from_user.mention()} , ๐ฅ\n\n
เน๐ง๐ต๐ถ๐ ๐ถ๐ [{bn}](t.me/{bu}) ,  !
โป ๐ง๐ต๐ฒ ๐บ๐ผ๐๐ ๐ฝ๐ผ๐๐ฒ๐ฟ๐ณ๐๐น ๐๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ ๐บ๐๐๐ถ๐ฐ  ๐ฏ๐ผ๐ ๐๐ถ๐๐ต ๐๐ผ๐บ๐ฒ ๐ฎ๐๐ฒ๐๐ผ๐บ๐ฒ ๐ฎ๐ป๐ฑ ๐๐๐ฒ๐ณ๐๐น ๐ณ๐ฒ๐ฎ๐๐๐ฟ๐ฒ๐.

โโโโโโโโโโโโโโโโโโ
เน  ๐๐น๐น ๐ผ๐ณ ๐บ๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฐ๐ฎ๐ป ๐ฏ๐ฒ ๐๐๐ฒ๐ฑ ๐๐ถ๐๐ต ๐บ๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ต๐ฎ๐ป๐ฑ๐น๐ฒ : ( / . โข $ ^ ~ + * ? )
โป ๐ ๐ฎ๐ฑ๐ฒ ๐ค ๐ฏ๐ : [โคออ ๐จ๐๐๐๐๐ โข{๐ฎ๐ณ}๐ฅ](https://t.me/{me}) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ๐๐ฑ๐ฑ ๐บ๐ฒ ๐๐ผ ๐๐ผ๐๐ฟ ๐๐ฟ๐ผ๐๐ฝ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "๐จ ๐๐ต๐ฎ๐ป๐ป๐ฒ๐น ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "๐จ ๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐ ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "๐ค ๐๐ผ๐ ๐ข๐๐ป๐ฒ๐ฟ ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "๐จโ๐ป ๐๐ฒ๐๐ฒ๐น๐ผ๐ฝ๐ฒ๐ฟ ", url=f"https://t.me/Null_Coder_Bot"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "โ ๐๐ป๐น๐ถ๐ป๐ฒ ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "๐ก ๐๐ถ๐ ๐ฅ๐ฒ๐ฝ๐ผ ", url="https://te.legra.ph/file/db7c6b18567b5e81165ad.mp4"
                    )]
            ]
       ),
    )

