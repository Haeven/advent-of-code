with open('input.txt', 'r') as f:
    _input = f.read()

def part1(_input):
    grid = [list(row) for row in _input.split('\n')]
    m, n = len(grid), len(grid[0])
    for c in range(n):
        lim = 0
        for r in range(m):
            if grid[r][c] == '#':
                lim = r + 1
            elif grid[r][c] == 'O':
                if r > lim:
                    grid[lim][c] = 'O'
                    grid[r][c] = '.'
                lim += 1

    total_load = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 'O':
                total_load += m - r

    return total_load

def part2(_input):
    def spin_cycle():
        # North
        for c in range(n):
            lim = 0
            for r in range(m):
                if grid[r][c] == '#':
                    lim = r + 1
                elif grid[r][c] == 'O':
                    if r > lim:
                        grid[lim][c] = 'O'
                        grid[r][c] = '.'
                    lim += 1
        # West
        for r in range(m):
            lim = 0
            for c in range(n):
                if grid[r][c] == '#':
                    lim = c + 1
                elif grid[r][c] == 'O':
                    if c > lim:
                        grid[r][lim] = 'O'
                        grid[r][c] = '.'
                    lim += 1
        # South
        for c in range(n):
            lim = m - 1
            for r in reversed(range(m)):
                if grid[r][c] == '#':
                    lim = r - 1
                elif grid[r][c] == 'O':
                    if r < lim:
                        grid[lim][c] = 'O'
                        grid[r][c] = '.'
                    lim -= 1
        # East
        for r in range(m):
            lim = n - 1
            for c in reversed(range(n)):
                if grid[r][c] == '#':
                    lim = c - 1
                elif grid[r][c] == 'O':
                    if c < lim:
                        grid[r][lim] = 'O'
                        grid[r][c] = '.'
                    lim -= 1

    # Record loads over 300 spin cycles
    grid = [list(row) for row in _input.split('\n')]
    m, n = len(grid), len(grid[0])
    loads = []
    history = {}
    for i in range(300):
        spin_cycle()
        total_load = sum((grid[r][c]=='O') * (m-r) for r in range(m) for c in range(n))
        loads.append(total_load)

        # Check for repetition cycle
        if i > 20:
            state_hash = str(loads[-20:])
            if state_hash in history:
                rep_cycle_start = history[state_hash]
                rep_cycle_length = i - rep_cycle_start
                break
            history[state_hash] = i

    target = 1_000_000_000
    offset = (target - rep_cycle_start) % rep_cycle_length - 1  # -1 because initial load was not recorded 
    return loads[rep_cycle_start + offset]

print('Part 1:', part1(_input))
print('Part 2:', part2(_input))