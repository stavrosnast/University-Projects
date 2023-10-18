import cv2  # Version 4.5.3.56
import numpy as np  # Version 1.19.5
import random
import sys
from skimage.metrics import structural_similarity as ssim


def noise_salt_pepper(anImage, prob):
    output = np.zeros(anImage.shape, np.uint8)  # do not use original image it overwrites the image
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


def calculateMAE(imageA, imageB):
    total = np.sum(np.absolute((imageB.astype("float") - imageA.astype("float"))))
    total /= float(imageA.shape[0] * imageA.shape[1] * 255)

    if total < 0:
        return total * -1
    else:
        return total


original_Image = cv2.imread('original_1.jpg', 0)  # Read Original Image
sp = noise_salt_pepper(original_Image, 0.1)  # Noise Salt & Pepper at 10% probability
mf = cv2.medianBlur(sp, 5)  # Median Blur to remove noise
gf = cv2.GaussianBlur(sp, (5, 5), cv2.BORDER_DEFAULT)  # Gaussian blur to remove noise by applying 5x5 kernel
avf = cv2.blur(sp, (5, 5), cv2.BORDER_DEFAULT)  # Average blur to remove noise

# Show image
cv2.namedWindow('Salt & Pepper', cv2.WINDOW_NORMAL)
cv2.imshow('Salt & Pepper', sp)
cv2.resizeWindow('Salt & Pepper', 480, 360)
cv2.waitKey(0)
cv2.namedWindow('Median Filtering', cv2.WINDOW_NORMAL)
cv2.imshow('Median Filtering', mf)
cv2.resizeWindow('Median Filtering', 480, 360)
cv2.waitKey(0)
cv2.namedWindow('Gaussian Blurring', cv2.WINDOW_NORMAL)
cv2.imshow('Gaussian Blurring', gf)
cv2.resizeWindow('Gaussian Blurring', 480, 360)
cv2.waitKey(0)
cv2.namedWindow('Average Blurring', cv2.WINDOW_NORMAL)
cv2.imshow('Average Blurring', avf)
cv2.resizeWindow('Average Blurring', 480, 360)
cv2.waitKey(0)

# Save image
cv2.imwrite('SaltAndPepper.jpg', sp)
cv2.imwrite('MedianFiltering.jpg', mf)
cv2.imwrite('GaussianBlurring.jpg', gf)
cv2.imwrite('AverageBlurring.jpg', avf)

# Close windows after user input
print("Press any key to close the windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

# Checking Similarity with SSIM after noise and denoising
simil_score, _ = ssim(original_Image, mf, full=True)
print('SSIM score for median blur is: {:.3f}'.format(simil_score))
simil_score, _ = ssim(original_Image, gf, full=True)
print('SSIM score for gauss blur is: {:.3f}'.format(simil_score))
simil_score, _ = ssim(original_Image, avf, full=True)
print('SSIM score for average blur is: {:.3f}'.format(simil_score))

# Calculating the Mean Absolute Error between original and given processed picture
mae = calculateMAE(mf, original_Image)
print('MAE between original and  median blur is: {:.3f}'.format(mae))
mae = calculateMAE(gf, original_Image)
print('MAE between original and gauss blur is: {:.3f}'.format(mae))
mae = calculateMAE(avf, original_Image)
print('MAE between original and average blur is: {:.3f}'.format(mae))

# Terminate script
sys.exit(0)
