def find_cycles(graph, start, max_len):
    cycles = []

    def dfs(current, visited, path):
        if len(path) > max_len:
            return

        for neighbor in graph[current]:
            if neighbor == start and len(path) > 1:
                cycles.append(path + [start])

            if neighbor not in visited:
                dfs(neighbor, visited | {neighbor}, path + [neighbor])

    dfs(start, {start}, [start])
    return cycles


def normalize_cycle(cycle):
    cycle = cycle[:-1]
    n = len(cycle)
    variants = [tuple(cycle[i:] + cycle[:i]) for i in range(n)]
    return min(variants)


def unique_cycles(cycles):
    seen = set()
    result = []

    for cycle in cycles:
        norm = normalize_cycle(cycle)
        if norm not in seen:
            seen.add(norm)
            result.append(cycle)

    return result


graph = {
    0: [1],
    1: [2, 3],
    2: [0],
    3: [4],
    4: [1]
}

v = 1
K = 5

cycles = find_cycles(graph, v, K)
cycles = unique_cycles(cycles)

for c in cycles:
    print(c)

print(len(cycles))
print(len(cycles) > 0)