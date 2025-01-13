import nextcord
from BLL.server_bll import ServerBLL
from DTO.color_dto import ColorDTO

# Custom Embed class with default color and methods to set/get color
class EmbedCustom(nextcord.Embed):
    def __init__(self, id_server: str, **kwargs):
        # Fetch the default color from the server's settings
        server_bll = ServerBLL()
        server_dto = server_bll.get_server_by_server_id(id_server)
        if 'color' not in kwargs:
            # If no color is provided, use the server's default color
            if (server_dto is None):
                default_color = ColorDTO("red").get_hex_color()
            else:
                default_color = server_dto.get_hex_color()
            kwargs['color'] = nextcord.Color(int(default_color, 16))  # Convert hex to int

        # Set a default footer if not already set
        if 'footer' not in kwargs:
            self.set_footer(text="GCdev Summer Project 2024")
            
        super().__init__(**kwargs)

    def set_color(self, color):
        # Set the color of the embed. Color should be a nextcord.Color instance.
        if isinstance(color, nextcord.Color):
            self.color = color
        else:
            raise ValueError("color must be an instance of nextcord.Color")

    def get_color_hex(self):
        # Returns the hex code of the embed color as a string.
        return hex(self.color.value)