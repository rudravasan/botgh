import discord
from discord.ext import commands
import json
import os

class LevelSystem(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.levels_file = "levels.json"
        self.load_levels()

    def load_levels(self):
        if os.path.exists(self.levels_file):
            with open(self.levels_file, "r") as file:
                self.levels = json.load(file)
        else:
            self.levels = {}

    def save_levels(self):
        with open(self.levels_file, "w") as file:
            json.dump(self.levels, file, indent=4)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        user_id = str(message.author.id)
        if user_id not in self.levels:
            self.levels[user_id] = {"xp": 0, "level": 1}
            self.save_levels()

        self.levels[user_id]["xp"] += 5

        if self.levels[user_id]["xp"] >= 100:
            self.levels[user_id]["level"] += 1
            self.levels[user_id]["xp"] = 0
            await message.channel.send(f" Congratulations, {message.author.mention}! You've leveled up to level {self.levels[user_id]['level']}!<a:levelup:1218896151139323965>")

        self.save_levels()

    @commands.command()
    async def rank(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        user_id = str(member.id)
        if user_id in self.levels:
            level_info = self.levels[user_id]
            await ctx.send(f"{member.display_name} is at level {level_info['level']} with {level_info['xp']} XP<:levele6LevelLVL:1218896335152091176>")
        else:
            await ctx.send("User not found in the leveling system.")

async def setup(bot):
    
    if bot.get_command("LevelSystem") is None:
       
        await bot.add_cog(LevelSystem(bot))
    else:
        print("Command 'LevelSystem' already exists. Skipping cog registration.")
