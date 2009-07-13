import xml.dom.minidom

class nodeset:


    def __init__(self ,doc, nodeset_name):
        self.doc = doc  
        self.nodeset = self.doc.createElement("bind")
        self.nodeset.setAttribute("nodeset",nodeset_name)

    def update_required(self,true_or_false):
      if(true_or_false == "true"):
        self.nodeset.setAttribute("required","true()")
      else:
        self.nodeset.setAttribute("required","false()")

    def update_type(self,data_type):
        self.nodeset.setAttribute("type",data_type)

    def return_object(self):
        return self.nodeset


      # need to add support for relevant and constraints.

      
    
