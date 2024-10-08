from typing import Optional
from nextcord import DMChannel, TextChannel
from nextcord.ext.commands import Context
from nextcord import Interaction
from typing import Optional

from pyparsing import Opt

class CheckCogs:
    @staticmethod
    async def is_dm_channel(ctx):
        if isinstance(ctx.channel, DMChannel):
            return True
        return False
    
    @staticmethod
    async def is_text_channel(ctx):
        if isinstance(ctx.channel, TextChannel):
            return True
        return False
    
    @staticmethod
    async  def is_server_owner(ctx: Optional[Context] = None, interaction: Optional[Interaction] = None):
        # Kiểm tra nếu ctx hoặc interaction có giá trị, và đảm bảo chỉ có một trong hai được sử dụng
        if ctx and not interaction:
            # Kiểm tra guild có tồn tại và ctx.author có phải là chủ sở hữu guild không
            return ctx.guild is not None and ctx.author.id == ctx.guild.owner_id
        elif interaction and not ctx: 
        # Kiểm tra guild có tồn tại và interaction.user có phải là chủ sở hữu guild không
            if interaction.guild and interaction.user:
                return interaction.user.id == interaction.guild.owner_id
        return False