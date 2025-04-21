class Graph_Node():
    def __init__(self , start_line_no , end_line_no , hierarchy , code_block , node_type):
        self.start_line_no = start_line_no
        self.end_line_no = end_line_no
        self.hierarchy = hierarchy
        self.code_block = code_block
        self.node_type = node_type      # start , end , if , switch , while , for , continue , break , try , catch , finally , throw , return , pass
        self.next_node = [] 
        self.prev_node = []
        self.conditions = []        #condition to jump to next node
    

    def add_child(self , graph_node , condition):
        if graph_node not in self.next_node:
            self.next_node.append(graph_node)
            self.conditions.append(condition)
            graph_node.prev_node.append(self) 

class Program_Graph():
    def __init__(self , packages , imports , static_vars , signiture, start_node , end_node):
        self.root = Graph_Node(0 , 0 , 0 , [] , node_type="Entry")
        self.root.add_child(start_node , "Entry of Program")
        self.current_node = self.root
        self.exit = Graph_Node(0 , 0 , 0 , [] , node_type="Exit")
        self.add_set_exit(end_node)
        self.pachages = packages
        self.imports = imports
        self.signature = signiture
        self.static_vars = static_vars
    
    def add_set_exit(self , end_node):
        if end_node.node_type == "return":
            end_node.add_child(self.exit , "End of Program")