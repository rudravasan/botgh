import discord
from discord.ext import commands

class hide(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hide(self, ctx):
       
        if ctx.author.guild_permissions.manage_channels:
          
            channel = ctx.channel

           
            await channel.set_permissions(ctx.guild.default_role, read_messages=False)

            await ctx.send(f"{channel.mention} has been hidden <a:tick_black:1218880210536239186>")
        else:
            await ctx.send("You do not have permission to manage channels.")

async def setup(bot):
    
    if bot.get_command("hide") is None:
        
        await bot.add_cog(hide(bot))
    else:
        print("Command 'hide' already exists. Skipping cog registration.") 
