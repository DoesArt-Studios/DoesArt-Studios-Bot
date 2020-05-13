import discord
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self) :
        print('Fun cog is ready!')

    @commands.command()
    async def ing(self, ctx):
        await ctx.send('Pong!')


def setup(client):
    client.add_cog(Fun(client))
