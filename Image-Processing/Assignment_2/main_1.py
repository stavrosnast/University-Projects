import cv2
import numpy as np
from matplotlib import colors
from matplotlib import pyplot as plt
from skimage.color import label2rgb
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.metrics import silhouette_score

"""""""""""
  | 1.1 |
"""""""""""
# read image and convert it to rgb
originalImage = cv2.imread('Original.jpg')
originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
# set up the plot
red, green, blue = cv2.split(originalImage)  # divide in 3 color channels
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection = "3d")
# set up the pixel colors
pixel_colors = originalImage.reshape((np.shape(originalImage)[0] * np.shape(originalImage)[1], 3))
norm = colors.Normalize(vmin = -1., vmax = 1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()
# build the scatter plot
axis.scatter(red.flatten(), green.flatten(), blue.flatten(), facecolors = pixel_colors, marker = ".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
axis.set_title("3d Plot RGB")
# save, open, view and close file
plt.savefig("3D_RGB_PLOT.png")
plt.show()
"""""""""""
#   | 1.2 |
# """""""""""
# convert image to rgb
hsv_original_img = cv2.cvtColor(originalImage, cv2.COLOR_RGB2HSV)
hue, saturation, value = cv2.split(hsv_original_img)
# set up the plot
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection = "3d")
"""
We use the same pixel_colors variable for coloring the pixels, since Matplotlib expects the values to be in RGB
"""
# build the scatter plot and view
axis.scatter(hue.flatten(), saturation.flatten(), value.flatten(), facecolors = pixel_colors, marker = ".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
axis.set_title("3d Plot HSV")
# save file and view
plt.savefig("3D_HSV_PLOT.png")
plt.show()
"""""""""""""""""
  | 1.3 RGB |
"""""""""""""""""
# create the histograms
redHist = cv2.calcHist([red], [0], None, [256], [0, 256])
blueHist = cv2.calcHist([green], [0], None, [256], [0, 256])
greenHist = cv2.calcHist([blue], [0], None, [256], [0, 256])
# create plot
plt.plot(redHist, 'red', label = "red")
plt.plot(blueHist, 'blue', label = "blue")
plt.plot(greenHist, 'green', label = "green")
plt.xlabel("Color value")
plt.ylabel("Pixels")
plt.legend(loc = "best")
# save file and view
plt.savefig("RGB_HISTOGRAM.png")
plt.show()
"""""""""""""""""
  | 1.3 HSV |
"""""""""""""""""
# create the histograms
img2 = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
h, s, v = img2[:, :, 0], img2[:, :, 1], img2[:, :, 2]
hist_h = cv2.calcHist([h], [0], None, [256], [0, 256])
hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])
# create plot
plt.plot(hist_h, color = 'r', label = "h")
plt.plot(hist_s, color = 'g', label = "s")
plt.plot(hist_v, color = 'b', label = "v")
plt.xlabel("Color value")
plt.ylabel("Pixels")
plt.legend(loc = "best")
# save file and view
plt.savefig("HSV_HISTOGRAM.png")
plt.show()
"""""""""""""""""""""
  | 1.4 KMeans |
    RGB Image
"""""""""""""""""""""
# read the original file
imageRGBKMEANS = cv2.imread("Original.jpg")
# convert to RGB
imageRGBKMEANS = cv2.cvtColor(imageRGBKMEANS, cv2.COLOR_BGR2RGB)
# reshape the imageRGBKMEANS to a 2D array of pixels and 3 color values (RGB)
pixel_values_RGB_KMEANS = imageRGBKMEANS.reshape((-1, 3))
# convert to float
pixel_values_RGB_KMEANS = np.float32(pixel_values_RGB_KMEANS)
# define stopping for criteria_RGB_KMEANS
criteria_RGB_KMEANS = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
# number of clusters (K)
k = 3
_, labels_RGB_KMEANS, (centers) = cv2.kmeans(pixel_values_RGB_KMEANS, k, None, criteria_RGB_KMEANS, 10, cv2.KMEANS_RANDOM_CENTERS)
# convert back to 8 bit values
centers = np.uint8(centers)
# flatten the labels_RGB_KMEANS array
labels_RGB_KMEANS = labels_RGB_KMEANS.flatten()
# convert all pixels to the color of the centroids
segmented_image_RGB_KMEANS = centers[labels_RGB_KMEANS.flatten()]
# reshape back to the original imageRGBKMEANS dimension
segmented_image_RGB_KMEANS = segmented_image_RGB_KMEANS.reshape(imageRGBKMEANS.shape)
# show the imageRGBKMEANS
plt.imshow(segmented_image_RGB_KMEANS)
plt.savefig("RGB_KMEANS.png")
plt.show()
print("Silhouette Score RGB KMEANS:", silhouette_score(pixel_values_RGB_KMEANS, labels_RGB_KMEANS.ravel(), sample_size=25000))

