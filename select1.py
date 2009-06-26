import xml.dom.minidom

class select1:

    
    def __init__(self , doc):
        self.doc = doc
        self.items = 0

    def add_select1_node(self, question):    
        self.select1 = self.doc.createElement("select1")
        self.select1_label = self.doc.createElement("label")
        self.select1_label.appendChild(self.doc.createTextNode(question))
        self.select1.appendChild(self.select1_label)
        self.doc.appendChild(self.select1)
        
 
    def add_item(self, label_val , value_val):

        # add an item to the select node
        if(self.items < 2):
            item = self.doc.createElement("item")
            label = self.doc.createElement("label")
            value = self.doc.createElement("value")
            label.appendChild(self.doc.createTextNode(label_val))
            value.appendChild(self.doc.createTextNode(value_val))
            item.appendChild(label)
            item.appendChild(value)
            self.select1.appendChild(item)
            self.items = self.items +1
            print self.doc.toprettyxml()
            
        
        

        
