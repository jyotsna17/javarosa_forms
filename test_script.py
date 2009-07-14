from instance import *
from controls import *
from group import *
from nodeset import *
from basic_layout import *
import xml.dom.minidom


obj = Xtree("Test Form")
model_node = obj.return_model_node()
instance_node = instance(obj.doc,"household")
instance_node.add_instance_nodes("name")
instance_node.add_instance_nodes("age")
instance_node.add_instance_nodes("birthday")
instance_node.add_instance_nodes("zipcode")
model_node.appendChild(instance_node.return_instance_node())

nodeset1 = nodeset(obj.doc,"name")
nodeset1.update_attributes("","false","true")
model_node.appendChild(nodeset1.return_object())

nodeset2 = nodeset(obj.doc,"age")
nodeset2.update_attributes("","false","true")
model_node.appendChild(nodeset2.return_object())

nodeset3 = nodeset(obj.doc,"birthday")
nodeset3.update_attributes("date","false","true")
nodeset3.add_lt_gt_constraint("today","","Birthdays cannot be in the future!")
model_node.appendChild(nodeset3.return_object())

nodeset4 = nodeset(obj.doc,"zipcode")
nodeset4.update_attributes("integer","false","true")
nodeset4.add_lt_gt_constraint("99950","00210","Zipcodes must less than 99951 and greater than 00209!")
model_node.appendChild(nodeset4.return_object())

body = obj.return_body_node()
grp_element = group(obj.doc,"person's details")
input_item = inputs(obj.doc,"Enter5 patients name")
input_item.add_referenceAttribute("name")
grp_element.add_group_item(input_item.return_object())

select1_item = select1(obj.doc,"Is the child suffering from malaria")
select1_item.add_referenceAttribute("age")
select1_item.add_item("yes","yes")
select1_item.add_item("no","no")

grp_element.add_group_item(select1_item.return_object())

item3 = inputs(obj.doc,"When was the person born")
item3.add_referenceAttribute("birthday")
grp_element.add_group_item(item3.return_object())


item4 = inputs(obj.doc,"Household features")
item4.add_referenceAttribute("zipcode")
grp_element.add_group_item(item4.return_object())
body.appendChild(grp_element.return_object())

f = open('test.xml', 'w')
f.write(obj.doc.toprettyxml())
f.close()

