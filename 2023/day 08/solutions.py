from itertools import cycle
import re
import math

with open('input.txt', 'r') as f:
    _input = f.read()

def part1(_input):
    directions, connections = _input.split('\n\n')
    directions = cycle(0 if d == 'L' else 1 for d in directions)
    graph = {}
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    node = 'AAA'
    for steps, d in enumerate(directions, start=1):
        node = graph[node][d]
        if node == 'ZZZ':
            break

    return steps

def part2(_input):
    directions, connections = _input.split('\n\n')
    directions = [0 if d == 'L' else 1 for d in directions]
    graph = {}
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    starting_nodes = [node for node in graph if node[2] == 'A']
    cycles = []
    for node in starting_nodes:
        for steps, d in enumerate(cycle(directions), start=1):
            node = graph[node][d]
            if node[2] == 'Z':
                cycles.append(steps)
                break

    return math.lcm(*cycles)

print('Part 1:', part1(_input))
print('Part 2:', part2(_input))