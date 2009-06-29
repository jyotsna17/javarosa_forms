import xml.dom.minidom
from controls import *

class group:
    
    def __init__(self,doc ,label):
         self.doc = doc
         self.group = self.doc.createElement("group")
         self.group_label = self.doc.createElement("label")
         self.group_label.appendChild(self.doc.createTextNode(label))
         self.group.appendChild(self.group_label)
         self.doc.appendChild(self.group)
         # supports no addition of item
     
    def add_referenceAttribute(self,ref):
       self.group.setAttribute("ref",ref)

    def add_group_item(self,group_node):
        self.group.appendChild(group_node)
        print self.doc.toprettyxml()
        
        
        


    
