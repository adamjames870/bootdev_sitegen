import sys, os
import unittest

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    TEST_TAG = 'test_tag'
    TEST_CHILDREN = [1, 2, 3]
    TEST_PROP = {'href': 'https://www.google.com'}
    
    def test_create_blank_vars(self):
        node = ParentNode(None, None)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
    def sample_node(self):
        return ParentNode(self.TEST_TAG, self.TEST_CHILDREN, self.TEST_PROP)
    
    def test_create_sets_vars(self):
        node = self.sample_node()
        self.assertEqual(self.TEST_TAG, node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(self.TEST_CHILDREN, node.children)
        self.assertEqual(self.TEST_PROP, node.props)
        
    def test_tohtml_thros_null_tag(self):
        node = ParentNode(None, self.TEST_CHILDREN)
        self.assertRaises(ValueError, node.to_html)
        
    def test_tohtml_throws_null_children(self):
        node = ParentNode(self.TEST_TAG, None)
        self.assertRaises(ValueError, node.to_html)
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_to_html_children_with_props(self):
        child_node = LeafNode("a", "Click me!", self.TEST_PROP)
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><a href="https://www.google.com">Click me!</a></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_more_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )


