import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Adding Roles!'))
    print('Bot is Online!')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 673890004799455273 or 674004097799553105 :
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '\U0001F913':
           role = discord.utils.get(guild.roles, name='lowkey')
        elif payload.emoji.name == '\U0001F916':
            role = discord.utils.get(guild.roles, name='bot restocks')
        elif payload.emoji.name == '\U0001F40B':
            role = discord.utils.get(guild.roles, name='UK')
        elif payload.emoji.name == '\U0001F4AA':
            role = discord.utils.get(guild.roles, name='Germany')
        elif payload.emoji.name == '\U0001F35E':
            role = discord.utils.get(guild.roles, name='Italy')
        elif payload.emoji.name == '\U0001F956':
            role = discord.utils.get(guild.roles, name='France')
        elif payload.emoji.name == '\U0001F604':
            role = discord.utils.get(guild.roles, name='Sweden')
        elif payload.emoji.name == '\U0001F339':
            role = discord.utils.get(guild.roles, name='Spain')
        elif payload.emoji.name == '\U0001F36A':
            role = discord.utils.get(guild.roles, name='Belgium')
        elif payload.emoji.name == '\U0001F983':
            role = discord.utils.get(guild.roles, name='Turkey')
        elif payload.emoji.name == '\U0001F5FB':
            role = discord.utils.get(guild.roles, name='Netherlands')
        elif payload.emoji.name == '\U0001F9CA':
            role = discord.utils.get(guild.roles, name='Poland')
        elif payload.emoji.name == '\U0001F919':
            role = discord.utils.get(guild.roles, name='Romania')
        elif payload.emoji.name == '\U0001F96B':
            role = discord.utils.get(guild.roles, name='Hungary')
        elif payload.emoji.name == '\U0001F954':
            role = discord.utils.get(guild.roles, name='Denmark')
        elif payload.emoji.name == '\U0001F31E':
            role = discord.utils.get(guild.roles, name='Greece')
        elif payload.emoji.name == '\U000023F0':
            role = discord.utils.get(guild.roles, name='Russia')
        elif payload.emoji.name == '\U0001F426':
            role = discord.utils.get(guild.roles, name='Portugal')
        elif payload.emoji.name == '\U0001F3EB':
           role = discord.utils.get(guild.roles, name='London')
        elif payload.emoji.name == '\U0001F5FC':
            role = discord.utils.get(guild.roles, name='Paris')
        elif payload.emoji.name == '\U0001F488':
            role = discord.utils.get(guild.roles, name='Berlin')
        elif payload.emoji.name == '\U0001F33B':
            role = discord.utils.get(guild.roles, name='Barcelona')
        elif payload.emoji.name == '\U0001F451':
            role = discord.utils.get(guild.roles, name='Madrid')
        elif payload.emoji.name == '\U0001F37B':
            role = discord.utils.get(guild.roles, name='Kyiv')
        else:
           role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                emb=discord.Embed(title='Reaction Role Bot',description="You've added a new role!", colour=0xffe000)
                emb.set_footer(text="made by chihi")
                await member.send(embed=emb)
                print("Role added!")
            else:
                print("member not found")
        else:
            print("role not found")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 673890004799455273 or 674004097799553105 :
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '\U0001F913':
           role = discord.utils.get(guild.roles, name='lowkey')
        elif payload.emoji.name == '\U0001F916':
            role = discord.utils.get(guild.roles, name='bot restocks')
        elif payload.emoji.name == '\U0001F40B':
            role = discord.utils.get(guild.roles, name='UK')
        elif payload.emoji.name == '\U0001F4AA':
            role = discord.utils.get(guild.roles, name='Germany')
        elif payload.emoji.name == '\U0001F35E':
            role = discord.utils.get(guild.roles, name='Italy')
        elif payload.emoji.name == '\U0001F956':
            role = discord.utils.get(guild.roles, name='France')
        elif payload.emoji.name == '\U0001F604':
            role = discord.utils.get(guild.roles, name='Sweden')
        elif payload.emoji.name == '\U0001F339':
            role = discord.utils.get(guild.roles, name='Spain')
        elif payload.emoji.name == '\U0001F36A':
            role = discord.utils.get(guild.roles, name='Belgium')
        elif payload.emoji.name == '\U0001F983':
            role = discord.utils.get(guild.roles, name='Turkey')
        elif payload.emoji.name == '\U0001F5FB':
            role = discord.utils.get(guild.roles, name='Netherlands')
        elif payload.emoji.name == '\U0001F9CA':
            role = discord.utils.get(guild.roles, name='Poland')
        elif payload.emoji.name == '\U0001F919':
            role = discord.utils.get(guild.roles, name='Romania')
        elif payload.emoji.name == '\U0001F96B':
            role = discord.utils.get(guild.roles, name='Hungary')
        elif payload.emoji.name == '\U0001F954':
            role = discord.utils.get(guild.roles, name='Denmark')
        elif payload.emoji.name == '\U0001F31E':
            role = discord.utils.get(guild.roles, name='Greece')
        elif payload.emoji.name == '\U000023F0':
            role = discord.utils.get(guild.roles, name='Russia')
        elif payload.emoji.name == '\U0001F426':
            role = discord.utils.get(guild.roles, name='Portugal')
        elif payload.emoji.name == '\U0001F3EB':
           role = discord.utils.get(guild.roles, name='London')
        elif payload.emoji.name == '\U0001F5FC':
            role = discord.utils.get(guild.roles, name='Paris')
        elif payload.emoji.name == '\U0001F488':
            role = discord.utils.get(guild.roles, name='Berlin')
        elif payload.emoji.name == '\U0001F33B':
            role = discord.utils.get(guild.roles, name='Barcelona')
        elif payload.emoji.name == '\U0001F451':
            role = discord.utils.get(guild.roles, name='Madrid')
        elif payload.emoji.name == '\U0001F37B':
            role = discord.utils.get(guild.roles, name='Kyiv')
        else:
           role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                emb=discord.Embed(title='Reaction Role Bot',description="You've removed a role!", colour=0xffe000)
                emb.set_footer(text="made by chihi")
                await member.send(embed=emb)
                print("Role removed!")
            else:
                print("member not found")
        else:
            print("role not found")

client.run('NjczOTIzMTA0NTc3NDIxMzMx.XjhF1A.t5kr1JruTZ4EODzcPkHMMGFkcDc')
