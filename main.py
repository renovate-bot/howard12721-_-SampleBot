import discord
from discord.ext import commands
from cogs.sample_cog import SampleCog
import os
import json
import shutil

class SampleBot(commands.Bot):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')

if __name__ == "__main__":
    
    if not os.path.exists('./config.json'):
        shutil.copy('./config.json.template', './config.json')
        
    with open('./config.json', 'r') as f:
        data = json.load(f)

    token = data['token']
    
    bot = SampleBot(command_prefix='!', intents=discord.Intents.all())
    
    bot.add_cog(SampleCog(bot))
    
    bot.run(token=token)
