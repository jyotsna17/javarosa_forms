import xml.dom.minidom


class Xtree:

    def __init__(self,document_title):
        self.doc = xml.dom.minidom.Document()
        self.__html_node__ = self.doc.createElementNS("http://www.w3.org/2002/xforms","h:html")
        self.__html_node__.setAttribute("xmlns","http://www.w3.org/2002/xforms")
        self.__html_node__.setAttribute("xmlns:h","http://www.w3.org/1999/xhtml")
        self.__html_node__.setAttribute("xmlns:ev","http://www.w3.org/2001/xml-events")
        self.__html_node__.setAttribute("xmlns:xsd","http://www.w3.org/2001/XMLSchema")
        self.__html_node__.setAttribute("xmlns:jr","http://openrosa.org/javarosa")
        self.doc.appendChild(self.__html_node__)        
        title_node = self.doc.createElement("h:title")
        title_node.appendChild(self.doc.createTextNode(document_title))
        self.__add_head_node__()
        self.__head_node__.appendChild(title_node)
        self.__add_model_node__()
        self.__add_body_node__()     

    def __add_head_node__(self):
        self.__head_node__ = self.doc.createElement("h:head")
        self.__html_node__.appendChild(self.__head_node__)

    def __add_model_node__(self):
        self.__model_node__ = self.doc.createElement("model")
        self.__head_node__.appendChild(self.__model_node__)

     
    #programatically instance and nodeset nodes would be added to model node


    def __add_body_node__(self):
        self.__body_element__ = self.doc.createElement("h:body")
        self.__html_node__.appendChild(self.__body_element__)

    def return_body_node(self):
        return self.__body_element__

    def return_model_node(self):
        return self.__model_node__
    

    
                                                  
