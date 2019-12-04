def test_num(num):
    prev = num[0]
    for i in range(1, len(num)):
        if num[i] >= prev:
            prev = num[i]
        else:
            return False
    for i in range(0, len(num)-1):
        if num[i] == num[i+1]:
            return True
    return False


def main():
    a = 236491 # 236777 first valid
    b = 713787 # 699999 last valid
    count = 0
    for i in range(a, b+1):
        if test_num([int(k) for k in str(i)]):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
