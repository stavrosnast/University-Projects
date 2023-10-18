# Image Processing with OpenCV and Python Part 1

This project is aimed at introducing students to the field of Image Processing, specifically focusing on tasks such as noise introduction, filtering, and result comparison using the Python programming language and the OpenCV library. We will perform several steps to process images and achieve the desired outcomes.

## Requirements

Before running the code, make sure you have the required libraries installed:

- OpenCV (Version 4.5.3.56)
- NumPy (Version 1.19.5)
- scikit-image (for Structural Similarity Index - SSIM)

You can install these libraries using pip:

```bash
pip install opencv-python-headless==4.5.3.56 numpy==1.19.5 scikit-image
```

## Code 1: Solarization of an Image

The following code performs solarization on an image by inverting pixel values based on a threshold.

```python
import cv2

# Function for solarization of the given image
def solarize(originalImage, thresValue):
    img_original_gray = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)  # Convert Original Image to Grayscale
    cv2.imwrite("Grayscale.jpg", img_original_gray)  # Save the newly created image
    row, col = img_original_gray.shape
    for i in range(row):
        for j in range(col):
            if thresValue > img_original_gray[i, j]:
                img_original_gray[i, j] = 255 - img_original_gray[i, j]  # Invert pixel values
    return img_original_gray

# Read Original Image & Create/Save New Images
img_original_colour = cv2.imread('original.jpg')  # Read Original Image
img_original_gray_64 = solarize(img_original_colour, 64)
cv2.imwrite("Grayscale_64.jpg", img_original_gray_64)

# Show Images
cv2.imshow("Original Color", img_original_colour)
cv2.imshow('Solarized 64', img_original_gray_64)
cv2.waitKey(0)  # Wait for user input
cv2.destroyAllWindows()
```

## Code 2: Adding Salt & Pepper Noise and Denoising

This code adds salt and pepper noise to an image, applies various filters to denoise it, and calculates SSIM and MAE for comparison.

```python
import cv2
import numpy as np
import random
import sys
from skimage.metrics import structural_similarity as ssim

# Function to add salt and pepper noise to an image
def noise_salt_pepper(anImage, prob):
    output = np.zeros(anImage.shape, np.uint8)
    for colIdx in range(anImage.shape[0]):
        for rowIdx in range(anImage.shape[1]):
            rand = random.random()
            if rand < prob:
                output[rowIdx][colIdx] = 0  # Black
            elif rand > (1 - prob):
                output[rowIdx][colIdx] = 255  # White
            else:
                output[rowIdx][colIdx] = anImage[rowIdx][colIdx]
    return output

# Function to calculate Mean Absolute Error (MAE) between two images
def calculateMAE(imageA, imageB):
    total = np.sum(np.absolute((imageB.astype("float") - imageA.astype("float")))
    total /= float(imageA.shape[0] * imageA.shape[1] * 255)
    return total

original_Image = cv2.imread('jinx.jpg', 0)  # Read Original Image
sp = noise_salt_pepper(original_Image, 0.1)  # Add Salt & Pepper Noise
mf = cv2.medianBlur(sp, 5)  # Median Blur to remove noise
gf = cv2.GaussianBlur(sp, (5, 5), cv2.BORDER_DEFAULT)  # Gaussian Blur to remove noise
avf = cv2.blur(sp, (5, 5), cv2.BORDER_DEFAULT)  # Average Blur to remove noise

# Calculate SSIM
simil_score, _ = ssim(original_Image, mf, full=True)
print('SSIM score for median blur is: {:.3f}'.format(simil_score))
simil_score, _ = ssim(original_Image, gf, full=True)
print('SSIM score for gauss blur is: {:.3f}'.format(simil_score))
simil_score, _ = ssim(original_Image, avf, full=True)
print('SSIM score for average blur is: {:.3f}'.format(simil_score))

# Calculate MAE
mae = calculateMAE(mf, original_Image)
print('MAE between original and median blur is: {:.3f}'.format(mae))
mae = calculateMAE(gf, original_Image)
print('MAE between original and gauss blur is: {:.3f}'.format(mae))
mae = calculateMAE(avf, original_Image)
print('MAE between original and average blur is: {:.3f}'.format(mae))
```

## Usage

1. Make sure you have the required libraries installed as mentioned in the "Requirements" section.

2. Place the original image (e.g., 'original.jpg') in the project directory.

3. Execute the respective code blocks in a Python environment to perform solarization (Code 1) and add noise, denoise, and compare results (Code 2).

4. Observe the output images and comparison metrics for your image processing tasks.
