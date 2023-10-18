# Computer Vision Project

This project is designed to introduce students to the field of Computer Vision, with a specific focus on image classification, semantic segmentation, and feature extraction. We use the Python programming language and the OpenCV library to perform various image processing tasks to achieve the desired results.

## Introduction

Computer Vision is a multidisciplinary field that enables machines to interpret and understand visual information from the world, just as humans do. In this project, we explore the following key aspects of computer vision:

1. **Image Classification:** We classify images into different categories or classes. This is a fundamental task in computer vision and has a wide range of applications.

2. **Semantic Segmentation:** We perform semantic segmentation to identify and classify the objects in an image, pixel by pixel. This is crucial for tasks like object recognition and scene understanding.

3. **Feature Extraction:** Feature extraction is essential for computer vision tasks. We use the Oriented FAST and Rotated BRIEF (ORB) feature detector to extract relevant features from images.

## Code

The project code is implemented in Python and uses the following libraries:

- [OpenCV](https://opencv.org/): Open Source Computer Vision Library for image processing.
- [NumPy](https://numpy.org/): A library for numerical computations in Python.
- [Pandas](https://pandas.pydata.org/): A data manipulation and analysis library.
- [Scikit-learn](https://scikit-learn.org/): A machine learning library for building and training classifiers.

The code is organized as follows:

- Loading and processing the dataset.
- Extracting features from images using the ORB feature detector.
- Creating visual words using K-Means clustering.
- Mapping feature values to histograms.
- Training and evaluating different classifiers, including Decision Trees, K-Nearest Neighbors, Gaussian Naive Bayes, and Support Vector Machines.

## Datasets

This project processes two datasets with different training and testing splits:

1. The "80/20 Split" dataset.
2. The "60/40 Split" dataset.

These datasets contain images that are used for training and testing the classifiers.

## Running the Project

To run the project, execute the `main` function in the code. This will process both datasets, evaluate different classifiers, and export the results to an Excel file.

```python
if __name__ == "__main__":
    main()
```

Make sure to update the file paths for your datasets accordingly.

## License

This project is open source and is provided under the terms of the [MIT License](LICENSE). You are free to use, modify, and distribute the code, subject to the conditions specified in the license.
