from discord.ext import commands
import discord

class lock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lock(self, ctx):
        
        if ctx.author.guild_permissions.manage_channels:
            
            if not ctx.channel.overwrites_for(ctx.guild.default_role).send_messages:
                embed = discord.Embed(title="Channel Lock Status", description="This channel is already locked.", color=discord.Color.blue())
                await ctx.send(embed=embed)
                return

            
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
            embed = discord.Embed(title="Channel Lock Status", description="Channel locked successfully <a:tick_black:1218880210536239186>", color=discord.Color.green())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Permission Denied", description="You do not have permission to manage channels.", color=discord.Color.red())
            await ctx.send(embed=embed)

async def setup(bot):
    
    if bot.get_command("lock") is None:
        
        await bot.add_cog(lock(bot))
    else:
        print("Command 'lock' already exists. Skipping cog registration.")