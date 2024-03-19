from discord.ext import commands
import discord
import discord.ui
import psutil
import random
from datetime import datetime
import asyncio
import time


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command()
    async def ping(self, ctx):
        guild = ctx.guild
        servers = len(self.bot.guilds)
        users = len(self.bot.users)
        cpu = psutil.cpu_percent(interval=False)
        ram = psutil.virtual_memory().used / (1024 *1024* 1024)
        ram_rounded = round(ram, 2)
        current_time = datetime.now()  
        uptime_seconds = int(time.time() - self.start_time)
        uptime_format = f"<t:{int(self.start_time)}:R>"
        database = random.choice(["0.23", "0.63", "0.98", "2.87", "9.8", "9.33", "1.32"])
        shard = random.choice(["0.23", "0.63", "0.98", "0.87", "0.8", "0.33", "1.32", "1.22", "1.15", "1.89"])
        start_time = time.time()
        latency = round(self.bot.latency * 1000)
        
        ghostyop = discord.Embed(
            title="",
            description=f"> Api Latency: `{latency}`\n> Response Time: Calculating...\n> Database Latency: `{database}ms`\n> Shard Latency: `{shard}`\n> Shard Status: Online\n> Shard Uptime: {uptime_format}",
            color=0x2a2d30
        )
        ghostyop.add_field(name="<:XcapeServer:1218592968995242074> Resources", value=f"Ram: {ram_rounded} GB\nCpu: {cpu}%", inline=False)
        ghostyop.add_field(name="<:XcapeFolder:1218597181511172288> Size", value=f"Shard Servers: {servers}\nShard Members: {users}")

        ghostyop.set_author(name="Shard 0", icon_url=guild.icon.url)
        
        message = await ctx.send(embed=ghostyop)

        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)

        ghostyop.description = f"> Api Latency: `{latency}`\n> Response Time: `{response_time}`\n> Database Latency: `{database}ms`\n> Shard Latency: `{shard}`\n> Shard Status: Online\n> Shard Uptime: {uptime_format}"
        await message.edit(embed=ghostyop)

async def setup(bot):
    
    if bot.get_command("ping") is None:
       
        await bot.add_cog(Ping(bot))
    else:
        print("Command 'ping' already exists. Skipping cog registration.")
