import os
import time
import discord
from discord.ext import commands, tasks
from quotes import get_quote
from birthdays import get_birthdays
from datetime import datetime as dt
import pytz
from dateutil.relativedelta import relativedelta
from discord import Intents

intents = Intents.default()
intents.message_content = True


ENV=os.getenv("ENV","prod")
dctx = None
bot = None
if ENV == 'prod':
  token = os.environ['TOKEN']
  channel_id= int(os.environ['CHANNEL_ID'])
else:
  token = os.environ['TEST_TOKEN']
  channel_id= int(os.environ['TEST_CHANNEL_ID'])


@tasks.loop(hours=1)
async def declare():
    tz = pytz.timezone("Australia/Perth")
    quote = get_quote()
    now=dt.now(tz)
    d1 = dt(2024,11,1,9,0,0,0,tz)
    if now.hour == 3:
      embed= discord.Embed(title="+++THOUGHT FOR THE DAY+++", type='rich', color=discord.Color.red())
      embed.set_author(name="Office of the Inquisition (Ordo Proverbinatus)",icon_url="https://www.belloflostsouls.net/wp-content/uploads/2016/09/Inquisition.jpg")
      embed.add_field(inline=False, name=f"{quote['text']}", value= '')
      embed.add_field(inline=False, name=f"+++++THEME+++++", value= ', '.join(quote['topics']))
      embed.set_footer(text=f"Go about your day with purpose citizen. The Inquisition maintains a vigilant eye for heresy. The Emperor Protects.")
      print("proverbinatus sent")
      await dctx.send(embed=embed)
      d1 = dt(2024,11,1,9,0,0,0,tz)
      length = d1 - now
      if length.days > 1:
        await dctx.send(f"WARNING: {length.days} DAYS UNTIL SFTC. LOYAL CITIZENS, PREPARE YOURSELF FOR MIRTH")
        await dctx.send(f"<@321580905544286209> THIS IS A DAILY REMINDER FOR YOU TO SEND A DAILY REMINDER FOR <@368751796945944577> TO SEND A DAILY REMINDER TO <@550616372120387585> TO BRING GINS OR SOMETHING. EMPEROR HELP ME I USED TO BE A SCHOLAR....")
      if length.days == 1:
        await dctx.send("WARNING: TOMORROW IS SFTC")
      if length.days == 0:
        await dctx.send("WARNING: TODAY IS SFTC, EMPEROR BE WITH US ALL")
      await handle_birthdays(dctx)

bot = commands.Bot(command_prefix="!40kbot ", case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    global dctx
    dctx = bot.get_channel(channel_id)
    print(f'{bot.user.name} has connected to discord!')
    await bot.change_presence(activity = discord.Activity(
                          type = discord.ActivityType.watching, 
                          name = 'steamed hams netflix true crime docos'))
    print("heresy detected. starting proverbinatus")
    declare.start()

async def handle_birthdays(dctx):
  birthdays = get_birthdays()
  for person in birthdays:
      birthday = birthdays.get(person).get("birthday")
      discord_mention_name = f"<@{birthdays.get(person).get('discord_user_id')}>"
      birthday_dt = dt.strptime(birthday, "%Y-%m-%d")
      now = dt.now()
      if birthday_dt.day == now.day and birthday_dt.month == now.month:
        years_old = relativedelta(dt.now(), birthday_dt).years
        embed= discord.Embed(title="++++++++BIRTHDAY HERESY DETECTED!++++++++", type='rich', description="Details of the **Heretic** and their crimes are outlined below:", color=discord.Color.red())
        embed.set_author(name="Office of the Inquisition (Ordo Birthdayeus)",icon_url="https://www.belloflostsouls.net/wp-content/uploads/2016/09/Inquisition.jpg")
        embed.add_field(inline=False, name=f"Heretical Offence:", value=f"Growing older and thus seeking to diminish your service To the God Emperor of Mankind with pointless celebration and needless consumption")
        embed.add_field(inline=False, name=f"Convicted Heretic:", value=f"The vile creature know as **{person}**, they have thus far delivered **{years_old}** years of (previously) impeccable service to our (undying) Lord.")
        embed.add_field(inline=False, name=f"Punishment for Heresy:", value=f"Chastistment by the **Canticles of Age Heresy Rejection**. Prepare yourself for your sentence!")
        embed.set_footer(text=f"In Fealty to our (undying) God Emperor and by the Grace of the Golden Throne\r\nI denounce {person} as an age-heretic and hope that they may return to the Grace of our (undying) Lord and serve Him faithfully\r\nMay Imperial Justice account in all balance.\r\nThe Emperor Protects")
        await dctx.send(embed=embed)
        await dctx.send(f"Now we will commence the sentence: Singing the glorious hymn: **THE CANTICLES OF AGE HERESY REJECTION** in chastisement of convicted age-heretic: {discord_mention_name}.\r\n\r\n{birthdays.get(person).get('video_url')}")
        await dctx.send(f"+++++++++++++++++Closing Statement++++++++++++++\r\nSuck it Tim.")

bot.run(token)