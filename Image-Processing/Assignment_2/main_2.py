import cv2
import numpy as np

# read the original image
img = cv2.imread('Original.jpg')
# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# defining all the parameters
t_lower = 100  # Lower Threshold
t_upper = 200  # Upper threshold
aperture_size = 5  # Aperture size
L2Gradient = True  # Boolean
# applying the Canny Edge filter with Aperture Size and L2Gradient
edge = cv2.Canny(img_gray, t_lower, t_upper, apertureSize = aperture_size, L2gradient = L2Gradient)
cv2.imwrite("CannyGrayscale.png", edge)
cv2.imshow("Canny", edge)
# generate Gaussian noise
gauss = np.random.normal(0, 1, edge.size)
gauss = gauss.reshape(edge.shape[0], edge.shape[1]).astype('uint8')
# add the Gaussian noise to the image
img_gauss = cv2.add(img_gray, gauss)
cv2.imwrite("GaussNoise.png", img_gauss)
cv2.imshow("Gauss Noise", img_gauss)
# denoise img with median blur filter
clean_img = cv2.medianBlur(img_gauss, 5)
cv2.imwrite("medianBlur.png", clean_img)
cv2.imshow("Median Blur", clean_img)
# applying the Canny Edge filter on denoise Img
edge_denoise_img = cv2.Canny(clean_img, t_lower, t_upper, L2gradient = L2Gradient)
# Show final canny
cv2.imwrite("finalCanny.png", edge_denoise_img)
cv2.imshow("Final Canny", edge_denoise_img)
cv2.waitKey(0)
# clean all opened windows
cv2.destroyAllWindows()
