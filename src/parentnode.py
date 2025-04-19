from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props:dict=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("no tag in ParentNode")
        if not self.children:
            raise ValueError("no children in ParentNode")
    
        return_string = ""

        if self.props is None:
            return_string = f"<{self.tag}>"
        else:
            return_string = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            if child is None:
                continue
            return_string += child.to_html()
        
        return_string += f"</{self.tag}>"
        return return_string
    

