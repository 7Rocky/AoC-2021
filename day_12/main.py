def dfs(root, nodes, visited, paths, special, path=''):
    if root == 'end':
        return paths.add(f'{path}end')

    path += f'{root},'

    if root.islower() and root not in special:
        visited.add(root)

    if root in special:
        special.clear()

    for node in nodes[root]:
        if node not in visited:
            dfs(node, nodes, visited.copy(), paths, special.copy(), path)


def main():
    nodes = {}

    with open('input.txt') as f:
        for line in f.readlines():
            src, dst = line.strip().split('-')

            if src in nodes:
                nodes[src].add(dst)
            else:
                nodes[src] = {dst}

            if dst in nodes:
                nodes[dst].add(src)
            else:
                nodes[dst] = {src}

    paths = set()

    dfs('start', nodes, {'start'}, paths, set())
    print(f'Number of paths (1): { len(paths) }')

    paths.clear()

    for node in nodes.keys():
        if node not in {'start', 'end'} and node.islower():
            dfs('start', nodes, {'start'}, paths, {node})

    print(f'Number of paths (2): { len(paths) }')


if __name__ == '__main__':
    main()
