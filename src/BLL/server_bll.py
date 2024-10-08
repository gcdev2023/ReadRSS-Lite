from BLL.singleton import Singleton
from DTO.server_dto import ServerDTO
from DAL.server_dal import ServerDAL
from typing import Optional, List


class ServerBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__serverDAL = ServerDAL()
            self._initialized = True
        
    def insert_server(self, server_dto: ServerDTO) -> bool:
            return self.__serverDAL.insert_server(server_dto)

            
    def update_server(self, server_dto: ServerDTO) -> bool:
            return self.__serverDAL.update_server(server_dto)

            
    def delete_all_server(self) -> bool:
            return self.__serverDAL.delete_all_server()

            
    def delete_server_by_server_id(self, server_id: str) -> bool:
            return self.__serverDAL.delete_server_by_server_id(server_id)

            
    def get_server_by_server_id(self, server_id: str) -> Optional[ServerDTO]:
            return self.__serverDAL.get_server_by_server_id(server_id)

    def get_all_server(self) -> List[ServerDTO]:
            return self.__serverDAL.get_all_server()

            

