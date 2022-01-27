import asyncio
import os
import discord
import cloudscraper
from discord.ext import commands, tasks
from discord.channel import TextChannel, VoiceChannel
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.member import Member, VoiceState
from discord.message import Message
from discord_components import *
from bs4 import BeautifulSoup as bs
from utils.randomColor import randColor
from settings import load_requirements
from games import Games

config = load_requirements()
request = cloudscraper.create_scraper()

TOKEN = os.environ.get('TOKEN')
prefix = config['prefix']
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print('Auto message sender is online....')
    await auto_send_msg.start()


@tasks.loop(hours=1)
async def auto_send_msg():
    response = request.get('https://revolexscripts.com').text
    html = bs(response, 'html.parser')
    bought = html.find_all('span', {'class': 'label-info'})[-1].text.strip()
    license = html.find_all('span', {'class': 'label-success'})[0].text.strip()
    using = html.find_all('span', {'class': 'label-success'})[1].text.strip()
    embed = discord.Embed(color=randColor())
    embed_txt = f'**{bought}\n{license}\n{using}**'
    embed.title = 'Revolex Scripts ❤'
    embed.description = embed_txt
    # embed.set_image(url='https://revolexscripts.com/img/logo.png')
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/852299725511327764/936325072770175077/rifle.ak.png')
    for _id in config['channels']:
        channel = client.get_channel(_id)
        await channel.send(embed=embed)

client.run(TOKEN)