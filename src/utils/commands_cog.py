import logging
from nextcord.ext import commands
from .check_cogs import CheckCogs
from typing import Optional
from nextcord.ext.commands import Context
from nextcord import Interaction

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    async def is_dm_channel(self, ctx):
        if await CheckCogs.is_dm_channel(ctx):
            await ctx.send("Can not send DMChannels")
            return True
        else: 
            return False
      
    async def is_server_owner(self, ctx: Optional[Context] = None, interaction: Optional[Interaction] = None) -> bool:
        if not ctx and not interaction:
            logging.error("Both ctx and interaction are None")
            return False

        if ctx and await CheckCogs.is_server_owner(ctx=ctx):
            await ctx.send("You are not the server owner")
            return True
        
        if interaction and await CheckCogs.is_server_owner(interaction=interaction):
            await interaction.followup.send("You are not the server owner", ephemeral=True)
            return True
        
        return False