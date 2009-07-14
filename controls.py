import xml.dom.minidom

class select1:
    
    def __init__(self , doc , question):
        self.__doc__ = doc
        self.__items__ = 0
        self.__select1__ = self.__doc__.createElement("select1")
        self.__select1___label__ = self.__doc__.createElement("label")
        self.__select1___label__.appendChild(self.__doc__.createTextNode(question))
        self.__select1__.appendChild(self.__select1___label__)     
       
   
    def add_item(self, label_val , value_val):

        # add an item to the select node
        if(self.__items__ < 2):
            item = self.__doc__.createElement("item")
            label = self.__doc__.createElement("label")
            value = self.__doc__.createElement("value")
            label.appendChild(self.__doc__.createTextNode(label_val))
            value.appendChild(self.__doc__.createTextNode(value_val))
            item.appendChild(label)
            item.appendChild(value)
            self.__select1__.appendChild(item)
            self.__items__ = self.__items__ +1
            #print self.__doc__.toprettyxml()


    def add_referenceAttribute(self,ref):
        self.__select1__.setAttribute("ref",ref)


    def return_object(self):
        return self.__select1__
            
class select:
    
    def __init__(self , doc,question):
        self.__doc__ = doc
        self.__select__ = self.__doc__.createElement("select")
        self.__select___label__ = self.__doc__.createElement("label")
        self.__select___label__.appendChild(self.__doc__.createTextNode(question))
        self.__select__.appendChild(self.__select___label__)

     
    def add_item(self, label_val , value_val):

        # add an item to the select node
            item = self.__doc__.createElement("item")
            label = self.__doc__.createElement("label")
            value = self.__doc__.createElement("value")
            label.appendChild(self.__doc__.createTextNode(label_val))
            value.appendChild(self.__doc__.createTextNode(value_val))
            item.appendChild(label)
            item.appendChild(value)
            self.__select__.appendChild(item)

    def add_referenceAttribute(self,ref):
        self.__select__.setAttribute("ref",ref)

    def return_object(self):
        return self.__select__

class inputs:
    
    def __init__(self,doc ,question):
        self.__doc__ = doc
        self.__input__ = self.__doc__.createElement("input")
        self.__input_label__ = self.__doc__.createElement("label")
        self.__input_label__.appendChild(self.__doc__.createTextNode(question))
        self.__input__.appendChild(self.__input_label__)
         # supports no addition of item

 
        
    def add_referenceAttribute(self,ref):
        self.__input__.setAttribute("ref",ref)

    def return_object(self):
        return self.__input__
    


    

            
        

        
