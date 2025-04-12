

class HTMLNode():
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return_string = ""
        for key, val in self.props.items():
            return_string += f' {key}="{val}"'
        return return_string
    
    def __repr__(self):
        return f'tag: {self.tag} | value: {self.value} | children: {self.children} |{self.props_to_html()}'
    
    def __str__(self):
        return self.__repr__()