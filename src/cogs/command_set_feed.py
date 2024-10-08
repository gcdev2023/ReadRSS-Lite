import logging
from typing import Optional, Union
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, TextChannel, DMChannel, User
from BLL.feed_bll import FeedBLL
from BLL.channel_bll import ChannelBLL
from BLL.server_bll import ServerBLL
from DTO.server_dto import ServerDTO
from DTO.channel_dto import ChannelDTO
from utils.commands_cog import CommandsCog
from utils.handle_rss import get_rss_link, read_rss_link

logger = logging.getLogger("CommandSetFeed")

class CommandSetFeed(CommandsCog):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name="setfeed")
    async def set_feed(self, ctx, link_rss: str, channel: Optional[Union[TextChannel, DMChannel]] = None):
        """Set the feed notification channel."""
        
        if not link_rss:
            await ctx.send('Please provide an RSS link.')
            return
        
        # Sử dụng kênh hiện tại nếu không có kênh nào được chỉ định
        if not channel:
            channel = ctx.channel

        await self._handle_feed(ctx, channel, ctx.author, link_rss)

    @nextcord.slash_command(name="setfeed", description="Set feed notification channel")
    async def slash_set_feed(self, interaction: Interaction, 
                             link_rss: str = SlashOption(description="The RSS feed link", required=False),
                             url: str = SlashOption(description="Website URL", required=False),
                             channel: Optional[Union[TextChannel, DMChannel]] = SlashOption(description="Kênh thông báo RSS", required=False)):
        """Lệnh slash dùng để thiết lập kênh nhận thông báo từ RSS feed. Nếu không chỉ định kênh, sẽ mặc định dùng kênh hiện tại."""
        await interaction.response.defer()

        # Sử dụng kênh hiện tại nếu không có kênh nào được chỉ định
        if not channel:
            channel = interaction.channel if isinstance(channel, TextChannel) else await interaction.user.create_dm() # type: ignore

        if link_rss and url:
            await interaction.followup.send('Please provide either an RSS link or a URL, not both.')
            return

        if not link_rss and not url:
            await interaction.followup.send('Please provide either an RSS link or a URL.')
            return

        if not link_rss and url:
            link_rss = get_rss_link(url)  # type: ignore
            if not link_rss:
                await interaction.followup.send('Not found any RSS link for the provided URL.')
                return

        await self._handle_feed(interaction.followup, channel, interaction.user, link_rss)

    async def _handle_feed(self, source, channel, user, link_rss: str):
        """Xử lý cài đặt feed và lưu vào cơ sở dữ liệu."""
        try:
            if isinstance(channel, DMChannel):
                await source.send("This command is only available in servers.")
                return
            
            feed_data = read_rss_link(rss_link=link_rss)
            if not feed_data or not feed_data[0]:
                await source.send("Not found any feed data.")
                return

            feed_dto = feed_data[0]

            # Xử lý cho DMChannel và TextChannel
            if isinstance(channel, DMChannel):
                channel_id = str(user.id) 
                server_id = str(user.id) # Trong trường hợp DM, server_id cũng là user_id
                server_name = user.name 
                channel_name = user.name
            else:
                server_id = str(channel.guild.id)
                server_name = channel.guild.name
                channel_id = str(channel.id)
                channel_name = channel.name

            server_dto = ServerDTO(server_id, server_name)
            channel_dto = ChannelDTO(channel_id, channel_name, server_dto.get_server_id())

            ServerBLL().insert_server(server_dto)
            ChannelBLL().insert_channel(channel_dto)

            feed_dto.set_channel_id(channel_dto.get_channel_id())
            FeedBLL().insert_feed(feed_dto)
            
            if isinstance(channel, TextChannel):
                await source.send(f"RSS feed has been set up for {channel.mention}.")
            elif  isinstance(channel, DMChannel):
                await source.send(f"RSS feed has been set up for **{user.name}** channel.")
            return 

        except Exception as e:
            await source.send(f"An error occurred: {e}")
            logger.error(f"Error: {e}")

async def setup(bot):
    """Hàm khởi tạo để thêm cog vào bot."""
    bot.add_cog(CommandSetFeed(bot))