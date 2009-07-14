import xml.dom.minidom

# need to add the namespace support

class instance:

    def __init__(self,doc, instance_name):
        self.__doc__ = doc
        self.__instance__ = self.__doc__.createElement("instance")
        self.__instance___name__ = self.__doc__.createElement(instance_name)
        self.__instance__.appendChild(self.__instance___name__)

    def add_instance_nodes(self,node_name):
        node = self.__doc__.createElement(node_name)
        self.__instance___name__.appendChild(node)

    def add_submit_node_value(self,node_name,value):
        node = self.__doc__.createElement(node_name)
        node.appendChild(self.__doc__.createTextNode(value))
        self.__instance___name__.appendChild(node)

    def add_select_node_value(self,node_description , node_name , value):
                          node = self.__doc__.createElement(node_description)
                          node.setAttribute(node_name, value)
                          self.__instance___name__.appendChild(node)

    def return_instance_node(self):
        return self.__instance__

    def add_node(self,node):
        self.__instance___name__.appendChild(node)


class subinstance:

    def __init__(self,doc,instance_name):
        self.__doc__ = doc
        self.__instance__ = self.__doc__.createElement(instance_name)

    def add_sub_instance(self, sub_node):
        self.__instance__.appendChild(sub_node)

    def add_node_with_value(self,node_name , value):
        node = self.__doc__.createElement(node_name)
        node.appendChild(self.__doc__.createTextNode(value))
        self.__instance__.appendChild(node)

    def add_only_node(self,node_name):
        node = self.__doc__.createElement(node_name)
        self.__instance__.appendChild(node)

    def return_instance_node(self):
        return self.__instance__

                          


    
