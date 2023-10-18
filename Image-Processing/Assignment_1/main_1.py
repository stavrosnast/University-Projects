import cv2

# Function for solarization of the given image
def solarize(originalImage, thresValue):
    img_original_gray = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)  # Convert Original Image to Grayscale
    cv2.imwrite("Grayscale.jpg", img_original_gray)  # Save newly created image on the directory
    row, col = img_original_gray.shape
    for i in range(row):
        for j in range(col):
            if thresValue > img_original_gray[i, j]:
                img_original_gray[i, j] = 255 - img_original_gray[i, j]  # Check pixel for pixel and change it
    return img_original_gray

# Read Original Image & Create/Save New Images on the directory
img_original_colour = cv2.imread('original.jpg')  # Read Original Image
img_original_gray_64 = solarize(img_original_colour, 64)
cv2.imwrite("Grayscale_64.jpg", img_original_gray_64)
img_original_gray_128 = solarize(img_original_colour, 128)
cv2.imwrite("Grayscale_128.jpg", img_original_gray_128)
img_original_gray_192 = solarize(img_original_colour, 192)
cv2.imwrite("Grayscale_192.jpg", img_original_gray_192)

# Show Images
cv2.imshow("Original Color", img_original_colour)
cv2.imshow('Solarized 64', img_original_gray_64)
cv2.imshow('Solarized 128', img_original_gray_128)
cv2.imshow('Solarized 192', img_original_gray_192)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()






