class Node:
    def __init__(self, id):
        self.id = id
        self.dependants = []
        self.dependencies = []
        self.completed = False

def part1():

    id_to_node_dict = {}
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            must_be_finished = line[5]
            before = line[36]                        

            if must_be_finished not in id_to_node_dict:
                id_to_node_dict[must_be_finished] = Node(must_be_finished)

            if before not in id_to_node_dict:
                id_to_node_dict[before] = Node(before)

            id_to_node_dict[must_be_finished].dependants.append(id_to_node_dict[before])
            id_to_node_dict[before].dependencies.append(id_to_node_dict[must_be_finished])

    # DAG complete, now find nodes which have no dependencies
    runnable_step_ids = []
    for id, node in id_to_node_dict.items():
        if len(node.dependencies) == 0:
            runnable_step_ids.append(id)

    step_order = ''
    while(True):

        if len(runnable_step_ids) == 0:
            print('Finished all steps.')
            break

        runnable_step_ids = sorted(runnable_step_ids)
        print(f'runnable_step_ids = {runnable_step_ids}')
        step_id_to_run = runnable_step_ids.pop(0)
        print(f'step_id_to_run = {step_id_to_run}')

        # Run step
        id_to_node_dict[step_id_to_run].completed = True
        step_order += step_id_to_run

        # Check if any of the run step's dependants are now runnable
        for node in id_to_node_dict[step_id_to_run].dependants:
            # For this node to be runnable, all of it's dependencies must be completed
            all_completed = True
            for dependancy_node in node.dependencies:
                if not dependancy_node.completed:
                    all_completed = False
                    break

            if all_completed:
                print(f'node {node.id} is runnable.')
                runnable_step_ids.append(node.id)

    print(f'part 1: step order = {step_order}')
    

if __name__ == '__main__':
    part1()