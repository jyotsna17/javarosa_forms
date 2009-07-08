import xml.dom.minidom


class Xtree:

    def __init__(self,document_title):
        self.doc = xml.dom.minidom.Document()
        self.html_node = self.doc.createElementNS("http://www.w3.org/2002/xforms","h:html")
        self.html_node.setAttribute("xmlns","http://www.w3.org/2002/xforms")
        self.html_node.setAttribute("xmlns:h","http://www.w3.org/1999/xhtml")
        self.html_node.setAttribute("xmlns:ev","http://www.w3.org/2001/xml-events")
        self.html_node.setAttribute("xmlns:xsd","http://www.w3.org/2001/XMLSchema")
        self.html_node.setAttribute("xmlns:jr","http://openrosa.org/javarosa")
        self.doc.appendChild(self.html_node)        
        title_node = self.doc.createElement("h:title")
        title_node.appendChild(self.doc.createTextNode(document_title))
        self.add_head_node()
        self.head_node.appendChild(title_node)
        self.add_model_node()
        self.add_body_node()
        print self.doc.toprettyxml()

    def add_head_node(self):
        self.head_node = self.doc.createElement("h:head")
        self.html_node.appendChild(self.head_node)

    def add_model_node(self):
        self.model_node = self.doc.createElement("model")
        self.head_node.appendChild(self.model_node)

    def return_model_node(self):
        return self.model_node

    #programatically instance and nodeset nodes would be added to model node


    def add_body_node(self):
        self.body_element = self.doc.createElement("h:body")
        self.html_node.appendChild(self.body_element)

    def return_body_node(self):
        return self.body_element
    

    

    
                                                  
