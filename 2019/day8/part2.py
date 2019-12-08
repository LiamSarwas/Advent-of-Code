def main():
    image = None
    with open("input") as image_file:
        image = image_file.readline().strip()

    height = 6
    width = 25
    layer_length = width*height
    layer_count = len(image)//layer_length

    result = [0]*layer_length

    for i in range(0, layer_length):
        for j in range(0, layer_count):
            value = image[layer_length*j + i]
            if value != "2":
                result[i] = value
                break

    result = ''.join([a if a == "1" else " " for a in result])
    for i in range(0, height):
        print(result[width*i:width*(i+1)])


if __name__ == "__main__":
    main()
