import cv2

# STEP 1:
# reading image
image = cv2.imread('image.jpg')

# STEP 2:
# converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# STEP 3: Invert the grayscale/negative img. this will be our
# inverted grayscale img
# image inversion
inverted_image = 255 - gray_image

# Step 4: make sketch by mixing grayscale img with inverted blurry img.
# divid grayscale img by inverted blurry img.

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# We now got our pencil_sketch. So, display it using OpenCV.
cv2.imshow("Original Image", image)
cv2.imshow("pencil Sketch of lion_cub", pencil_sketch)
cv2.waitKey(0)

