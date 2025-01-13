from DTO.feed_dto import FeedDTO
from DTO.emty_dto import EmtyDTO
from GUI.embed_custom import EmbedCustom
from utils.text_processor import TextProcessor

class EmbedFeed(EmbedCustom):
    def __init__(self, id_server: str, feed_dto: FeedDTO, emty_dto: EmtyDTO, **kwargs):
        # Khởi tạo các thuộc tính
        self.__feed = feed_dto
        self.__emty = emty_dto
        
        self.__link = self.__feed.get_link_feed()
        self.__logo = self.__feed.get_logo_feed()
        self.__footer_text = self.__feed.get_description_feed()
        self.__title = self.__feed.get_title_feed()
        self.__image = ""  # Khởi tạo mặc định cho __image nếu không có ảnh

        # Gọi super để kế thừa khởi tạo từ lớp cha CustomEmbed
        super().__init__(id_server=id_server, description="", **kwargs)

        # Xử lý mô tả và link bài viết
        self.description = f'''
            [**Xem bài viết**]({self.__emty.get_link_emty()})
            {self.__emty.get_description_emty()}
        '''
        self.description = TextProcessor.clean_feed_text(self.description)

        # Kiểm tra nếu có image từ entry (emty)
        if self.__emty is not None and self.__emty.get_image_emty() != "":
            self.__image = self.__emty.get_image_emty()
            self.set_image(url=self.__image)  # Cài đặt ảnh cho embed nếu có

        # Cài đặt các thông tin của Embed như author và footer
        self.set_author(name=self.__title, url=self.__link, icon_url=self.__logo)
        self.set_footer(text=self.__footer_text)