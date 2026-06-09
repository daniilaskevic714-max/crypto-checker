from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests, os
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
 coin=context.args[0] if context.args else 'bitcoin'
 data=requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd').json()
 await update.message.reply_text(str(data))
app=ApplicationBuilder().token(os.getenv('BOT_TOKEN')).build()
app.add_handler(CommandHandler('price',price))
app.run_polling()