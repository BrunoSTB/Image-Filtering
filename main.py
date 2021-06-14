from PIL import Image
from imghdr import what

def main():
    # User inputs image via file path
    print("Usage: 'filename.png' if in the same folder or 'directory/filename.png'")
    user_input = input("Enter a PNG image's path: ")

    if not user_input:
        print("Couldn't find image.")
        return 

    if what(user_input).lower() != 'png':
        print("Not a valid image format.")
        return

    myImage = Image.open(user_input)

    # User selects filter
    chosen_filter = input("Choose a filter (Grayscale / Sepia / Reflect / Blur / Edges): ")

    # Applies chosen filter
    if chosen_filter.lower() in ["g", "gray", "grayscale"]:
        grayscale(myImage)
        print("Image filtered to grayscale!")
    elif chosen_filter.lower() in ["s", "sepia"]:
        sepia(myImage)
        print("Image filtered to sepia!")
    elif chosen_filter.lower() in ["r", "reflect"]:
        reflect(myImage)
        print("Image reflected!")
    elif chosen_filter.lower() in ["b", "blur"]:
        blur(myImage)
        print("Image blurred!")
    else:
        print("Filter does not exist")


def grayscale(image):
    # Creates image pixel map and defines its height/width
    pixel_map = image.load()
    width, height = image.size

    for i in range(width):
        for j in range(height): #A8 03 14
            # Gets rgb for each pixel (at i,j coordinates) and turns it grayscaled
            r, g, b = image.getpixel((i, j))
            grayscale = (r + g + b) / 3.0
            pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))
    # Saves image as grayscale.png
    image.save("grayscale", format="png")


def sepia(image):
        # Creates image pixel map and defines its height/width
    pixel_map = image.load()
    width, height = image.size

    for i in range(width):
        for j in range(height):
            # Gets rgb for each pixel (at i,j coordinates) and turns it into sepia
            r, g, b= image.getpixel((i, j))

            sepiaRed = 0.393 * r + 0.769 * g + 0.189 * b
            sepiaGreen = 0.349 * r + 0.686 * g + 0.168 * b
            sepiaBlue = 0.272 * r + 0.534 * g + 0.131 * b

            if sepiaRed > 255:
                sepiaRed = 255
            if sepiaGreen > 255:
                sepiaGreen = 255
            if sepiaBlue > 255:
                sepiaBlue = 255

            pixel_map[i, j] = (int(sepiaRed), int(sepiaGreen), int(sepiaBlue))
    # Saves image as sepia.png
    image.save("sepia", format="png")


def reflect(image):
    # Creates image pixel map and defines its height/width
    pixel_map = image.load()
    width, height = image.size

    # Creates a new blank image and gets it's pixel map
    reflected = Image.new(mode="RGB", size=(width, height))
    reflected_map = reflected.load()

    # Defines the variable "a" so that the pixels can be copied from the end to the start, making it reflected
    a = width - 1
    for i in range(width):
        for j in range(height):
            reflected_map[a, j] = pixel_map[i, j]
        a -= 1
    reflected.save("reflected", format="png")         

def blur(image):
    # Creates image pixel map and defines its height/width
    pixel_map = image.load()
    width, height = image.size

    # Creates a reference image to be used, so it can be properly blurred
    img_copy = image
    copy_pixel_map = img_copy.load()

    for i in range(width):
        for j in range(height):
            # Declares rgb variables to contain the sum of the 3x3 pixel grid
            red = 0
            green = 0
            blue = 0
            # Counter variable to keep track of the valid pixels in the 3x3 pixel grid
            counter = 0
            
            # Loops for the 3x3 pixel grid so it can be properly blurred
            for a in range(i - 1, i + 2):
                # Check if the pixel is valid (inside the img)
                if a >= 0 and a < width:
                    for b in range(j - 1, j + 2):
                        # Check if the pixel is valid (inside the img)
                        if b >= 0 and b < height:
                            # Sums all of the rgb values and add 1 to the counter
                            r, g, b = img_copy.getpixel((a, b))
                            red += r
                            green += g
                            blue += b
                            counter += 1

            # Divides the sum by how many pixels were summed
            red = int(float(red) / float(counter))
            green = int(float(green) / float(counter))
            blue = int(float(blue) / float(counter))

            # Checks if all values are capped at max 255
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
                
            pixel_map[i, j] = (red, green, blue)

    # Saves image as blur.png
    image.save("blur", format="png")


if __name__ == "__main__":
    main()



