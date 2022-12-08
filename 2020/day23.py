import time
import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


class Node():
    def __init__(self, cup, next_node):
        self.cup = cup
        self.next_node = next_node

    def __repr__(self):
        return f"{self.cup} --> {self.next_node.cup}"

def construct_linked_list(input_data, part=1):
    nodes = {}
    head_node = Node(input_data[0], None)
    nodes[input_data[0]] = head_node
    for i in range(1, len(input_data)):
        new_node = Node(input_data[i], None)
        nodes[input_data[i-1]].next_node = new_node
        nodes[input_data[i]] = new_node
    if part == 1:
        nodes[input_data[-1]].next_node = head_node
        return head_node, nodes
    else:
        new_node = Node(10, None)
        nodes[input_data[-1]].next_node = new_node
        nodes[10] = new_node
        for i in range(11, 1000001):
            new_node = Node(i, None)
            nodes[i-1].next_node = new_node
            nodes[i] = new_node
        nodes[1000000].next_node = head_node
        return head_node, nodes

def part_one(input_data):
    starting_node, nodes = construct_linked_list(input_data)
    for i in range(100):
        pulled_nodes = [starting_node.next_node, starting_node.next_node.next_node, starting_node.next_node.next_node.next_node]
        starting_node.next_node = pulled_nodes[-1].next_node
        pulled_node_labels = {node.cup for node in pulled_nodes}
        insert_position = starting_node.cup - 1
        if insert_position == 0:
            insert_position = 9
        while insert_position in pulled_node_labels:
            insert_position -= 1
            if insert_position == 0:
                insert_position = 9
        insert_node = nodes[insert_position]
        insert_next_node = insert_node.next_node
        insert_node.next_node = pulled_nodes[0]
        pulled_nodes[-1].next_node = insert_next_node
        starting_node = starting_node.next_node
    
    res = ""
    current_node = nodes[1]
    for i in range(8):
        res += str(current_node.next_node.cup)
        current_node = current_node.next_node
    return res


def part_two(input_data):
    starting_node, nodes = construct_linked_list(input_data, part=2)
    for i in range(10000000):
        pulled_nodes = [starting_node.next_node, starting_node.next_node.next_node, starting_node.next_node.next_node.next_node]
        starting_node.next_node = pulled_nodes[-1].next_node
        pulled_node_labels = {node.cup for node in pulled_nodes}
        insert_position = starting_node.cup - 1
        if insert_position == 0:
            insert_position = 1000000
        while insert_position in pulled_node_labels:
            insert_position -= 1
            if insert_position == 0:
                insert_position = 1000000
        insert_node = nodes[insert_position]
        insert_next_node = insert_node.next_node
        insert_node.next_node = pulled_nodes[0]
        pulled_nodes[-1].next_node = insert_next_node
        starting_node = starting_node.next_node

    node_one = nodes[1]
    return node_one.next_node.cup * node_one.next_node.next_node.cup


if __name__ == "__main__":
    DATA = "215694783"
    DATA = [int(c) for c in DATA]
    print(part_one(DATA))
    print(part_two(DATA))
