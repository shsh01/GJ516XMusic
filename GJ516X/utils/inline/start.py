from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from GJ516X import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴍᴀɪɴᴛᴀɪɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ", callback_data="settings_back_helper"
            ),
              InlinekeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/export_gabbar"
            ),
        ],
        [
              InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"{config.SUPPORT_CHANNEL}"),
              InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
              InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ", url=f"{config.UPSTREAM_REPO}"
             ),
              InlinekeyboardButton(
                text="ᴍᴀɪɴᴛᴀɪɴᴇʀ", user_id=OWNER)
        ],
     ]
    return buttons
