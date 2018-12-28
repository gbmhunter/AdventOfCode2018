class Node:
    def __init__(self, id):
        self.id = id
        self.dependants = []
        self.dependencies = []
        self.completed = False

class Worker:
    def __init__(self, id):
        self.id = id
        self.curr_step = None
        self.remaining_time = 0

def run_sleigh_building(num_workers, offset_seconds):

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
    workers = []
    for i in range(num_workers):
        workers.append(Worker(i))

    total_runtime = 0
    while(True):

        all_free = True
        for worker in workers:
            if worker.curr_step is not None:
                all_free = False

        if len(runnable_step_ids) == 0 and all_free:            
            break

        runnable_step_ids = sorted(runnable_step_ids)        

        # Check how many workers are free
        for worker in workers:
            if worker.curr_step is None:
                # Worker is free, see if there is a job to assign
                if len(runnable_step_ids) > 0:                    
                    worker.curr_step = runnable_step_ids.pop(0)
                    # Calculate step time
                    step_time = offset_seconds + ord(worker.curr_step)%32                    
                    worker.remaining_time = step_time

        # Increment elapsed seconds
        total_runtime += 1        

        # Update workers remaining times
        for worker in workers:
            if worker.curr_step is not None:
                worker.remaining_time -= 1
                if worker.remaining_time == 0:                    
                    # Worker has finished step
                    id_to_node_dict[worker.curr_step].completed = True
                    step_order += worker.curr_step

                    # Check if any of the run step's dependants are now runnable
                    for node in id_to_node_dict[worker.curr_step].dependants:
                        # For this node to be runnable, all of it's dependencies must be completed
                        all_completed = True
                        for dependancy_node in node.dependencies:
                            if not dependancy_node.completed:
                                all_completed = False
                                break

                        if all_completed:                            
                            runnable_step_ids.append(node.id)
                    worker.curr_step = None
                    worker.remaining_time = 0
    
    return step_order, total_runtime

if __name__ == '__main__':
    step_order, run_time = run_sleigh_building(1, 0)
    print(f'part1: step_order = {step_order}')
    step_order, run_time = run_sleigh_building(5, 60)
    print(f'part2: run_time = {run_time}')