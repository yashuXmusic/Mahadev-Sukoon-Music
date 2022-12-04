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
        caption=f""" ** 𝗛𝗲𝗹𝗹𝗼 𝘀𝗶𝗿 {message.from_user.mention()} , 🥀\n\n
๏𝗧𝗵𝗶𝘀 𝗶𝘀 [{bn}](t.me/{bu}) ,  !
➻ 𝗧𝗵𝗲 𝗺𝗼𝘀𝘁 𝗽𝗼𝘄𝗲𝗿𝗳𝘂𝗹 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗺𝘂𝘀𝗶𝗰  𝗯𝗼𝘁 𝘄𝗶𝘁𝗵 𝘀𝗼𝗺𝗲 𝗮𝘄𝗲𝘀𝗼𝗺𝗲 𝗮𝗻𝗱 𝘂𝘀𝗲𝗳𝘂𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲𝘀.

──────────────────
๏  𝗔𝗹𝗹 𝗼𝗳 𝗺𝘆 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗰𝗮𝗻 𝗯𝗲 𝘂𝘀𝗲𝗱 𝘄𝗶𝘁𝗵 𝗺𝘆 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗵𝗮𝗻𝗱𝗹𝗲 : ( / . • $ ^ ~ + * ? )
➻ 𝗠𝗮𝗱𝗲 🖤 𝗯𝘆 : [⏤͟͞ 𝑨𝒂𝒌𝒂𝒔𝒉 ™{🇮🇳}🥀](https://t.me/{me}) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "📨 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "📨 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ", url=f"https://t.me/Null_Coder_Bot"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ 𝗜𝗻𝗹𝗶𝗻𝗲 ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 𝗚𝗶𝘁 𝗥𝗲𝗽𝗼 ", url="https://te.legra.ph/file/db7c6b18567b5e81165ad.mp4"
                    )]
            ]
       ),
    )

