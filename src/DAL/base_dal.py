import  os, sqlite3
import logging

logger = logging.getLogger('dal')

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # Lấy thư mục gốc của dự án
db_path = os.path.join(base_dir, "db.sqlite3")

class BaseDAL:
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor
    def __init__(self):
        # Sử dụng đường dẫn tuyệt đối đến tệp cơ sở dữ liệu
        self.create_table()
        pass
        
    def create_table(self):
        pass
    
    def open_connection(self):
        self.connection = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        self.connection.close()
    