import discord
from discord.ext import commands

class AFK(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.afk_users = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

       
        for user_id, data in self.afk_users.items():
            if f"<@{user_id}>" in message.content:
                embed = discord.Embed(title="AFK Status", description=f"{message.author.mention}, {message.guild.get_member(user_id)} is currently AFK: {data['message']}", color=discord.Color.orange())
                await message.channel.send(embed=embed)

     
        if message.author.id in self.afk_users:
            del self.afk_users[message.author.id]
            embed = discord.Embed(title="AFK Removed", description=f"Welcome back, {message.author.mention}! Your AFK status has been removed.", color=discord.Color.green())
            await message.channel.send(embed=embed)

    @commands.command()
    async def afk(self, ctx, *, message: str = "AFK"):
        self.afk_users[ctx.author.id] = {'message': message}
        embed = discord.Embed(title="AFK Set", description=f"{ctx.author.mention} is now AFK: {message}", color=discord.Color.orange())
        await ctx.send(embed=embed)

async def setup(bot):
    
    if bot.get_command("afk") is None:
        
        await bot.add_cog(AFK(bot))
    else:
        print("Command 'afk' already exists. Skipping cog registration.")            
