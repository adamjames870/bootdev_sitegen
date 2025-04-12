from enum import Enum

class TextType(Enum):
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'
    
class TextNode():
    
    def __init__(self, text:str, text_type:TextType, url:str=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, value):
        eq_text = self.text == value.text
        eq_type = self.text_type == value.text_type
        eq_url = self.url == value.url
        return eq_text and eq_type and eq_url
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"