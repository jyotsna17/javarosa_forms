import xml.dom.minidom

class select1:
    
    def __init__(self , doc , question):
        self.doc = doc
        self.items = 0
        self.select1 = self.doc.createElement("select1")
        self.select1_label = self.doc.createElement("label")
        self.select1_label.appendChild(self.doc.createTextNode(question))
        self.select1.appendChild(self.select1_label)     
       
   
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


    def add_referenceAttribute(self,ref):
        self.select1.setAttribute("ref",ref)


    def return_object(self):
        return self.select1
            
class select:
    
    def __init__(self , doc,question):
        self.doc = doc
        self.select = self.doc.createElement("select")
        self.select_label = self.doc.createElement("label")
        self.select_label.appendChild(self.doc.createTextNode(question))
        self.select.appendChild(self.select_label)

     
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

    def add_referenceAttribute(self,ref):
        self.select.setAttribute("ref",ref)

    def return_object(self):
        return self.select

class input:
    
    def __init__(self,doc ,question):
        self.doc = doc
        self.input = self.doc.createElement("input")
        self.input_label = self.doc.createElement("label")
        self.input_label.appendChild(self.doc.createTextNode(question))
        self.input.appendChild(self.input_label)
         # supports no addition of item

 
        
    def add_referenceAttribute(self,ref):
        self.input.setAttribute("ref",ref)

    def return_object(self):
        return self.input
    


    

            
        

        
