import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import json
from discord.ext import commands
import asyncio
import os

prefix= '>'
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes.get(str(message.guild.id), ">")

intents = discord.Intents().all()
client = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=None)

@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = ">"
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)

@client.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)  
    await ctx.send(f"The prefix was changed to {prefix}")

@client.event
async def on_message(message):
    if not message.author.bot:  
        await client.process_commands(message)  

        if client.user.mentioned_in(message) and not message.mention_everyone:
            prefix = get_prefix(client, message)
            total_commands = len(client.commands)
            embed = discord.Embed(title = "BOT INFORMATION", color=discord.Color.blurple())
            embed.add_field(name="Hey", value=f"{message.author.mention}")
            embed.add_field(name="My Prefix for this server is", value=f"`{prefix}`", inline=False)
            embed.add_field(name="invite me", value="[click here](https://discord.com/oauth2/authorize?client_id=1218230792216641586&permissions=8&scope=bot)", inline=False)
            embed.add_field(name="support server", value="[support](https://discord.com/invite/wsqjEVzTnn)", inline=False)
            embed.set_footer(text=f"Total Commands: {total_commands} & Prefix of Xcape is: {prefix}\nDeveloped By XCAPE team")
            await message.channel.send(embed=embed)

@client.event
async def on_ready():
    print(f'{client.user} is online and ready to use')
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f'ping me to know my prefix'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply(f'I can\'t find this command\ntype {prefix}help to get help')

@client.command()
async def utility(ctx):
    embed = discord.Embed(colour=0xc8dc6c)
    embed.add_field(name=f"``ping``", value="")
    embed.add_field(name=f"``invite``", value="")
    embed.add_field(name=f"``afk``", value="")
    embed.add_field(name=f"``av``", value="")
    embed.add_field(name=f"``userinfo``", value="")
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    total_commands = len(client.commands)
    embed = discord.Embed(colour=0xc8dc6c)
    embed.set_footer(text=f"Total Commands: {total_commands} & Prefix of Xcape is: {prefix}")
    embed.set_author(name=f"{client.user.name} Help")
    embed.add_field(name="<:Utility_ActividadIcon:1218631244821041304> Utility", value="Utility commands", inline=False)
    embed.add_field(name="<a:utility:1218630535069302815> Moderation", value="Moderation commands", inline=False)
    embed.add_field(name="<a:welcomer:1218631719293550712> Welcome", value="Welcome commands", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def moderation(ctx):
    embed = discord.Embed(colour=0xc8dc6c)
    embed.add_field(name=f"``ban``", value="")
    embed.add_field(name=f"``kick``", value="")
    embed.add_field(name=f"``mute``", value="")
    embed.add_field(name=f"``unmute``", value="")
    embed.add_field(name=f"``purge``", value="")
    embed.add_field(name=f"``hide``", value="")
    embed.add_field(name=f"``unhide``", value="")
    embed.add_field(name=f"``lock``", value="")
    embed.add_field(name=f"``unlock``", value="")
    embed.add_field(name=f"``trigger``", value="")
    await ctx.send(embed=embed)    

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    await ctx.reply(
      f'I can\'t find this command\ntype {prefix}help to get help')
    
@client.command()
async def invite(ctx):
  await ctx.reply("[Click here to invite me](https://discord.com/oauth2/authorize?client_id=1218230792216641586&permissions=8&scope=bot)")

@client.command()
async def dmuser(ctx, member: discord.Member, *, message):
    try:
        await member.send(message)
        await ctx.send(f"Direct message sent to {member.mention}")
    except discord.Forbidden:
        await ctx.send("Could not send a direct message to this user. Please make sure your DMs are open.")

@client.command()
async def purge(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount} messages deleted.", delete_after=5)
    else:
        await ctx.send("You do not have the permissions to manage messages.")


@client.command()
async def setwelcome(ctx, channel: discord.TextChannel, *, message):
    print("Set welcome command executed.")  

    
    if ctx.author.guild_permissions.manage_channels:
        
        try:
            with open("welcome_messages.json", "r") as file:
                welcome_messages = json.load(file)
        except FileNotFoundError:
            welcome_messages = {}

        
        welcome_messages[str(ctx.guild.id)] = {"channel_id": channel.id, "message": message}

       
        print("Updated welcome messages:", welcome_messages)

        
        try:
            with open("welcome_messages.json", "w") as file:
                json.dump(welcome_messages, file, indent=4)
        except Exception as e:
            print("Error saving welcome message to JSON file:", e)  
            await ctx.send("An error occurred while saving the welcome message.")

        await ctx.send(f"Welcome message set for {channel.mention}.")
    else:
        await ctx.send("You do not have the permissions to manage channels.")
@client.event
async def on_member_join(member):
    try:
        with open("welcome_messages.json", "r") as file:
            welcome_messages = json.load(file)
    except FileNotFoundError:
        welcome_messages = {}

    if str(member.guild.id) in welcome_messages:
        welcome_data = welcome_messages[str(member.guild.id)]
        channel = member.guild.get_channel(welcome_data["channel_id"])
        message = welcome_data["message"]

        embed = discord.Embed(title="Welcome", description=message.format(member=member.mention), color=discord.Color.green())
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)
    else:
        
        default_message = f"Welcome to the server, {member.mention}!"
        embed = discord.Embed(title="Welcome", description=default_message, color=discord.Color.green())
        embed.set_thumbnail(url=member.avatar_url)
        await member.guild.system_channel.send(embed=embed)
