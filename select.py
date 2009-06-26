import xml.dom.minidom

class select:

    
    def __init__(self , doc):
        self.doc = doc

    def add_select_node(self, question):    
        self.select = self.doc.createElement("select")
        self.select_label = self.doc.createElement("label")
        self.select_label.appendChild(self.doc.createTextNode(question))
        self.select.appendChild(self.select_label)
        self.doc.appendChild(self.select)
        
 
    def add_item(self, label_val , value_val):

        # add an item to the select node
            item = self.doc.createElement("item")
            label = self.doc.createElement("label")
            value = self.doc.createElement("value")
            label.appendChild(self.doc.createTextNode(label_val))
            value.appendChild(self.doc.createTextNode(value_val))
            item.appendChild(label)
            item.appendChild(value)
            self.select.appendChild(item)
            print self.doc.toprettyxml()
            
        
        

        
