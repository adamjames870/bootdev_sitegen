from textnode import TextNode, TextType

def main():
    dummy_node = TextNode("anchor text", TextType.IMAGE, "http://url")
    print(dummy_node)

main()