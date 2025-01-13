from calendar import c
import logging
import nextcord
from nextcord.ext import commands
from nextcord import DMChannel, Interaction, SlashOption, TextChannel
from typing import Optional, Union
from BLL.channel_bll import ChannelBLL
from BLL.emty_bll import EmtyBLL
from BLL.feed_bll import FeedBLL
from utils.commands_cog import CommandsCog
from utils.handle_rss import get_rss_link

logger = logging.getLogger("CommandDeleteFeed")

class CommandDeleteFeed(CommandsCog):
    def __init__(self, bot):
        super().__init__(bot)
        
    @commands.command(name="deletefeed")
    async def command_delete_feed(self, ctx, channel, link_rss: Optional[str] = None):
        '''Delete feed notification channel.'''
        if not link_rss:
            await ctx.send('Please provide an RSS link.')
            return
        await self._delete_feed(ctx, channel, ctx.author,link_rss)

    @nextcord.slash_command(name="deletefeed", description="Delete feed notification channel")
    async def slash_delete_feed(self, interaction: Interaction, 
                                channel: Union[TextChannel, DMChannel] = SlashOption(description="Target channel"), 
                                link_rss: Optional[str] = SlashOption(description="The RSS feed link", required=False), 
                                url: Optional[str] = SlashOption(description="Website URL", required=False)):
        await interaction.response.defer()
        
        if link_rss and url:
            await interaction.followup.send('Please provide either an RSS link or a URL, not both.')
            return
        
        if url:
            link_rss = get_rss_link(url)
            if not link_rss:
                await interaction.followup.send('RSS link not found for the provided URL.')
                return
        await self._delete_feed(interaction.followup, channel, interaction.user, link_rss)

    async def _delete_feed(self, source, channel, user, link_rss: Optional[str] = None):
        try:
            
            feed_bll = FeedBLL()
            emty_bll = EmtyBLL()
            channel_id = str(channel.id) if channel else str(user.id)
            
            # Chi dung duoc o kenh DMChannel khi co premium
            if isinstance(channel, DMChannel):
                await source.send("This command is only available in servers.")
                return
            
            if link_rss:
                if not feed_bll.get_feed_by_link_atom_feed_and_channel_id(link_rss, channel_id):
                    if isinstance(channel, TextChannel):
                        await source.send(f"RSS feed not found in {channel.mention}.")
                    else:
                        await source.send(f"RSS feed not found in the **{user.name}** channel.")
                    return 
                feed_bll.delete_feed_by_link_atom_feed_and_channel_id(link_rss, channel_id)
                emty_bll.delete_emty_by_link_atom_feed_and_channel_id(link_rss, channel_id)
            else:
                feed_bll.delete_feed_by_channel_id(channel_id or str(user.id))
                emty_bll.delete_emty_by_channel_id(channel_id or str(user.id))
        
            await source.send(f"Successfully deleted feed(s) from channel.")
        
        except Exception as e:
            await source.send(f"An error occurred: {e}")
            logger.error(f"Error: {e}")
                  
async def setup(bot):
    bot.add_cog(CommandDeleteFeed(bot))