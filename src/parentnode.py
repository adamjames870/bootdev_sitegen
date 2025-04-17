from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props:dict=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("no tag in ParentNode")
        if not self.children:
            raise ValueError("no children in ParentNode")
        