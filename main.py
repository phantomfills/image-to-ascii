from PIL import Image

def convert_to_ascii(image, type, scale):
    scale = int(scale)

    # open and get image size
    img = Image.open(image)
    width, height = img.size

    # resize image (downscale)
    img.resize((width // scale, height // scale)).save("resized.%s" % type)

    # open new image
    img = Image.open("resized.%s" % type)
    width, height = img.size

    # list with correct width and height (same as resized image)
    grid = []
    for i in range(height):
        grid.append(["X"] * width)

    pixels = img.load()

    for y in range(height):
        for x in range(width):
            if sum(pixels[x, y]) == 0:
                grid[y][x] = "#"
            elif sum(pixels[x, y]) < 70:
                grid[y][x] = "X"
            elif sum(pixels[x, y]) < 140:
                grid[y][x] = "%"
            elif sum(pixels[x, y]) < 210:
                grid[y][x] = "%"
            elif sum(pixels[x, y]) < 280:
                grid[y][x] = "&"
            elif sum(pixels[x, y]) < 350:
                grid[y][x] = "*"
            elif sum(pixels[x, y]) < 420:
                grid[y][x] = "+"
            elif sum(pixels[x, y]) < 490:
                grid[y][x] = "/"
            elif sum(pixels[x, y]) < 560:
                grid[y][x] = "-"
            elif sum(pixels[x, y]) < 700:
                grid[y][x] = " "

    with open(f"ascii.txt", "w") as file:
        for row in grid:
            file.write("".join(row) + "\n")

def main():
    convert_to_ascii("mona-lisa.png", "png", 3)

if __name__ == "__main__":
    main()