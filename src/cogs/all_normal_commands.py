import logging
import nextcord
from nextcord.ext import commands
from utils.handle_rss import get_rss_link
from GUI.embed_custom import EmbedCustom
from GUI.button_of_help_command import ButtonOfHelpCommnad
from utils.commands_cog import CommandsCog

logger = logging.getLogger("AllNormalCommands")

class AllNormalCommands(CommandsCog):  # Đảm bảo kế thừa từ CommandsCog
    def __init__(self, bot):
        super().__init__(bot)  # Gọi lớp cha để khởi tạo bot và logger
        
    def ping(self):
        return f'Pong! {round(self.bot.latency * 1000)}ms'

    @commands.command(name="ping")
    async def commmand_ping(self, ctx):
        '''Check bot latency'''
        await ctx.send(self.ping())

    @nextcord.slash_command(name="ping", description="Check bot latency")
    async def slash_command_ping(self, interaction):
        await interaction.response.defer()
        await interaction.followup.send(self.ping())
        
    def get_rss(self, url: str) -> str:
        link_rss = get_rss_link(url)
        return f'''RSS link:```{link_rss}```''' if link_rss else "No RSS link found."
    
    @commands.command(name="getrss")
    async def command_get_rss(self, ctx, url: str):
        '''Get the RSS link of a website'''
        if await self.is_dm_channel(ctx):
            return
        try:
            await ctx.send(self.get_rss(url))
        except Exception as e:
            await ctx.send(f"Error: {e}")
            logger.error(f"Error: {e}")

    @nextcord.slash_command(name="getrss", description="Get the RSS link of a website")
    async def slash_command_get_rss(self, interaction, url: str):
        await interaction.response.defer()
        try:
            await interaction.followup.send(self.get_rss(url))
        except Exception as e:
            await interaction.followup.send(f"Error: {e}", ephemeral=True)
            logger.error(f"Error: {e}")

    @nextcord.slash_command(name="help", description="List of commands")
    async def help(self, interaction):
        '''List of commands'''
        await interaction.response.defer()
        try:
            available_commands = [command.name for command in self.bot.commands]
            available_slash_commands = [command.name for command in self.bot.get_application_commands()]

            embed = EmbedCustom(
                id_server=str(interaction.guild.id) if interaction.guild else "DM",
                title="List of commands",
                description=f'''
command prefix `{self.bot.command_prefix}`
- The current commands have: {", ".join(available_commands)}
- The current slash commands have: {", ".join(available_slash_commands)}
                '''
            )
            await interaction.followup.send(embed=embed, view=ButtonOfHelpCommnad())
        except Exception as e:
            await interaction.followup.send(f"An error occurred: {e}", ephemeral=True)
            logger.error(f"Error: {e}")

async def setup(bot):
    bot.add_cog(AllNormalCommands(bot))