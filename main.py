import os
import discord
from discord.ext import commands
import time
from keep_alive import keep_alive

token = os.environ['TOKEN']

bot = commands.Bot(command_prefix="!", case_insensitive=True)



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord!')
    await bot.change_presence(activity = discord.Activity(
                          type = discord.ActivityType.watching, 
                          name = 'Porn on Disney+'))

@bot.command()
async def print(ctx, *args):
	await ctx.channel.send(args)

bot.run(token)