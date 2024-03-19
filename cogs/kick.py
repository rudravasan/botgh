import discord
from discord.ext import commands

class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        
        if ctx.author.guild_permissions.kick_members:
            try:
                await member.kick(reason=reason)
                await ctx.send(f"{member.mention} has been kicked <a:tick_black:1218880210536239186>")
            except discord.Forbidden:
                await ctx.send("I don't have permission to kick members.")
        else:
            await ctx.send("You do not have the permissions to kick members.")


async def setup(bot):
    
    if bot.get_command("kick") is None:
        
        await bot.add_cog(KickCog(bot))
    else:
        print("Command 'kick' already exists. Skipping cog registration.")                                    