import sys, os
import unittest

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    
    TEST_TAG = 'test_tag'
    TEST_VAL = 'test_val'
    TEST_CHILDREN = [1, 2, 3]
    TEST_PROP = {'href': 'https://www.google.com', 'target': '_blank'}
    
    def test_create_blank_vars(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
    def sample_node(self):
        return HTMLNode(self.TEST_TAG, self.TEST_VAL, self.TEST_CHILDREN, self.TEST_PROP)
        
    def test_create_sets_vars(self):
        node = self.sample_node()
        self.assertEqual(self.TEST_TAG, node.tag)
        self.assertEqual(self.TEST_VAL, node.value)
        self.assertEqual(self.TEST_CHILDREN, node.children)
        self.assertEqual(self.TEST_PROP, node.props)
    
    def test_props_to_html(self):
        props_response = self.sample_node().props_to_html()
        expected_respnse = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(props_response, expected_respnse)
        
    def test_to_html_exception(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)
        
    def test_repr(self):
        
        test_tag = "h1"
        test_value = "text"
        test_children = None
        
        test_dict = dict()
        test_dict['href'] = 'https://www.google.com'
        test_dict['target'] = '_blank'
        
        node = HTMLNode(test_tag, test_value, test_children, test_dict)
        
        repr_response = node.__repr__()
        expected_respnse = 'tag: h1 | value: text | children: None | href="https://www.google.com" target="_blank"'
        
        self.assertEqual(repr_response, expected_respnse)