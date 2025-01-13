import re
from bs4 import BeautifulSoup
from typing import Optional

class TextProcessor:
    
    @staticmethod
    def fix_surrogates(text: str) -> str:
        # Convert surrogate pairs to characters
        return re.sub(r'\\u(d[89ab][0-9a-f]{2})\\u(d[cdef][0-9a-f]{2})', 
                      lambda m: chr((int(m.group(1), 16) - 0xD800) * 0x400 + (int(m.group(2), 16) - 0xDC00) + 0x10000), text)
        
    @staticmethod
    def decode_unicode_escapes(text: str) -> str:
        # Decode regular unicode escape sequences
        return re.sub(r'\\u[0-9a-fA-F]{4}', 
                      lambda m: chr(int(m.group(0)[2:], 16)), text)
        
    @staticmethod
    def finally_change_formatting(text: str) -> str:
        # Replace \n and \/ for proper formatting
        return text.replace(r'\n', '\n').replace(r'\/', '/')
    
    @staticmethod
    def proccess_unicode_text(text: str) -> str:
        text = TextProcessor.fix_surrogates(text)
        text = TextProcessor.decode_unicode_escapes(text)
        text = TextProcessor.finally_change_formatting(text)
        return text
    
    @staticmethod
    def parse_html(content: Optional[str]) -> Optional[str]:
        if content is None:
            return None
        
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')
        
        # Strip away HTML tags and keep only the text
        text = soup.get_text()
        return text

    @staticmethod
    def clean_feed_text(text: str) -> str:
        # Sử dụng regex để loại bỏ khoảng trắng dư thừa và giữ lại 1 dòng giữa văn bản và đoạn "(Feed generated with FetchRSS)"
        cleaned_text = re.sub(r'\s*\n\s*(\(Feed generated with FetchRSS\))', r'\n\1', text)
        return cleaned_text