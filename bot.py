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

TOKEN = os.environ.get('TOKEN')
prefix = config['prefix']
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')
ddb = DiscordComponents(client)
games = Games()
request = cloudscraper.create_scraper()


def getEmbed(game: str, game_txt: str):
    embed = discord.Embed(color=randColor())
    embed.title = game
    embed.description = game_txt
    return embed


def getBuyComponents():
    components = [[
        Button(
            label='Rust',
            style=ButtonStyle.green,
            id='rust-btn'
        ),
        Button(
            label='Valorant',
            style=ButtonStyle.red,
            id='valo-btn'
        ),
        Button(
            label='Universal',
            style=ButtonStyle.blue,
            id='uni-btn'
        ),
        Button(
            label='Rainbow Six',
            style=ButtonStyle.grey,
            id='r6-btn'
        ),
        Button(
            label='COD Warzone',
            style=ButtonStyle.green,
            id='cod-btn'
        )
    ]]
    return components


@client.command(name='buy')
async def send_buying_details(ctx: Context):
    await ctx.send(
        content='**`Please select a product`**',
        components=[[
            Button(
                label='Rust',
                style=ButtonStyle.green,
                id='rust-btn'
            ),
            Button(
                label='Valorant',
                style=ButtonStyle.red,
                id='valo-btn'
            ),
            Button(
                label='Universal',
                style=ButtonStyle.blue,
                id='uni-btn'
            ),
            Button(
                label='Rainbow Six',
                style=ButtonStyle.grey,
                id='r6-btn'
            ),
            Button(
                label='COD Warzone',
                style=ButtonStyle.green,
                id='cod-btn'
            )
        ]]
    )


@client.command(name='shop')
async def _send_buying_details(ctx: Context):
    await send_buying_details.invoke(ctx)


