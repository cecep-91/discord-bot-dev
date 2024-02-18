import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

bot.run('MTIwODMxMjY5NzA1ODIzNDM4OQ.GqiANw.TDvgyBLg86sBOX79RoqPrL-_QZgIESW-QM7FN4')
