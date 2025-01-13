from BLL.singleton import Singleton
from DAL.channel_dal import ChannelDAL
from DTO.channel_dto import ChannelDTO
from typing import Optional, List

class ChannelBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__channelDAL = ChannelDAL()
            self._initialized = True
    
    def insert_channel(self, channel_dto: ChannelDTO) -> bool:
        return self.__channelDAL.insert_channel(channel_dto)

    def delete_channel_by_channel_id(self, channel_link: str) -> bool:
        return self.__channelDAL.delete_channel_by_channel_id(channel_link)
            
    def delete_all_channel(self) -> bool:
        return self.__channelDAL.delete_all_channel()

    def update_channel(self, Channel_dto: ChannelDTO) -> bool:
        return self.__channelDAL.update_channel(Channel_dto)
            
    def get_channel_by_channel_id(self, channel_id: str) -> Optional[ChannelDTO]:
        return self.__channelDAL.get_channel_by_channel_id(channel_id)

    def get_all_channel(self) -> List[ChannelDTO]:
        return self.__channelDAL.get_all_channel()
    