import discord
from discord.ext import commands
import json

class AutoRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        try:
            with open("autoroles.json", "r") as file:
                autoroles = json.load(file)
        except FileNotFoundError:
            autoroles = {}

        
        autorole_id = autoroles.get(str(member.guild.id))

       
        if autorole_id:
            
            autorole = member.guild.get_role(autorole_id)
            if autorole:
               
                try:
                    await member.add_roles(autorole)
                    print(f"Assigned autorole {autorole.name} to {member}")
                except Exception as e:
                    print(f"Failed to assign autorole to {member}: {e}")
            else:
                print("Autorole not found for guild:", member.guild.id)

    @commands.command()
    async def setautorole(self, ctx, role: discord.Role):
       
        if ctx.author == ctx.guild.owner:
            
            try:
                with open("autoroles.json", "r") as file:
                    autoroles = json.load(file)
            except FileNotFoundError:
                autoroles = {}

            
            autoroles[str(ctx.guild.id)] = role.id

            
            with open("autoroles.json", "w") as file:
                json.dump(autoroles, file, indent=4)

            await ctx.send(f" Successfully autorole set to {role.name}<a:tick_black:1218880210536239186>")
        else:
            await ctx.send("Only the server owner can set the autorole.")

async def setup(bot):
    
    if bot.get_command("autorole") is None:
        
        await bot.add_cog(AutoRole(bot))
    else:
        print("Command 'autorole' already exists. Skipping cog registration.")


async def setup(bot):
   
    if bot.get_command("autorole") is None:
       
        await bot.add_cog(AutoRole(bot))
    else:
        print("Command 'autorole' already exists. Skipping cog registration.") 
