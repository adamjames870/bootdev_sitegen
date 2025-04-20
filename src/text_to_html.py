from leafnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    tag = ""
    value = ""
    props = None #dictonary
    
    if text_node.text_type == TextType.TEXT:
        tag = None
        value = text_node.text
    
    if text_node.text_type == TextType.BOLD:
        tag = 'b'
        value = text_node.text
    
    if text_node.text_type == TextType.ITALIC:
        tag = 'i'
        value = text_node.text

    if text_node.text_type == TextType.CODE:
        tag = 'code'
        value = text_node.text

    if text_node.text_type == TextType.LINK:
        tag = 'a'
        value = text_node.text
        props = {'href': text_node.url}

    if text_node.text_type == TextType.IMAGE:
        tag = 'img'
        props = {'src': text_node.url, 'alt': text_node.text}

    if text_node.text_type not in TextType:
        raise Exception("Invalid text type")

    return LeafNode(tag, value, props)


