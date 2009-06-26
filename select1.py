import xml.dom.minidom

class select1:
    
    def __init__(self , doc):
        self.doc = doc
        self.count_of_nodes = 0;5

    def add_select1_node(self, question):    
        self.select1 = self.doc.createElement("select")
        self.select1_label = self.doc.createElement("label")
        self.select1_label.appendChild(self.doc.createTextNode(question))
        self.select1.appendChild(self.select1_label)
        self.doc.appendChild(self.select1)
        
 
    def add_item(self, label_val,value_val):

        if(self.count_of_nodes < 2):
            # add an item to the select node

            item = self.doc.createElement("item")
            label = self.doc.createElement("label")
            value = self.doc.createElement("value")
            label.appendChild(self.doc.createTextNode(label_val))
            value.appendChild(self.doc.createTextNode(value_val))
            item.appendChild(label)
            item.appendChild(value)
            self.select1.appendChild(item)
            print self.doc.toprettyxml()
            self.count_of_nodes = self.count_of_nodes +1  

            #need to throw the corresponding exception if more than 2 items are added

        
        
        
        

        
