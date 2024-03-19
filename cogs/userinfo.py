import discord
from discord.ext import commands
import time

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        """
        Display information about the specified user or the user invoking the command.
        """
        try:
            if member is None:
                member = ctx.author

            embed = discord.Embed(title="<a:users:1218628526648070256> User Information", color=discord.Color.blue())

            embed.add_field(name="<:username:1218629837665861824> Username", value=member.name, inline=True)
            embed.add_field(name="<a:gd_hashtag:1218626813597716530> Discriminator", value=member.discriminator, inline=True)
            embed.add_field(name="<a:dancingcat:1218629406004740238> User ID", value=member.id, inline=True)
            embed.add_field(name="<a:joined:1218630200997187724> Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
            embed.add_field(name="<a:discord4:1218627576222711869> Joined Discord", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)

            await ctx.send(embed=embed)
        except Exception as e:
            print(e)  
            await ctx.send("An error occurred while processing the command.")

async def setup(bot):
    
    if bot.get_command("userinfo") is None:
        
        await bot.add_cog(UserInfo(bot))
    else:
        print("Command 'userninfo' already exists. Skipping cog registration.")

