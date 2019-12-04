def generate_path(p):
    path = [(0, 0)]
    for d in p:
        last_element = path[-1]
        if d.startswith("R"):
            for j in range(1, int(d[1:])+1):
                new_loc = (last_element[0]+j, last_element[1])
                path.append(new_loc)
        if d.startswith("L"):
            for j in range(1, int(d[1:])+1):
                new_loc = (last_element[0]-j, last_element[1])
                path.append(new_loc)
        if d.startswith("U"):
            for j in range(1, int(d[1:])+1):
                new_loc = (last_element[0], last_element[1]+j)
                path.append(new_loc)
        if d.startswith("D"):
            for j in range(1, int(d[1:])+1):
                new_loc = (last_element[0], last_element[1]-j)
                path.append(new_loc)
    return path


with open("input") as f:
    p1, p2 = f.readlines()
    p1 = p1.strip().split(',')
    p2 = p2.strip().split(',')

    path_one = set(generate_path(p1))
    path_two = set(generate_path(p2))
    min_dist = 10000000000
    for a in path_one.intersection(path_two):
        if a[0] != 0 and a[1] != 0:
            dist = abs(a[0])+abs(a[1])
            if dist < min_dist:
                min_dist = dist
    print(min_dist)
