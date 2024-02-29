import cv2       # Install Opencv-python library

# Read the image
img = cv2.imread("abc.jpg")

# Check if the image was successfully loaded
if img is None:
    print("Error: Image not found.")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray_image = 255 - gray_image

# Apply Gaussian blur to the inverted grayscale image
blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19, 19), 0)

# Invert the blurred image
inverted_blurred_image = 255 - blurred_inverted_gray_image

# Divide the grayscale image by the inverted blurred image to create the sketch effect
sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

# Display the original image and the pencil sketch
cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch", sketch)

# Wait for a key press and close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
