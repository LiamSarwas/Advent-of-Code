from collections import Counter


def get_layers(image, width, height):
    layer_length = width*height
    layer_count = len(image)//layer_length
    for i in range(0, layer_count):
        layer = image[i*layer_length:(i+1)*layer_length]
        yield layer


def main():
    image = None
    with open("input") as image_file:
        image = image_file.readline().strip()

    counters = [Counter(layer) for layer in get_layers(image, 25, 6)]

    result = 0
    min_zeroes = 99999999999

    for c in counters:
        if c["0"] < min_zeroes:
            min_zeroes = c["0"]
            result = c["1"]*c["2"]

    print(result)


if __name__ == "__main__":
    main()
