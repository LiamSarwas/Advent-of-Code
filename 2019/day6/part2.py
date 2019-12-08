def main():
    root = "COM"
    inverse_orbits = {}
    with open("input") as orbit_map:
        for orbit in orbit_map:
            start, end = orbit.strip().split(')')
            inverse_orbits[end] = start

    current_node = "YOU"
    you_path = []
    while True:
        next_node = inverse_orbits.get(current_node, None)
        if next_node:
            you_path.append(next_node)
            current_node = next_node
        else:
            break

    current_node = "SAN"
    san_path_length = 0
    while True:
        next_node = inverse_orbits.get(current_node, None)
        if next_node in you_path:
            current_node += next_node
            break
        else:
            san_path_length += 1
            current_node = next_node

    print(san_path_length + you_path.index(next_node))


if __name__ == "__main__":
    main()
