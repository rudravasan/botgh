from discord.ext import commands
import discord

class unmute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        if ctx.author.guild_permissions.manage_roles:
            muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

            if muted_role in member.roles:
                await member.remove_roles(muted_role)
                await ctx.send(f"{member.mention} has been unmuted <a:tick_black:1218880210536239186>")
            else:
                await ctx.send(f"{member.mention} is not muted.")
        else:
            await ctx.send("You do not have the permissions to manage roles.")

async def setup(bot):
    
    if bot.get_command("unmute") is None:
        
        await bot.add_cog(unmute(bot))
    else:
        print("Command 'unmute' already exists. Skipping cog registration.")                