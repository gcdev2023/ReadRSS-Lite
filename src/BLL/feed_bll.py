from BLL.singleton import Singleton
from DTO.feed_dto import FeedDTO
from DAL.feed_dal import FeedDAL
from typing import Optional, List


class FeedBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__feedDAL = FeedDAL()
            self._initialized = True

    def insert_feed(self, feed_dto: FeedDTO) -> bool:
        return self.__feedDAL.insert_feed(feed_dto)

    def delete_feed_by_link_atom_feed_and_channel_id(self, linkAtom_feed: str, channel_id: str) -> bool:
        return self.__feedDAL.delete_feed_by_link_atom_feed_and_channel_id(linkAtom_feed, channel_id)
    
    def delete_feed_by_link_feed_and_channel_id(self, link_feed: str, channel_id: str) -> bool:
        return self.__feedDAL.delete_feed_by_link_feed_and_channel_id(link_feed, channel_id)
   
    def delete_feed_by_channel_id(self, channel_id: str) -> bool:
        return self.__feedDAL.delete_feed_by_channel_id(channel_id)
    
    def delete_all_feed(self) -> bool:
        return self.__feedDAL.delete_all_feed()

    def update_feed_by_link_atom_feed_and_channel_id(self, linkAtom_feed: str, channel_id: str, feed_dto: FeedDTO) -> bool:
        return self.__feedDAL.update_feed_by_link_atom_feed_and_channel_id(linkAtom_feed, channel_id, feed_dto)

    def get_feed_by_link_atom_feed_and_channel_id(self, linkAtom_feed: str, channel_id: str) -> Optional[FeedDTO]:
        return self.__feedDAL.get_feed_by_link_atom_feed_and_channel_id(linkAtom_feed, channel_id)

    def get_all_feed(self) -> List[FeedDTO]:
        return self.__feedDAL.get_all_feed()
    
    def get_all_feed_by_channel_id(self, channel_id: str) -> List[FeedDTO]:
        return self.__feedDAL.get_all_feed_by_channel_id(channel_id)