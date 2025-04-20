import sys, os
import unittest

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from extract_markdown_detail import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):

    def test_no_image(self):
        text = "This is text with no images"
        images = extract_markdown_images(text)
        expected_result = []
        self.assertEqual(images, expected_result)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_two_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        expected_result = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(images, expected_result)

class TestExtractLinkText(unittest.TestCase):

    def test_no_link(self):
        text = "This is text with no links"
        links = extract_markdown_links(text)
        expected_result = []
        self.assertEqual(links, expected_result)

    def test_two_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        expected_result = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(links, expected_result)