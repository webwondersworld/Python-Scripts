from rembg import remove
from PIL import Image

# Path for input and output image
input_img = 'abc.jpg'
output_img = 'abc_rmbg.png'

# loading and removing background
inp = Image.open(input_img)
output = remove(inp)

print("Background Removed!")
# Saving background removed image to same location as input image
output.save(output_img)
print("Image Saved!")
