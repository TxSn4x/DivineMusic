from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app

start_txt = """
⟢ Rᴇᴘᴏ Nʜɪ Mɪʟᴇɢᴀ
 
⟢ Lᴀɢ Fʀᴇᴇ Rᴜɴ 24/7 Nᴏɴ Sᴛᴏᴘ

⟢ @AniWeb_bots
 
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Aᴅᴅ Mᴇ Bᴀʙᴇ", url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Aniweb_bots"),
          InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/aniweb_nexus"),
          ],
               [
                InlineKeyboardButton("Nᴇᴛᴡᴏʀᴋ", url=f"https://t.me/aniweb_network"),
],
[
InlineKeyboardButton("𝖠ɴɪ𝖶ᴇʙ 𝖲ʜᴏɢᴜɴᴀᴛᴇ", url=f"https://t.me/AniWeb_Shogunate"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
