def calc_num(l, i):
    pattern = [0]*i
    pattern += [1]*i
    pattern += [0]*i
    pattern += [-1]*i
    while len(pattern) <= len(l):
        pattern += pattern

    pattern = pattern[1:len(l)+1]

    return int(str(sum(a[0]*a[1] for a in zip(pattern, l)))[-1])


def execute_phase(l):
    r = []
    for i in range(1, len(l) + 1):
        r.append(calc_num(l, i))
    return r


def execute_phases(n, input_list):
    next_list = input_list
    for i in range(n):
        next_list = execute_phase(next_list)
    return next_list


def main():
    with open("input") as f:
        first_list = [int(a) for a in f.readline().strip()]

    print(''.join(str(a) for a in execute_phases(100, first_list))[0:8])


if __name__ == "__main__":
    main()
