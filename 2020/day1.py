def part_one():
    expenses = set()
    with open("input/day1.txt") as f:
        for line in f:
            num = int(line.strip())
            if num in expenses:
                return num * (2020 - num)
            else:
                expenses.add(2020 - num)

def part_two():
    with open("input/day1.txt") as f:
        nums = [int(line.strip()) for line in f]
    for i, num in enumerate(nums):
        expenses = set()
        for j, num2 in enumerate(nums):
            if i == j:
                pass
            else:
                if num2 in expenses:
                    return (2020 - num - num2) * num * num2
                else:
                    expenses.add(2020 - num - num2)


def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
