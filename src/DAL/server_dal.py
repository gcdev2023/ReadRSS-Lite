import sqlite3
from typing import Optional, List
from DTO.server_dto import ServerDTO
from .base_dal import BaseDAL, logger

class ServerDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        self.open_connection()
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tbl_server(
                server_id TEXT PRIMARY KEY,
                server_name TEXT,
                hex_color TEXT,
                is_active INTERGER DEFAULT 1
            )
            ''')
            self.connection.commit()
            logger.info(f"Table 'tbl_server' created successfully.")
        except sqlite3.Error as e:
            logger.error(f"Error creating table 'tbl_server': {e}")
        finally:
            self.close_connection()
            
    def insert_server(self, server_dto: ServerDTO) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                    INSERT INTO tbl_server (server_id, server_name, hex_color)
                    VALUES (?, ?, ?)
                    ''', (server_dto.get_server_id(), server_dto.get_server_name(), server_dto.get_hex_color()))
                self.connection.commit()
                logger.info(f"Data inserted successfully into 'tbl_server'.")
                return True
        except sqlite3.IntegrityError as e:
            logger.error(f"Server with server_id={server_dto.get_server_id()} already exists in 'tbl_server'")
            return False
        except sqlite3.Error as e:
            logger.error(f"Error inserting data into 'tbl_server': {e}")
            return False
        finally:
            self.close_connection()
            
    def delete_server_by_server_id(self, server_id: str) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                UPDATE tbl_server
                SET is_active = 0
                WHERE server_id = ?
                ''', (server_id,))
                self.connection.commit()
                logger.info(f"Data deleted successfully from 'tbl_server'.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting data from 'tbl_server': {e}")
            return False
        finally:
            self.close_connection()
            
    def delete_all_server(self) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.connection.execute('''
                UPDATE tbl_server
                SET is_active = 0
                ''')
                self.connection.commit()
                logger.info(f"All data deleted successfully from 'tbl_server'.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting all data from 'tbl_server': {e}")
            return False
        finally:
            self.close_connection()
        
    def update_server(self, server_dto: ServerDTO) -> bool:
        self.open_connection()
        try:
            with self.connection:
                self.cursor.execute('''
                UPDATE tbl_server
                SET server_name = ?, hex_color = ?, is_active = ?
                WHERE server_id = ?
                ''', (server_dto.get_server_name(), server_dto.get_hex_color(), server_dto.get_state(), server_dto.get_server_id()))
                self.connection.commit()
                logger.info(f"ALl data updated successfully in 'tbl_server'.")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error updating data by server_id in 'tbl_server': {e}")
            return False
        finally:
            self.close_connection()
            
    def get_server_by_server_id(self, server_id: str) -> Optional[ServerDTO]:
        self.open_connection()
        try:
            self.cursor.execute('''
            SELECT * FROM tbl_server
            WHERE server_id = ?
            ''', (server_id,))
            row = self.cursor.fetchone()
            if row:
                return ServerDTO(row[0], row[1], row[2], bool(row[3]))
            else:
                return None
        except sqlite3.Error as e:
            logger.error(f"Error fetching data by server_id from 'tbl_server': {e}")
            return None
        finally:
            self.close_connection()
        
    def get_all_server(self, ignore_state=False, is_active=True) -> List[ServerDTO]:
        self.open_connection()
        try:
            if ignore_state:
                self.cursor.execute('''
                SELECT * FROM tbl_server
                ''')
            else:
                self.cursor.execute('''
                SELECT * FROM tbl_server
                WHERE is_active = ?
                ''', (is_active,))
            rows = self.cursor.fetchall()
            if rows:
                return [ServerDTO(row[0], row[1], row[2]) for row in rows]
            else:
                return []
        except sqlite3.Error as e:
            logger.error(f"Error fetching all data from 'tbl_server': {e}")
            return []
        finally:
            self.close_connection()
    