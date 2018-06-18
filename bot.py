import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = "?")
bot_token = "BOT_TOKEN"

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
	log_channel = None
	for server in client.servers:
		log_channel = discord.utils.get(server.channels, name="message-log") or log_channel
	if message.author.id != client.user.id:
		msg = message.content
		await client.send_message(log_channel, "{}`{}` just said in {}: *'{}'*".format(message.author.name, message.author.id, message.channel.mention, message.clean_content.replace("@","")))
		for att in message.attachments:
			await client.send_message(log_channel, att.get("url"))
		for emb in message.embeds:
			await client.send_message(log_channel, "A Bot sent an Embed.")
		await client.process_commands(message)
    
    
async def connect():
	print("Logging in...")
	while not client.is_closed:
		try:
			await client.start(bot_token)
		except:
			await asyncio.sleep(5)
		
client.loop.run_until_complete(connect())
