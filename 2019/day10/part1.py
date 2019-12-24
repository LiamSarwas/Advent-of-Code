from math import gcd


def print_map(m):
    c_map = {0: "_", 1: "#", -1: 'X'}
    for row in m:
        print(''.join([c_map[a] for a in row]))


def count_visible(ast_map, i, j):
    m = []
    for row in ast_map:
        m.append(row.copy())
    height = len(m)
    width = len(m[0])
    ast_count = 0

    for a in range(0, height):
        for b in range(0, width):
            if m[a][b] == -1:
                continue
            if a == i and b == j:
                continue

            rel_i = i - a
            rel_j = j - b
            mult = gcd(rel_i, rel_j)

            rel_i = rel_i//mult
            rel_j = rel_j//mult

            for d in (-1, 1):
                seen_ast = False
                c = 1
                while True:
                    test_i = i+rel_i*c*d
                    test_j = j+rel_j*c*d
                    if test_i < 0 or test_i >= height or test_j < 0 or test_j >= width:
                        break
                    if m[test_i][test_j] == 1:
                        seen_ast = True
                    m[test_i][test_j] = -1
                    c += 1
                if seen_ast:
                    ast_count += 1
    return ast_count


def main():
    ast_map = []
    with open("input") as f:
        for line in f:
            new_row = [0 if a == "." else 1 for a in line.strip()]
            ast_map.append(new_row)

    height = len(ast_map)
    width = len(ast_map[0])
    print_map(ast_map)
    max_result = 0
    max_loc = (0, 0)
    for i in range(0, height):
        for j in range(0, width):
            if ast_map[i][j] == 1:
                result = count_visible(ast_map, i, j)
                if result > max_result:
                    max_loc = (i, j)
                    max_result = result
    print(max_result)
    print(max_loc)


if __name__ == '__main__':
    main()
