import discord
from discord.ext import commands
import time

class badg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()


    @commands.command()
    async def badges(self, ctx, member: discord.Member = None):
        """
        badges information 
        """
        try:
            if member is None:
                member = ctx.author

            embed = discord.Embed(title="<a:users:1218628526648070256> Badges Information", color=discord.Color.blue())

            embed.add_field(name="<:owner:1219196598379216936> Owner", value="", inline=True)
            embed.add_field(name="<:XcapeStar:1219242695957155972> Co Owner", value="", inline=True)
            embed.add_field(name="<:MekoAdmin:1219236243314053213> Admin", value="", inline=True)
            embed.add_field(name="<:MekoModeration:1219236271763755029> Staff", value="" ,inline=True)
            embed.add_field(name="<:XcapeSupporter:1219249225615937636> Supporter", value="" , inline=True)
            embed.add_field(name="<:XcapeFriend:1219243868826898504> Friend", value="" , inline=True)

            await ctx.send(embed=embed)
        except Exception as e:
            print(e)  
            await ctx.send("An error occurred while processing the command.")

async def setup(bot):
    
    if bot.get_command("bgi") is None:
        
        await bot.add_cog(badg(bot))
    else:
        print("Command 'bgi' already exists. Skipping cog registration.") 
