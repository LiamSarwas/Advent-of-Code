from collections import defaultdict


def get_leaf_path_lengths(root, orbits, path_length):
    leaves = orbits.get(root, None)
    if not leaves:
        return path_length
    else:
        return path_length + sum(get_leaf_path_lengths(leaf, orbits, path_length+1) for leaf in leaves)


def main():
    root = "COM"
    orbits = defaultdict(set)
    with open("input") as orbit_map:
        for orbit in orbit_map:
            start, end = orbit.strip().split(')')
            orbits[start].add(end)

    results = get_leaf_path_lengths("COM", orbits, 0)
    print(results)


if __name__ == "__main__":
    main()
