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
model_node.appendChild(instance_node.return_instance_node())
nodeset1 = nodeset(obj.doc,"name")
nodeset1.update_attributes("","false","true")
model_node.appendChild(nodeset1.return_object())
nodeset2 = nodeset(obj.doc,"age")
nodeset2.update_attributes("","false","true")
model_node.appendChild(nodeset2.return_object())
body = obj.return_body_node()
grp_element = group(obj.doc,"person's details")
input_item = inputs(obj.doc,"Enter5 patients name")
grp_element.add_group_item(input_item.return_object())

select1_item = select1(obj.doc,"Is the child suffering from malaria")
select1_item.add_item("yes","yes")
select1_item.add_item("no","no")

grp_element.add_group_item(select1_item.return_object())
body.appendChild(grp_element.return_object())

f = open('test.xml', 'w')
obj.doc.writexml(f)
f.close()

