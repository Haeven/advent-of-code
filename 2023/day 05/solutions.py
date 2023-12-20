import re

with open('input.txt', 'r') as f:
    _input = f.read()

def part1(_input):
    segments = _input.split('\n\n')
    seeds = re.findall(r'\d+', segments[0])

    min_location = float('inf')
    for x in map(int, seeds):
        for seg in segments[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)

    return min_location

def part2(_input):
    segments = _input.split('\n\n')
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # No overlap
                continue
            if x1 < y1:                 # Split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # Split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            break
            intervals.append((x1 + diff, x2 + diff, level + 1)) # Perfect overlap -> make conversion and let pass to next nevel 

        else:
            intervals.append((x1, x2, level + 1))
  
    return min_location

print('Part 1:', part1(_input))
print('Part 2:', part2(_input))