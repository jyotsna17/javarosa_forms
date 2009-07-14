import xml.dom.minidom

class nodeset:


    def __init__(self ,doc, nodeset_name):
        self.__doc__ = doc
        self.__nodeset__ = self.__doc__.createElement("bind")
        self.__nodeset__.setAttribute("nodeset",nodeset_name)

    def getattr(self,name):
        if (name == 'doc'):
            return self.__doc__

    def update_attributes(self,data_type, readonly , required):
        if(data_type!= ""):
            self.__update_type__(data_type)
        if(required != ""):
            self.__update_required__(required)
        if(readonly != ""):
            self.__update_readonly__(readonly)

    def __update_readonly__(self,readonly):
        if(readonly == "true"):
            self.__nodeset__.setAttribute("readonly","true()")
        else:
            self.__nodeset__.setAttribute("readonly","false()")
        
    def __update_required__(self,true_or_false):
      if(true_or_false == "true"):
        self.__nodeset__.setAttribute("required","true()")
      else:
        self.__nodeset__.setAttribute("required","false()")

    def __update_type__(self,data_type):
        self.__nodeset__.setAttribute("type",data_type)    

    def add_lt_gt_constraint(self,lt_constraint , gt_constraint):
        if( lt_constraint != ""):
            constraint = ". &lt;=" + lt_constraint
        if( gt_constraint != ""):
            constraint = ". &lt;=" + gt_constraint
        self.__nodeset__.setAttribute("constraint", constraint)

        if(message != ""):
            self.__nodeset__.setAttribute("jr:constraintMsg = ",message)
    def return_object(self):
        return self.__nodeset__
    
       #need to add support for relevant attribute
        
