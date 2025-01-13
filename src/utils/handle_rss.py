from operator import is_
import re
import feedparser
import cloudscraper
from bs4 import BeautifulSoup
from typing import Optional, Tuple
from DTO.feed_dto import FeedDTO
from DTO.emty_dto import EmtyDTO
from utils.text_processor import TextProcessor

class GetRSS:
    def __init__(self, url: str):
        self.__rss_link = self.__fetch_rss_link(url)

    def __fetch_rss_link(self, url: str) -> Optional[str]:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tìm link RSS
        rss_link = soup.find('link', attrs={'type': 'application/rss+xml'})
        return rss_link['href'] if rss_link else None  # type: ignore

    def get_rss_link(self) -> Optional[str]:
        return self.__rss_link

def handle_url(url: str) -> str:
    # Xử lý để đảm bảo URL đúng định dạng và không chứa dấu gạch chéo thừa
    url = url.strip()  # Xóa khoảng trắng đầu và cuối chuỗi
    if not url.startswith("http://") and not url.startswith("https://"):
        url = f"https://{url}"
    
    # Đảm bảo rằng chỉ có một cặp dấu gạch chéo sau https:
    url = url.replace("https://", "https://").replace("http://", "http://").replace(":///", "://").replace("///", "//")

    return url

def get_rss_link(url: str) -> Optional[str]:
    return GetRSS(handle_url(url)).get_rss_link()

def read_rss_link(url: Optional[str] = None, rss_link: Optional[str] = None) -> Optional[Tuple[FeedDTO, EmtyDTO]]:
    if url:
        rss_link = get_rss_link(url)
    if not rss_link:
        raise ValueError("Cần cung cấp 'url' hoặc 'rss_link'")

    feed = feedparser.parse(rss_link)
    
    # Xử lý các thông tin chung cho cả Atom và RSS
    logo_url = getattr(feed.feed, 'image', {}).get('href', '')  # Atom có thể dùng 'logo'
    description = getattr(feed.feed, 'subtitle', '') or getattr(feed.feed, 'description', '')
    
    # Tạo đối tượng FeedDTO
    feed_dto = FeedDTO(
        link_feed=feed.feed.get('link', ''),
        link_atom_feed=feed.feed.get('id', feed.feed.get('link', '')),
        title_feed=feed.feed.get('title', ''),
        description_feed=description,
        logo_feed=logo_url,
        pubDate_feed=feed.feed.get('updated', feed.feed.get('pubDate', ''))
    )
    
    # Kiểm tra xem có entries không và xử lý entry đầu tiên
    if feed.entries:
        entry = feed.entries[0]
        
        # Xử lý hình ảnh trong entry (dùng cho cả Atom và RSS)
        media_content = ""
        if hasattr(entry, 'media_thumbnail') and entry.media_thumbnail:
            media_content = entry.media_thumbnail[0]['url']
        elif hasattr(entry, 'media_content') and entry.media_content:
            media_content = entry.media_content[0]['url']

        # Kiểm tra xem có 'content' không, nếu không có thì dùng 'description'
        if entry.get('content') and isinstance(entry['content'], list) and len(entry['content']) > 0:
            content = entry['content'][0].get('value', '')
        else:
            content = entry.get('summary', entry.get('description', ''))
        
        # Kiểm tra xem feed có phải là Atom hay không
        def is_github_link(link: str) -> bool:
            """
            Kiểm tra xem link có phải từ GitHub không.
            """
            return 'github.com' in link

        # Nếu feed là Atom (link GitHub), xử lý không xuống dòng và gộp khoảng trắng
        if is_github_link(feed_dto.get_link_atom_feed()):
            content = re.sub(r'\s+', ' ', content.replace('\n', ' ')).strip()
                    
        # Tạo đối tượng EmtyDTO
        emty_dto = EmtyDTO(
            link_emty=entry.get('link', ''),
            link_feed=feed_dto.get_link_feed(),
            link_atom_feed=feed_dto.get_link_atom_feed(),
            title_emty=entry.get('title', '').strip(),
            description_emty=str(TextProcessor.parse_html(content)),
            image_emty=media_content,
            pubdate_emty=entry.get('updated', entry.get('published', ''))
        )
        return (feed_dto, emty_dto)

    return None
