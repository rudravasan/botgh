import discord
from discord.ext import commands
import json

class Trigger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.trigger_messages = {}

        
        try:
            with open('trigger_messages.json', 'r') as file:
                self.trigger_messages = json.load(file)
        except FileNotFoundError:
            self.trigger_messages = {}

    def save_trigger_messages(self):
        
        with open('trigger_messages.json', 'w') as file:
            json.dump(self.trigger_messages, file, indent=4)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def trigger(self, ctx, trigger_word, *, message):
       
        self.trigger_messages[trigger_word.lower()] = message
        self.save_trigger_messages()
        await ctx.send(f'Trigger message set for "{trigger_word}".')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()

        for trigger_word, response in self.trigger_messages.items():
            if trigger_word in content:
                await message.channel.send(response)


async def setup(bot):
   
    if bot.get_command("trigger") is None:
        
        await bot.add_cog(Trigger(bot))
    else:
        print("Command 'trigger' already exists. Skipping cog registration.")
