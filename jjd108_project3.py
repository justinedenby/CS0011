import bmp

class ImageProcessor:
    def __init__(self, filename):
        self.pixelgrid = bmp.ReadBMP(filename)
        self.height = len(self.pixelgrid)
        self.width = len(self.pixelgrid[0])

    def save(self, new_name):
        bmp.WriteBMP(self.pixelgrid, new_name)

    def invert(self):
        for h in range(self.height):
            for w in range(self.width):
                for c in range(3):
                    self.pixelgrid[h][w][c] = 255 - self.pixelgrid[h][w][c]

    def display_channel(self, channel):
        if channel not in ['r','g','b']:
            print("\n")
            print("Invalid option, choose [r, g, or b]:  ")

        if channel in ['r','g','b']:
            for h in range(self.height):
                for w in range(self.width):
                    if channel == 'r':
                        self.pixelgrid[h][w][1] = 0
                        self.pixelgrid[h][w][2] = 0
                    elif channel == 'g':
                        self.pixelgrid[h][w][0] = 0
                        self.pixelgrid[h][w][2] = 0
                    elif channel == 'b':
                        self.pixelgrid[h][w][0] = 0
                        self.pixelgrid[h][w][1] = 0
                    
    def flip(self, axis):
        if axis in ['h','v']:
            if axis == 'h':
                for h in range(self.height):
                    self.pixelgrid[h] = self.pixelgrid[h][::-1]
            elif axis == 'v':
                self.pixelgrid = self.pixelgrid[::-1]
        if axis not in ['h','v']:
            print("Invalid axis choice. Use 'h' for horizontal or 'v' for vertical flip:  ")

    def grayscale(self):
        for h in range(self.height):
            for w in range(self.width):
                red_channel = self.pixelgrid[h][w][0]
                green_channel = self.pixelgrid[h][w][1]
                blue_channel = self.pixelgrid[h][w][2]

                gray = (red_channel + green_channel + blue_channel) // 3
                self.pixelgrid[h][w] = [gray, gray, gray]

    def brightness(self, operation):
        while True:
            if operation == 'q':
                print("Exiting brightness adjustment")
                return

            elif operation in ['+', '-']:
                adjustment = 25 if operation == '+' else -25

                for h in range(self.height):
                    for w in range(self.width):
                        for c in range(3):
                            self.pixelgrid[h][w][c] += adjustment

                            if self.pixelgrid[h][w][c] > 255:
                                self.pixelgrid[h][w][c] = 255
                            elif self.pixelgrid[h][w][c] < 0:
                                self.pixelgrid[h][w][c] = 0

                operation = input("[+] Increase brightness\n[-] Decrease brightness\n[q] Exit\n(+/-/q): ").lower()
            else:
                print("Invalid Option. Select [+,-,q]  ")
        

    def contrast(self):
        while True:
            operation = input("[+] Increase contrast\n[-] Decrease contrast\n[q] Quit\n(+/-/q): ").lower()
            if operation not in ['q','+','-']:
                print("Invalid option. Select [+,-,q]")
                continue
            elif operation == 'q':
                break
            elif operation == '+':
                C = 45
            elif operation == '-':
                C = -45
            factor = (259 * (C + 255)) / (255 * (259 - C))

            for h in range(self.height):
                for w in range(self.width):
                    for c in range(3):
                        new_value = int(factor * (self.pixelgrid[h][w][c] - 128) + 128)

                        if new_value > 255:
                            new_value = 255
                        elif new_value < 0:
                            new_value = 0
                        self.pixelgrid[h][w][c] = new_value
            else:
                print("Invalid option. Select [+,-,q]  ")


def main():
    filename = input("Enter filename containing source image (MUST be bmp):  ")
    image_processor = ImageProcessor(filename)

    while True:
        print("==============================")
        print("Python Basic Image Processor")
        print("==============================")
        print("a) Invert Colors")
        print("b) Flip Image")
        print("c) Display Color Channel")
        print("d) Convert to Grayscale")
        print("e) Adjust Brightness")
        print("f) Adjust Contrast")
        print("-------------------------")
        print("s) Save Current Image")
        print("o) Open New Image")
        print("q) Quit")
        print("==============================")

        action = input("(a/b/c/d/e/f/s/o/q): ").lower()

        if action == 'a':
            image_processor.invert()
        elif action == 'b':
            axis = input("Choose axis to flip: 'v'-vertically or 'h'-horizontally: ").lower()
            image_processor.flip(axis)
        elif action == 'c':
            channel = input("To change color, choose channel: 'r'-red, 'g'-green, 'b'-blue: ").lower()
            image_processor.display_channel(channel)
        elif action == 'd':
            image_processor.grayscale()
        elif action == 'e':
            operation = input("[+] Increase brightness\n[-] Decrease brightness\n[q] Exit\n(+/-/q): ").lower()
            image_processor.brightness(operation)
        elif action == 'f':
            image_processor.contrast()
        elif action == 's':
            new_name = input("Enter name to save new image to (MUST be .bmp): ")
            image_processor.save(new_name)
        elif action == 'o':
            filename = input("Enter filename containing source image (MUST be .bmp): ")
            image_processor = ImageProcessor(filename)
        elif action == 'q':
            print("Quitting process")
            break
        else:
            print("")
            print("Invalid Option. Please select (a/b/c/d/e/f/s/o/q) ")
main()