async def wait():
    while True:
        tasks = [
            asyncio.create_task(client.wait_for(
                'button_click',
                # timeout=30
            ), name='button_click'),
            asyncio.create_task(client.wait_for(
                'select_option',
                # timeout=30
            ), name='select_option')
        ]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        finished: asyncio.Task = list(done)[0]
        for task in pending:
            try:
                task.cancel()
            except asyncio.CancelledError:
                pass
        else:
            event: str = finished.get_name()
            interaction: Interaction = finished.result()

            if event == 'button_click':
                btn_id = interaction.component.id
                if btn_id == 'rust-btn':
                    await interaction.respond(
                        content='**`Select Product`**',
                        components=[[
                            Button(
                                label='Script',
                                style=ButtonStyle.green,
                                id='sc-btn'
                            ),
                            Button(
                                label='Cheat',
                                style=ButtonStyle.blue,
                                id='ch-btn'
                            )
                        ]]
                    )
                elif btn_id == 'sc-btn':
                    await interaction.respond(
                        content='**`Please select a payment method`**',
                        components=[
                            Select(
                                placeholder='Select Method!',
                                options=[
                                    SelectOption(label='Sellix (Instant Delivery)',
                                                 value='sellix'),
                                    SelectOption(label='Weepay (Manuel Delivery)',
                                                 value='weepay'),
                                    # SelectOption(label='Payhesap',
                                    #              value='payhesap'),
                                    SelectOption(label='Paymes (Manuel Delivery)',
                                                 value='paymes'),
                                    # SelectOption(label='Paypal',
                                    #             value='paypal')
                                ],
                                custom_id='rust-script-select'
                            )
                        ]
                    )
                elif btn_id == 'ch-btn':
                    await interaction.respond(
                        content='**`Please select a payment method`**',
                        components=[
                            Select(
                                placeholder='Select Method!',
                                options=[
                                    # SelectOption(label='Sellix (Instant Delivery)',
                                    #              value='sellix'),
                                    SelectOption(label='Weepay (Manuel Delivery)',
                                                 value='weepay'),
                                    SelectOption(label='Payhesap (Manuel Delivery)',
                                                 value='payhesap'),
                                    SelectOption(label='Paymes (Manuel Delivery)',
                                                 value='paymes'),
                                    SelectOption(label='Paypal (Manuel Delivery)',
                                                 value='paypal')
                                ],
                                custom_id='rust-cheat-select'
                            )
                        ]
                    )
                elif btn_id == 'valo-btn':
                    await interaction.respond(
                        content='**`Please select a payment method`**',
                        components=[
                            Select(
                                placeholder='Select Method!',
                                options=[
                                    # SelectOption(label='Sellix (Instant Delivery)',
                                    #              value='sellix'),
                                    SelectOption(label='Weepay (Manuel Delivery)',
                                                 value='weepay'),
                                    SelectOption(label='Payhesap (Manuel Delivery)',
                                                 value='payhesap'),
                                    SelectOption(label='Paymes (Manuel Delivery)',
                                                 value='paymes'),
                                    SelectOption(label='Paypal (Manuel Delivery)',
                                                 value='paypal')
                                ],
                                custom_id='valo-select'
                            )
                        ]
                    )
                elif btn_id == 'uni-btn':
                    await interaction.respond(
                        content='**`Please select a payment method`**',
                        components=[
                            Select(
                                placeholder='Select Method!',
                                options=[
                                    # SelectOption(label='Sellix (Instant Delivery)',
                                    #              value='sellix'),
                                    SelectOption(label='Weepay (Manuel Delivery)',
                                                 value='weepay'),
                                    SelectOption(label='Payhesap (Manuel Delivery)',
                                                 value='payhesap'),
                                    SelectOption(label='Paymes (Manuel Delivery)',
                                                 value='paymes'),
                                    SelectOption(label='Paypal (Manuel Delivery)',
                                                 value='paypal')
                                ],
                                custom_id='uni-select'
                            )
                        ]
                    )
                elif btn_id == 'r6-btn':
                    await interaction.respond(
                        content='**`Please select a payment method`**',
                        components=[
                            Select(
                                placeholder='Select Method!',
                                options=[
                                    # SelectOption(label='Sellix (Instant Delivery)',
                                    #              value='sellix'),
                                    SelectOption(label='Weepay (Manuel Delivery)',
                                                 value='weepay'),
                                    # SelectOption(label='Payhesap (Manuel Delivery)',
                                    #              value='payhesap'),
                                    SelectOption(label='Paymes (Manuel Delivery)',
                                                 value='paymes'),
                                    SelectOption(label='Paypal (Manuel Delivery)',
                                                 value='paypal')
                                ],
                                custom_id='r6-select'
                            )
                        ]
                    )
                elif btn_id == 'cod-btn':
                    await interaction.respond(
                        content='**`Please select a payment method`**',
                        components=[
                            Select(
                                placeholder='Select Method!',
                                options=[
                                    # SelectOption(label='Sellix (Instant Delivery)',
                                    #              value='sellix'),
                                    SelectOption(label='Weepay (Manuel Delivery)',
                                                 value='weepay'),
                                    # SelectOption(label='Payhesap (Manuel Delivery)',
                                    #              value='payhesap'),
                                    SelectOption(label='Paymes (Manuel Delivery)',
                                                 value='paymes'),
                                    SelectOption(label='Paypal (Manuel Delivery)',
                                                 value='paypal')
                                ],
                                custom_id='cod-select'
                            )
                        ]
                    )
            elif event == 'select_option':
                product = interaction.custom_id
                selection = interaction.component[0].value
                if product == 'rust-script-select':
                    if selection == 'sellix':
                        embed = getEmbed('Rust', games.rust_script_sellix)
                    elif selection == 'weepay':
                        embed = getEmbed('Rust', games.rust_script_weepay)
                    elif selection == 'payhesap':
                        embed = getEmbed('Rust', games.rust_script_payhesap)
                    elif selection == 'paymes':
                        embed = getEmbed('Rust', games.rust_script_paymes)
                    elif selection == 'paypal':
                        embed = getEmbed('Rust', games.rust_script_paypal)
                        embed.set_footer(
                            text='[Write your order number after payment]')
                elif product == 'rust-cheat-select':
                    if selection == 'sellix':
                        embed = getEmbed('Rust', games.rust_cheat_sellix)
                    elif selection == 'weepay':
                        embed = getEmbed('Rust', games.rust_cheat_weepay)
                    elif selection == 'payhesap':
                        embed = getEmbed('Rust', games.rust_cheat_payhesap)
                    elif selection == 'paymes':
                        embed = getEmbed('Rust', games.rust_cheat_paymes)
                    elif selection == 'paypal':
                        embed = getEmbed('Rust', games.rust_cheat_paypal)
                        embed.set_footer(
                            text='[Write your order number after payment]')
                elif product == 'valo-select':
                    if selection == 'sellix':
                        embed = getEmbed('Valorant', games.valo_weepay)
                    elif selection == 'weepay':
                        embed = getEmbed('Valorant', games.valo_weepay)
                    elif selection == 'payhesap':
                        embed = getEmbed('Valorant', games.valo_payhesap)
                    elif selection == 'paymes':
                        embed = getEmbed('Valorant', games.valo_paymes)
                    elif selection == 'paypal':
                        embed = getEmbed('Valorant', games.valo_paypal)
                        embed.set_footer(
                            text='[Write your order number after payment]')
                elif product == 'uni-select':
                    if selection == 'sellix':
                        embed = getEmbed('Universal', games.universal_weepay)
                    elif selection == 'weepay':
                        embed = getEmbed('Universal', games.universal_weepay)
                    elif selection == 'payhesap':
                        embed = getEmbed('Universal', games.universal_payhesap)
                    elif selection == 'paymes':
                        embed = getEmbed('Universal', games.universal_paymes)
                    elif selection == 'paypal':
                        embed = getEmbed('Universal', games.universal_paypal)
                        embed.set_footer(
                            text='[Write your order number after payment]')
                elif product == 'r6-select':
                    if selection == 'sellix':
                        embed = getEmbed('Rainbow Six: Siege', games.r6_weepay)
                    elif selection == 'weepay':
                        embed = getEmbed('Rainbow Six: Siege', games.r6_weepay)
                    elif selection == 'payhesap':
                        embed = getEmbed('Rainbow Six: Siege',
                                         games.r6_payhesap)
                    elif selection == 'paymes':
                        embed = getEmbed('Rainbow Six: Siege', games.r6_paymes)
                    elif selection == 'paypal':
                        embed = getEmbed('Rainbow Six: Siege', games.r6_paypal)
                        embed.set_footer(
                            text='[Write your order number after payment]')
                elif product == 'cod-select':
                    if selection == 'sellix':
                        embed = getEmbed('Cod Warzone', games.warzone_weepay)
                    elif selection == 'weepay':
                        embed = getEmbed('Cod Warzone', games.warzone_weepay)
                    elif selection == 'payhesap':
                        embed = getEmbed('Cod Warzone', games.warzone_payhesap)
                    elif selection == 'paymes':
                        embed = getEmbed('Cod Warzone', games.warzone_paymes)
                    elif selection == 'paypal':
                        embed = getEmbed('Cod Warzone', games.warzone_paypal)
                        embed.set_footer(
                            text='[Write your order number after payment]')
                await interaction.respond(embed=embed)


@client.event
async def on_ready():
    print('Bot is online....')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"!buy | !shop"))
    # await auto_send_msg.start()
    await wait()


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


@client.event
async def on_guild_channel_create(channel):
    if 'ticket' in channel.name:
        await send_buying_details(channel)


client.run(TOKEN)
