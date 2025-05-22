from typing import Union, Optional, Protocol
from pyrogram import filters, types, enums
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from crushi import app
from crushi.utils import help_pannel
from crushi.utils.database import get_lang
from crushi.utils.decorators.language import LanguageStart, languageCB
from crushi.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from crushi.utils.stuffs.buttons import BUTTONS
from crushi.utils.stuffs.helper import Helper

class EditableMessage(Protocol):
    text: str
    async def edit_message_text(self, text: str, reply_markup: Optional[InlineKeyboardMarkup] = None) -> None: ...

async def safe_edit_message(message: EditableMessage, text: str, reply_markup: Optional[InlineKeyboardMarkup] = None):
    try:
        if message.text != text:
            await message.edit_message_text(text, reply_markup=reply_markup)
    except Exception as e:
        if "MESSAGE_NOT_MODIFIED" not in str(e):
            raise e

@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: types.Client, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await safe_edit_message(update, _["help_1"].format(SUPPORT_CHAT), keyboard)
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    help_text = getattr(helpers, f"HELP_{cb[-1]}")
    await safe_edit_message(CallbackQuery, help_text, keyboard)


@app.on_callback_query(filters.regex("mbot_cb") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await safe_edit_message(CallbackQuery, Helper.HELP_M, InlineKeyboardMarkup(BUTTONS.MBUTTON))


@app.on_callback_query(filters.regex('managebot123'))
@languageCB
async def on_back_button(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_pannel(_, True)
    if cb == "settings_back_helper":
        await safe_edit_message(CallbackQuery, _["help_1"].format(SUPPORT_CHAT), keyboard)

@app.on_callback_query(filters.regex('mplus'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"mbot_cb")]])
    if cb == "Okieeeeee":
        await safe_edit_message(CallbackQuery, f"`something errors`", keyboard)
    else:
        await safe_edit_message(CallbackQuery, getattr(Helper, cb), keyboard)
