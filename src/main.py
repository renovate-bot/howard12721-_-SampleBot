import discord
from discord.ext import commands
from cogs.sample_cog import SampleCog
import os

class SampleBot(commands.Bot):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        
    async def setup_hook(self) -> None:
        await bot.add_cog(SampleCog(bot))

if __name__ == "__main__":
    
    bot = SampleBot(command_prefix='!', intents=discord.Intents.all())
    
    bot.run(token=os.getenv("TOKEN"))
