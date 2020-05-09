import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

client.run('NzA4NTYyOTkwNjc2NTc0MjE5.XrZMUg.iI4BcXJo8QqiTyh8MwTHc9dKvu0')
