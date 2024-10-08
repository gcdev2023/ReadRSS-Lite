from BLL.singleton import Singleton
from DTO.emty_dto import EmtyDTO
from DAL.emty_dal import EmtyDAL
from typing import Optional, List


class EmtyBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__emtyDAL = EmtyDAL()
            self._initialized = True

    def insert_emty(self, emty_dto: EmtyDTO) -> bool:
        return self.__emtyDAL.insert_emty(emty_dto)

    def delete_emty_by_link_emty_and_channel_id(self, emty_link: str, channel_id: str) -> bool:
        return self.__emtyDAL.delete_emty_by_link_emty_and_channel_id(emty_link, channel_id)

    def delete_emty_by_link_atom_feed_and_channel_id(self, link_atom_feed: str, channel_id: str) -> bool:
        return self.__emtyDAL.delete_emty_by_link_atom_and_channel_id(link_atom_feed, channel_id)
    
    def delete_emty_by_channel_id(self, channel_id: str) -> bool:
        return self.__emtyDAL.delete_emty_by_channel_id(channel_id)
    
    def delete_all_emty(self) -> bool:
        return self.__emtyDAL.delete_all_emty()

    def get_emty_by_link_emty_and_channel_emty(self, emty_link: str, channel_id: str) -> Optional[EmtyDTO]:
        return self.__emtyDAL.get_emty_by_link_emty_and_channel_id(emty_link, channel_id)

    def get_all_emty(self) -> List[EmtyDTO]:
        return self.__emtyDAL.get_all_emty()