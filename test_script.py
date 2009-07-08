from instance import *
from controls import *
from group import *
from nodeset import *
from basic_layout import *
import xml.dom.minidom


obj = Xtree("Test Form")
body = obj.return_body_node()
grp_element = group(obj.doc,"person's details")
input_item = inputs(obj.doc,"Enter5 patients name")
grp_element.add_group_item(input_item.return_object())

select1_item = select1(obj.doc,"Is the child suffering from malaria")
select1_item.add_item("yes","yes")
select1_item.add_item("no","no")

grp_element.add_group_item(select1_item.return_object())
body.appendChild(grp_element.return_object())
print obj.doc.toprettyxml()
