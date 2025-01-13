import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ui import View, Button, button

class ButtonOfHelpCommnad(View):
    def __init__(self):
        super().__init__(timeout=None)
        link_server_button = Button(style=nextcord.ButtonStyle.link, label="Our server", url="https://discord.com/invite/Q7NXBFpZeM")
        self.add_item(link_server_button)
        link_bot_button = Button(style=nextcord.ButtonStyle.link, label="Link invite", url="https://discord.com/oauth2/authorize?client_id=1236720788187381760&permissions=0&integration_type=0&scope=bot")
        self.add_item(link_bot_button)

    @button(label="Infor", style=nextcord.ButtonStyle.primary)
    async def send_message(self, button: Button, interaction: Interaction):
        await interaction.response.defer()
        await interaction.followup.send(''' 
```This is a Discord bot built with Python. ReadRSS bot brings RSS feeds 
to your Discord server. Receive notifications from news sources 
including Facebook and much more. 

                        -- ABOUT US --
                                                       Summer 2024
         ██████╗  ██████╗██████╗ ███████╗██╗   ██╗     + HaoWasabi
        ██╔════╝ ██╔════╝██╔══██╗██╔════╝██║   ██║     + nguyluky
        ██║  ███╗██║     ██║  ██║█████╗  ██║   ██║     + NaelTuhline
        ██║   ██║██║     ██║  ██║██╔══╝  ╚██╗ ██╔╝     + tivibin789
        ╚██████╔╝╚██████╗██████╔╝███████╗ ╚████╔╝      + phusomnia
        ╚═════╝  ╚═════╝╚═════╝ ╚══════╝  ╚═══╝        + camdao
                                                     
        ```''')