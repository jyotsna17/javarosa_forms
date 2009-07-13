import xml.dom.minidom

class nodeset:


    def __init__(self ,doc, nodeset_name):
        self.doc = doc  
        self.nodeset = self.doc.createElement("bind")
        self.nodeset.setAttribute("nodeset",nodeset_name)

    def update_required(self,true_or_false):
        self.nodeset.setAttribute("required",true_or_false)

    def update_type(self,data_type):
        self.nodeset.setAttribute("type",data_type)

    def return_object(self):
        return self.nodeset


      # need to add support for relevant and constraints.

      
    
