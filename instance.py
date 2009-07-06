import xml.dom.minidom

# need to add the namespace support

class instance:

    def __init__(self,doc, instance_name):
        self.doc = doc
        self.instance = self.doc.createElement("instance")
        self.instance_name = self.doc.createElement(instance_name)
        self.instance.appendChild(self.instance_name)

    def add_instance_nodes(self,node_name):
        node = self.doc.createElement(node_name)
        self.instance_name.appendChild(node)

    def add_submit_node_value(self,node_name,value):
        node = self.doc.createElement(node_name)
        node.appendChild(self.doc.createTextNode(value))
        self.instance_name.appendChild(node)

    def add_select_node_value(self,node_description , node_name , value):
                          node = self.doc.createElement(node_description)
                          node.setAttribute(node_name, value)
                          self.instance_name.appendChild(node)

    def return_instance_node(self):
        return self.instance

    def add_node(self,node):
        self.instance_name.appendChild(node)


class subinstance:

    def __init__(self,doc,instance_name):
        self.doc = doc
        self.instance = self.doc.createElement(instance_name)

    def add_sub_instance(self, sub_node):
        self.instance.appendChild(sub_node)

    def add_node_with_value(self,node_name , value):
        node = self.doc.createElement(node_name)
        node.appendChild(self.doc.createTextNode(value))
        self.instance.appendChild(node)

    def add_only_node(self,node_name):
        node = self.doc.createElement(node_name)
        self.instance.appendChild(node)

    def return_instance_node(self):
        return self.instance

                          


    
