import sys
from typing import List
import re
from timeit import default_timer as timer
from datetime import timedelta

class GardenMapEntry:
    def __init__(self, destination_start: int, source_start: int, range_length) -> None:
        self.destination_start = destination_start
        self.source_start = source_start
        self.range_length = range_length
        self.destination_end = destination_start + range_length - 1
        self.source_end = source_start + range_length - 1

    def resolve_next(self, number: int):
        if number < self.source_start or number > self.source_end: return None
        
        offset = number - self.source_start
        res = self.destination_start + offset

        #print(f's:{self.source_start}; e:{self.source_end}; n:{number}; o{offset}; r{res}')

        return res

class GardenMap:
    def __init__(self, name: str) -> None:
        self.name = name
        self.source_to_destination = dict()
        self.destination_to_source = dict()
        self.map_entries: list[GardenMapEntry] = []
        self.prev: GardenMap = None
        self.next: GardenMap = None

    def add(self, line: str):
        search_result = re.findall(r'\d+', line)
        destination_start = int(search_result[0])
        source_start = int(search_result[1])
        range_length = int(search_result[2])

        self.map_entries.append(GardenMapEntry(destination_start, source_start, range_length))

        # for offset in range(0, range_length):
        #     self.source_to_destination[source_start + offset] = destination_start + offset
        #     self.destination_to_source[destination_start + offset] = source_start + offset

        #print(self.source_to_destination)

    def resolve_next(self, number: int) -> int:
        next_number = number
        
        for map_entry in self.map_entries:
            possible_next_number = map_entry.resolve_next(number)
            
            if possible_next_number is not None:
                next_number = possible_next_number
                break

        #print(f'{self.name}{number}-->{next_number}')

        if self.next is None: return next_number
        return self.next.resolve_next(next_number)

def get_seeds(line: str) -> list[int]:
    seeds: list[int] = []
    
    for seed in re.findall(r'\d+', line):
        seeds.append(int(seed))

    return seeds

def main():
    #file = open('day05_part2_example_input.txt', 'r')
    file = open('day05_part2_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    
    seeds: list[int] = get_seeds(lines[0])
    print(seeds)

    seed_to_soil_map = GardenMap("seed-to-soil map:")
    soil_to_fertiilizer_map = GardenMap("soil-to-fertilizer map:")
    fertilizer_to_water_map = GardenMap("fertilizer-to-water map:")
    water_to_light_map = GardenMap("water-to-light map:")
    light_to_temparature_map = GardenMap("light-to-temperature map:")
    temparature_humidity_map = GardenMap("temperature-to-humidity map:")
    humidity_to_location_map = GardenMap("humidity-to-location map:")

    seed_to_soil_map.next = soil_to_fertiilizer_map
    soil_to_fertiilizer_map.next = fertilizer_to_water_map
    fertilizer_to_water_map.next = water_to_light_map
    water_to_light_map.next = light_to_temparature_map
    light_to_temparature_map.next = temparature_humidity_map
    temparature_humidity_map.next = humidity_to_location_map

    map_dict = { 
        "seed-to-soil map:": seed_to_soil_map,
        "soil-to-fertilizer map:": soil_to_fertiilizer_map,
        "fertilizer-to-water map:": fertilizer_to_water_map,
        "water-to-light map:": water_to_light_map,
        "light-to-temperature map:": light_to_temparature_map,
        "temperature-to-humidity map:": temparature_humidity_map,
        "humidity-to-location map:": humidity_to_location_map
        }

    current_map = None

    for line in lines[1:]:
        if len(line) < 3: continue
        elif line[-1] == ':': current_map = line
        else:
            map_dict[current_map].add(line)

    min_location = sys.maxsize

    iterations = 0

    for i in range(0, len(seeds), 2):
        seed_start = seeds[i]
        seed_length = seed_start + seeds[i + 1]
        iterations += len(range(seed_start, seed_length))

    count = 0
    needed_iterations = len(seeds)/2
    iteration = 0
    start = timer()

    for i in range(0, len(seeds), 2):
        seed_start = seeds[i]
        seed_length = seed_start + seeds[i + 1]
        #print(f'{seed_start}-{seed_length}')

        seed_count = 0
        for seed in range(seed_start, seed_length):
            #print(f'{seed}')
            location = seed_to_soil_map.resolve_next(seed)
            if location < min_location: min_location = location

            seed_count += 1
            iteration += 1

            #if iteration % 100000 == 0: print(f'{count}/{needed_iterations} --> seed_count: {iteration}/{iterations}')
            if iteration % 500000 == 0:
                current_end = timer()
                t = timedelta(seconds=current_end-start)
                needed_secods = timedelta(seconds=t.seconds / iteration * (iterations - iteration))
                percent = round(iteration / iterations * 100, 2)
                print(f'{count}/{needed_iterations} --> seed_count: {iteration}/{iterations}; {t}/{needed_secods} --> {percent}%')

        count += 1
        #end = timer()
        #print(f'#### {count}/{needed_iterations} finished in {timedelta(seconds=end-start)}#####')
        
    print(min_location)

if __name__ == "__main__":
    main()