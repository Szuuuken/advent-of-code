import re
from math import lcm

def run_loop(nodes: dict, instructions: str, starting_node_code: (str, str)):
    instruction_count = len(instructions)
    searching = True
    current_node = nodes[starting_node_code]
    instruction_pointer = 0
    steps = 0
    next_node_code = ""

    while searching:
        steps += 1
        instruction = instructions[instruction_pointer]
        next_index = 0 if instruction == 'L' else 1
        next_node_code = current_node[next_index]
        
        current_node = nodes[next_node_code]
        instruction_pointer += 1
        if(instruction_pointer >= instruction_count): instruction_pointer = 0

        searching = next_node_code[2] != 'Z' 

    print(f'loop from {starting_node_code} to {next_node_code} took {steps} steps')
    return steps

def main():
    #file = open('day08_part2_example_input_1.txt', 'r')
    #file = open('day08_part2_example_input_2.txt', 'r')
    #file = open('day08_part2_example_input_3.txt', 'r')
    file = open('day08_part2_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    starting_nodes = []
    instructions = lines[0]
    nodes = dict()

    for line in lines[2:]:
        node_codes = re.findall(r'[A-Z,0-9]{3}', line)
        nodes[node_codes[0]] = (node_codes[1], node_codes[2])

        if node_codes[0][2] == 'A':
            starting_nodes.append(node_codes[0])

    loops = [run_loop(nodes, instructions, starting_node) for starting_node in starting_nodes]
    lcm_of_loops = lcm(*loops)
    print(f'\nthe lcm of the loops is {lcm_of_loops}')
    
if __name__ == "__main__":
    main()


    #https://www.reddit.com/r/adventofcode/comments/18dwgu0/2023_day_08_part_2_surely_it_wont_take_longer/