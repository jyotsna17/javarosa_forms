from instance import *
from controls import *
from group import *
from nodeset import *
import xml.dom.minidom


doc = xml.dom.minidom.Document()
x = instance(doc,"household")
y = subinstance(doc,"household_person")
z = subinstance(doc,"person")
z.add_node_with_value("name","jyotsna")
z.add_node_with_value("age","25")
z.add_node_with_value("color","wheatish")
y.add_sub_instance(z.return_instance_node())
x.add_node(y.return_instance_node())
doc.appendChild(x.return_instance_node())
print doc.toprettyxml()
