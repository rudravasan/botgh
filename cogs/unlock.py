from discord.ext import commands
import discord

class unlock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unlock(self, ctx):
       
        if ctx.author.guild_permissions.manage_channels:
            
            if ctx.channel.overwrites_for(ctx.guild.default_role).send_messages:
                embed = discord.Embed(title="Channel Unlock Status", description="This channel is already unlocked.", color=discord.Color.blue())
                await ctx.send(embed=embed)
                return

            
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
            embed = discord.Embed(title="Channel Unlock Status", description="Channel unlocked successfully <a:tick_black:1218880210536239186>", color=discord.Color.green())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Permission Denied", description="You do not have permission to manage channels.", color=discord.Color.red())
            await ctx.send(embed=embed)

async def setup(bot):
    
    if bot.get_command("unlock") is None:
        
        await bot.add_cog(unlock(bot))
    else:
        print("Command 'unlock' already exists. Skipping cog registration.")            