import sqlite3
from typing import Optional, List
from DTO.emty_dto import EmtyDTO

from .base_dal import BaseDAL, logger


class EmtyDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def create_table(self):
        self.open_connection()
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tbl_emty(
                    link_emty TEXT,
                    link_feed TEXT,
                    link_atom_feed TEXT,
                    title_emty TEXT,
                    description_emty TEXT,
                    image_emty TEXT,
                    pubdate_emty DATETIME,
                    channel_id TEXT,
                    PRIMARY KEY (link_emty, channel_id),
                    FOREIGN KEY (link_feed) REFERENCES tbl_feed(link_feed),
                    FOREIGN KEY (link_atom_feed) REFERENCES tbl_feed(link_atom_feed),
                    FOREIGN KEY (channel_id) REFERENCES tbl_feed(channel_id)
                )
            ''')
            self.connection.commit()
            logger.info(f"Table 'tbl_emty' created successfully.")
        except sqlite3.Error as e:
            logger.error(f"Error creating table 'tbl_emty': {e}")
        finally:
            self.close_connection()


    def insert_emty(self, emty_dto: EmtyDTO) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                INSERT INTO tbl_emty (link_emty, link_feed, link_atom_feed, title_emty, description_emty, image_emty, pubdate_emty, channel_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (emty_dto.get_link_emty(), emty_dto.get_link_feed(), emty_dto.get_link_atom_feed(),
                    emty_dto.get_title_emty(), emty_dto.get_description_emty(), emty_dto.get_image_emty(),
                    emty_dto.get_pubdate_emty(), emty_dto.get_channel_id()))
                self.connection.commit()
                logger.info(f"Data inserted into 'tbl_emty' successfully.")
                return True
        except sqlite3.IntegrityError as e:
            logger.error(f"Emty with link_emty={emty_dto.get_link_emty()} and channel_id={emty_dto.get_channel_id()} already exists.")
            return False
        except sqlite3.Error as e:
            logger.error(f"Error inserting data into 'tbl_emty': {e}")
            return False
        finally:
            self.close_connection()


    def delete_emty_by_link_emty_and_channel_id(self, emty_link: str, channel_id: str) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                DELETE FROM tbl_emty WHERE link_emty = ? AND channel_id = ?
                ''', (emty_link, channel_id))
                self.connection.commit()
                logger.info(f"Data deleted from 'tbl_emty' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting data from 'tbl_emty': {e}")
            return False
        finally:
            self.close_connection()
            
    def delete_emty_by_link_atom_and_channel_id(self, link_atom_feed: str, channel_id: str) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                DELETE FROM tbl_emty WHERE link_atom_feed = ? AND channel_id = ?
                ''', (link_atom_feed, channel_id))
                self.connection.commit()
                logger.info(f"Data deleted from 'tbl_emty' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting data from 'tbl_emty': {e}")
            return False
        finally:
            self.close_connection()
            
    def delete_emty_by_channel_id(self, channel_id: str) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                DELETE FROM tbl_emty WHERE channel_id = ?
                ''', (channel_id,))
                self.connection.commit()
                logger.info(f"Data deleted from 'tbl_emty' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting data from 'tbl_emty': {e}")
            return False
        finally:
            self.close_connection()
            
    def delete_all_emty(self) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                DELETE FROM tbl_emty
                ''')
                self.connection.commit()
                logger.info(f"All data deleted from 'tbl_emty' successfully.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting all data from 'tbl_emty': {e}")
            return False
        self.close_connection()

    def get_emty_by_link_emty_and_channel_id(self, emty_link: str, channel_id: str) -> Optional[EmtyDTO]:
        self.open_connection()
        try:
            self.cursor.execute('''
            SELECT * FROM tbl_emty WHERE link_emty = ? AND channel_id = ?
            ''', (emty_link, channel_id))
            row = self.cursor.fetchone()
            if row:
                return EmtyDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            else:
                return None
        except sqlite3.Error as e:
            logger.error(f"Error fetching data from 'tbl_emty': {e}")
            return None
        finally:
            self.close_connection()


    def get_all_emty(self) -> List[EmtyDTO]:
        self.open_connection()
        try:
            self.cursor.execute('''
            SELECT * FROM tbl_emty
            ''')
            rows = self.cursor.fetchall()
            if rows:
                return [EmtyDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in rows]
            else:
                return []
        except sqlite3.Error as e:
            logger.error(f"Error fetching all data from 'tbl_emty': {e}")
            return []
        finally:
            self.close_connection()

    