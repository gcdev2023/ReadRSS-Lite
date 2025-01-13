from types import NotImplementedType

class ChannelDTO:
    def __init__(self, channel_id: str, server_id: str, channel_name: str, is_active=True):
        self.__channel_id = channel_id
        self.__server_id = server_id
        self.__channel_name = channel_name
        self.__is_active = is_active
        
    def __str__(self) -> str:
        return f"ChannelDTO(channel_id={self.__channel_id}, server_id={self.__server_id}, channel_name={self.__channel_name}, is_active={self.__is_active})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ChannelDTO):
            return NotImplementedType
        return self.__channel_id == other.__channel_id and self.__channel_name == other.__channel_name
    
    def set_channel_id(self, channel_id: str) -> None:
        self.__channel_id = channel_id
    
    def set_server_id(self, server_id: str) -> None:
        self.__server_id = server_id
        
    def set_channel_name(self, channel_name: str) -> None:
        self.__channel_name = channel_name
        
    def set_state(self, is_active: bool) -> None:
        self.__is_active = is_active
        
    def get_channel_id(self) -> str:
        return self.__channel_id
    
    def get_server_id(self) -> str:
        return self.__server_id
    
    def get_channel_name(self) -> str:
        return self.__channel_name
    
    def get_state(self) -> bool:
        return self.__is_active