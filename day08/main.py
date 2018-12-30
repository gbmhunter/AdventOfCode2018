class Node:
    def __init__(self, num_child_nodes, num_metadata_entries):
        self.child_nodes = []
        self.metadata_entries = []
        self.node_value = 0

class Tree:
    pass

def part1and2():
    with open('input.txt', 'r') as file:        
        for line in file:
            data = line.split(' ')         

    tree = Tree()
    metadata_sum_incl_children = process_node(data, tree, None)
    print(f'part 1: sum of all metadata entries = {metadata_sum_incl_children}')
    print(f'part 2: value of root node = {tree.root_node.node_value}')


def process_node(data, tree, parent_node):
    num_child_nodes = int(data.pop(0))
    num_metadata_entries = int(data.pop(0))

    node = Node(num_child_nodes, num_metadata_entries)

    # Add to parent node
    if parent_node is not None:
        parent_node.child_nodes.append(node)
    else:
        # Must be root node, add to Tree
        tree.root_node = node

    metadata_sum_incl_children = 0 # part 1
    node_value = 0   # part 2
    for i in range(num_child_nodes):
        metadata_sum_incl_children += process_node(data, tree, node)

    # Now that we have processed the child nodes, the data at the start of the input should
    # be this nodes metadata
    metadata_sum = 0
    for i in range(num_metadata_entries):
        metadata_value = int(data.pop(0))
        node.metadata_entries.append(metadata_value)
        metadata_sum_incl_children += metadata_value
        metadata_sum += metadata_value
    
    node.metadata_sum = metadata_sum

    # Now that all the children and metadata is valid, we can calculate the node value
    if num_child_nodes == 0:
        node.node_value = node.metadata_sum
    else:
        for i in range(len(node.metadata_entries)):
            try:
                node.node_value += node.child_nodes[node.metadata_entries[i] - 1].node_value
            except IndexError:
                pass

    return metadata_sum_incl_children

if __name__ == '__main__':
    part1and2()