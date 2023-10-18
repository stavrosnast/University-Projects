import cv2
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import os

# Function to load images from a dataset folder
def load_dataset(folder, input_image_size):
    images = {}
    for filename in os.listdir(folder):
        category = []
        path = os.path.join(folder, filename)
        for category_img in os.listdir(path):
            img = cv2.imread(os.path.join(path, category_img))
            if img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.resize(img, (input_image_size[0], input_image_size[1]))
                category.append(img)
        images[filename] = category
    return images

# Function to extract features from images using ORB detector
def detector_features(images):
    detector_vectors = {}
    descriptor_list = []
    detectorToUse = cv2.ORB_create()
    for nameOfCategory, availableImages in images.items():
        features = []
        tmp_img_counter = 1
        for img in availableImages:
            kp, des = detectorToUse.detectAndCompute(img, None)
            tmp_img_counter += 1
            if des is not None:
                descriptor_list.extend(des)
                features.append(des)
            else:
                print(' .. WARNING: image {:d} cannot be used'.format(tmp_img_counter))
        detector_vectors[nameOfCategory] = features
    return [descriptor_list, detector_vectors]

# Function to create visual words using K-Means clustering
def kmeansVisualWordsCreation(k, descriptor_list):
    batchSize = np.ceil(descriptor_list.__len__() / 50).astype('int')
    kmeansModel = MiniBatchKMeans(n_clusters=k, batch_size=batchSize, verbose=0)
    kmeansModel.fit(descriptor_list)
    visual_Words = kmeansModel.cluster_centers_
    return visual_Words, kmeansModel

# Function to map feature values to histograms
def mapFeatureValsToHistogram(data_features_by_class, visual_words, trained_kmeans_model):
    histogramsList = []
    targetClassList = []
    numberOfBinsPerHistogram = visual_words.shape[0]

    for categoryIdx, featureValues in data_features_by_class.items():
        for tmpImageFeatures in featureValues:
            tmpImageHistogram = np.zeros(numberOfBinsPerHistogram)
            tmpIdx = list(trained_kmeans_model.predict(tmpImageFeatures.astype('float')))
            cluster_value, visualWordMatchCounts = np.unique(tmpIdx, return_counts=True)
            tmpImageHistogram[cluster_value] = visualWordMatchCounts
            numberOfDetectedPointsInThisImage = tmpIdx.__len__()
            tmpImageHistogram = tmpImageHistogram / numberOfDetectedPointsInThisImage

            histogramsList.append(tmpImageHistogram)
            targetClassList.append(categoryIdx)

    return histogramsList, targetClassList

# Function to train and evaluate a classifier
def train_and_evaluate_classifier(classifier, classifier_name, X_train, y_train, X_test, y_test):
    classifier.fit(X_train, y_train)
    train_score = classifier.score(X_train, y_train)
    test_score = classifier.score(X_test, y_test)

    y_pred_train = classifier.predict(X_train)
    y_pred_test = classifier.predict(X_test)

    precision_train = precision_score(y_train, y_pred_train, average='macro')
    precision_test = precision_score(y_test, y_pred_test, average='macro')

    recall_train = recall_score(y_train, y_pred_train, average='macro')
    recall_test = recall_score(y_test, y_pred_test, average='macro')

    f1_train = f1_score(y_train, y_pred_train, average='macro')
    f1_test = f1_score(y_test, y_pred_test, average='macro')

    print(f'Accuracy of {classifier_name} classifier on training set: {train_score:.2f}')
    print(f'Accuracy of {classifier_name} classifier on test set: {test_score:.2f}')
    print('')
    print(f'Precision scores of {classifier_name} classifier are:')
    print(f'train: {precision_train:.2f} and test: {precision_test:.2f}.')
    print('')
    print(f'Recall scores of {classifier_name} classifier are:')
    print(f'train: {recall_train:.2f} and test: {recall_test:.2f}.')
    print('')
    print(f'F1 scores of {classifier_name} classifier are:')
    print(f'train: {f1_train:.2f} and test: {f1_test:.2f}.')
    print('')

