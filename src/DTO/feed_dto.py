from datetime import datetime
from types import NotImplementedType
from typing import Optional

class FeedDTO:
    def __init__(self, link_feed: str, link_atom_feed: str, title_feed: str, description_feed: str, logo_feed: str, pubDate_feed: datetime, channel_id: Optional[str]=None):
        self.__link_feed = link_feed
        self.__link_atom_feed = link_atom_feed
        self.__title_feed = title_feed
        self.__description_feed = description_feed
        self.__logo_feed = logo_feed
        self.__pubdate_feed = pubDate_feed
        self.__channel_id = channel_id

    def __str__(self) -> str:
        return f"FeedDTO(link_feed={self.__link_feed}, link_atom_feed={self.__link_atom_feed}, title_feed={self.__title_feed}, description_feed={self.__description_feed}, logo_feed={self.__logo_feed}, pubdate_feed={self.__pubdate_feed}, channel_id={self.__channel_id})"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, FeedDTO):
            return NotImplementedType
        return self.__link_feed == other.__link_feed and self.__link_atom_feed == other.__link_atom_feed and self.__title_feed == other.__title_feed and self.__description_feed == other.__description_feed \
            and self.__logo_feed == other.__logo_feed and self.__pubdate_feed == other.__pubdate_feed and self.__channel_id == other.__channel_id
    
    def set_link_feed(self, link_feed: str) -> None:
        self.__link_feed = link_feed
    
    def set_link_atom_feed(self, link_atom_feed: str) -> None:
        self.__link_atom_feed = link_atom_feed
        
    def set_title_feed(self, title_feed: str) -> None:
        self.__title_feed = title_feed
    
    def set_description_feed(self, description_feed: str) -> None:
        self.__description_feed = description_feed
    
    def set_logo_feed(self, logo_feed: str) -> None:
        self.__logo_feed = logo_feed
    
    def set_pubdate_feed(self, pubdate_feed: datetime) -> None:
        self.__pubdate_feed = pubdate_feed
    
    def set_channel_id(self, channel_id: str) -> None:
        self.__channel_id = channel_id
        
    def get_link_feed(self) -> str:
        return self.__link_feed
    
    def get_link_atom_feed(self) -> str:
        return self.__link_atom_feed
    
    def get_title_feed(self) -> str:
        return self.__title_feed
    
    def get_description_feed(self) -> str:
        return self.__description_feed
    
    def get_logo_feed(self) -> str:
        return self.__logo_feed
    
    def get_pubdate_feed(self) -> datetime:
        return self.__pubdate_feed
    
    def get_channel_id(self) -> str:
        return self.__channel_id