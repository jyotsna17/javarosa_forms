import xml.dom.minidom
from controls import *

class group:
    
    def __init__(self,doc ,label):
         self.__doc__ = doc
         self.__group__ = self.__doc__.createElement("group")
         self.__group___label__ = self.__doc__.createElement("label")
         self.__group___label__.appendChild(self.__doc__.createTextNode(label))
         self.__group__.appendChild(self.__group___label__)
         # supports no addition of item
     
    def add_referenceAttribute(self,ref):
       self.__group__.setAttribute("ref",ref)

    def add_group_item(self,group_node):
        self.__group__.appendChild(group_node)

    def return_object(self):
        return self.__group__
        
        
        


    