@client.command()
async def testwelcome(ctx):
    try:
        with open("welcome_messages.json", "r") as file:
            welcome_messages = json.load(file)
    except FileNotFoundError:
        await ctx.send("Welcome messages have not been set up yet.")
        return

    if str(ctx.guild.id) in welcome_messages:
        welcome_data = welcome_messages[str(ctx.guild.id)]
        channel = ctx.guild.get_channel(welcome_data["channel_id"])
        message = welcome_data["message"]
        await channel.send(message.format(member=ctx.author.mention))
        await ctx.send("Test welcome message sent.")
    else:
        await ctx.send("Welcome message has not been set up for this server.")

import discord
from discord.ext import commands
import json


BANLIST_FILE = "banlist.json"


try:
    with open(BANLIST_FILE, "r") as f:
        banlist = json.load(f)
except FileNotFoundError:
    banlist = {}


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    
    await member.ban(reason=reason)
    
   
    banlist[str(member.id)] = {
        "username": str(member),
        "reason": reason if reason else "No reason provided",
        "banned_by": str(ctx.author)
    }
    
    
    with open(BANLIST_FILE, "w") as f:
        json.dump(banlist, f)
    
    await ctx.send(f"{member.mention} has been banned <a:tick_black:1218880210536239186>")


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member_id: int):
    
    if str(member_id) in banlist:
        
        await ctx.guild.unban(discord.Object(id=member_id))
        
        
        del banlist[str(member_id)]
        
        
        with open(BANLIST_FILE, "w") as f:
            json.dump(banlist, f)
        
        await ctx.send(f"User with ID {member_id} has been unbanned <a:tick_black:1218880210536239186>")
    else:
        await ctx.send("User not found in the banlist.")




@client.command()
async def welcome(ctx):
  embed = discord.Embed(colour=0xc8dc6c)
  embed.add_field(name=f"``setwelcome``", value="type !setwelcome [channel id] {member} then your message ")
  embed.add_field(name=f"``testwelcome``", value="test your welcome message")
  embed.add_field(name=f"``autorole``", value="")



  await ctx.send(embed=embed)


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await client.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension: {filename[:-3]}")
            except Exception as e:
                print(f"Failed to load extension {filename[:-3]}: {e}")


async def main():
    async with client:
        await load()
        await client.start("MTIxODIzMDc5MjIxNjY0MTU4Ng.G86KOv.xT6x_SNab7rBHZeer-ocUfgJIbU9_k2r9fEZ6Q")
        
asyncio.run(main())


