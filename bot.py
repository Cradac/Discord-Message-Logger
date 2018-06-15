import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import re


Client = discord.Client()
client = commands.Bot(command_prefix = "?")
bot_token = "BOT_TOKEN"
log_channel = dicord.Object(id=CHANNEL_ID)

@client.event
async def on_ready():
	print("Bot is ready!")
	await client.change_presence(game=discord.Game(name="watching all messages"))
	print("Logged in as: " + client.user.name)
	print("Bot ID: "+client.user.id)
	for server in client.servers:
		print ("Connected to server: {}".format(server))
	print("------")

@client.event
async def on_message(message):
	if message.author.id != client.user.id:
		msg = message.content
		#print(msg)
		counter1 = 0
		counter2 = 0
		for m in message.mentions:
			msg = re.sub('<@!?\d*>', message.mentions[counter1].display_name, msg, 1)
			counter1 += 1
		for n in message.role_mentions:
			msg = re.sub('<@&\d*>', message.role_mentions[counter2].name, msg, 1)
			counter2 += 1
		#print(msg)
		msg = re.sub('@', '', msg)
		#print(msg)
		await client.send_message(log_channel, "{}`{}` just said in {}: *'{}'*".format(message.author.name, message.author.id, message.channel.name, msg))
		if len(message.attachments) > 0:
			pic = message.attachments[0].get("url")
			print(pic)
			await client.send_message(log_channel, pic)
		await client.process_commands(message)
    
    
async def connect():
	print("Logging in...")
	while not client.is_closed:
		try:
			await client.start(bot_token)
		except:
			await asyncio.sleep(5)
		
client.loop.run_until_complete(connect())
