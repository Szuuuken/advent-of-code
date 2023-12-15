import sys
from typing import List
import re
from functools import cmp_to_key

def main():
    #file = open('day08_part2_example_input_1.txt', 'r')
    #file = open('day08_part2_example_input_2.txt', 'r')
    file = open('day08_part2_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    instructions = lines[0]
    nodes = dict()

    for line in lines[2:]:
        node_codes = re.findall(r'[A-Z]{3}', line)
        nodes[node_codes[0]] = (node_codes[1], node_codes[2])

    print(instructions)
    print(nodes)
    searching = True
    current_node = nodes['AAA']
    instruction_pointer = 0
    steps = 0

    while searching:
        steps += 1
        instruction = instructions[instruction_pointer]
        next_index = 0 if instruction == 'L' else 1
        next_node_code = current_node[next_index]
        
        print(f'inststruction: {instruction}; node: {current_node}; next: {next_node_code}')

        current_node = nodes[next_node_code]
        instruction_pointer += 1
        if(instruction_pointer >= len(instructions)): instruction_pointer = 0

        searching = next_node_code != "ZZZ" 

    print(steps)
    
if __name__ == "__main__":
    main()