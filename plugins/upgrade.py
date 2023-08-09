from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 50  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month

        Pay Using Paytm Upi I'd ```devagovin@paytm```
	Pay Using GPay Upi I'd ```thriudev04@okhdfcbank```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/MD_TAMILAN_ADMIN_Bot")], 
        			[InlineKeyboardButton("GPay 🌎",url = "https://t.me/MD_TAMILAN_ADMIN_Bot"),
        			InlineKeyboardButton("UPI ",url = "https://t.me/MD_TAMILAN_ADMIN_Bot")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 50  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	Pay Using Paytm Upi I'd ```devagovin@paytm```
	Pay Using GPay Upi I'd ```thriudev04@okhdfcbank```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/MD_TAMILAN_ADMIN_Bot")], 
        			[InlineKeyboardButton("GPay 🌎",url = "https://t.me/MD_TAMILAN_ADMIN_Bot"),
        			InlineKeyboardButton("UPI ",url = "https://t.me/MD_TAMILAN_ADMIN_Bot")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
