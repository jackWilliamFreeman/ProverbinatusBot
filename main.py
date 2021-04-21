import os
import discord
from discord.ext import commands, tasks
import time
from keep_alive import keep_alive
from quotes import get_quote
import random
dctx = None

token = os.environ['TOKEN']
channel_id= int(os.environ['CHANNEL_ID'])
inquisitor_id= int(os.environ['INQUISITOR_ID'])

@tasks.loop(hours=12)
async def declare():
    quote = get_quote()
    message_text = "+++++THOUGHT FOR THE DAY+++++\r\n\r\n"+"+++++THEME:"+quote["topics"][0].upper()+"+++++\r\n\r\n"+quote["text"]
    await dctx.send(message_text)

bot = commands.Bot(command_prefix="!40kbot ", case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord!')
    await bot.change_presence(activity = discord.Activity(
                          type = discord.ActivityType.watching, 
                          name = 'out for Heresy'))

@bot.command(name="proverbinatus", 
brief="Call down righteous Proverbinatus on the Emperors foes",
help="Immediate and Righteous Proverbinatus")
async def proverbinatus(ctx):
    quote = get_quote()
    quote_text = quote["text"]
    quote_theme = quote["topics"][0].upper()
    message_text = "+++++THOUGHT FOR THE DAY+++++\r\n\r\n"+"+++++THEME:"+quote_theme+"+++++\r\n\r\n"+quote_text
    await ctx.message.reply(message_text)

@bot.command(name="begin", brief="Begin calling down continual Proverbinatus on the heretical masses.",
help="Continual and RIGHTEOUS Proverbinatus every 24 hours. Only holy Administrators or the Grand Inquisitor can begin continual Proverbinatus")
async def begin_proverbinatus(ctx):
    if (ctx.message.author.guild_permissions.administrator or ctx.message.author.id == inquisitor_id) and ctx.channel.id == channel_id:
        global dctx
        await ctx.send("Proverbinatus has begun!")
        time.sleep(2)
        dctx = bot.get_channel(channel_id)
        declare.start()
    else:
        await ctx.message.reply("You are not holy enough to sanction Proverbinatus continually!")

keep_alive()
bot.run(token)