"""""""""""""""""""""
  | 1.4 KMeans |
    HSV Image
"""""""""""""""""""""
# read the original file
original_image = cv2.imread("Original.jpg")
# convert to hsv
imgHSVKMEANS = cv2.cvtColor(original_image, cv2.COLOR_RGB2HSV)
# reshape the imageRGBKMEANS to a 2D array of pixels and 3 color values
vectorized_HSVKMEANS = imgHSVKMEANS.reshape((-1, 3))
# convert to float
vectorized_HSVKMEANS = np.float32(vectorized_HSVKMEANS)
# define stopping for vectorized_HSVKMEANS
criteria_HSVKMEANS = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# number of clusters (K)
K = 3
attempts = 10
ret, label_HSVKMEANS, center = cv2.kmeans(vectorized_HSVKMEANS, K, None, criteria_HSVKMEANS, attempts, cv2.KMEANS_PP_CENTERS)
# convert back to 8 bit values
center = np.uint8(center)
# flatten the label_HSVKMEANS array
res = center[label_HSVKMEANS.flatten()]
# reshape back to the original imgHSVKMEANS dimension
result_image_HSVKMEANS = res.reshape(imgHSVKMEANS.shape)
# show the image
plt.imshow(result_image_HSVKMEANS)
plt.savefig("HSV_KMEANS.png")
plt.show()
print("Silhouette Score HSV KMEANS: ", silhouette_score(vectorized_HSVKMEANS, label_HSVKMEANS.ravel(), sample_size=25000))
"""""""""""""""""""""
  | 1.4 KMeans |
    RGB + HSV Image
"""""""""""""""""""""
#  Combine RGB and HSV
img = cv2.imread("Original.jpg")
rgb_original_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_original_img = cv2.cvtColor(rgb_original_img,  cv2.COLOR_RGB2HSV)
combined_image = np.concatenate((rgb_original_img, hsv_original_img), axis=2)
# reshpane and convert it to float
imgShape = combined_image.shape
flatimg = np.reshape(combined_image, [-1, 6])
vectorized = np.float32(flatimg)
# define stopping
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# number of clusters (K)
K = 6
attempts = 10
ret, label, center = cv2.kmeans(vectorized, K, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
# convert back to 8 bit values
center = np.uint8(center)
# flatten
res = center[label.flatten()]
# reshape back to the original combined_image dimension
result_image = res.reshape(combined_image.shape)
# do segment
segmented_image = (label2rgb(np.reshape(label, imgShape[:2]), bg_label=0) * 255).astype(np.uint8)
# show the image
plt.imshow(segmented_image)
plt.savefig("COMB_KMEANS.png")
plt.show()
print("Silhouette Score COMBINED KMEANS:", silhouette_score(flatimg, label.ravel(), sample_size=25000))
"""""""""""""""""""""
  | 1.4 MeanShift |
    RGB Image
"""""""""""""""""""""
img = cv2.imread("Original.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# dimensions
imgShape = img.shape
flatimg = np.reshape(img, [-1, 3])
# meanshift
bandwidth = estimate_bandwidth(flatimg, quantile=0.1, n_samples=100)
meanshift = MeanShift(bandwidth=bandwidth, bin_seeding=True)
meanshift.fit(flatimg)
labels = meanshift.labels_
# do segment
segmented_image = (label2rgb(np.reshape(labels, imgShape[:2]), bg_label=0) * 255).astype(np.uint8)
# show the image
plt.imshow(segmented_image)
plt.savefig("RGB_MS.png")
plt.show()
print("Silhouette Score RGB MS: ", silhouette_score(flatimg, labels, sample_size=25000))
"""""""""""""""""""""
  | 1.4 MeanShift |
    HSV Image
"""""""""""""""""""""
img = cv2.imread("Original.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# dimensions
imgShape = img.shape
flatimg = np.reshape(img, [-1, 3])
# meanshift
bandwidth = estimate_bandwidth(flatimg, quantile=0.1, n_samples=100)
meanshift = MeanShift(bandwidth=bandwidth, bin_seeding=True)
meanshift.fit(flatimg)
labels = meanshift.labels_
# do segment
segmented_image = (label2rgb(np.reshape(labels, imgShape[:2]), bg_label=0) * 255).astype(np.uint8)
# show the image
plt.imshow(segmented_image)
plt.savefig("HSV_MS.png")
plt.show()
print("Silhouette Score HSV MS: ", silhouette_score(flatimg, labels, sample_size=25000))
"""""""""""""""""""""""
  | 1.4 MeanShift |
    RGB + HSV Image
"""""""""""""""""""""""
#  Combine RGB and HSV
img = cv2.imread("Original.jpg")
rgb_original_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_original_img = cv2.cvtColor(rgb_original_img,  cv2.COLOR_RGB2HSV)
combined_image = np.concatenate((rgb_original_img, hsv_original_img), axis=2)
# dimensions
imgShape = combined_image.shape
flatimg = np.reshape(combined_image, [-1, 6])
# meanshift
bandwidth = estimate_bandwidth(flatimg, quantile=0.1, n_samples=100)
meanshift = MeanShift(bandwidth=bandwidth, bin_seeding=True)
meanshift.fit(flatimg)
labels = meanshift.labels_
# do segment
segmented_image_ms_comb = (label2rgb(np.reshape(labels, imgShape[:2]), bg_label=0) * 255).astype(np.uint8)
# show image
plt.imshow(segmented_image_ms_comb)
plt.savefig("COMB_MS.png")
plt.show()
print("Silhouette Score COMBINED MS:", silhouette_score(flatimg, labels, sample_size=25000))