# Function to process the dataset
def process_dataset(dataset_name, train_path, test_path):
    input_image_size = [200, 200, 3]  # Define the image size

    # Load and process the training images
    trainImages = load_dataset(train_path, input_image_size)
    trainDataFeatures = detector_features(trainImages)
    TrainDescriptorList = trainDataFeatures[0]
    numberOfClasses = trainImages.__len__()
    possibleNumOfCentersToUse = 10 * numberOfClasses
    visualWords, TrainedKmeansModel = kmeansVisualWordsCreation(possibleNumOfCentersToUse, TrainDescriptorList)
    trainBoVWFeatureVals = trainDataFeatures[1]
    trainHistogramsList, trainTargetsList = mapFeatureValsToHistogram(trainBoVWFeatureVals, visualWords,
                                                                      TrainedKmeansModel)
    X_train = np.stack(trainHistogramsList, axis=0)
    labelEncoder = preprocessing.LabelEncoder()
    labelEncoder.fit(trainTargetsList)
    y_train = labelEncoder.transform(trainTargetsList)

    # Load and process the testing images
    testImages = load_dataset(test_path, input_image_size)
    testDataFeatures = detector_features(testImages)
    testBoVWFeatureVals = testDataFeatures[1]
    testHistogramsList, testTargetsList = mapFeatureValsToHistogram(testBoVWFeatureVals, visualWords,
                                                                    TrainedKmeansModel)
    X_test = np.array(testHistogramsList)
    y_test = labelEncoder.transform(testTargetsList)

    # Create and evaluate different classifiers
    classifiers = [
        (DecisionTreeClassifier(), 'Decision Tree Classifier'),
        (KNeighborsClassifier(), 'K-Nearest Neighbors Classifier'),
        (GaussianNB(), 'Gaussian Naive Bayes Classifier'),
        (SVC(), 'Support Vector Machine Classifier')
    ]

    results = {
        'Classifier': [],
        'Train Set Accuracy': [],
        'Test Set Accuracy': [],
        'Train Set Precision': [],
        'Test Set Precision': [],
        'Train Set Recall': [],
        'Test Set Recall': [],
        'Train Set F1 Score': [],
        'Test Set F1 Score': []
    }

    for classifier, classifier_name in classifiers:
        train_and_evaluate_classifier(classifier, classifier_name, X_train, y_train, X_test, y_test)

        train_score = classifier.score(X_train, y_train)
        test_score = classifier.score(X_test, y_test)

        y_pred_train = classifier.predict(X_train)
        y_pred_test = classifier.predict(X_test)

        precision_train = precision_score(y_train, y_pred_train, average='macro')
        precision_test = precision_score(y_test, y_pred_test, average='macro')

        recall_train = recall_score(y_train, y_pred_train, average='macro')
        recall_test = recall_score(y_test, y_pred_test, average='macro')

        f1_train = f1_score(y_train, y_pred_train, average='macro')
        f1_test = f1_score(y_test, y_pred_test, average='macro')

        results['Classifier'].append(classifier_name)
        results['Train Set Accuracy'].append(train_score)
        results['Test Set Accuracy'].append(test_score)
        results['Train Set Precision'].append(precision_train)
        results['Test Set Precision'].append(precision_test)
        results['Train Set Recall'].append(recall_train)
        results['Test Set Recall'].append(recall_test)
        results['Train Set F1 Score'].append(f1_train)
        results['Test Set F1 Score'].append(f1_test)

    df = pd.DataFrame(results)

    # Specify an absolute path for saving the Excel file
    excel_filename = f'C:/Users/amnesia /{dataset_name}_results.xlsx'
    df.to_excel(excel_filename, index=False)
    print(f'Results exported to {excel_filename}')


def main():
    # Process the first dataset (80/20 split)
    process_dataset("80_20_Split", 'C:/Users/{User}/Downloads/Datasets/animalTenEightyTwenty/train/',
                    'C:/Users/{User}/Downloads/Datasets/animalTenEightyTwenty/test/')

    # Process the second dataset (60/40 split)
    process_dataset("60_40_Split", 'C:/Users/{User}/Downloads/Datasets/animalTenSixtyForty/train/',
                    'C:/Users/{User}/Downloads/Datasets/animalTenSixtyForty/test/')


if __name__ == "__main__":
    main()
