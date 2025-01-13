# ReadRSS lite
ReadRSS Lite is the free version of Aiko (ReadRSS) - a Discord bot built with Python, bringing RSS feed notifications to your Discord server. Stay updated with news sources like Facebook and much more.

ReadRSS Lite là phiên bản miễn phí của Aiko (ReadRSS) - một bot Discord được xây dựng bằng Python, giúp đưa thông báo từ RSS feed đến server Discord của bạn. Nhận thông báo từ các nguồn tin tức như Facebook và nhiều hơn nữa.


This is link to invite Aiko bot:
```
https://discord.com/oauth2/authorize?client_id=1236720788187381760&permissions=0&integration_type=0&scope=bot
```

```
                        -- ABOUT US --
                                                       Summer 2024
         ██████╗  ██████╗██████╗ ███████╗██╗   ██╗     + HaoWasabi
        ██╔════╝ ██╔════╝██╔══██╗██╔════╝██║   ██║     + nguyluky
        ██║  ███╗██║     ██║  ██║█████╗  ██║   ██║     + NaelTuhline
        ██║   ██║██║     ██║  ██║██╔══╝  ╚██╗ ██╔╝     + tivibin789
        ╚██████╔╝╚██████╗██████╔╝███████╗ ╚████╔╝      + phusomnia
        ╚═════╝  ╚═════╝╚═════╝ ╚══════╝  ╚═══╝        + camdao
``` 
## Installation

1. Clone the repository.  
   Sao chép repository về máy.

2. Create a virtual environment and activate it.  
   Tạo môi trường ảo và kích hoạt nó.

3. Install dependencies:  
   Cài đặt các phụ thuộc:  
    `pip install -r requirements.txt`

4. Create a `.env` file and add the following information:  
    Tạo file `.env` và thêm thông tin sau:
```
DISCORD_TOKEN=your_bot_token_here
```

5. Run the bot:
    Chạy bot:
    `python main.py`

## **Basic slash commands / Các lệnh cơ bản**

- '/ping': Check bot latency.
Kiểm tra tốc độ phản hồi của bot.

- `/getrss url:<url web>`: Check if the website has an RSS feed.  
Kiểm tra xem trang web có link RSS không.

- `/test`: Send a test post from the fit.sgu website.  
Gửi thử bài đăng đầu tiên từ trang web fit.sgu.

- `/setfeed channel:<select text channel> url:<website url>`: Set up a channel to receive posts from the website.  
Thiết lập kênh để nhận thông báo bài đăng từ trang web bằng URL.

- `/deletefeed channel:<channel> rss:<rss link>`: Remove the RSS feed from the channel.  
Hủy thiết lập nhận thông báo từ link RSS đã đăng ký ở kênh chỉ định.

- `/show`: Show the list of registered RSS feeds in the server.  
Hiển thị danh sách các feed đã được đăng ký trong server.

**Note / Lưu ý**:  
The Lite version of ReadRSS has limited features and cannot be used in DM channels.  
Phiên bản Lite của ReadRSS bị giới hạn tính năng, không thể sử dụng ở các kênh DMChannel.

## **Other Information / Thông Tin Khác**

- **Feed**: Entity containing website information.  
Thực thể chứa thông tin trang web.

- **Emty**: The entity contains the website information of the website.
Thực thể chứa thông tin bài đăng của trang web.

- **Channel**: Server’s communication channels.  
Kênh liên lạc của server.

**Errors / Lỗi có thể gặp**:
- If the bot takes too long to respond, use command-based actions like `_ping` instead of slash commands (`/ping`).  
Nếu bot phản hồi chậm, hãy ưu tiên sử dụng các lệnh như `_ping` thay vì `/ping`.

---

This project is designed with a focus on efficient and responsive Discord integration.  
Dự án này được thiết kế với mục tiêu tích hợp hiệu quả và đáp ứng nhanh trong môi trường Discord.
