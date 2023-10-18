# Image Processing with OpenCV and Python Part 2

In this assignment, we will perform edge detection using the Canny technique on various parts of our original image, which we will process  appropriately.

## Requirements

Before running the code, make sure you have the required libraries installed:

- OpenCV (Version 4.5.3.56)
- NumPy (Version 1.19.5)
- scikit-image (for Structural Similarity Index - SSIM)

You can install these libraries using pip:

```bash
pip install opencv-python-headless==4.5.3.56 numpy==1.19.5 scikit-image
```

## Code 1: RGB and HSV Analysis

### 1.1 RGB 3D Plot
- Displays a 3D plot of the RGB values of an input image.
- Converts the image to RGB and visualizes the distribution of pixel colors.

### 1.2 HSV 3D Plot
- Creates a 3D plot of the HSV (Hue, Saturation, Value) color space.
- Demonstrates the distribution of pixel colors in the HSV space.

### 1.3 RGB and HSV Histograms
- Generates histograms for the RGB and HSV color channels.
- Provides insight into the distribution of color values in the image.

### 1.4 K-Means and MeanShift Clustering
- Applies K-Means and MeanShift clustering algorithms to segment the image.
- Visualizes the clustering results and computes silhouette scores.

## Code 2: Canny Edge Detection and Denoising

- Utilizes Canny edge detection on a grayscale image.
- Adds Gaussian noise to the image and denoises it using a median blur filter.
- Applies Canny edge detection to the denoised image for better edge detection.

## Usage

To run these code snippets, make sure you have Python installed with the required libraries. You can execute the code files and observe the visualizations and results for each task.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of this license.
