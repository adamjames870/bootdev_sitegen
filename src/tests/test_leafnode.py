import sys, os
import unittest

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    TEST_TAG = 'test_tag'
    TEST_VAL = 'test_val'
    TEST_PROP = {'href': 'https://www.google.com', 'target': '_blank'}
    
    def sample_node(self):
        return LeafNode(self.TEST_TAG, self.TEST_VAL, self.TEST_PROP)
        
    def test_create_sets_vars(self):
        node = self.sample_node()
        self.assertEqual(self.TEST_TAG, node.tag)
        self.assertEqual(self.TEST_VAL, node.value)
        self.assertEqual(self.TEST_PROP, node.props)
        self.assertIsNone(node.children)
        
    def test_to_html_exception_on_blank_value(self):
        node_blank_string = LeafNode(self.TEST_TAG, "", self.TEST_PROP)
        node_null_value = LeafNode(self.TEST_TAG, None, self.TEST_PROP)
        self.assertRaises(ValueError, node_blank_string.to_html)
        self.assertRaises(ValueError, node_null_value.to_html)
        
    def test_to_html_no_tag(self):
        node = LeafNode("", self.TEST_VAL, self.TEST_PROP)
        self.assertEqual(node.to_html(), self.TEST_VAL)
        
    def test_to_html_decorates(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        
    def test_to_html_decorates_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node.props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        