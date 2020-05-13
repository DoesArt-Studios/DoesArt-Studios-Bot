import discord
from discord.ext import commands


class Art(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Art cog is ready!')

    @commands.command()
    async def art(self, ctx):
         embed = discord.Embed(color=0xff8000)
         embed.set_image(url="https://cdn.discordapp.com/attachments/708861766389596225/709267643030568981/art.png?size=1024")
         await ctx.send(embed=embed)

    @commands.command()
    async def art1(self, ctx):
         embed = discord.Embed(color=0xff8000)
         embed.set_image(url="https://cdn.discordapp.com/attachments/708861766389596225/709267643030568981/art.png?size=1024")
         await ctx.send(embed=embed)

    @commands.command()
    async def art2(self, ctx):
         embed = discord.Embed(color=0xff8000)
         embed.set_image(url="https://cdn.discordapp.com/attachments/353076698386006016/708473875322896414/image0.png?size=1024")
         await ctx.send(embed=embed)

    @commands.command()
    async def art3(self, ctx):
         embed = discord.Embed(color=0xff8000)
         embed.set_image(url="https://cdn.discordapp.com/attachments/353076698386006016/709086588398731365/image0.png?size=1024")
         await ctx.send(embed=embed)

    @commands.command()
    async def art4(self, ctx):
         embed = discord.Embed(color=0xff8000)
         embed.set_image(url="https://cdn.discordapp.com/attachments/353076698386006016/707710404540760074/image0.png?size=1024")
         await ctx.send(embed=embed)

    @commands.command()
    async def art5(self, ctx):
          embed = discord.Embed(color=0xff8000)
          embed.set_image(url="https://cdn.discordapp.com/attachments/474808181579841546/708782836852850719/image0.png?size=1024")
          await ctx.send(embed=embed)

    @commands.command()
    async def art6(self, ctx):
          embed = discord.Embed(color=0xff8000)
          embed.set_image(url="https://cdn.discordapp.com/attachments/474808181579841546/708673865198600252/image0.png?size=1024")
          await ctx.send(embed=embed)

    @commands.command()
    async def art7(self, ctx):
          embed = discord.Embed(color=0xff8000)
          embed.set_image(url="https://cdn.discordapp.com/attachments/474808181579841546/708569324667011112/image0.png?size=1024")
          await ctx.send(embed=embed)

    @commands.command()
    async def art8(self, ctx):
          embed = discord.Embed(color=0xff8000)
          embed.set_image(url="https://cdn.discordapp.com/attachments/474808181579841546/708565275213168680/image0.jpg?size=1024")
          await ctx.send(embed=embed)

    @commands.command()
    async def art9(self, ctx):
          embed = discord.Embed(color=0xff8000)
          embed.set_image(url="https://cdn.discordapp.com/attachments/474808181579841546/709208908035784845/image0.jpg?size=1024")
          await ctx.send(embed=embed)

    @commands.command(aliases=['discord'])
    async def _discord(self ,ctx):
          await ctx.send("https://discord.gg/9teJTGf")

def setup(client):
    client.add_cog(Art(client))