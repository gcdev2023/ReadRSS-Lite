class ColorDTO:
    def __init__(self, color: str):
        color_mapping = {
            "red": "0xFF0000",
            "yellow": "0xF1C40F",
            "green": "0x2ECC71",
            "blue": "0x3498DB"
        }
        # Set the color, or default to white if the color is not in the mapping
        self.__hex_color = color_mapping[color] if color in color_mapping else "0x808080"
        self.__name_color = color if color in color_mapping else "gray"
        
    def __str__(self):
        return f"ColorDTO(name_color={self.__name_color}, hex_color={self.__hex_color})"
    
    def __eq__(self, other):
        return self.__hex_color == other.__hex_color
    
    def get_hex_color(self):
        return self.__hex_color
    
    def get_name_color(self):
        return self.__name_color