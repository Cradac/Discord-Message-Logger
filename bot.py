import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix = ["?"])
bot_token = "BOT_TOKEN"

@client.event
async def on_ready():
	print("Bot is ready!")
	print("Logged in as: " + client.user.name)
	print("Bot ID: " + str(client.user.id))
	for guild in client.guilds:
		print ("Connected to server: {}".format(guild))
	print("------")
		
@client.event
async def on_message(message):
	guild = message.guild
	log_channel = discord.utils.get(guild.channels, name="message-log")
	if log_channel is None:
		await client.process_commands(message)
		return
	if not message.author.bot:
		embed=discord.Embed(
			color=0xffd700,
			timestamp=datetime.datetime.utcnow(),
			description="in {}:\n{}".format(message.channel.mention, message.content)
		)
		embed.set_author(name=message.author, icon_url=message.author.avatar_url)
		embed.set_footer(text=message.author.id)
		if len(message.attachments) > 0:
			embed.set_image(url = message.attachments[0].url)
		await log_channel.send(embed=embed)
		await client.process_commands(message)
    
client.run(bot_token)
