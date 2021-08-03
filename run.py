from os import system as terminal
from pyrogram import Client, filters, idle
from random import randint, choice

app = Client('gosu')
app.start()

@app.on_message(~filters.me)
def message(client, message):
	try:
		client.join_chat(message.text)
	except:
		pass
	if message.from_user.is_bot == True:
		return
	try:
		if randint(1, 8) == 3:
			client.send_chat_action(message.chat.id, 'typing')
			text = client.get_inline_bot_results('DotaGosuBot', 'Дентли топ')['results'][1]['send_message']['message']
			message.reply_text(text)
	except:
		pass
		
idle()
