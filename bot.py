import discord
import os
import random
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['DoesArt Studios', '.Help'])

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    change_status.start()
    print('Bot is ready.')

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def art(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708861766389596225/709267643030568981/art.png?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
    'Ask again later.',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Do not count on it',
    'It is certain',
    'It is decidely so',
    'Most likely',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Outlook good',
    'Reply hazy, try again',
    'Signs point to yes',
    'Very doutbful',
    'without a doubt',
    'Yes',
    'Definitely',
    'You may rely on it']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
async def art1(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708861766389596225/709267643030568981/art.png?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def art2(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/353076698386006016/708473875322896414/image0.png?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def art3(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/353076698386006016/709086588398731365/image0.png?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def art4(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/353076698386006016/707710404540760074/image0.png?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def art5(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/474808181579841546/708782836852850719/image0.png?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def art6(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/474808181579841546/708673865198600252/image0.png?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def art7(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/474808181579841546/708569324667011112/image0.png?size=1024")
    await ctx.send(embed=embed)


@client.command()
async def art8(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/474808181579841546/708565275213168680/image0.jpg?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def art9(ctx):
    embed=discord.Embed(color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/474808181579841546/709208908035784845/image0.jpg?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def website(ctx):
    await ctx.send('https://fanart.tv')

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

@client.command()
async def Help(ctx):
    embed=discord.Embed(title="DoesArt Studios", color=0xff8000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708839730468618290/708896887981342730/Brody_does_art_official_logo.png?size=256")
    embed.add_field(name="```.Help```", value="Shows this message you must do .Help otherwise it will show a different help message that is not ment to be used", inline=False)
    embed.add_field(name="```.8ball```", value="do .8ball [QUESTION GOES HERE] it should then give you a random answer.", inline=False)
    embed.add_field(name="```.ping```", value="Shows the ping of the bot", inline=False)
    embed.add_field(name="```.art```", value="Do .art for art inspiration there is currently nine images do .art[number out of 2-9] do .art if you want the first art", inline=False)
    embed.add_field(name="```.website```", value="Shows the website we get our art off", inline=False)
    embed.set_footer(text="If you need any help with commands contact the support team")
    await ctx.send(embed=embed)

client.remove_command("help")
client.run('YOUR TOKEN GOES HERE')
