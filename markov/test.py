import matplotlib.image as img


class Image:
    def __init__(self, pixels, width, height):
        self.pixels = []
        self.width = width
        self.height = height
        for x in range(0, width):
            for y in range(0, height):
                self.pixels.append(pixels[x][y])


# Load image
data = []
for i in range(1, 20):
    image = img.imread('./data/' + str(i) + '.jpg')
    data.append(Image(image, image.shape[0], image.shape[1]))
