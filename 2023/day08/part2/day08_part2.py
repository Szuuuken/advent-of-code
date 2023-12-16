import re

def main():
    #file = open('day08_part2_example_input_1.txt', 'r')
    #file = open('day08_part2_example_input_2.txt', 'r')
    #file = open('day08_part2_example_input_3.txt', 'r')
    file = open('day08_part2_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    current_nodes = []
    instructions = lines[0]
    instruction_count = len(instructions)
    nodes = dict()

    for line in lines[2:]:
        node_codes = re.findall(r'[A-Z,0-9]{3}', line)
        nodes[node_codes[0]] = (node_codes[1], node_codes[2])

        if node_codes[0][2] == 'A':
            current_nodes.append(nodes[node_codes[0]])

    searching = True
    instruction_pointer = 0
    steps = 0

    while searching:
        steps += 1
        instruction = instructions[instruction_pointer]
        next_index = 0 if instruction == 'L' else 1

        next_nodes = []
        all_end_with_z = True
        for current_node in current_nodes:
            next_node = current_node[next_index]
            next_nodes.append(nodes[next_node])

            if next_node[2] != 'Z':
                all_end_with_z = False

        searching = not all_end_with_z

        #print(next_nodes)
        current_nodes = next_nodes
        
        instruction_pointer += 1
        if(instruction_pointer >= instruction_count): instruction_pointer = 0

        if steps % 1000000 == 0:
            print(steps) 

    print(steps)
    
if __name__ == "__main__":
    main()