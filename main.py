import os
import time
import discord
from discord.ext import commands, tasks
from quotes import get_quote
from datetime import datetime as dt
import pytz


dctx = None
token = os.environ['TOKEN']
#token = os.environ['TEST_TOKEN']
channel_id= int(os.environ['CHANNEL_ID'])
#channel_id= int(os.environ['TEST_CHANNEL_ID'])


@tasks.loop(hours=1)
async def declare():
    tz = pytz.timezone("Australia/Perth")
    quote = get_quote()
    message_text = "+++++THOUGHT FOR THE DAY+++++\r\n\r\n"+"+++++THEME:"+quote["topics"][0].upper()+"+++++\r\n\r\n"+quote["text"]
    now=dt.now(tz)
    print("checking for proverbinatus time is "+ str(now))
    if now.hour == 3:
      print("proverbinatus sent")
      await dctx.send(message_text)
      d1 = dt.datetime(2022,9,29,9,0,0,0,tz)
      length = d1 - now
      if length.days > 1:
        await dctx.send(f"WARNING: {length.days} DAYS UNTIL SFTC")
      if length.days == 1:
        await dctx.send("WARNING: TOMORROW IS SFTC")
      if length.days == 0:
        await dctx.send("WARNING: TODAY IS SFTC, EMPEROR BE WITH US ALL")

bot = commands.Bot(command_prefix="!40kbot ", case_insensitive=True)

@bot.event
async def on_ready():
    global dctx
    dctx = bot.get_channel(channel_id)
    print(f'{bot.user.name} has connected to discord!')
    await bot.change_presence(activity = discord.Activity(
                          type = discord.ActivityType.watching, 
                          name = 'out for Pendragons Spite Lazer'))
    print("heresy detected. starting proverbinatus")
    declare.start()

bot.run(token)