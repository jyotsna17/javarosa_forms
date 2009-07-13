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

    def add_lt_constraint(self,constraint):
        self.nodeset.setAttribute("constraint",". &lt;="+ constraint)

    def add_gt_constraint(self,constraint):
        self.nodeset.setAttribute("constraint",". &gt;=" + constraint)
    def add_lt_gt_constraint(self,lt_constraint , gt_constraint):
        self.nodeset.setAttribute("constraint",". &lt;=" + lt_constraint + " " +". &gt;=" + gt_constraint)

    def set_constraint_message(message):
        self.nodeset.setAttribute("jr:constraintMsg = ",message)

    
       #need to add support for relevant attribute
        
