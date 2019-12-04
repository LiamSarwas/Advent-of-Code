import sys


def execute(x, y):
    prog = [1,x,y,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0]
    i = 0
    while True:
        if prog[i] == 99:
            return prog[0]
        if prog[i] == 1:
            prog[prog[i+3]] = prog[prog[i+1]] + prog[prog[i+2]]
        if prog[i] == 2:
            prog[prog[i+3]] = prog[prog[i+1]] * prog[prog[i+2]]
        i += 4

def main():
    for x in range(100):
        for y in range(100):
            print(x, y)
            if execute(x, y) == 19690720:
                print(f"Noun: {x}\nVerb: {y}")
                return

if __name__ == '__main__':
    main()
