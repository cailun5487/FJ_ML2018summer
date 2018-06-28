from PIL import Image
import sys

filepath = sys.argv[1]

imgInput = Image.open(filepath) # open photo from filepath.
listPixels = list(imgInput.getdata()) # get list of pixels from input image.

for i in range(len(listPixels)):
    r, g, b = listPixels[i] # extract the RGB value pixel by pixel.
    listPixels[i] = ( int(r/2), int(g/2), int(b/2) ) # replace the value of RGB that are divided by half in the pixel.

imgOutput = Image.new(imgInput.mode, imgInput.size) # Create a new image with the same mode and image size with the image inputed.
imgOutput.putdata(listPixels) # put the list of pixels into output image. 
imgOutput.save("./Q2.jpg", "jpeg") # save the new photo.