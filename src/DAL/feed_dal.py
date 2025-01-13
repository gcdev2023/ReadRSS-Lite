import sqlite3
from typing import List, Optional
from DTO.feed_dto import FeedDTO
from .base_dal import BaseDAL, logger

class FeedDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        self.open_connection()
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tbl_feed(
                link_feed TEXT,
                link_atom_feed TEXT,
                title_feed TEXT,
                description_feed TEXT,
                logo_feed TEXT,
                pubdate_feed DATETIME,
                channel_id TEXT ,
                PRIMARY KEY (link_feed, link_atom_feed, channel_id),
                FOREIGN KEY (channel_id) REFERENCES tbl_channel(channel_id)
            )
            ''')
            self.connection.commit()
            logger.info(f"Table 'tbl_feed' created successfully.")
        except sqlite3.Error as e:
            logger.error(f"Error creating table 'tbl_feed': {e}")
        finally:
            self.close_connection()
            
    def insert_feed(self, feed_dto: FeedDTO) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                    INSERT INTO tbl_feed (link_feed, link_atom_feed, title_feed, description_feed, logo_feed, pubdate_feed, channel_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (feed_dto.get_link_feed(), feed_dto.get_link_atom_feed(), feed_dto.get_title_feed(), 
                          feed_dto.get_description_feed(), feed_dto.get_logo_feed(), feed_dto.get_pubdate_feed(), feed_dto.get_channel_id()))
                self.connection.commit()
                logger.info(f"Data inserted into 'tbl_feed' successfully.")
                return True
        except sqlite3.IntegrityError as e:
            logger.error(f"Feed with link_atom_feed={feed_dto.get_link_atom_feed()} and link_feed={feed_dto.get_link_feed()} already exists in 'tbl_feed'")
            return False
        except sqlite3.Error as e:
            logger.error(f"Error inserting data into 'tbl_feed': {e}")
            return False
        finally:
            self.close_connection()
            
    def delete_feed_by_link_atom_feed_and_channel_id(self, link_atom_feed: str, channel_id: str) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                DELETE FROM tbl_feed WHERE link_atom_feed = ? and channel_id = ?
                ''', (link_atom_feed,channel_id))
                self.connection.commit()
                logger.info(f"Data deleted from 'tbl_feed' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting data from 'tbl_feed': {e}")
            return False
        finally:
            self.close_connection()
            
    def delete_feed_by_link_feed_and_channel_id(self, link_feed: str, channel_id: str) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                DELETE FROM tbl_feed WHERE link_feed = ? and channel_id = ?
                ''', (link_feed,channel_id))
                self.connection.commit()
                logger.info(f"Data deleted from 'tbl_feed' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting data from 'tbl_feed': {e}")
            return False
        finally:
            self.close_connection()
            
    def delete_feed_by_channel_id(self, channel_id: str) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                DELETE FROM tbl_feed WHERE channel_id = ?
                ''', (channel_id,))
                self.connection.commit()
                logger.info(f"Data deleted from 'tbl_feed' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting data from 'tbl_feed': {e}")
            return False
        finally:
            self.close_connection()
        
    def delete_all_feed(self) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                DELETE FROM tbl_feed
                ''')
                self.connection.commit()
                logger.info(f"All data deleted into 'tbl_feed' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting data into 'tbl_feed': {e}")
            return False
        finally:
            self.close_connection()
            
    def update_feed_by_link_atom_feed_and_channel_id(self, link_atom_feed: str, channel_id: str, feed_dto: FeedDTO) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                UPDATE tbl_feed SET link_feed = ?, link_atom_feed = ?, title_feed = ?, description_feed = ?, logo_feed = ?, pubdate_feed = ?
                WHERE link_atom_feed = ? and channel_id = ?
                ''', (feed_dto.get_link_feed(), feed_dto.get_link_atom_feed(), feed_dto.get_title_feed(), 
                      feed_dto.get_description_feed(), feed_dto.get_logo_feed(), feed_dto.get_pubdate_feed(), link_atom_feed, channel_id))
                self.connection.commit()
                logger.info(f"Data updated in 'tbl_feed' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error updating data in 'tbl_feed': {e}")
            return False
        finally:
            self.close_connection()
            
    def get_feed_by_link_atom_feed_and_channel_id(self, link_atom_feed: str, channel_id: str) -> Optional[FeedDTO]:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                SELECT * FROM tbl_feed WHERE link_atom_feed = ? and channel_id = ?
                ''', (link_atom_feed, channel_id))
                row = self.cursor.fetchone()
                if row:
                    return FeedDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                return None
        except sqlite3.Error as e:
            logger.error(f"Error fetching data from 'tbl_feed': {e}")
            return None
        finally:
            self.close_connection()
        
    def get_all_feed(self) -> List[FeedDTO]:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                SELECT * FROM tbl_feed 
                ''')
                rows = self.cursor.fetchall()
                if rows:
                    return [FeedDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]
                else:
                    return []
        except sqlite3.Error as e:
            logger.error(f"Error fetching all data from 'tbl_feed': {e}")
            return []
        finally:
            self.close_connection()

    def get_all_feed_by_channel_id(self, channel_id: str) -> List[FeedDTO]:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                SELECT * FROM tbl_feed WHERE channel_id =?
                ''', (channel_id,))
                rows = self.cursor.fetchall()
                if rows:
                    return [FeedDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]
                else:
                    return []
        except sqlite3.Error as e:
            logger.error(f"Error fetching all data from 'tbl_feed': {e}")
            return []
        finally:
            self.close_connection()
