import discord
from discord.ext import commands
from datetime import datetime


class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f"Server Information - {guild.name}", color=discord.Color.blurple())
        embed.add_field(name="Owner", value=guild.owner, inline=True)
        embed.add_field(name="Region", value=guild.region, inline=True)
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Roles", value=len(guild.roles), inline=True)
        embed.add_field(name="Text Channels", value=len(guild.text_channels), inline=True)
        embed.add_field(name="Voice Channels", value=len(guild.voice_channels), inline=True)
        embed.add_field(name="Created At", value=guild.created_at.strftime("%b %d, %Y"), inline=True)
        await ctx.send(embed=embed)


async def setup(bot):
    
    if bot.get_command("serverinfo") is None:
      
        await bot.add_cog(serverinfo(bot))
    else:
        print("Command 'serverinfo' already exists. Skipping cog registration.") 

