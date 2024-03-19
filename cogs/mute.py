from discord.ext import commands
import discord

class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        if ctx.author.guild_permissions.manage_roles:
            
            muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
            if not muted_role:
                muted_role = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muted_role, send_messages=False)

            
            await member.add_roles(muted_role)
            await ctx.send(f"{member.mention} has been muted <a:tick_black:1218880210536239186>")
        else:
            await ctx.send("You do not have the permissions to manage roles.")


async def setup(bot):
    
    if bot.get_command("mute") is None:
        
        await bot.add_cog(mute(bot))
    else:
        print("Command 'mute' already exists. Skipping cog registration.")                