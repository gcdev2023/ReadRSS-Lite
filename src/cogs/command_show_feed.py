import logging
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, DMChannel
from BLL.feed_bll import FeedBLL
from GUI.embed_custom import EmbedCustom
from utils.commands_cog import CommandsCog

logger = logging.getLogger("CommandShowChannel")

class CommandShowChannel(CommandsCog):
    def __init__(self, bot):
        super().__init__(bot)
        
    @commands.command(name="show")
    async def command_show(self, ctx):
        await self._show_channel(ctx=ctx, guild=ctx.guild, user=ctx.author)
        
    @nextcord.slash_command(name="show", description="Show the feed notification channel")
    async def slash_command_show(self, interaction: Interaction):
        await interaction.response.defer()
        await self._show_channel(ctx=interaction.followup, guild=interaction.guild, user=interaction.user)

    async def _show_channel(self, ctx, guild=None, user=None):
        try:
            if not guild:
                await ctx.send("This command is only available in servers.")
                return
            else:
                guild_id = str(guild.id)  # Guild ID for servers
                guild_name = guild.name

            feed_bll = FeedBLL()
            server_data = {}
            num_feeds = 0

            for feed_dto in feed_bll.get_all_feed():
                channel_id = int(feed_dto.get_channel_id())
                
                if not guild:
                    # So sánh ID kênh với user ID trong DM
                    if str(user.id) == str(channel_id): # type: ignore
                        channel_info = f"- **DM Channel** - [{feed_dto.get_title_feed()}]({feed_dto.get_link_feed()})"
                        server_data.setdefault("Direct Message", []).append(channel_info)
                        num_feeds += 1
                else:
                    # Xử lý cho TextChannel trong guild
                    channel = self.bot.get_channel(channel_id)
                    if channel is not None and channel.guild.id == int(guild_id):
                        server_name = f"**Server:** {guild_name} ({guild_id})"
                        channel_info = f"- **Channel:** {channel.mention} - [{feed_dto.get_title_feed()}]({feed_dto.get_link_feed()})"
                        server_data.setdefault(server_name, []).append(channel_info)
                        num_feeds += 1

            embed = EmbedCustom(
                id_server=guild_id,
                title="List of Feeds in Channels",
                description=f"You have {num_feeds} feeds in channels:"
            )

            for server_name, channels in server_data.items():
                embed.add_field(name=server_name, value="\n".join(channels), inline=False)

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            logger.error(f"Error: {e}")

async def setup(bot):
    bot.add_cog(CommandShowChannel(bot))