import sys, os
import unittest

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from leafnode import LeafNode
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from text_to_html import text_node_to_html_node

class TestTextToHtml(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        expected_prop = {'href': 'https://www.google.com'}
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, expected_prop)
        
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, 'imagelink.url')
        html_node = text_node_to_html_node(node)
        expected_prop = {'src': 'imagelink.url', 'alt': 'This is an image node'}
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, expected_prop)

    def test_invalid_type(self):
        node = TextNode("No type", 'random')
        with self.assertRaises(Exception):
            text_node_to_html_node(node)