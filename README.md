
# ReadRSS Lite
ReadRSS Lite is the free version of Aiko (ReadRSS) - a Discord bot built with Python, bringing RSS feed notifications to your Discord server. Stay updated with news sources like Facebook and much more.

ReadRSS Lite là phiên bản miễn phí của Aiko (ReadRSS) - một bot Discord được xây dựng bằng Python, giúp đưa thông báo từ RSS feed đến server Discord của bạn. Nhận thông báo từ các nguồn tin tức như Facebook và nhiều hơn nữa.

## Invite Link
You can invite Aiko bot to your server using the following link:
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

## Bot Installation Guide / Hướng dẫn cài đặt bot

### Step 1: Setting up the bot in Discord Developer Portal
1. Go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on **New Application** to create a new bot.
3. Enter a name for your bot and agree to the terms of service.
4. After creation, navigate to **OAuth2** and select **bot** as the scope.
5. Grant the bot **Administrator** permissions.
6. Copy the generated invite URL and paste it into your browser, then invite the bot to your server.

### Step 2: Setting up bot parameters
1. Obtain the bot's Token from the **Bot** section and save it to a `.env` file in your project directory:
```
DISCORD_TOKEN=your_discord_bot_token_here
```
2. Enable the following intents in the **Privileged Gateway Intents** section:
   - **Presence Intent**
   - **Server Member Intent**
   - **Message Content Intent**
   - Save the changes.

### Step 3: Running the bot
1. Clone the repository to your machine:
```
git clone <repository_url>
```

2. Create and activate a virtual environment:
    - On **Windows**:
      ```
      python -m venv env
      .\env\Scripts\activate.bat
      ```
    - On **Linux/MacOS**:
      ```
      python3 -m venv env
      source env/bin/activate
      ```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the bot:
```
python main.py
```

## **Basic Slash Commands / Các lệnh cơ bản**

- `/ping`: Check bot latency.  
Kiểm tra độ trễ của bot.

- `/getrss url:<website_url>`: Check if the website has an RSS feed.  
Kiểm tra xem trang web có link RSS hay không.

- `/test`: Send a test post from fit.sgu's website.  
Gửi thử bài đăng từ trang web fit.sgu.

- `/setfeed channel:<text_channel> url:<rss_url>`: Set a channel to receive RSS feed posts.  
Thiết lập kênh để nhận bài đăng từ trang web qua RSS.

- `/deletefeed channel:<text_channel> rss:<rss_url>`: Remove the RSS feed from the specified channel.  
Xóa thiết lập RSS từ kênh chỉ định.

- `/show`: Display the list of registered RSS feeds in the server.  
Hiển thị danh sách các feed đã đăng ký trong server.

**Note / Lưu ý**:  
ReadRSS Lite has limited features and does not support DMChannel features such as `setfeed`, `deletefeed`, and `show`.  
Phiên bản Lite của ReadRSS bị giới hạn và không hỗ trợ tính năng trong các kênh DMChannel như `setfeed`, `deletefeed`, và `show`.

## **Other Information / Thông tin khác**

- **Feed**: Entity containing the website's information.  
Thực thể chứa thông tin trang web.

- **Emty**: The entity containing post information from the website.  
Thực thể chứa thông tin bài đăng từ trang web.

- **DMChannel**: A private channel between two users.  
Kênh liên lạc giữa hai người dùng.

## **Possible Errors / Lỗi có thể gặp**

- If the bot takes too long to respond, use command-based actions like `_ping` instead of slash commands (`/ping`).  
Nếu bot phản hồi chậm, hãy sử dụng các lệnh dựa trên ký tự như `_ping` thay vì các lệnh slash (`/ping`).

---

This project is designed with efficiency and responsiveness in mind, aiming for seamless integration into Discord.  
Dự án này được thiết kế với trọng tâm là hiệu quả và tốc độ phản hồi nhanh, tích hợp dễ dàng với Discord.
